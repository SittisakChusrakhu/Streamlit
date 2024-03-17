import streamlit as st
from textblob import TextBlob
import nltk
nltk.download('punkt')
import re
from nltk.tokenize import sent_tokenize

def analyze_sentiment(text):
    blob = TextBlob(text)
    words = re.findall(r'\b\w+\b', text)
    word_count = len(words)
    sentiment_score = blob.sentiment.polarity
    sentences = sent_tokenize(text)
    sentence_count = len(sentences) 

    if sentiment_score > 0.5:
        sentiment_label = "Positive"
        sentiment_desc = "ข้อความนี้มีความรู้สึกเชิงบวกมาก"
    elif sentiment_score > 0:
        sentiment_label = "Positive"
        sentiment_desc = "ข้อความนี้มีความรู้สึกเชิงบวก"
    elif sentiment_score < -0.5:
        sentiment_label = "Negative"
        sentiment_desc = "ข้อความนี้มีความรู้สึกเชิงลบมาก"
    elif sentiment_score < 0:
        sentiment_label = "Negative"
        sentiment_desc = "ข้อความนี้มีความรู้สึกเชิงลบ"
    else:
        sentiment_label = "Neutral"
        sentiment_desc = "ข้อความนี้มีความรู้สึกเป็นกลาง"

    return sentiment_score, word_count, sentiment_label, sentiment_desc, words, sentence_count  # เพิ่ม sentence_count ในการ return


st.title("Text Analysis")

text_inp = st.text_area("Input your text")
# Upload file
uploaded_file = st.file_uploader("Upload a file", type=["txt", "pdf", "docx"])

if uploaded_file is not None:
    file_contents = uploaded_file.getvalue().decode("utf-8")
    st.write("File Content:")
    st.write(file_contents)    
    text_inp = file_contents

if st.button("Analyze Text"):
    sentiment_score, word_count, sentiment_label, sentiment_desc, words, sentence_count = analyze_sentiment(text_inp)  

    st.write(f"ค่าความรู้สึก: {sentiment_score}")
    st.write("รายละเอียดความรู้สึก:")
    st.write(sentiment_desc)
    st.write(f"จำนวนประโยคในข้อความ: {sentence_count} ประโยค")
    st.write(f"จำนวนคำในข้อความ: {word_count} คำ")
    st.write("|".join(words))
    # Display sentiment label with image
    if sentiment_label == "Positive":
        st.image("Positive.gif", caption="Positive")
    elif sentiment_label == "Negative":
        st.image("Negative.gif", caption="Negative")
    else:
        st.image("Neutral.gif", caption="Neutral")
