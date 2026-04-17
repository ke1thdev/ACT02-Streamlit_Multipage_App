import streamlit as st
st.title(" My Projects")
projects = {
"E-Attendance Navigator": " Attendance system with reports.",
"SAOD Web App": " Promotes local products.",
"Banking System": " Handles transactions and analytics."
}
for name, desc in projects.items():
    with st.expander(name):
        st.write(desc)