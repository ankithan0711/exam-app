import streamlit as st

st.set_page_config(page_title="Exam App", layout="centered")

st.title("🚀 My Exam App")

st.write("This is a starter template. I will modify this during the test.")

name = st.text_input("Enter your name:")

if st.button("Submit"):
    st.success(f"Hello {name} 👋")
