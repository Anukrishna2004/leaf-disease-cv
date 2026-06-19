# Error Analysis

## Summary

This error analysis report is based on the current evaluation run in `src/evaluate.py`.
The model achieved:

- Accuracy: 0.97
- Macro average precision: 0.97
- Macro average recall: 0.97
- Macro average F1-score: 0.97

## Class Performance

- `Tomato___healthy`: precision 1.00, recall 1.00, F1-score 1.00
- `Tomato___Early_blight`: precision 0.94, recall 0.94, F1-score 0.94
- `Tomato___Late_blight`: precision 0.99, recall 0.96, F1-score 0.97
- `Tomato___Leaf_Mold`: precision 0.94, recall 0.99, F1-score 0.97

## Confusion Matrix

The confusion matrix is saved as `reports/confusion_matrix.png`.
This matrix should be reviewed to identify the specific class pairs that are most often confused.

## Misclassified Samples

The first 10 misclassified validation samples are saved as image files in `reports/errors/`:

- `reports/errors/error_0.png`
- `reports/errors/error_1.png`
- `reports/errors/error_2.png`
- `reports/errors/error_3.png`
- `reports/errors/error_4.png`
- `reports/errors/error_5.png`
- `reports/errors/error_6.png`
- `reports/errors/error_7.png`
- `reports/errors/error_8.png`
- `reports/errors/error_9.png`

Each image includes the true and predicted label in the plot title.

## Key Observations

- The model performs perfectly on the healthy leaf class.
- The most notable errors are likely in `Tomato___Early_blight` and `Tomato___Leaf_Mold`, since those classes have the lowest precision or recall.
- `Tomato___Late_blight` has very high precision but slightly lower recall, suggesting some false negatives.

## Recommended Next Steps

1. Review `reports/confusion_matrix.png` for the exact confusion pairs.
2. Inspect the saved misclassified images in `reports/errors/` to understand visual failure modes.
3. Consider adding a more detailed error log in `src/evaluate.py` that records true label, predicted label, and image filename for all misclassifications.
4. If misclassification patterns suggest inter-class similarity, consider additional augmentation or fine-tuning with a larger validation split.
