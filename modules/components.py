import streamlit as st


def employee_card(employee):
    full_name = employee["first name"] + " " + employee["last name"]
    st.subheader(full_name.title())
    st.text(employee["role"])
    st.image("images/" + employee["image"])


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
