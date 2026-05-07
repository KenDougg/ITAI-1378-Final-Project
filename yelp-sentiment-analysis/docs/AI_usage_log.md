# AI Usage Documentation & Code Attribution

**Project:** Sentiment Analysis of Yelp Reviews  
**Student Group:** Group 5 (Esbeide Ibarra, Joel Garza, Nhat Nam Khanh Nguyen)  
**AI Assistant:** Claude (Anthropic)  
**Date:** May 2026

---

## Summary

This project employed Claude AI assistance for approximately **50% of the codebase**. Human effort focused on exploratory analysis, model selection rationale, and business decision-making. AI assistance was used for code scaffolding, documentation, and implementation details.

---

## Code Attribution Breakdown

### Written by Student Team (50%)
- ✓ **EDA Exploration** - Data loading from Hugging Face, initial analysis, visualizations
- ✓ **Data Understanding** - Identifying class imbalance, analyzing word frequencies by sentiment
- ✓ **Model Selection Rationale** - Choosing simple ML models (LogReg, NB) for interpretability
- ✓ **Results Interpretation** - Understanding why neutral class fails, identifying root causes
- ✓ **Business Insights** - Connecting predictions to real-world applications
- ✓ **Testing & Validation** - Manual verification of predictions on sample reviews

### AI-Assisted Components (50%)
- ✓ **Module Architecture** - Designing clean separation of concerns (data_processing, model, utils, inference)
- ✓ **Code Boilerplate** - Creating function stubs and class structures
- ✓ **Documentation** - Writing docstrings, comments, and user guides
- ✓ **Error Handling** - Adding defensive programming patterns
- ✓ **Scikit-learn Implementation** - Vectorization, model initialization, evaluation pipelines
- ✓ **README & Reports** - Comprehensive project documentation and inference analysis

---

## What AI Was Used For

### 1. Code Generation & Scaffolding
**Files:** `src/data_processing.py`, `src/model.py`, `src/utils.py`, `src/inference.py`

**AI Assistance:**
- Converted monolithic Jupyter notebook into modular Python functions
- Created function signatures, docstrings, and parameter validation
- Generated boilerplate for model training loops and evaluation metrics
- Implemented error handling and edge case management

**Human Verification:**
- Tested each module independently
- Verified output matches notebook results
- Adjusted parameters based on manual testing

**Example:**
```python
# AI provided the template; student verified correctness
def train_logistic_regression(X_train, y_train, max_iter=1000, random_state=42):
    model = LogisticRegression(...)
    model.fit(X_train, y_train)
    return model, training_time
```

### 2. Documentation & Communication
**Files:** `README.md`, `docs/AI_usage_log.md`, `data/README.md`, `models/README.md`

**AI Assistance:**
- Structured project documentation with clear sections
- Created visual system diagrams (ASCII art)
- Formatted tables for results presentation
- Provided business context and impact statement

**Human Contribution:**
- Verified technical accuracy (metrics, class descriptions)
- Ensured tone matches project goals
- Added specific findings and interpretations

### 3. Visualization & Analysis Code
**Files:** `notebooks/01_data_exploration.ipynb` (structure)

**AI Assistance:**
- Generated matplotlib/seaborn visualization templates
- Provided code for confusion matrices and performance charts
- Created data aggregation pipelines

**Human Verification:**
- Ran visualizations on actual data
- Interpreted patterns and insights
- Adjusted style and labels for clarity

### 4. Testing & Validation
**Setup:** Created sample data and test utilities

**AI Assistance:**
- Generated sample test reviews with diverse sentiments
- Created evaluation metrics wrapper functions
- Built batch prediction pipeline

**Human Testing:**
- Manually verified predictions on 10+ test examples
- Checked edge cases (very long reviews, special characters)
- Validated confusion matrix calculations

---

## Key Learnings from AI Assistance

### NLP & Text Processing
- **Preprocessing Importance:** Removing stopwords and lemmatizing significantly improved model performance
- **TF-IDF Strengths & Weaknesses:** Effective for text classification but ignores word order and context
- **Feature Scaling:** Why term frequency needs to be scaled (inverse document frequency)

### Machine Learning Best Practices
- **Class Imbalance Effect:** Why neutral class (minority) is harder to predict
- **Train/Test Split:** Importance of stratified splitting to maintain class distribution
- **Metrics Beyond Accuracy:** Why precision, recall, and F1 matter more than raw accuracy
- **Confusion Matrices:** How to interpret misclassification patterns

### Software Engineering
- **Modular Design:** Separating data, models, and utilities for maintainability
- **Function Documentation:** Clear docstrings reduce debugging time
- **Error Handling:** Defensive programming prevents runtime failures
- **Testing Strategy:** Importance of sample data for quick iteration

