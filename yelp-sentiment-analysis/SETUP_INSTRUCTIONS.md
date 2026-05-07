# Setup Instructions for ITAI 1378 - Yelp Sentiment Analysis Project

**Group 5:** Esbeide Ibarra, Joel Garza, Nhat Nam Khanh Nguyen  
**Professor:** Viswanatha Rao  
**Date:** May 2026

---

## Quick Start (5 minutes)

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Run Training
```bash
python train.py
```

This will:
- Load 1,000 Yelp reviews
- Preprocess the text
- Train both models (Logistic Regression & Naive Bayes)
- Evaluate performance
- Save metrics to `results/metrics.txt`

### 3. View Results
```bash
cat results/metrics.txt
```

---

## Project Overview

### What's Included

✓ **Source Code (`src/`)**
- Modular Python modules (data_processing, model, utils, inference)
- Clean, reusable functions
- Well-documented with docstrings

✓ **Data (`data/`)**
- 10 sample reviews for quick testing
- Link to full dataset (Hugging Face yelp_review_full)
- Data documentation

✓ **Documentation (`docs/`)**
- `README.md` - Main project overview
- `AI_usage_log.md` - 50/50 AI/Human code attribution
- `inference_report.md` - Detailed performance analysis
- `presentation_outline.md` - 6-slide presentation guide

✓ **Models & Results**
- Model documentation in `models/README.md`
- Results directory for outputs
- Sample README in `models/trained/`

✓ **Notebooks (`notebooks/`)**
- Templates for interactive analysis
- Can be populated with Jupyter code

---

## Project Structure

```
yelp-sentiment-analysis/
├── README.md                          ← Main project overview
├── SETUP_INSTRUCTIONS.md              ← This file
├── train.py                           ← Run to train models
├── demo.py                            ← Demo script
├── requirements.txt                   ← Python dependencies
├── environment.yml                    ← Conda environment (optional)
│
├── src/                               ← Core Python modules
│   ├── __init__.py
│   ├── data_processing.py             ← Data loading & preprocessing
│   ├── model.py                       ← Model training functions
│   ├── utils.py                       ← Evaluation utilities
│   └── inference.py                   ← Prediction functions
│
├── data/                              ← Data directory
│   ├── raw/                           ← Original dataset link
│   ├── processed/                     ← Preprocessed data
│   ├── sample/                        ← 10 sample reviews
│   ├── README.md                      ← Data documentation
│   └── sample_reviews.csv             ← Sample data
│
├── models/                            ← Model artifacts & info
│   ├── pretrained/                    ← Pre-trained models (if any)
│   ├── trained/                       ← Your trained models
│   └── README.md                      ← Model documentation
│
├── notebooks/                         ← Jupyter notebooks
│   ├── README.md
│   ├── 01_data_exploration.ipynb      ← (Add your EDA)
│   ├── 02_model_training.ipynb        ← (Add your training)
│   ├── 03_evaluation.ipynb            ← (Add your evaluation)
│   └── 04_demo.ipynb                  ← (Add your demo)
│
├── results/                           ← Output results
│   ├── images/                        ← Prediction visualizations
│   ├── visualizations/                ← Charts & confusion matrices
│   ├── metrics.txt                    ← Performance metrics
│   └── .gitkeep
│
└── docs/                              ← Documentation
    ├── AI_usage_log.md                ← AI assistance record
    ├── inference_report.md            ← Detailed analysis
    ├── presentation_outline.md        ← 6-slide presentation guide
    └── proposal.pdf                   ← (Optional) Midterm proposal
```

---

## Workflow

### Step 1: Setup Environment
```bash
# Option A: pip
pip install -r requirements.txt

# Option B: Conda
conda env create -f environment.yml
conda activate yelp-sentiment
```

### Step 2: Train Models
```bash
python train.py
```

**Output:**
- Console output with performance metrics
- Trained models saved to `models/trained/`
- Metrics saved to `results/metrics.txt`

### Step 3: Review Results
```bash
# Check metrics
cat results/metrics.txt

# Review analysis
cat docs/inference_report.md
```

### Step 4: Make Predictions (After Training)
```bash
python -c "
import pickle
from src import predict_sentiment

# Load model
with open('models/trained/naive_bayes_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('models/trained/tfidf_vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Make prediction
result = predict_sentiment(
    'Great food and excellent service!',
    model, vectorizer,
    {'Negative': 0, 'Neutral': 1, 'Positive': 2}
)

print(f'Sentiment: {result[\"sentiment\"]}')
"
```

### Step 5: Run Jupyter Notebooks (Optional)
```bash
jupyter notebook
```

