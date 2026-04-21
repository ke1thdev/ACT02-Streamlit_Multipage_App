"""
Modern portfolio UI system — animations, SVG icons, glassmorphism, scroll reveals.
No gradient colors. All solid colours with opacity / shadow depth.
"""
import streamlit as st
import streamlit.components.v1 as components

# ═══════════════════════════════════════════════════════════════
# SVG ICONS  (Lucide-style, 24×24, stroke-based)
# ═══════════════════════════════════════════════════════════════
ICONS: dict[str, str] = {
    "code": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="16 18 22 12 16 6"/><polyline points="8 6 2 12 8 18"/></svg>',
    "shield": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    "globe": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="2" y1="12" x2="22" y2="12"/><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10A15.3 15.3 0 0 1 12 2z"/></svg>',
    "mail": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>',
    "user": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>',
    "folder": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"/></svg>',
    "tool": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/></svg>',
    "map_pin": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>',
    "phone": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>',
    "calendar": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>',
    "external_link": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg>',
    "github": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.565 21.796 24 17.3 24 12c0-6.627-5.373-12-12-12z"/></svg>',
    "terminal": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="4 17 10 11 4 5"/><line x1="12" y1="19" x2="20" y2="19"/></svg>',
    "database": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><ellipse cx="12" cy="5" rx="9" ry="3"/><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"/><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"/></svg>',
    "layout": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><line x1="3" y1="9" x2="21" y2="9"/><line x1="9" y1="21" x2="9" y2="9"/></svg>',
    "server": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="2" width="20" height="8" rx="2" ry="2"/><rect x="2" y="14" width="20" height="8" rx="2" ry="2"/><line x1="6" y1="6" x2="6.01" y2="6"/><line x1="6" y1="18" x2="6.01" y2="18"/></svg>',
    "award": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="7"/><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"/></svg>',
    "send": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>',
    "zap": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
    "book": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>',
    "briefcase": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>',
    "link": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>',
    "arrow_right": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="5" y1="12" x2="19" y2="12"/><polyline points="12 5 19 12 12 19"/></svg>',
    "layers": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>',
    "clipboard": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/><rect x="8" y="2" width="8" height="4" rx="1" ry="1"/></svg>',
    "bar_chart": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="20" x2="12" y2="10"/><line x1="18" y1="20" x2="18" y2="4"/><line x1="6" y1="20" x2="6" y2="16"/></svg>',
    "camera": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>',
    "message_circle": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z"/></svg>',
    "gamepad": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="6" y1="12" x2="10" y2="12"/><line x1="8" y1="10" x2="8" y2="14"/><line x1="15" y1="13" x2="15.01" y2="13"/><line x1="18" y1="11" x2="18.01" y2="11"/><rect x="2" y="6" width="20" height="12" rx="2"/></svg>',
    "dollar": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',
    "hash": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="9" x2="20" y2="9"/><line x1="4" y1="15" x2="20" y2="15"/><line x1="10" y1="3" x2="8" y2="21"/><line x1="16" y1="3" x2="14" y2="21"/></svg>',
    "check_circle": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>',
}


def get_icon(name: str, size: int = 24) -> str:
    svg = ICONS.get(name, "")
    if size != 24:
        svg = svg.replace('width="24"', f'width="{size}"').replace('height="24"', f'height="{size}"')
    return svg


# ═══════════════════════════════════════════════════════════════
# THEME
# ═══════════════════════════════════════════════════════════════
def render_theme_controls() -> str:
    if "theme_mode" not in st.session_state:
        st.session_state.theme_mode = "Light"
    st.sidebar.title("Appearance")
    mode = st.sidebar.radio(
        "Select mode",
        ["Light", "Dark"],
        index=0 if st.session_state.theme_mode == "Light" else 1,
        horizontal=True,
    )
    st.session_state.theme_mode = mode
    return mode


