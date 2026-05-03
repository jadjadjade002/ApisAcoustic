🐝 ApisAcoustic: Queen Bee Acoustic Monitoring

An AI-powered bioacoustic monitoring system to detect the state of beehives ("Active" vs "Missing Queen") using audio classification.

## About the Project
This project leverages state-of-the-art **Audio Spectrogram Transformers (AST)** to analyze the acoustic signatures of beehives. By listening to the hum of the colony, the AI can classify whether a hive is functioning normally (Active) or is in distress due to the absence of a queen (Missing Queen). 

This non-invasive monitoring method helps beekeepers manage their apiaries more efficiently and prevents colony collapse.

## Key Features
- **Audio Preprocessing:** Automatically slices raw audio (`.wav`, `.mp3`) into uniform 5-second chunks and resamples them to 16kHz for optimal model input.
- **Advanced AI Model:** Fine-tuned on the `MIT/ast-finetuned-audioset-10-10-0.4593` Hugging Face model, adapted specifically for binary bioacoustic classification.
- **Robust Validation:** Uses `StratifiedGroupKFold` (grouped by audio source file) to ensure absolute zero data leakage between training and testing sets.
- **Optimized Training:** Implements Mixed Precision Training (`autocast`, `GradScaler`) and Gradient Accumulation to maximize GPU memory efficiency.

## Model Performance
The model achieves highly accurate and balanced results on the perfectly split test set (13,466 clips):

- **Accuracy:** **94.64%**
- **Macro F1-Score:** **0.95**
- **Recall:** **0.95**

### Classification Report
| Hive State | Precision | Recall | F1-Score | Support |
| :--- | :---: | :---: | :---: | :---: |
| **Active (0)** | 0.94 | 0.95 | 0.95 | 6,776 |
| **Missing Queen (1)** | 0.95 | 0.94 | 0.95 | 6,690 |

### Confusion Matrix
*(Note: Upload your confusion matrix image to GitHub and replace this text with the image link, e.g., `![Confusion Matrix](link-to-image.png)`)*

## Tech Stack
- **Deep Learning:** PyTorch, Torchaudio
- **Transformers:** Hugging Face `transformers` (ASTFeatureExtractor, ASTForAudioClassification)
- **Data Manipulation:** Pandas, NumPy, Scikit-learn
- **Visualization:** Matplotlib, Seaborn

## Project Structure
```text
AI-BIOACOUSTIC-BEE/
│
├── dataset/                  # Directory for raw audio (.wav) and state_labels.csv (Ignored in Git)
├── .env                      # Environment variables (e.g., Hugging Face Token)
├── .gitignore                # Ignores large files like *.pth, *.zip, and raw datasets
├── ApisAcoustic_V1.0.ipynb   # Main Jupyter Notebook containing the ML Pipeline
├── README.md                 # Project documentation
