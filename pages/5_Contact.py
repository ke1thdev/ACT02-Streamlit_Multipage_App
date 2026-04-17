import streamlit as st
st.title(" Contact Me")
name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")
if st.button("Send"):
    if name and email and message:
        st.success("Message sent successfully! ✅")
else:
    st.error("Please fill all fields.")
    st.markdown("### Social Links")
    st.write("- GitHub: https://github.com/ke1th.dev")
    st.write("- Facebook: https://facebook.com/ke1th.dev")