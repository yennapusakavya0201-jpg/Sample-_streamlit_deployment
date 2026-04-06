import streamlit as st

st.title("Chess Box Color")

row = st.number_input("Enter row (1-8)", 1, 8)
col = st.number_input("Enter column (1-8)", 1, 8)

if st.button("Check"):
    if (row + col) % 2 == 0:
        st.write("White Box")
    else:
        st.write("Black Box")
