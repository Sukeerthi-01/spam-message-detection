# Spam Message Detection System

## Project Description
This project uses machine learning to classify text messages as Spam or Not Spam. It is built using Python, TF-IDF text vectorization, and the Multinomial Naive Bayes algorithm.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Multinomial Naive Bayes
- Streamlit
- Joblib

## Features
- Enter a text message for classification.
- Predict whether a message may be spam.
- Simple and interactive web interface.
- Uses a trained machine learning model.

## Project Files
- `app.py` — Streamlit application
- `spam_model.pkl` — Trained model
- `tfidf_vectorizer.pkl` — Text vectorizer
- `requirements.txt` — Required packages

## How to Run Locally

1. Install Python.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Install dependencies:

   `pip install -r requirements.txt`

5. Start the application:

   `streamlit run app.py`

## Model Information
The project uses TF-IDF to convert text into numerical features and Multinomial Naive Bayes to classify messages.

**Note:** The current prototype uses only 30 sample messages. Its accuracy results are preliminary and do not establish reliable real-world spam detection.

## Future Improvements
- Train using a larger public SMS spam dataset.
- Improve model evaluation.
  <img width="948" height="591" alt="image" src="https://github.com/user-attachments/assets/f2f3ee30-e294-4a8f-82d2-c008b6290bab" />

<img width="921" height="342" alt="Screenshot 2026-10-24 213352" src="https://github.com/user-attachments/assets/475f6645-f907-43bd-85c9-c8b0e92e72a7" />

