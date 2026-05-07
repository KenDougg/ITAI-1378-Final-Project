"""Utility functions for evaluation and analysis."""

from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    classification_report, confusion_matrix
)
import pandas as pd


def evaluate_model(y_true, y_pred, model_name, target_names=None):
    """
    Evaluate model performance with multiple metrics.

    Args:
        y_true: True labels
        y_pred: Predicted labels
        model_name: Name of the model
        target_names: Names of target classes

    Returns:
        dict: Dictionary containing all metrics
    """
    if target_names is None:
        target_names = ['Negative', 'Neutral', 'Positive']

    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted', zero_division=0)
    recall = recall_score(y_true, y_pred, average='weighted', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='weighted', zero_division=0)

    print(f"\n{'='*60}")
    print(f"Model: {model_name}")
    print(f"{'='*60}")
    print(f"Accuracy:  {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1-Score:  {f1:.4f}")

    print(f"\nClassification Report:")
    print(classification_report(y_true, y_pred, target_names=target_names, zero_division=0))

    return {
        'model_name': model_name,
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1,
        'cm': confusion_matrix(y_true, y_pred)
    }


def compare_models(results_list, target_names=None):
    """Generate comparison DataFrame of model results."""
    if target_names is None:
        target_names = ['Negative', 'Neutral', 'Positive']

    metrics = []
    for result in results_list:
        metrics.append({
            'Model': result['model_name'],
            'Accuracy': result['accuracy'],
            'Precision': result['precision'],
            'Recall': result['recall'],
            'F1-Score': result['f1_score']
        })

    comparison_df = pd.DataFrame(metrics)
    print(f"\n{'='*70}")
    print("MODEL COMPARISON SUMMARY")
    print(f"{'='*70}")
    print(comparison_df.to_string(index=False))

    return comparison_df


def get_top_words(texts, n=10, stop_words=None):
    """Extract top N most common words from texts."""
    from collections import Counter
    from nltk.corpus import stopwords as nltk_stopwords

    if stop_words is None:
        stop_words = set(nltk_stopwords.words('english'))

    all_words = ' '.join(texts).lower().split()
    filtered_words = [word for word in all_words
                      if word.isalpha() and word not in stop_words]

    return Counter(filtered_words).most_common(n)


def analyze_by_sentiment(df, sentiment_column='sentiment_label', text_column='text'):
    """Analyze top words by sentiment."""
    print("\n" + "="*70)
    print("TOP WORDS BY SENTIMENT")
    print("="*70)

    for sentiment in ['Positive', 'Negative', 'Neutral']:
        if sentiment in df[sentiment_column].values:
            print(f"\nTop 10 words in {sentiment.upper()} reviews:")
            texts = df[df[sentiment_column] == sentiment][text_column]
            top_words = get_top_words(texts, n=10)

            for i, (word, count) in enumerate(top_words, 1):
                print(f"  {i}. {word}: {count}")


def sentiment_summary(df, sentiment_column='sentiment_label', rating_column='rating'):
    """Print sentiment analysis summary."""
    sentiment_dist = df[sentiment_column].value_counts(normalize=True) * 100

    print("\n" + "="*70)
    print("SENTIMENT ANALYSIS SUMMARY")
    print("="*70)

    print(f"\nOverall Customer Sentiment Distribution:")
    for sentiment in ['Positive', 'Negative', 'Neutral']:
        if sentiment in sentiment_dist.index:
            pct = sentiment_dist[sentiment]
            print(f"  {sentiment:10s}: {pct:5.1f}%")

    print(f"\nDataset Summary:")
    print(f"  Total Reviews: {len(df):,}")
    print(f"  Average Rating: {df[rating_column].mean():.2f} stars")
