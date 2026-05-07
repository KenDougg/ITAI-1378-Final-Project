# Models Directory

## Structure

- **pretrained/** - References to pre-trained models or links to download them
- **trained/** - Your trained model artifacts (pickle files, model weights, etc.)

## Models Used

### 1. Logistic Regression
- **Framework:** scikit-learn
- **Accuracy:** 67.5% on test set
- **Training Time:** ~0.5 seconds
- **Parameters:** max_iter=1000, multi_class='multinomial'

### 2. Multinomial Naive Bayes
- **Framework:** scikit-learn
- **Accuracy:** 68.0% on test set (Best Model)
- **Training Time:** ~0.02 seconds
- **Parameters:** Default (alpha smoothing at 1.0)

## Vectorizer

**TF-IDF Vectorizer**
- **Max features:** 5,000 words
- **N-gram range:** (1, 2) - both unigrams and bigrams
- **Min DF:** 2 (minimum document frequency)
- **Max DF:** 0.8 (maximum document frequency)

This creates a sparse feature matrix of shape (n_samples, 5000).

## How to Load Models

```python
import pickle

# Load trained model
with open('models/trained/naive_bayes_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load vectorizer
with open('models/trained/tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)
```

## Model Performance Comparison

| Metric    | Logistic Regression | Naive Bayes |
|-----------|-------------------|-------------|
| Accuracy  | 0.6750            | 0.6800      |
| Precision | 0.5423            | 0.5409      |
| Recall    | 0.6750            | 0.6800      |
| F1-Score  | 0.6013            | 0.6025      |

**Note:** Both models struggle with the neutral class (3-star reviews) due to class imbalance and ambiguous language. See the inference report for details.
