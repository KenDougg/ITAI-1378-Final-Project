"""Model training and prediction utilities."""

import time
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split


def train_logistic_regression(X_train, y_train, max_iter=1000, random_state=42):
    """Train Logistic Regression model."""
    model = LogisticRegression(
        max_iter=max_iter,
        random_state=random_state,
        multi_class='multinomial'
    )

    start_time = time.time()
    model.fit(X_train, y_train)
    training_time = time.time() - start_time

    return model, training_time


def train_naive_bayes(X_train, y_train):
    """Train Multinomial Naive Bayes model."""
    model = MultinomialNB()

    start_time = time.time()
    model.fit(X_train, y_train)
    training_time = time.time() - start_time

    return model, training_time


def train_models(X_tfidf, y_encoded, test_size=0.2, random_state=42, verbose=True):
    """
    Train both models and return predictions.

    Returns:
        dict: Contains trained models, predictions, and metadata
    """
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X_tfidf, y_encoded, test_size=test_size,
        random_state=random_state, stratify=y_encoded
    )

    if verbose:
        print(f"\n{'='*60}")
        print(f"Data split: {X_train.shape[0]} train, {X_test.shape[0]} test")
        print(f"{'='*60}")

    results = {}

    # Train Logistic Regression
    if verbose:
        print("\nTraining Logistic Regression...")
    lr_model, lr_time = train_logistic_regression(X_train, y_train)
    y_pred_lr = lr_model.predict(X_test)

    if verbose:
        print(f"✓ Training complete in {lr_time:.3f} seconds")

    results['logistic_regression'] = {
        'model': lr_model,
        'predictions': y_pred_lr,
        'training_time': lr_time
    }

    # Train Naive Bayes
    if verbose:
        print("\nTraining Naive Bayes...")
    nb_model, nb_time = train_naive_bayes(X_train, y_train)
    y_pred_nb = nb_model.predict(X_test)

    if verbose:
        print(f"✓ Training complete in {nb_time:.3f} seconds")

    results['naive_bayes'] = {
        'model': nb_model,
        'predictions': y_pred_nb,
        'training_time': nb_time
    }

    results['X_test'] = X_test
    results['y_test'] = y_test
    results['X_train'] = X_train
    results['y_train'] = y_train

    return results


def get_model_predictions(model, X_data):
    """Get predictions from a trained model."""
    return model.predict(X_data)


def get_prediction_probabilities(model, X_data):
    """Get prediction probabilities from a trained model."""
    return model.predict_proba(X_data)
