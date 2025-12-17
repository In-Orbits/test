import streamlit as st

st.title("My First App")
st.write("Hello! I deployed this without installing Python.")

user_input = st.text_input("Enter your name:")
if user_input:
    st.write(f"Welcome, {user_input}!")
