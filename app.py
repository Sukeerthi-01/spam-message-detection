import streamlit as st
import joblib

st.set_page_config(
    page_title="Spam Message Detection",
    page_icon="📩"
)

@st.cache_resource
def load_model():
    model = joblib.load("spam_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_model()

st.title("📩 Spam Message Detection System")
st.write(
    "Enter a message below to check whether it may be spam or not."
)

message = st.text_area("Enter your message:")

if st.button("Check Message"):
    if message.strip():
        message_vectorized = vectorizer.transform([message])
        prediction = model.predict(message_vectorized)[0]

        if prediction == "spam":
            st.error("⚠️ This message may be SPAM!")
        else:
            st.success("✅ This message appears to be NOT SPAM.")
    else:
        st.warning("Please enter a message first.")
