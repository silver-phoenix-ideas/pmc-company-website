# Imports
import streamlit as st
import pandas

# Contact Section
st.title("Contact")

data = pandas.read_csv("data/topics.csv")
topics = data["topic"].to_list()

with st.form(key="contact_form"):
    sender = st.text_input("Your email address:")
    topic = st.selectbox("What topic do you want to discuss?", topics)
    message = st.text_area("Your message:")
    submit = st.form_submit_button("Send Message")

if submit:
    status = st.info("Sending...")
    try:
        status.info("Your message was sent successfully.")
    except:
        status.error("Your message could not be sent.")