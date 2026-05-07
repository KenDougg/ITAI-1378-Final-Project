#!/usr/bin/env python
"""
Main training script for Yelp sentiment analysis.
Trains both models, evaluates them, and saves results.
"""

import sys
import pickle
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent))

from src import (
    prepare_dataset,
    train_models,
    evaluate_model,
    compare_models
)


def main():
    """Main training pipeline."""

    print("="*70)
    print("YELP SENTIMENT ANALYSIS - TRAINING SCRIPT")
    print("="*70)

    # Step 1: Load and preprocess data
    print("\n[1/4] Loading and preprocessing data...")
    X_tfidf, y_encoded, df, vectorizer, label_mapping = prepare_dataset(
        sample_size=1000,
        verbose=True
    )

    # Step 2: Train models
    print("\n[2/4] Training models...")
    results = train_models(X_tfidf, y_encoded, verbose=True)

    # Step 3: Evaluate models
    print("\n[3/4] Evaluating models...")
    eval_results = []

    for model_key, model_data in results.items():
        if model_key not in ['X_test', 'y_test', 'X_train', 'y_train']:
            print(f"\n{'='*60}")
            eval_result = evaluate_model(
                results['y_test'],
                model_data['predictions'],
                f"{model_key.title()}"
            )
            eval_results.append(eval_result)

    # Step 4: Compare models
    print("\n[4/4] Comparing models...")
    comparison_df = compare_models(eval_results)

    # Find best model
    best_idx = comparison_df['Accuracy'].idxmax()
    best_model_name = comparison_df.loc[best_idx, 'Model']

    print(f"\n{'='*70}")
    print(f"BEST MODEL: {best_model_name}")
    print(f"ACCURACY: {comparison_df.loc[best_idx, 'Accuracy']:.4f}")
    print(f"{'='*70}")

    # Save results to file
    output_file = Path('results/metrics.txt')
    output_file.parent.mkdir(parents=True, exist_ok=True)

    with open(output_file, 'w') as f:
        f.write("YELP SENTIMENT ANALYSIS - MODEL COMPARISON\n")
        f.write("="*70 + "\n\n")
        f.write(comparison_df.to_string(index=False))
        f.write("\n\n")
        f.write(f"Best Model: {best_model_name}\n")
        f.write(f"Best Accuracy: {comparison_df.loc[best_idx, 'Accuracy']:.4f}\n")

    print(f"\n✓ Results saved to: {output_file}")

    # Save models
    trained_model_path = Path('models/trained/naive_bayes_model.pkl')
    vectorizer_path = Path('models/trained/tfidf_vectorizer.pkl')

    trained_model_path.parent.mkdir(parents=True, exist_ok=True)

    # Save the best model (Naive Bayes)
    best_model = results['naive_bayes']['model']
    with open(trained_model_path, 'wb') as f:
        pickle.dump(best_model, f)

    # Save vectorizer
    with open(vectorizer_path, 'wb') as f:
        pickle.dump(vectorizer, f)

    print(f"✓ Model saved to: {trained_model_path}")
    print(f"✓ Vectorizer saved to: {vectorizer_path}")

    # Save label mapping
    label_mapping_path = Path('models/trained/label_mapping.pkl')
    with open(label_mapping_path, 'wb') as f:
        pickle.dump(label_mapping, f)

    print(f"✓ Label mapping saved to: {label_mapping_path}")

    print("\n" + "="*70)
    print("TRAINING COMPLETE!")
    print("="*70)
    print("\nNext steps:")
    print("1. Review metrics.txt for detailed results")
    print("2. Check docs/inference_report.md for analysis")
    print("3. Run notebooks for interactive exploration")
    print("4. Use trained models for predictions on new data")


if __name__ == '__main__':
    main()
