import streamlit as st

st.title("Multiplication Table")

number = st.number_input("Enter the number:", value=None, step=1)

if st.button("Generate Table"):
    st.subheader(f"GK - Multiplication Table of {int(number)}")

    for i in range(1, 21):
        st.write(f"{i} x {int(number)} = {i * int(number)}")
