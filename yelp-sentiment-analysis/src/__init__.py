"""Yelp Sentiment Analysis Package"""

from .data_processing import (
    load_yelp_data,
    preprocess_text,
    extract_tfidf_features,
    prepare_dataset,
    map_rating_to_sentiment
)
from .model import (
    train_logistic_regression,
    train_naive_bayes,
    train_models,
    get_model_predictions
)
from .utils import (
    evaluate_model,
    compare_models,
    analyze_by_sentiment,
    sentiment_summary
)
from .inference import (
    predict_sentiment,
    batch_predict,
    print_prediction
)

__version__ = "1.0.0"
__author__ = "Group 5: Esbeide Ibarra, Joel Garza, Nhat Nam Khanh Nguyen"
