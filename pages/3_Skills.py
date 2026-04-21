import streamlit as st

from ui import (
    get_icon,
    render_divider,
    render_info_card,
    render_section_header,
    render_skill_bar,
    render_theme_controls,
    render_topbar,
    set_page_style,
)

st.set_page_config(page_title="Skills | Keith Portfolio", page_icon="🛠️", layout="wide")
mode = render_theme_controls()
set_page_style(mode)
render_topbar("Skills", "Languages, databases, and web libraries", "tool")

st.title("Skills")

lang_db = [
    ("Python", "code"),
    ("HTML5", "layout"),
    ("CSS3", "layout"),
    ("MySQL", "database"),
    ("JavaScript", "terminal"),
    ("PHP", "server"),
]

frameworks = [
    ("Bootstrap", "layers"),
    ("AOS", "zap"),
    ("Driver.js", "arrow_right"),
    ("SweetAlert2", "check_circle"),
]

render_section_header("Languages & Databases", "database")
st.markdown(
    '<div style="display:flex;flex-wrap:wrap;gap:.45rem;margin-bottom:1rem;" class="reveal-stagger">'
    + "".join(
        f'<span class="chip reveal">{get_icon(icon, 14)} {name}</span>'
        for name, icon in lang_db
    )
    + "</div>",
    unsafe_allow_html=True,
)

render_section_header("Frameworks & Libraries", "layers")
st.markdown(
    '<div style="display:flex;flex-wrap:wrap;gap:.45rem;margin-bottom:1rem;" class="reveal-stagger">'
    + "".join(
        f'<span class="chip reveal">{get_icon(icon, 14)} {name}</span>'
        for name, icon in frameworks
    )
    + "</div>",
    unsafe_allow_html=True,
)

render_divider()

render_section_header("Self-assessment", "bar_chart")
focus_col, _ = st.columns([1, 1])
focus = focus_col.selectbox("Pick a focus area", ["Backend (PHP/MySQL)", "Frontend (HTML/CSS/JS)", "Full Stack Integration"])

data = {
    "Backend (PHP/MySQL)": (85, "server", "Strong in practical backend implementation and database handling."),
    "Frontend (HTML/CSS/JS)": (80, "layout", "Comfortable building responsive and user-friendly interfaces."),
    "Full Stack Integration": (83, "layers", "Able to connect front-end workflows with backend systems effectively."),
}

value, icon, desc = data[focus]
render_skill_bar(focus, value, icon)
render_info_card(icon, f'<span style="font-size:.92rem;">{desc}</span>')

render_divider()

render_section_header("Tech Match Tool", "zap")
project_kind = st.radio(
    "What are you building?",
    ["School Web System", "Portfolio", "Interactive Student Tool"],
    horizontal=True,
)

rec = {
    "School Web System": ("server", "PHP + MySQL + Bootstrap + SweetAlert2"),
    "Portfolio": ("layout", "HTML + CSS + JavaScript + AOS"),
    "Interactive Student Tool": ("terminal", "PHP + JavaScript + Driver.js"),
}

icon_name, stack = rec[project_kind]
render_info_card(icon_name, f'<strong>Recommended stack:</strong> {stack}')
