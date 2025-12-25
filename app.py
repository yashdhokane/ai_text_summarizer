import streamlit as st
from transformers import pipeline

st.title("🧠 Free AI Text Summarizer")

# Load summarization model (will download first time)
@st.cache_resource
def get_summarizer():
    return pipeline("summarization")

summarizer = get_summarizer()

text = st.text_area("Paste your text here", height=250)

if st.button("Summarize"):
    if not text.strip():
        st.warning("Please enter some text")
    else:
        with st.spinner("Summarizing..."):
            summary = summarizer(text, max_length=250, min_length=50, do_sample=False)
            st.subheader("Summary")
            st.write(summary[0]['summary_text'])
