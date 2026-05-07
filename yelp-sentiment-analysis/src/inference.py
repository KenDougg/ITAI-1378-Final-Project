"""Inference and prediction utilities."""

from src.data_processing import preprocess_text


def predict_sentiment(text, model, vectorizer, label_mapping):
    """
    Predict sentiment for a single review.

    Args:
        text: Review text
        model: Trained model
        vectorizer: Fitted TF-IDF vectorizer
        label_mapping: Dictionary mapping labels to sentiment names

    Returns:
        dict: Contains prediction, probabilities, and sentiment label
    """
    # Preprocess text
    cleaned_text = preprocess_text(text)

    # Vectorize
    X = vectorizer.transform([cleaned_text])

    # Predict
    prediction = model.predict(X)[0]
    probabilities = model.predict_proba(X)[0]

    # Reverse label mapping
    reverse_mapping = {v: k for k, v in label_mapping.items()}
    sentiment = reverse_mapping[prediction]

    return {
        'original_text': text,
        'cleaned_text': cleaned_text,
        'predicted_label': prediction,
        'sentiment': sentiment,
        'probabilities': {
            reverse_mapping[i]: float(probabilities[i])
            for i in range(len(probabilities))
        }
    }


def batch_predict(texts, model, vectorizer, label_mapping):
    """
    Predict sentiment for multiple reviews.

    Args:
        texts: List of review texts
        model: Trained model
        vectorizer: Fitted TF-IDF vectorizer
        label_mapping: Dictionary mapping labels to sentiment names

    Returns:
        list: List of predictions
    """
    results = []
    for text in texts:
        result = predict_sentiment(text, model, vectorizer, label_mapping)
        results.append(result)

    return results


def print_prediction(result):
    """Print formatted prediction result."""
    print(f"\nText: {result['original_text'][:150]}...")
    print(f"Predicted Sentiment: {result['sentiment']}")
    print(f"Confidence Scores:")
    for sentiment, prob in result['probabilities'].items():
        print(f"  {sentiment:10s}: {prob:.4f}")
