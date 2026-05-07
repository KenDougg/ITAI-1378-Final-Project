#!/usr/bin/env python
"""
Demo script: Run sentiment predictions on sample reviews.
No training required - uses pre-defined examples.
"""

import sys
from pathlib import Path
import pandas as pd

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src import predict_sentiment
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB


def demo_with_mock_model():
    """Run demo with sample data (no training needed)."""

    print("="*70)
    print("YELP SENTIMENT ANALYSIS - DEMO")
    print("="*70)

    # Sample reviews to demonstrate
    sample_reviews = [
        {
            'text': "Amazing place! Food was delicious and service was excellent.",
            'sentiment': 'Positive'
        },
        {
            'text': "Terrible experience. Cold food, rude staff, never going back.",
            'sentiment': 'Negative'
        },
        {
            'text': "Service was okay. Food was decent but a bit overpriced.",
            'sentiment': 'Neutral'
        },
        {
            'text': "Love this restaurant! Best meal I've had in months!",
            'sentiment': 'Positive'
        },
        {
            'text': "Not impressed. Waited too long and food was mediocre.",
            'sentiment': 'Negative'
        },
    ]

    print("\nSAMPLE PREDICTIONS:")
    print("-" * 70)

    for i, review in enumerate(sample_reviews, 1):
        print(f"\n[{i}] Original Review:")
        print(f"Text: {review['text']}")
        print(f"Expected Sentiment: {review['sentiment']}")

        # Note: In a real scenario, you would:
        # 1. Load trained model and vectorizer
        # 2. Make actual predictions
        #
        # For demo purposes, we show the expected flow:
        print(f"\nTo make predictions, you would:")
        print(f"  1. Load trained model: pickle.load('models/trained/naive_bayes_model.pkl')")
        print(f"  2. Load vectorizer: pickle.load('models/trained/tfidf_vectorizer.pkl')")
        print(f"  3. Call: predict_sentiment(text, model, vectorizer, label_mapping)")

    print("\n" + "="*70)
    print("How to run actual predictions:")
    print("="*70)

    print("""
from src import predict_sentiment
import pickle

# Load model and vectorizer
with open('models/trained/naive_bayes_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/trained/tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Label mapping
label_mapping = {'Negative': 0, 'Neutral': 1, 'Positive': 2}

# Make prediction
text = "Great food and excellent service!"
result = predict_sentiment(text, model, vectorizer, label_mapping)

print(f"Sentiment: {result['sentiment']}")
print(f"Confidence: {result['probabilities']}")
    """)

    print("\nAlternatively, run 'train.py' to generate models first:")
    print("  python train.py")


if __name__ == '__main__':
    demo_with_mock_model()
