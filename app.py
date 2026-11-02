import streamlit as st

st.title("Student Performance Dashboard")

name = st.text_input("Enter student name")

marks = st.number_input("Enter marks",
                        min_value = 0,
                        max_value = 100
                        )

if st.button("Check Result"):
    
    st.write("Student Name:",name)
    st.write("Marks:",marks)
    
    if marks >= 40:
        st.success("Pass")
    else:
        st.error("Fail")