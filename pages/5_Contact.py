import streamlit as st

from ui import (
    get_icon,
    render_divider,
    render_glass_card,
    render_info_card,
    render_section_header,
    render_theme_controls,
    render_topbar,
    set_page_style,
)

st.set_page_config(page_title="Contact | Keith Portfolio", page_icon="📬", layout="wide")
mode = render_theme_controls()
set_page_style(mode)
render_topbar("Contact", "Reach out for collaboration, projects, or opportunities", "mail")

st.title("Contact")

left, right = st.columns(2, gap="large")
with left:
    render_glass_card(f"""
        <h3>Direct Info</h3>
        <p style="display:flex;align-items:center;gap:6px;">{get_icon('phone',16)} +639107323578</p>
        <p style="display:flex;align-items:center;gap:6px;">{get_icon('mail',16)} contactme@ke1th.dev</p>
        <p style="display:flex;align-items:center;gap:6px;margin-bottom:0;">{get_icon('map_pin',16)} Masbate, PH</p>
    """, icon_name="phone")

with right:
    render_glass_card(f"""
        <h3>Profiles</h3>
        <div style="display:flex;flex-wrap:wrap;gap:.35rem;margin-top:.5rem;">
            <a class="social-link" href="https://facebook.com/ke1th.dev" target="_blank">{get_icon('external_link',14)} Facebook</a>
            <a class="social-link" href="https://www.instagram.com/ke1th.dev" target="_blank">{get_icon('external_link',14)} Instagram</a>
            <a class="social-link" href="https://www.github.com/ke1thdev" target="_blank">{get_icon('github',14)} GitHub</a>
            <a class="social-link" href="https://istorya.chat" target="_blank">{get_icon('message_circle',14)} Istorya</a>
        </div>
    """, icon_name="link")

render_divider()

render_section_header("Quick Message", "send")
with st.form("contact_form"):
    name = st.text_input("Name")
    email = st.text_input("Email")
    topic = st.selectbox("Topic", ["Project Collaboration", "Freelance Work", "General Inquiry"])
    message = st.text_area("Message")
    submitted = st.form_submit_button("Send")

if submitted:
    if name.strip() and email.strip() and message.strip():
        st.success("Message submitted successfully.")
        st.info(f"Topic: {topic}")
    else:
        st.error("Please complete all fields.")

render_divider()

render_section_header("Availability", "check_circle")
availability = st.radio("Preferred initial contact", ["Email", "Phone", "Either"], horizontal=True)
render_info_card("zap", f'<span class="status-dot"></span> You selected: <strong>{availability}</strong>')