# ═══════════════════════════════════════════════════════════════
# MASTER STYLE  (CSS + floating‑bg + scroll JS)
# ═══════════════════════════════════════════════════════════════
def set_page_style(mode: str) -> None:
    is_light = mode == "Light"

    p = _palette(is_light)

    # Dot‑grid SVG data URI  (solid dots — no gradient)
    dot_fill = "%231c1c1a" if is_light else "%23eae8e4"
    dot_opacity = "0.045" if is_light else "0.03"
    dot_svg = (
        f"data:image/svg+xml,%3Csvg width='28' height='28' xmlns='http://www.w3.org/2000/svg'%3E"
        f"%3Ccircle cx='14' cy='14' r='1' fill='{dot_fill}' opacity='{dot_opacity}'/%3E%3C/svg%3E"
    )

    st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    :root {{
        --bg:{p['bg']};--surface:{p['surface']};--card:{p['card']};--card-solid:{p['card_solid']};
        --text:{p['text']};--muted:{p['muted']};--border:{p['border']};
        --accent:{p['accent']};--accent2:{p['accent2']};--accent-subtle:{p['accent_subtle']};
        --shadow:{p['shadow']};--shadow-hover:{p['shadow_hover']};
        --navtext:{p['nav_text']};--navhover:{p['nav_hover']};--navactive:{p['nav_active']};
        --inputbg:{p['input_bg']};--inputtext:{p['input_text']};
        --buttonbg:{p['button_bg']};--buttontext:{p['button_text']};
    }}

    /* ── RESET & BASE ── */
    *, *::before, *::after {{ box-sizing:border-box; }}

    .stApp {{
        background: var(--bg);
        color: var(--text);
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
    }}

    .stApp::before {{
        content:'';position:fixed;inset:0;
        background-image:url("{dot_svg}");
        pointer-events:none;z-index:0;
    }}

    .stApp h1,.stApp h2,.stApp h3,.stApp h4,.stApp p,.stApp li,.stApp label {{
        font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif;
        color:var(--text);
    }}
    .stApp h1 {{ font-weight:900;letter-spacing:-1px;font-size:2.2rem; }}
    .stApp h2 {{ font-weight:800;letter-spacing:-.5px; }}
    .stApp h3 {{ font-weight:700;letter-spacing:-.3px; }}

    /* hide default chrome */
    #MainMenu {{ visibility:hidden; }}
    footer {{ visibility:hidden; }}
    [data-testid="stHeader"] {{ background:transparent; }}

    /* Fix header buttons (e.g. collapsed sidebar toggle) so they are visible in light mode */
    [data-testid="collapsedControl"],
    [data-testid="collapsedControl"] *,
    button[kind="header"],
    button[kind="header"] * {{
        color:var(--text)!important;
        fill:var(--text)!important;
    }}

    /* custom scrollbar */
    ::-webkit-scrollbar {{ width:6px; }}
    ::-webkit-scrollbar-track {{ background:var(--bg); }}
    ::-webkit-scrollbar-thumb {{ background:var(--border);border-radius:6px; }}
    ::-webkit-scrollbar-thumb:hover {{ background:var(--muted); }}

    /* selection */
    ::selection {{ background:var(--accent);color:#fff; }}

    /* ── ANIMATIONS ── */
    @keyframes fadeInUp {{
        from {{ opacity:0;transform:translateY(32px); }}
        to {{ opacity:1;transform:translateY(0); }}
    }}
    @keyframes fadeIn {{
        from {{ opacity:0; }}
        to {{ opacity:1; }}
    }}
    @keyframes scaleIn {{
        from {{ opacity:0;transform:scale(.88); }}
        to {{ opacity:1;transform:scale(1); }}
    }}
    @keyframes slideInLeft {{
        from {{ opacity:0;transform:translateX(-28px); }}
        to {{ opacity:1;transform:translateX(0); }}
    }}
    @keyframes typing {{
        from {{ max-width:0; }}
        to {{ max-width:100%; }}
    }}
    @keyframes blinkCursor {{
        0%,100% {{ border-right-color:var(--accent); }}
        50% {{ border-right-color:transparent; }}
    }}
    @keyframes float1 {{
        0%,100% {{ transform:translate(0,0); }}
        33% {{ transform:translate(-25px,18px); }}
        66% {{ transform:translate(18px,-22px); }}
    }}
    @keyframes float2 {{
        0%,100% {{ transform:translate(0,0); }}
        33% {{ transform:translate(20px,-15px); }}
        66% {{ transform:translate(-15px,25px); }}
    }}
    @keyframes float3 {{
        0%,100% {{ transform:translate(0,0); }}
        50% {{ transform:translate(-18px,-20px); }}
    }}
    @keyframes fillBar {{
        from {{ width:0; }}
        to {{ width:var(--bar-w); }}
    }}
    @keyframes accentLine {{
        from {{ width:0; }}
        to {{ width:48px; }}
    }}
    @keyframes pulseRing {{
        0% {{ box-shadow:0 0 0 0 var(--accent-subtle); }}
        70% {{ box-shadow:0 0 0 8px transparent; }}
        100% {{ box-shadow:0 0 0 0 transparent; }}
    }}

    /* ── REVEAL ON SCROLL (class toggled by IntersectionObserver) ── */
    .reveal {{
        opacity:0;
        transform:translateY(28px);
        transition:opacity .7s cubic-bezier(.22,1,.36,1),transform .7s cubic-bezier(.22,1,.36,1);
    }}
    .reveal.revealed {{
        opacity:1; transform:translateY(0);
    }}

    /* stagger children */
    .reveal-stagger > .reveal:nth-child(1) {{ transition-delay:.08s; }}
    .reveal-stagger > .reveal:nth-child(2) {{ transition-delay:.16s; }}
    .reveal-stagger > .reveal:nth-child(3) {{ transition-delay:.24s; }}
    .reveal-stagger > .reveal:nth-child(4) {{ transition-delay:.32s; }}
    .reveal-stagger > .reveal:nth-child(5) {{ transition-delay:.40s; }}
    .reveal-stagger > .reveal:nth-child(6) {{ transition-delay:.48s; }}

    /* ── MAIN CONTENT ── */
    .stMainBlockContainer {{ animation:fadeIn .5s ease-out; position:relative;z-index:1; }}

    /* ── FLOATING BG SHAPES ── */
    .bg-shapes {{
        position:fixed;inset:0;pointer-events:none;z-index:0;overflow:hidden;
    }}
    .bg-shape {{
        position:absolute;border-radius:50%;
    }}
    .bg-s1 {{
        width:480px;height:480px;top:-140px;right:-120px;
        background:var(--accent);opacity:.035;
        animation:float1 28s ease-in-out infinite;
    }}
    .bg-s2 {{
        width:360px;height:360px;bottom:-90px;left:-80px;
        background:var(--accent2);opacity:.03;
        animation:float2 32s ease-in-out infinite;
    }}
    .bg-s3 {{
        width:220px;height:220px;top:42%;left:62%;
        background:var(--accent);opacity:.025;
        animation:float3 22s ease-in-out infinite;
    }}

    /* ── SIDEBAR ── */
    [data-testid="stSidebar"] {{
        background:var(--surface);border-right:1px solid var(--border);
    }}
    [data-testid="stSidebarNav"] a,
    [data-testid="stSidebarNav"] a *,
    [data-testid="stSidebarNav"] span,
    [data-testid="stSidebarNav"] p,
    [data-testid="stSidebarNav"] li,
    [data-testid="stSidebarNavItems"] a,
    [data-testid="stSidebarNavItems"] a *,
    [data-testid="stSidebarNavLink"],
    [data-testid="stSidebarNavLink"] * {{
        color:var(--navtext)!important;opacity:1!important;
        transition:all .25s cubic-bezier(.22,1,.36,1);
    }}
    [data-testid="stSidebarNav"] a:hover,
    [data-testid="stSidebarNavLink"]:hover {{
        background:var(--navhover)!important;
        transform:translateX(4px);
    }}
    [data-testid="stSidebarNav"] li[aria-selected="true"] a,
    [data-testid="stSidebarNav"] li[data-selected="true"] a,
    [data-testid="stSidebarNav"] li[aria-selected="true"] a *,
    [data-testid="stSidebarNav"] li[data-selected="true"] a *,
    [data-testid="stSidebarNavLink"][aria-current="page"],
    [data-testid="stSidebarNavLink"][aria-current="page"] * {{
        background:var(--navactive)!important;color:var(--text)!important;
        font-weight:600;opacity:1!important;
    }}

    /* ── TOPBAR ── */
    .topbar {{
        background:var(--card);
        backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);
        border:1px solid var(--border);border-radius:16px;
        padding:1rem 1.3rem;margin-bottom:1.2rem;
        box-shadow:0 2px 12px var(--shadow);
        animation:fadeInUp .55s cubic-bezier(.22,1,.36,1);
        transition:box-shadow .35s,transform .35s;
        display:flex;align-items:center;gap:.85rem;
    }}
    .topbar:hover {{
        box-shadow:0 6px 24px var(--shadow-hover);transform:translateY(-2px);
    }}
    .topbar .topbar-icon {{
        flex-shrink:0;color:var(--accent);display:flex;align-items:center;
    }}
    .topbar .topbar-body strong {{ font-weight:700;font-size:1.05rem; }}
    .topbar .topbar-body p {{
        margin:.15rem 0 0;color:var(--muted);font-size:.88rem;font-weight:400;
    }}

    /* ── HERO / TYPING ── */
    .hero-section {{
        padding:2rem 0 1rem;animation:fadeIn .4s ease-out;
    }}
    .typing-wrapper {{
        display:inline-block;position:relative;
    }}
    .typing-text {{
        font-size:clamp(2rem,5vw,3.2rem);font-weight:900;letter-spacing:-1.5px;
        overflow:hidden;white-space:nowrap;display:inline-block;
        border-right:3px solid var(--accent);
        max-width:0;
        animation:
            typing 1.6s steps(13,end) .6s forwards,
            blinkCursor .7s step-end infinite .6s;
    }}
    .hero-title-static {{
        font-size:clamp(2rem,5vw,3.2rem);font-weight:900;letter-spacing:-1.5px;
    }}
    .hero-subtitle {{
        margin-top:.5rem;font-size:1.05rem;color:var(--muted);
        font-weight:400;letter-spacing:.1px;
        opacity:0;animation:fadeInUp .6s ease-out 2.4s forwards;
    }}
    .hero-subtitle-static {{
        margin-top:.5rem;font-size:1.05rem;color:var(--muted);
        font-weight:400;letter-spacing:.1px;
    }}

    /* ── GLASS CARD ── */
    .glass-card {{
        background:var(--card);
        backdrop-filter:blur(12px);-webkit-backdrop-filter:blur(12px);
        border:1px solid var(--border);border-radius:16px;
        padding:1.35rem 1.4rem 1.2rem;margin-bottom:.9rem;
        box-shadow:0 2px 10px var(--shadow);
        transition:transform .35s cubic-bezier(.22,1,.36,1),
                   box-shadow .35s,border-color .35s;
        position:relative;overflow:hidden;
    }}
    .glass-card::before {{
        content:'';position:absolute;top:0;left:0;width:3px;height:0;
        background:var(--accent);transition:height .45s cubic-bezier(.22,1,.36,1);
        border-radius:0 3px 3px 0;
    }}
    .glass-card:hover {{
        transform:translateY(-4px);
        box-shadow:0 10px 32px var(--shadow-hover);
        border-color:var(--accent);
    }}
    .glass-card:hover::before {{ height:100%; }}
    .glass-card h3 {{ margin:0 0 .5rem;font-weight:700; }}
    .glass-card p {{ color:var(--muted);line-height:1.7;margin:.3rem 0; }}

    /* card icon badge */
    .card-icon-badge {{
        width:44px;height:44px;border-radius:12px;
        background:var(--accent-subtle);
        display:flex;align-items:center;justify-content:center;
        margin-bottom:.8rem;color:var(--accent);
        transition:transform .3s,background .3s;
    }}
    .glass-card:hover .card-icon-badge {{
        transform:scale(1.08);
    }}

    /* ── SECTION HEADER ── */
    .section-hdr {{
        display:flex;align-items:center;gap:.65rem;
        margin:1.8rem 0 1rem;
    }}
    .section-hdr .sh-icon {{
        color:var(--accent);display:flex;align-items:center;
    }}
    .section-hdr h2 {{
        margin:0;font-size:1.4rem;position:relative;
    }}
    .section-hdr h2::after {{
        content:'';position:absolute;bottom:-5px;left:0;
        height:3px;width:0;background:var(--accent);border-radius:2px;
        animation:accentLine .7s ease-out .2s forwards;
    }}

    /* ── CHIP / TAG ── */
    .chip {{
        display:inline-flex;align-items:center;gap:.35rem;
        border:1px solid var(--border);background:var(--surface);
        border-radius:999px;padding:.3rem .85rem;
        margin:.25rem .3rem .25rem 0;font-size:.82rem;font-weight:500;
        transition:all .28s cubic-bezier(.22,1,.36,1);
    }}
    .chip:hover {{
        transform:translateY(-2px) scale(1.04);
        border-color:var(--accent);
        box-shadow:0 3px 10px var(--shadow);
    }}
    .chip svg {{ width:14px;height:14px; }}

    /* ── METRIC CARDS ── */
    div[data-testid="stMetric"] {{
        background:var(--card);
        backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
        border:1px solid var(--border);border-radius:14px;
        padding:.85rem;box-shadow:0 2px 10px var(--shadow);
        transition:transform .3s cubic-bezier(.22,1,.36,1),box-shadow .3s;
        animation:scaleIn .5s cubic-bezier(.22,1,.36,1) both;
    }}
    div[data-testid="stMetric"]:hover {{
        transform:translateY(-3px) scale(1.01);
        box-shadow:0 6px 20px var(--shadow-hover);
    }}

    /* ── SKILL BAR ── */
    .skill-bar {{ margin-bottom:1.1rem; }}
    .skill-bar-header {{
        display:flex;justify-content:space-between;align-items:center;
        margin-bottom:.4rem;
    }}
    .skill-bar-label {{ font-weight:600;font-size:.92rem; }}
    .skill-bar-value {{ font-weight:700;font-size:.88rem;color:var(--accent); }}
    .skill-bar-track {{
        height:8px;background:var(--border);border-radius:8px;overflow:hidden;
    }}
    .skill-bar-fill {{
        height:100%;background:var(--accent);border-radius:8px;
        width:0;animation:fillBar 1.4s cubic-bezier(.22,1,.36,1) .4s forwards;
    }}

    /* ── PROJECT ROW ── */
    .project-row {{
        background:var(--card);
        backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
        border:1px solid var(--border);border-radius:16px;
        padding:1rem 1.2rem;margin-bottom:.7rem;
        box-shadow:0 2px 10px var(--shadow);
        transition:all .35s cubic-bezier(.22,1,.36,1);
        display:flex;align-items:flex-start;gap:.9rem;
        position:relative;overflow:hidden;
    }}
    .project-row::after {{
        content:'';position:absolute;bottom:0;left:0;right:0;
        height:2px;background:var(--accent);
        transform:scaleX(0);transform-origin:left;
        transition:transform .4s cubic-bezier(.22,1,.36,1);
    }}
    .project-row:hover {{
        transform:translateY(-3px);
        box-shadow:0 8px 28px var(--shadow-hover);
        border-color:var(--accent);
    }}
    .project-row:hover::after {{ transform:scaleX(1); }}
    .project-row .proj-icon {{
        flex-shrink:0;width:40px;height:40px;border-radius:10px;
        background:var(--accent-subtle);
        display:flex;align-items:center;justify-content:center;
        color:var(--accent);
        transition:transform .3s;
    }}
    .project-row:hover .proj-icon {{ transform:scale(1.1); }}
    .project-row .proj-body {{ flex:1;min-width:0; }}
    .project-row h4 {{ margin:0 0 .2rem;font-weight:700;font-size:1rem;line-height:1.3; }}
    .project-row p {{ margin:0 0 .4rem;font-size:.88rem;color:var(--muted); }}

    /* ── BUTTONS ── */
    .stButton > button, [data-testid="stFormSubmitButton"] > button, button[kind="secondary"], button[kind="primary"] {{
        border:1px solid var(--border)!important;
        background:var(--buttonbg)!important;color:var(--buttontext)!important;
        border-radius:10px;font-weight:600;font-family:'Inter',sans-serif;
        transition:all .3s cubic-bezier(.22,1,.36,1);
        box-shadow:0 2px 8px var(--shadow);
    }}
    .stButton > button:hover, [data-testid="stFormSubmitButton"] > button:hover, button[kind="secondary"]:hover, button[kind="primary"]:hover {{
        transform:translateY(-2px);
        box-shadow:0 6px 18px var(--shadow-hover);
        border-color:var(--accent)!important;
    }}
    .stButton > button:active, [data-testid="stFormSubmitButton"] > button:active, button[kind="secondary"]:active, button[kind="primary"]:active {{ transform:translateY(0); }}

    [data-testid="stLinkButton"] a {{
        border:1px solid var(--border)!important;
        background:var(--buttonbg)!important;color:var(--buttontext)!important;
        border-radius:10px!important;font-weight:600!important;
        text-decoration:none!important;font-family:'Inter',sans-serif!important;
        transition:all .3s cubic-bezier(.22,1,.36,1)!important;
        box-shadow:0 2px 8px var(--shadow)!important;
    }}
    [data-testid="stLinkButton"] a:hover {{
        transform:translateY(-2px)!important;
        box-shadow:0 6px 18px var(--shadow-hover)!important;
    }}

    /* ── INPUTS ── */
    .stTextInput input,.stTextArea textarea {{
        border-radius:10px;border:1px solid var(--border)!important;
        background:var(--inputbg)!important;color:var(--inputtext)!important;
        font-family:'Inter',sans-serif;
        transition:border-color .3s,box-shadow .3s;
    }}
    .stTextInput input:focus,.stTextArea textarea:focus {{
        border-color:var(--accent)!important;
        box-shadow:0 0 0 3px var(--accent-subtle)!important;
    }}
    .stTextInput input::placeholder,.stTextArea textarea::placeholder {{
        color:var(--muted)!important;opacity:1;
    }}
    .stSelectbox div[data-baseweb="select"] > div {{
        border-radius:10px;border:1px solid var(--border)!important;
        background:var(--inputbg)!important;transition:border-color .3s;
    }}
    .stSelectbox div[data-baseweb="select"] > div:hover {{
        border-color:var(--accent)!important;
    }}
    .stSelectbox div[data-baseweb="select"] span,
    .stSelectbox div[data-baseweb="select"] svg {{
        color:var(--inputtext)!important;fill:var(--inputtext)!important;
    }}

    /* ── TABS ── */
    .stTabs [data-baseweb="tab-list"] {{ gap:.3rem; }}
    .stTabs [data-baseweb="tab"] {{
        border-radius:10px 10px 0 0;font-family:'Inter',sans-serif;font-weight:500;
        transition:all .25s;
    }}

    /* ── INFO / EXPLORE CARD ── */
    .info-card {{
        background:var(--card);
        backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);
        border:1px solid var(--border);border-radius:14px;
        padding:1rem 1.2rem;box-shadow:0 2px 10px var(--shadow);
        transition:all .3s cubic-bezier(.22,1,.36,1);
        display:flex;align-items:center;gap:.75rem;
    }}
    .info-card:hover {{
        transform:translateY(-2px);box-shadow:0 4px 16px var(--shadow-hover);
    }}
    .info-card .ic-icon {{
        flex-shrink:0;color:var(--accent);display:flex;align-items:center;
    }}

    /* ── SOCIAL LINK ── */
    .social-link {{
        display:inline-flex;align-items:center;gap:.45rem;
        color:var(--text);text-decoration:none;
        padding:.35rem .7rem;border-radius:8px;
        border:1px solid var(--border);margin:.25rem .3rem .25rem 0;
        font-size:.88rem;font-weight:500;
        transition:all .28s cubic-bezier(.22,1,.36,1);
    }}
    .social-link:hover {{
        border-color:var(--accent);color:var(--accent);
        transform:translateY(-2px);box-shadow:0 3px 10px var(--shadow);
    }}
    .social-link svg {{ width:16px;height:16px; }}

    /* ── STATUS DOT ── */
    .status-dot {{
        display:inline-block;width:8px;height:8px;border-radius:50%;
        background:var(--accent);margin-right:6px;
        animation:pulseRing 2s ease-in-out infinite;
    }}

    /* ── DIVIDER ── */
    .styled-hr {{
        border:none;height:1px;background:var(--border);
        margin:2rem 0 1.5rem;
    }}

    /* ── RESPONSIVE ── */
    @media (max-width:768px) {{
        .topbar {{ padding:.8rem;border-radius:12px; }}
        .glass-card {{ padding:1rem; }}
        .typing-text,.hero-title-static {{ font-size:1.8rem!important; }}
    }}

    @media (prefers-reduced-motion:reduce) {{
        *,*::before,*::after {{
            animation-duration:.01ms!important;
            transition-duration:.01ms!important;
        }}
    }}
    </style>

    <!-- floating bg shapes -->
    <div class="bg-shapes">
        <div class="bg-shape bg-s1"></div>
        <div class="bg-shape bg-s2"></div>
        <div class="bg-shape bg-s3"></div>
    </div>
    """, unsafe_allow_html=True)

    # Inject scroll-reveal observer via component iframe (height 0)
    _inject_scroll_observer()


def _palette(light: bool) -> dict:
    if light:
        return {
            "bg": "#f5f3ef",
            "surface": "#faf8f4",
            "card": "rgba(250,248,244,.82)",
            "card_solid": "#faf8f4",
            "text": "#1c1c1a",
            "muted": "#6e6b65",
            "border": "#e4ded6",
            "accent": "#4d8c5c",
            "accent2": "#c4917a",
            "accent_subtle": "rgba(77,140,92,.1)",
            "shadow": "rgba(0,0,0,.06)",
            "shadow_hover": "rgba(0,0,0,.13)",
            "nav_text": "#3a3833",
            "nav_hover": "#f2ece4",
            "nav_active": "#e8e1d7",
            "input_bg": "#faf8f4",
            "input_text": "#1c1c1a",
            "button_bg": "#4d8c5c",
            "button_text": "#ffffff",
        }
    return {
        "bg": "#0e1015",
        "surface": "#16181f",
        "card": "rgba(22,24,31,.82)",
        "card_solid": "#16181f",
        "text": "#eae8e4",
        "muted": "#8e8a83",
        "border": "#282c36",
        "accent": "#5fa36c",
        "accent2": "#d4a182",
        "accent_subtle": "rgba(95,163,108,.12)",
        "shadow": "rgba(0,0,0,.25)",
        "shadow_hover": "rgba(0,0,0,.45)",
        "nav_text": "#dbd7cf",
        "nav_hover": "#1e212a",
        "nav_active": "#262a34",
        "input_bg": "#1a1d25",
        "input_text": "#eae8e4",
        "button_bg": "#5fa36c",
        "button_text": "#0e1015",
    }


def _inject_scroll_observer():
    """Inject an IntersectionObserver via a 0-height component iframe."""
    components.html("""
    <script>
    (function(){
        const doc = window.parent.document;
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(e => {
                if (e.isIntersecting) {
                    e.target.classList.add('revealed');
                }
            });
        }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
        // observe all .reveal elements
        doc.querySelectorAll('.reveal').forEach(el => observer.observe(el));
        // re‑observe on DOM changes (Streamlit dynamic rendering)
        const mo = new MutationObserver(() => {
            doc.querySelectorAll('.reveal:not(.revealed)').forEach(el => observer.observe(el));
        });
        mo.observe(doc.body, { childList: true, subtree: true });
    })();
    </script>
    """, height=0)


# ═══════════════════════════════════════════════════════════════
# COMPONENT HELPERS
# ═══════════════════════════════════════════════════════════════
def _clean_html(html_str: str) -> str:
    import re
    return re.sub(r'^\s+', '', html_str, flags=re.MULTILINE).strip()

def render_topbar(title: str, subtitle: str, icon_name: str = "zap") -> None:
    icon = get_icon(icon_name, 22)
    st.markdown(_clean_html(f"""
    <div class="topbar">
        <div class="topbar-icon">{icon}</div>
        <div class="topbar-body">
            <strong>{title}</strong>
            <p>{subtitle}</p>
        </div>
    </div>
    """), unsafe_allow_html=True)


def render_typing_hero(name: str, subtitle: str) -> None:
    played = st.session_state.get("_typing_played", False)
    if not played:
        st.session_state["_typing_played"] = True
        st.markdown(_clean_html(f"""
        <div class="hero-section">
            <div class="typing-wrapper">
                <span class="typing-text">Hi, I'm {name}</span>
            </div>
            <div class="hero-subtitle">{subtitle}</div>
        </div>
        """), unsafe_allow_html=True)
    else:
        st.markdown(_clean_html(f"""
        <div class="hero-section">
            <div class="hero-title-static">Hi, I'm {name}</div>
            <div class="hero-subtitle-static">{subtitle}</div>
        </div>
        """), unsafe_allow_html=True)


def render_section_header(text: str, icon_name: str = "hash") -> None:
    icon = get_icon(icon_name, 20)
    st.markdown(_clean_html(f"""
    <div class="section-hdr">
        <div class="sh-icon">{icon}</div>
        <h2>{text}</h2>
    </div>
    """), unsafe_allow_html=True)


def render_glass_card(content_html: str, icon_name: str | None = None) -> None:
    content_html = _clean_html(content_html)
    icon_block = ""
    if icon_name:
        icon_block = f'<div class="card-icon-badge">{get_icon(icon_name, 22)}</div>'
    st.markdown(_clean_html(f"""
    <div class="glass-card reveal">
        {icon_block}
        {content_html}
    </div>
    """), unsafe_allow_html=True)


def render_interest_card_html(icon_name: str, title: str, desc: str) -> str:
    icon = get_icon(icon_name, 22)
    return _clean_html(f"""
    <div class="glass-card reveal">
        <div class="card-icon-badge">{icon}</div>
        <h3>{title}</h3>
        <p>{desc}</p>
    </div>
    """)


def render_skill_bar(label: str, value: int, icon_name: str = "zap") -> None:
    icon = get_icon(icon_name, 16)
    st.markdown(_clean_html(f"""
    <div class="skill-bar reveal">
        <div class="skill-bar-header">
            <span class="skill-bar-label">{icon} {label}</span>
            <span class="skill-bar-value">{value}%</span>
        </div>
        <div class="skill-bar-track">
            <div class="skill-bar-fill" style="--bar-w:{value}%;"></div>
        </div>
    </div>
    """), unsafe_allow_html=True)


def render_divider() -> None:
    st.markdown('<hr class="styled-hr">', unsafe_allow_html=True)


def render_info_card(icon_name: str, text_html: str) -> None:
    text_html = _clean_html(text_html)
    icon = get_icon(icon_name, 20)
    st.markdown(_clean_html(f"""
    <div class="info-card reveal">
        <div class="ic-icon">{icon}</div>
        <div>{text_html}</div>
    </div>
    """), unsafe_allow_html=True)
