import streamlit as st

from ui import (
    get_icon,
    render_divider,
    render_glass_card,
    render_section_header,
    render_theme_controls,
    render_topbar,
    set_page_style,
)

st.set_page_config(page_title="About | Keith Portfolio", page_icon="👨‍💻", layout="wide")
mode = render_theme_controls()
set_page_style(mode)
render_topbar("About Keith", "Profile, education, interests, and experience", "user")

st.title("About")

render_glass_card(
    """
    <h3>Developer Profile</h3>
    <p>
        Hi, I'm Keith, a 21-year-old third-year Computer Science student specialising
        in Full Stack Web Development.  I build and deploy real-world web applications,
        mainly using PHP and modern web tools.  I believe technology is valuable when
        it delivers reliable and meaningful solutions.
    </p>
    <p>
        Through LLM-assisted workflows and continuous self-learning, I create systems
        that are actively used in real scenarios.  I focus on clean, practical code and
        constant improvement.
    </p>
    """,
    icon_name="terminal",
)

info_left, info_right = st.columns(2, gap="large")
with info_left:
    render_glass_card(f"""
        <p style="margin-bottom:.45rem;"><span style="display:inline-flex;align-items:center;gap:6px;">{get_icon('calendar',16)} <strong>Birthday:</strong></span> 2004</p>
        <p style="margin-bottom:0;"><span style="display:inline-flex;align-items:center;gap:6px;">{get_icon('phone',16)} <strong>Phone:</strong></span> +639107323578</p>
    """)
with info_right:
    render_glass_card(f"""
        <p style="margin-bottom:.45rem;"><span style="display:inline-flex;align-items:center;gap:6px;">{get_icon('map_pin',16)} <strong>City:</strong></span> Masbate, PH</p>
        <p style="margin-bottom:0;"><span style="display:inline-flex;align-items:center;gap:6px;">{get_icon('mail',16)} <strong>Email:</strong></span> contactme@ke1th.dev</p>
    """)

render_divider()

render_section_header("Interests", "layers")
interests = st.multiselect(
    "Core interests",
    ["Programming", "Cybersecurity", "Web Development"],
    default=["Programming", "Cybersecurity", "Web Development"],
)
st.write("Selected:", ", ".join(interests))

render_divider()

render_section_header("Timeline", "calendar")
edu_tab, exp_tab, cert_tab = st.tabs(["Education", "Experience", "Certification"])

with edu_tab:
    render_glass_card(f"""
        <h3>BS Computer Science</h3>
        <p><span class="status-dot"></span> August 2023 – Present</p>
        <p>Relevant coursework: C/C++, Python, Web Development, Automata Theory, Algorithms and Data Structures</p>
    """, icon_name="book")

    render_glass_card("""
        <h3>ABM</h3>
        <p>August 2021 – August 2023</p>
        <p>Relevant coursework: Accounting, Business Mathematics, Marketing, Ethics, Entrepreneurship</p>
    """, icon_name="book")

    render_glass_card("""
        <h3>Earlier Education</h3>
        <p>Junior High School: 2017 – 2021<br>
        Elementary School: 2012 – 2017<br>
        Elementary School: 2011 – 2012</p>
    """)

with exp_tab:
    render_glass_card("""
        <h3>Domain MVP – Reverse Engineering</h3>
        <p>Web5 Development Hackathon 2025 (Season 3)</p>
        <p>Dr. Emilio B. Espinosa Sr. Memorial State College of Agriculture and Technology (DEBESMSCAT)</p>
        <p><strong>Date:</strong> December 2025</p>
    """, icon_name="award")
    st.write("- Awarded Domain MVP for outstanding performance in reverse engineering")
    st.write("- Recognized during the Semi-Finals Round Crossover")
    st.write("- Demonstrated cybersecurity and analytical problem-solving skills")

with cert_tab:
    render_glass_card("""
        <h3>HTML Essentials (Cisco)</h3>
    """, icon_name="check_circle")
    st.link_button("View Certificate", "https://drive.google.com/file/d/1rGvMjieuD32iUBoMnZWytAPoq-_WOrzM/view?usp=sharing")
