แอปพลิเคชันวิเคราะห์ข้อความ
แอปพลิเคชัน Streamlit นี้ช่วยให้ผู้ใช้สามารถวิเคราะห์ข้อความได้รวมถึงการวิเคราะห์ความรู้สึกของข้อความด้วยความสามารถในการแสดงข้อมูลเกี่ยวกับความรู้สึก จำนวนคำ และจำนวนประโยคในข้อความที่รับเข้ามา

วิธีการติดตั้ง
ตรวจสอบให้แน่ใจว่าคุณมี Python ติดตั้งอยู่แล้ว จากนั้นทำการติดตั้งแพ็กเกจที่จำเป็นด้วยคำสั่งต่อไปนี้: pip install streamlit textblob nltk

คุณยังต้องดาวน์โหลดตัวตัดคำของ NLTK โดยใช้คำสั่งต่อไปนี้ใน Python environment ของคุณ: import nltk
nltk.download('punkt')

การใช้งาน
เพื่อรันแอปพลิเคชัน ให้ทำการ execute คำสั่งต่อไปนี้ใน terminal: streamlit run app.py

วิธีการทำงาน
แอปพลิเคชันนี้ถูกสร้างขึ้นโดยใช้ Streamlit ซึ่งเป็นไลบรารี Python สำหรับสร้างเว็บแอปพลิเคชัน โดยมันใช้ TextBlob สำหรับการวิเคราะห์ความรู้สึกและ NLTK สำหรับการตัดคำ

การอธิบายโค้ด
ฟังก์ชันหลักของแอปพลิเคชันมีดังนี้:

ข้อความที่รับเข้ามา: ผู้ใช้สามารถใส่ข้อความโดยตรงในแอปพลิเคชันหรืออัปโหลดไฟล์ข้อความได้

การวิเคราะห์ความรู้สึก: เมื่อกดปุ่ม "วิเคราะห์ข้อความ" แอปพลิเคชันจะทำการวิเคราะห์ความรู้สึกของข้อความที่รับเข้ามาโดยใช้ TextBlob โดยจะคำนวณคะแนนความรู้สึก แยกแยะประเภทของความรู้สึก และให้คำอธิบายที่สอดคล้อง

จำนวนคำ: แอปพลิเคชันนับจำนวนคำในข้อความที่รับเข้ามา

จำนวนประโยค: มันยังนับจำนวนประโยคในข้อความโดยใช้ตัวตัดคำของ NLTK

การแสดงผล: ผลลัพธ์รวมถึงคะแนนความรู้สึก ป้ายชื่อของความรู้สึก จำนวนคำ และจำนวนประโยค จะถูกแสดงให้ผู้ใช้เห็น นอกจากนี้ คำแต่ละคำในข้อความก็จะถูกแสดง

รูปภาพป้ายชื่อความรู้สึก: ขึ้นอยู่กับป้ายชื่อความรู้สึกว่าเป็น "Positive", "Negative", หรือ "Neutral" รูปภาพที่สอดคล้องกับความรู้สึกจะถูกแสดง

ตัวอย่างโค้ด

import streamlit as st
from textblob import TextBlob
import nltk
nltk.download('punkt')
import re
from nltk.tokenize import sent_tokenize

# Function to analyze sentiment
def analyze_sentiment(text):
    # Perform sentiment analysis using TextBlob and NLTK
    ...

# Streamlit interface
st.title("Text Analysis")

text_inp = st.text_area("Input your text")
# Upload file
...

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