Then open notebooks to explore interactively.

---

## Key Files Overview

### train.py
**Purpose:** Main training script  
**Run:** `python train.py`  
**Output:** Trained models, metrics

```bash
python train.py
# Output: Models saved to models/trained/, metrics to results/metrics.txt
```

### src/data_processing.py
**Functions:**
- `load_yelp_data()` - Load from Hugging Face
- `prepare_dataset()` - Full preprocessing pipeline
- `preprocess_text()` - Clean individual reviews
- `extract_tfidf_features()` - Vectorization

### src/model.py
**Functions:**
- `train_logistic_regression()` - Train LogReg
- `train_naive_bayes()` - Train Naive Bayes
- `train_models()` - Train both & compare

### src/utils.py
**Functions:**
- `evaluate_model()` - Calculate metrics
- `compare_models()` - Generate comparison
- `analyze_by_sentiment()` - Word frequency analysis

### src/inference.py
**Functions:**
- `predict_sentiment()` - Single prediction
- `batch_predict()` - Multiple predictions
- `print_prediction()` - Format output

---

## Dependency Installation

### Via pip (Recommended)
```bash
pip install -r requirements.txt
```

**Key Dependencies:**
- Python 3.7+
- numpy, pandas - Data manipulation
- scikit-learn - Machine learning
- nltk - NLP preprocessing
- datasets - Hugging Face integration
- matplotlib, seaborn - Visualization

### Via Conda
```bash
conda env create -f environment.yml
conda activate yelp-sentiment
```

---

## Important Notes

### Data Download
The project downloads the Yelp dataset automatically via Hugging Face:
```python
from datasets import load_dataset
dataset = load_dataset("yelp_review_full")  # Auto-downloads on first run
```

**Size:** ~500MB (full dataset)  
**Sample Used:** 1,000 reviews (much faster for development)

### Model Performance
- **Expected Accuracy:** 68% on test set
- **Training Time:** <1 second on modern CPU
- **Neutral Class:** Completely fails (0% accuracy) - see inference report

### Running Without Internet
For offline use:
1. Download data once with internet
2. Save to `data/raw/`
3. Modify `load_yelp_data()` to use local path

---

## Submission Checklist

Before submitting, verify:

- [ ] All Python modules in `src/` execute without errors
- [ ] `python train.py` completes successfully
- [ ] Models saved to `models/trained/`
- [ ] Metrics in `results/metrics.txt`
- [ ] `README.md` is comprehensive
- [ ] `docs/AI_usage_log.md` documents AI assistance
- [ ] `docs/inference_report.md` analyzes results
- [ ] `docs/presentation_outline.md` ready for slides
- [ ] `requirements.txt` includes all dependencies
- [ ] Git repository has clean history
- [ ] Sample data in `data/sample/`
- [ ] Demo video created separately (mentioned in README)

---

## Troubleshooting

### Problem: `ModuleNotFoundError: No module named 'nltk'`
**Solution:** Run `pip install -r requirements.txt`

### Problem: `No module named 'datasets'`
**Solution:** Install Hugging Face: `pip install datasets`

### Problem: Slow first run
**Reason:** First run downloads NLTK data + Hugging Face dataset  
**Solution:** Normal; subsequent runs are fast

### Problem: NLTK data not found
**Solution:** Download manually:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

### Problem: "Cannot download from Hugging Face"
**Solution:** You need internet for first download. Use sample data while offline:
```bash
python -c "
from src.inference import predict_sentiment
# Load sample data from data/sample/sample_reviews.csv instead
"
```

---

## Next Steps After Submission

### Recommended Improvements
1. **Handle Class Imbalance** - Implement SMOTE or class weights (70% → 72% accuracy)
2. **Use Transformers** - Try BERT for context understanding (68% → 75%+ accuracy)
3. **Aspect-Based Sentiment** - Separate food/service/ambiance scores
4. **Production Deployment** - Add confidence thresholds, API endpoint

### Additional Resources
- [Hugging Face Datasets](https://huggingface.co/datasets)
- [scikit-learn Documentation](https://scikit-learn.org/)
- [NLTK Book](https://www.nltk.org/book/)
- [Keras/TensorFlow for NLP](https://www.tensorflow.org/guide/keras)

---

## Questions?

Refer to:
- `README.md` - Project overview
- `docs/inference_report.md` - Analysis & learnings  
- `docs/AI_usage_log.md` - Code attribution & context
- `docs/presentation_outline.md` - Slide notes

---

**Ready to start?** Run: `python train.py`

Good luck! 🚀
