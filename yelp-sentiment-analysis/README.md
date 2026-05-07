# Sentiment Analysis of Yelp Reviews

**Using Hugging Face yelp_review_full Dataset**

![Sentiment Distribution](results/visualizations/sentiment_distribution.png)

### A machine learning system that predicts customer sentiment from review text, enabling businesses to understand and act on customer feedback patterns.

---

## Team Members

- **Esbeide Ibarra** - Data Analysis & EDA
- **Joel Garza** - Model Training & Evaluation  
- **Nhat Nam Khanh Nguyen** - Project Management & Documentation

---

## Problem & Solution

### The Problem  
Businesses receive thousands of customer reviews across platforms like Yelp, but manually reading and analyzing all reviews is time-consuming and inefficient. Understanding sentiment patterns (positive, negative, neutral) helps identify key satisfaction drivers and pain points.

**Key Question:** Can we automatically classify customer sentiment from review text with reasonable accuracy?

### Our Solution
We built an end-to-end machine learning pipeline that:
1. **Loads & explores** 1,000 customer reviews from Yelp
2. **Preprocesses text** by removing noise, lemmatizing, and vectorizing
3. **Trains two classification models** (Logistic Regression & Naive Bayes)
4. **Evaluates performance** across sentiment categories
5. **Identifies patterns** in customer language by sentiment

### Impact
- Businesses can automatically categorize incoming reviews for quick triage
- Customer service teams can prioritize negative reviews for urgent response
- Marketing teams can identify positive keywords for campaigns
- Saves hours of manual review analysis per week

---

## Technical Details

### Approach

| Aspect | Details |
|--------|---------|
| **Task** | Multi-class sentiment classification (Negative / Neutral / Positive) |
| **Models** | Logistic Regression, Multinomial Naive Bayes |
| **Framework** | scikit-learn |
| **Feature Extraction** | TF-IDF Vectorization (5,000 features) |
| **Key Libraries** | datasets, nltk, pandas, numpy, matplotlib, seaborn |

### System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    SENTIMENT ANALYSIS PIPELINE                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                   │
│  [Yelp Reviews] → [Preprocessing] → [TF-IDF Features]           │
│                                           ↓                       │
│                                    ┌──────────────┐               │
│                                    │ Train Models │               │
│                                    ├──────────────┤               │
│                                    │ LogReg (68%) │               │
│                                    │   NB   (68%) │  ← Best       │
│                                    └──────────────┘               │
│                                           ↓                       │
│                               [Sentiment Prediction]             │
│                    (Negative / Neutral / Positive)               │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## Dataset

