import streamlit as st

from ui import (
    get_icon,
    render_divider,
    render_glass_card,
    render_info_card,
    render_interest_card_html,
    render_section_header,
    render_theme_controls,
    render_typing_hero,
    set_page_style,
)

st.set_page_config(page_title="Home | Keith Portfolio", page_icon="🏠", layout="wide")
mode = render_theme_controls()
set_page_style(mode)

# ── Hero ──
render_typing_hero(
    "Keith",
    "Third-year CS student  ·  Full Stack Web Developer  ·  Masbate, PH",
)

st.markdown("<div style='height:.8rem'></div>", unsafe_allow_html=True)

# ── About card ──
render_glass_card(
    """
    <h3>About Me</h3>
    <p>
        I build and deploy real-world web applications, mainly using PHP and modern
        web tools.  While some say PHP is outdated, I believe any technology is
        valuable as long as it delivers reliable, efficient, and meaningful solutions.
    </p>
    <p>
        With the help of LLMs and continuous self-learning, I have developed web
        applications that are actively used in real scenarios. I enjoy turning ideas
        into working systems through hands-on development.
    </p>
    """,
    icon_name="terminal",
)

# ── Quick stats ──
left, mid, right = st.columns(3)
left.metric("Age", "21")
mid.metric("Primary Stack", "PHP + Web Tools")
right.metric("Location", "Masbate, PH")

render_divider()

# ── Interests ──
render_section_header("Interests", "layers")

cols = st.columns(3)
cols[0].markdown(
    render_interest_card_html("code", "Programming", "Building practical systems with clean logic."),
    unsafe_allow_html=True,
)
cols[1].markdown(
    render_interest_card_html("shield", "Cybersecurity", "Interested in reverse engineering and secure development."),
    unsafe_allow_html=True,
)
cols[2].markdown(
    render_interest_card_html("globe", "Web Development", "Creating responsive applications for real users."),
    unsafe_allow_html=True,
)

render_divider()

# ── Explore ──
render_section_header("Explore This App", "arrow_right")

choice = st.radio(
    "What do you want to check first?",
    ["Projects", "Skills", "About and Experience", "Contact"],
    horizontal=True,
)

explore_map = {
    "Projects":             ("folder",    "Open the Projects page to view live links and project categories."),
    "Skills":               ("tool",      "Open the Skills page to view languages, databases, and libraries."),
    "About and Experience": ("user",      "Open the About page for education timeline and achievements."),
    "Contact":              ("mail",      "Open Contact for direct details and message form."),
}

icon_name, msg = explore_map[choice]
render_info_card(icon_name, f'<span style="color:var(--muted);font-size:.93rem;">{msg}</span>')
