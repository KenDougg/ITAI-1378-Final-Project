# Notebooks

This directory contains Jupyter notebooks for interactive exploration and development.

## Available Notebooks

- **01_data_exploration.ipynb** - EDA, sentiment distribution, word frequency analysis
- **02_model_training.ipynb** - Train Logistic Regression and Naive Bayes models
- **03_evaluation.ipynb** - Evaluate model performance, confusion matrices, metrics
- **04_demo.ipynb** - Interactive demo for making predictions on new reviews

## How to Run

```bash
# Start Jupyter server
jupyter notebook

# Or use JupyterLab
jupyter lab
```

Then open the desired notebook and run cells sequentially.

## Note

These notebooks call functions from the `src/` modules for clean, reusable code. To ensure they work:

1. Install requirements: `pip install -r requirements.txt`
2. Ensure you're in the project root directory
3. Run notebooks from the root, not from within subdirectories
