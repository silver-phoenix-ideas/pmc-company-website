# Imports
import streamlit as st
import pandas


# Functions
def get_column_sizes(data_count, column_count):
    quotient = data_count // column_count
    remainder = data_count % column_count
    columns = [quotient] * column_count

    if remainder:
        for index, column in enumerate(columns):
            if remainder:
                columns[index] += 1
                remainder -= 1

    return columns


def display_employee(employee):
    full_name = employee["first name"] + " " + employee["last name"]
    st.subheader(full_name.title())
    st.text(employee["role"])
    st.image("images/" + employee["image"])


def main():
    # Configurations
    st.set_page_config(layout="wide")
    column_count = 3

    # About Section
    st.title("The Best Company")

    with open("about.txt") as file:
        about = file.read()

    st.text(about)

    # Team Section
    st.header("Our Team")

    data = pandas.read_csv("data.csv")
    data_count = len(data)
    columns = list(st.columns(column_count))
    sizes = get_column_sizes(data_count, column_count)

    current_index = 0

    for i, column in enumerate(columns):
        start = current_index
        end = current_index + sizes[i]

        with column:
            for j, row in data[start:end].iterrows():
                display_employee(row)

        current_index = end


main()
