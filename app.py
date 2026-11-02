from datetime import date
import streamlit as st
from generations import which_generation_am_I

st.title("Which generation am I?")

current_year = date.today().year

birth_year = st.number_input("Birth year", min_value=1800, max_value=current_year, value=None, placeholder="e.g. 1990",)

if birth_year is not None:
    st.write(f"You belong to: **{which_generation_am_I(birth_year)}**")