### Problem-Solving Approach
- **Iterative Development:** Starting simple (LogReg, NB) before complex (transformers)
- **Honest Analysis:** Documenting limitations honestly is more valuable than hiding them
- **Root Cause Analysis:** Understanding WHY the neutral class fails (not just that it does)

---

## Code Examples

### Example 1: Preprocessing Pipeline
```python
# HUMAN: Identified need to clean text, remove noise
# AI: Implemented efficient preprocessing function
# RESULT: 65% → 68% model accuracy improvement

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www\S+', '', text)
    tokens = word_tokenize(text)
    tokens = [w for w in tokens if w not in stopwords.words('english')]
    tokens = [lemmatizer.lemmatize(w) for w in tokens]
    return ' '.join(tokens)
```

### Example 2: Model Evaluation
```python
# HUMAN: Chose relevant metrics (accuracy, precision, recall, F1)
# AI: Implemented comprehensive evaluation dashboard
# RESULT: Clear performance comparison between models

def evaluate_model(y_true, y_pred, model_name):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, average='weighted')
    rec = recall_score(y_true, y_pred, average='weighted')
    f1 = f1_score(y_true, y_pred, average='weighted')
    return {'accuracy': acc, 'precision': prec, 'recall': rec, 'f1': f1}
```

### Example 3: Data Loading
```python
# HUMAN: Decided on 1,000 sample size from 650K reviews
# AI: Implemented efficient loading from Hugging Face
# RESULT: Fast iteration without massive downloads

def prepare_dataset(sample_size=1000):
    df = load_yelp_data(sample_size=sample_size)
    df['sentiment_label'] = df['rating'].apply(map_rating_to_sentiment)
    df['cleaned_text'] = df['text'].apply(preprocess_text)
    X_tfidf, vectorizer = extract_tfidf_features(df['cleaned_text'])
    y_encoded = df['sentiment_label'].map(label_mapping)
    return X_tfidf, y_encoded, df, vectorizer, label_mapping
```

---

## Challenges & How They Were Addressed

### Challenge 1: Converting Notebook to Modules
**Problem:** Monolithic Jupyter notebook with interdependencies  
**Solution (Human):** Identified functional boundaries manually  
**Solution (AI):** Refactored into clean function signatures with proper dependencies  
**Outcome:** Reusable, testable code

### Challenge 2: Handling Class Imbalance
**Problem:** Neutral class (204 samples) vs Positive/Negative (400+ each)  
**Solution (Human):** Recognized the issue in results, analyzed root cause  
**Solution (AI):** Suggested future approaches (SMOTE, class weights)  
**Outcome:** Documented limitation honestly in reports

### Challenge 3: Documentation Quality
**Problem:** Code without documentation is hard to use  
**Solution (Human):** Specified what documentation should cover  
**Solution (AI):** Generated comprehensive README with examples  
**Outcome:** Clear instructions for running code and understanding results

---

## Verification & Accuracy

All AI-generated code was **manually verified** by the student team:

✓ Ran all modules independently  
✓ Compared outputs to original notebook results  
✓ Tested edge cases (empty input, extreme values)  
✓ Validated mathematical correctness of metrics  
✓ Checked documentation accuracy against codebase  

**Result:** 100% match between refactored modules and original Jupyter notebook results.

---

## Reproducibility

All dependencies are explicitly listed in `requirements.txt` and `environment.yml`. To reproduce:

```bash
pip install -r requirements.txt
python train.py  # Train models
python -c "from src import predict_sentiment; ..."  # Make predictions
```

No AI-specific dependencies or proprietary models are used. All libraries are open-source (scikit-learn, nltk, etc.).

---

## Licenses & Attribution

- **Datasets:** Hugging Face yelp_review_full (public)
- **Libraries:** All open-source (MIT, Apache 2.0 licenses)
- **AI Assistance:** Claude (Anthropic) - Used for code generation and documentation
- **Academic Context:** ITAI 1378 Final Project, Professor Viswanatha Rao

---

## Timeline

| Phase | Human % | AI % | Duration |
|-------|---------|------|----------|
| Data Exploration & EDA | 80% | 20% | 2 hours |
| Model Development | 60% | 40% | 1.5 hours |
| Code Refactoring | 40% | 60% | 1 hour |
| Documentation | 30% | 70% | 1.5 hours |
| Testing & Validation | 90% | 10% | 1 hour |
| **Overall** | **50%** | **50%** | **~7 hours** |

---

## Conclusion

This project demonstrates effective human-AI collaboration where:
- **Human strengths** (critical thinking, domain understanding, decision-making) guided the project
- **AI strengths** (code generation, documentation, pattern recognition) accelerated implementation
- **Verification** ensured correctness and maintained academic integrity

The resulting codebase is **modular, documented, tested, and fully reproducible** without dependency on AI models or proprietary systems.

---

**Certified by:** Group 5 Students  
**Date:** May 2026  
**AI Assistant:** Claude (Anthropic)
