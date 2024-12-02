# Imports
import streamlit as st
import pandas
import modules.config as config
import modules.components as components

# Configurations
st.set_page_config(layout="wide", page_title="Home | " + config.APP_TITLE)
components.page_navigation()
column_count = 3

# About Section
st.title("The Best Company")

with open("about.txt") as file:
    about = file.read()

st.text(about)

# Team Section
st.header("Our Team")

data = pandas.read_csv("data/team.csv")
data_count = len(data)
columns = list(st.columns(column_count))
sizes = components.get_column_sizes(data_count, column_count)

current_index = 0

for i, column in enumerate(columns):
    start = current_index
    end = current_index + sizes[i]

    with column:
        for j, row in data[start:end].iterrows():
            components.employee_card(row)

    current_index = end
