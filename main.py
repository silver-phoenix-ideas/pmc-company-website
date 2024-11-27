# Imports
import streamlit as st


# Functions
def main():
    # Configurations
    st.set_page_config(layout="wide")

    # About Section
    st.title("The Best Company")

    with open("about.txt") as file:
        about = file.read()

    st.text(about)


main()
