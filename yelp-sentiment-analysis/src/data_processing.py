"""Data loading, preprocessing, and feature extraction for sentiment analysis."""

import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from datasets import load_dataset
import pandas as pd

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('tokenizers/punkt_tab')
except LookupError:
    nltk.download('punkt_tab')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')


def load_yelp_data(sample_size=1000, random_state=42):
    """Load Yelp reviews dataset from Hugging Face."""
    print("Loading yelp_review_full dataset from Hugging Face...")
    dataset = load_dataset("yelp_review_full")

    df = pd.DataFrame(dataset['train'])
    df = df.sample(n=sample_size, random_state=random_state).reset_index(drop=True)

    # Rename and convert labels
    df = df.rename(columns={'text': 'text', 'label': 'rating'})
    df['rating'] = df['rating'] + 1  # Convert 0-indexed labels to 1-5 stars

    return df


def map_rating_to_sentiment(rating):
    """Map star ratings to sentiment labels."""
    if rating <= 2:
        return 'Negative'
    elif rating == 3:
        return 'Neutral'
    else:  # 4-5 stars
        return 'Positive'


def preprocess_text(text):
    """Clean and preprocess review text."""
    # 1. Lowercase
    text = text.lower()

    # 2. Remove URLs and special characters
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # 3. Tokenize
    tokens = word_tokenize(text)

    # 4. Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words and len(word) > 1]

    # 5. Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return ' '.join(tokens)


def extract_tfidf_features(texts, max_features=5000, ngram_range=(1, 2),
                           min_df=2, max_df=0.8):
    """Extract TF-IDF features from text data."""
    vectorizer = TfidfVectorizer(
        max_features=max_features,
        ngram_range=ngram_range,
        min_df=min_df,
        max_df=max_df
    )

    X_tfidf = vectorizer.fit_transform(texts)
    return X_tfidf, vectorizer


def prepare_dataset(sample_size=1000, verbose=True):
    """
    Load, preprocess, and extract features from Yelp reviews.

    Returns:
        tuple: (X_tfidf, y_encoded, df, vectorizer, label_mapping)
    """
    # Load data
    df = load_yelp_data(sample_size=sample_size)

    if verbose:
        print(f"\nDataset loaded: {len(df)} reviews")
        print(f"Columns: {df.columns.tolist()}")

    # Add sentiment labels
    df['sentiment_label'] = df['rating'].apply(map_rating_to_sentiment)

    if verbose:
        print(f"\nSentiment Distribution:")
        print(df['sentiment_label'].value_counts())
        print(f"\nPreprocessing reviews...")

    # Preprocess text
    df['cleaned_text'] = df['text'].apply(preprocess_text)

    # Extract features
    X_tfidf, vectorizer = extract_tfidf_features(df['cleaned_text'])

    # Encode labels
    label_mapping = {'Negative': 0, 'Neutral': 1, 'Positive': 2}
    y_encoded = df['sentiment_label'].map(label_mapping)

    if verbose:
        print(f"\nTF-IDF Matrix Shape: {X_tfidf.shape}")
        print(f"Features extracted successfully!")

    return X_tfidf, y_encoded, df, vectorizer, label_mapping
