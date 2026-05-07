# Quick Reference Card
## Yelp Sentiment Analysis - Group 5

### 🚀 First Time Setup
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Train models (generates ~400MB of data)
python train.py

# 3. View results
cat results/metrics.txt
```

### 📊 Model Performance
- **Best Model:** Naive Bayes (68% accuracy)
- **Positive Reviews:** 86% correctly identified ✓
- **Negative Reviews:** 86% correctly identified ✓
- **Neutral Reviews:** 0% (known issue) ✗

### 💻 Make Predictions
```python
import pickle
from src import predict_sentiment

# Load model & vectorizer
model = pickle.load(open('models/trained/naive_bayes_model.pkl', 'rb'))
vec = pickle.load(open('models/trained/tfidf_vectorizer.pkl', 'rb'))

# Predict
result = predict_sentiment(
    "Great food and excellent service!",
    model, vec,
    {'Negative': 0, 'Neutral': 1, 'Positive': 2}
)
print(result['sentiment'])  # Output: Positive
```

### 📁 Key Files
| File | Purpose |
|------|---------|
| `README.md` | What is this project? |
| `SETUP_INSTRUCTIONS.md` | How do I run it? |
| `AI_usage_log.md` | Who did what? (50/50) |
| `docs/inference_report.md` | Why did it fail on neutral? |
| `docs/presentation_outline.md` | How do I present? |
| `train.py` | One-command training |

### 🎯 Presentation Structure (6 Slides)
1. **Title** - Project name, team, date
2. **Problem** - Why sentiment analysis matters
3. **Dataset & Method** - 1,000 Yelp reviews, TF-IDF + ML
4. **Model & Validation** - Two models tested, 80/20 split
5. **Results** - 68% accuracy, what worked/failed
6. **Learnings** - What we learned, future improvements

### ⚡ Common Commands
```bash
# Train from scratch
python train.py

# Run demo
python demo.py

# Check git history
git log --oneline

# Push to GitHub
git remote add origin <URL>
git push -u origin main

# View all metrics
cat results/metrics.txt

# Read detailed analysis
cat docs/inference_report.md
```

### ✅ Before Submission
- [ ] Run `python train.py` successfully
- [ ] Review `results/metrics.txt`
- [ ] Read `docs/inference_report.md` (understand limitations)
- [ ] Prepare presentation using `docs/presentation_outline.md`
- [ ] Push to GitHub
- [ ] Create demo video (3-5 min)

### 🔑 Key Takeaways
- **Strength:** Easy to distinguish strong sentiments (positive/negative)
- **Weakness:** Can't classify 3-star (neutral) reviews
- **Why:** Too few neutral examples in training data (class imbalance)
- **Future:** Use SMOTE to balance classes or try BERT model

### 📞 Help
- Project structure confused? → See `SETUP_INSTRUCTIONS.md`
- Model failed on neutral? → Read `docs/inference_report.md` (root cause explained)
- Presentation stuck? → Follow `docs/presentation_outline.md` (6-slide template)
- Code broken? → Check `QUICK_START.md` or run `python train.py` fresh

---

**Questions? References:**
- `README.md` - Full overview
- `docs/AI_usage_log.md` - Code breakdown
- `docs/inference_report.md` - Performance analysis
- `DELIVERY_SUMMARY.md` - Complete project status

**Status:** ✅ Ready to submit. Push to GitHub, create video, present!