### Source
**Hugging Face:** [`yelp_review_full`](https://huggingface.co/datasets/yelp_review_full)

### Statistics
| Metric | Value |
|--------|-------|
| **Total Available** | 650,000+ reviews |
| **Sample Used** | 1,000 reviews |
| **Training Set** | 800 reviews (80%) |
| **Test Set** | 200 reviews (20%) |

### Class Distribution
| Sentiment | Count | Percentage |
|-----------|-------|-----------|
| Negative (1-2 stars) | 404 | 40.4% |
| Positive (4-5 stars) | 392 | 39.2% |
| Neutral (3 stars) | 204 | 20.4% |

**Note:** Class imbalance challenges model performance on neutral class.

### Data Preprocessing
Each review undergoes:
1. **Lowercase** conversion
2. **Remove** URLs and special characters  
3. **Tokenize** text into words
4. **Remove** English stopwords (common filler words)
5. **Lemmatize** words to base forms (e.g., "running" → "run")

Example:
```
Original:  "Thanks Yelp. I was looking for the words... bad reception!"
Cleaned:   "thanks yelp looking words bad reception"
```

---

## Results

### Model Performance

| Metric | Logistic Regression | Naive Bayes |
|--------|-------------------|-------------|
| **Accuracy** | 67.5% | **68.0%** ✓ |
| **Precision** | 54.2% | 54.1% |
| **Recall** | 67.5% | **68.0%** ✓ |
| **F1-Score** | 60.1% | 60.2% |

**Best Model:** Naive Bayes (68% accuracy on unseen test data)

### Per-Class Performance

#### Negative Class (1-2 stars)
- **Precision:** 66% | **Recall:** 86% | **F1:** 0.75
- Model correctly identifies ~86% of negative reviews
- Occasionally misclassifies neutral as negative

#### Positive Class (4-5 stars)
- **Precision:** 70% | **Recall:** 86% | **F1:** 0.77
- Best performed class, strong at distinguishing positive sentiment

#### Neutral Class (3 stars) ⚠️
- **Precision:** 0% | **Recall:** 0% | **F1:** 0.00
- **CHALLENGE:** Model completely fails on neutral reviews
- Root causes: class imbalance, ambiguous language in 3-star reviews

### Confusion Matrices

See `results/visualizations/` for detailed confusion matrices showing misclassification patterns.

---

## Quick Start

### 1. Installation

```bash
# Clone repository
git clone <repo-url>
cd yelp-sentiment-analysis

# Install dependencies
pip install -r requirements.txt

# Or use Conda
conda env create -f environment.yml
conda activate yelp-sentiment
```

### 2. Run Training

```bash
# Train models and evaluate
python train.py

# Or in Python
from src import prepare_dataset, train_models, evaluate_model
X, y, df, vectorizer, labels = prepare_dataset()
results = train_models(X, y)
evaluate_model(y, results['naive_bayes']['predictions'], 'Naive Bayes')
```

### 3. Make Predictions

```python
from src import predict_sentiment

# Single prediction
result = predict_sentiment(
    "Great food and excellent service!",
    model=trained_model,
    vectorizer=vectorizer,
    label_mapping=label_mapping
)

print(f"Sentiment: {result['sentiment']}")
print(f"Confidence: {result['probabilities']}")
```

### 4. Quick Test with Sample Data

```bash
# Use included sample data (no download required)
python -c "from src import predict_sentiment; ..."
```

---

## Project Structure

```
yelp-sentiment-analysis/
├── README.md                          # This file
├── requirements.txt                   # Python dependencies
├── environment.yml                    # Conda environment
│
├── data/
│   ├── README.md                      # Data documentation
│   ├── raw/                           # Original dataset link
│   ├── processed/                     # Preprocessed data
│   └── sample/                        # 10 sample reviews for quick testing
│
├── models/
│   ├── README.md                      # Model documentation
│   ├── pretrained/                    # Link to pre-trained models
│   └── trained/                       # Trained model artifacts
│
├── notebooks/                         # Jupyter notebooks
│   ├── 01_data_exploration.ipynb      # EDA and analysis
│   ├── 02_model_training.ipynb        # Train models
│   ├── 03_evaluation.ipynb            # Evaluate performance
│   └── 04_demo.ipynb                  # Interactive demo
│
├── src/                               # Python modules
│   ├── __init__.py
│   ├── data_processing.py             # Load & preprocess data
│   ├── model.py                       # Model training
│   ├── utils.py                       # Evaluation utilities
│   └── inference.py                   # Make predictions
│
├── results/
│   ├── images/                        # Output predictions
│   ├── visualizations/                # Charts, confusion matrices
│   └── metrics.txt                    # Performance metrics
│
├── docs/
│   ├── AI_usage_log.md                # AI assistance documentation
│   ├── inference_report.md            # Detailed analysis
│   │── presentation.pdf               # 6-slide presentation
│   └── proposal.pdf                   # Midterm proposal
│
└── .gitignore
```

---

## Key Findings

### What Worked Well ✓
1. **Text Preprocessing** - Removing stopwords & lemmatization significantly improved model performance
2. **TF-IDF Feature Extraction** - Effectively captured text semantics without complex embeddings
3. **Simple ML Models** - Naive Bayes performs competitively with minimal training time
4. **Negative & Positive Classes** - Models reliably distinguish strong sentiments (1-2 stars vs 4-5 stars)

### Challenges & Solutions 🔧
| Challenge | Root Cause | Approach |
|-----------|-----------|----------|
| Poor Neutral Performance | Class imbalance (204 vs 400+) | Documented as limitation; future SMOTE |
| Sarcasm Not Detected | TF-IDF ignores context | Future: Use BERT transformers |
| Ambiguous 3-Star Reviews | Reviews contain mixed sentiments | Future: Aspect-based sentiment analysis |

### What We'd Do Differently
1. **Collect more neutral examples** before training
2. **Use class weights** to penalize neutral class underrepresentation
3. **Implement BERT/Transformers** for contextual understanding
4. **Add aspect-based analysis** (food, service, ambiance separately)
5. **Cross-validate** with multiple splits for robust metrics

---

## Model Limitations

1. **Class Imbalance:** Model biases toward positive/negative due to fewer neutral examples
2. **Text-Only:** No consideration of review date, reviewer history, or metadata
3. **English Only:** Works only for English reviews; multilingual support needed
4. **Sarcasm & Irony:** Cannot detect ("Oh great, another cold coffee" = sarcasm)
5. **Limited Vocabulary:** Max 5,000 features may miss domain-specific words
6. **No Context:** TF-IDF ignores word order ("not good" vs "good")

---

## Future Improvements

### Short-term (High Impact)
- [ ] Balance classes using SMOTE or class weights
- [ ] Hyperparameter tuning (ridge penalty, class weights)
- [ ] Ensemble methods (combine LogReg + NB)

### Medium-term  
- [ ] Transformer-based models (DistilBERT, RoBERTa)
- [ ] Aspect-based sentiment (sentiment for food, service, etc.)
- [ ] Deep learning pipeline with PyTorch

### Long-term
- [ ] Multilingual support (Spanish, Mandarin, etc.)
- [ ] Real-time inference API
- [ ] Interactive dashboard for business users

---

## How to Run End-to-End

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the training script
python train.py

# 3. View results
cat results/metrics.txt

# 4. Run Jupyter notebooks for interactive exploration
jupyter notebook notebooks/01_data_exploration.ipynb

# 5. Generate predictions on new reviews
python -c "from src import predict_sentiment; ..."
```

---

## References

- **Dataset:** [Hugging Face yelp_review_full](https://huggingface.co/datasets/yelp_review_full)
- **Yelp Academic:** [Yelp Open Dataset](https://www.yelp.com/dataset)
- **Scikit-learn:** [Documentation](https://scikit-learn.org/)
- **NLTK:** [Natural Language Toolkit](https://www.nltk.org/)

---

## License

Academic Use Only - ITAI 1378 Final Project

---

## Acknowledgments

🙏 Thanks to **Professor Viswanatha Rao** for guidance and course instruction.

🤖 This project utilized Claude AI for code structure, documentation, and architectural suggestions (50% AI assistance).

---

**Last Updated:** May 2026  
**For questions or issues:** Please check the docs/ folder or review the inference report.
