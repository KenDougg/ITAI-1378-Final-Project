# Data Directory

## Structure

- **raw/** - Original dataset or download instructions
- **processed/** - Preprocessed data (cleaned, features extracted)
- **sample/** - Small sample of reviews for quick testing and demo

## Dataset Details

### Source
[Hugging Face yelp_review_full](https://huggingface.co/datasets/yelp_review_full)

**Note:** The full dataset contains 650,000+ reviews. This project uses a sample of 1,000 reviews for faster training and experimentation. To download the full dataset or a different sample size, run:

```python
from datasets import load_dataset
dataset = load_dataset("yelp_review_full")
```

### Sample Data
The `sample/sample_reviews.csv` contains 10 representative examples:
- 4 Negative reviews (1-2 stars)
- 2 Neutral reviews (3 stars)
- 4 Positive reviews (4-5 stars)

Use this for quick testing without downloading the full dataset.

## Size
- **Sample used:** 1,000 reviews
- **Training set:** 800 reviews (80%)
- **Test set:** 200 reviews (20%)

## Classes
- **Negative:** 1-2 stars (404 samples)
- **Neutral:** 3 stars (204 samples)
- **Positive:** 4-5 stars (392 samples)

## Preprocessing
Reviews are preprocessed as follows:
1. Lowercase conversion
2. Remove URLs and special characters
3. Tokenization
4. Remove stopwords
5. Lemmatization

The cleaned text is then converted to TF-IDF features for model input.
