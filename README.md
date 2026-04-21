<div align="center">
  <img src="https://user-images.githubusercontent.com/7164864/217935870-c0bc60a3-6fc0-4047-b011-7b4c59488c91.png" alt="Streamlit Logo" width="90" />
  
  <h1 align="center">Modern Streamlit Portfolio</h1>
  
  <p align="center">
    <strong>A highly customized, premium personal portfolio application pushing the visual limits of Streamlit.</strong>
    <br />
    <br />
    <a href="https://act02-appmultipageap.streamlit.app/"><strong>🔥 View Live Demo »</strong></a>
    <br />
    <br />
  </p>
</div>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white" alt="Streamlit Badge"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JS Badge"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS Badge"/>
</div>

<br />

## 🌟 About The Project

This project demonstrates what happens when you treat **[Streamlit](https://streamlit.io/)** less like a pure data science dashboarding framework and more like a canvas for modern web development. 

The goal was to build a personal portfolio that feels responsive, highly premium, and breaks away from generic "AI-generated" templates. By overriding Streamlit's native DOM using deep CSS injections, inline SVG components, and JavaScript-powered scroll listeners, this app achieves an aesthetic previously thought impossible in a basic Python script.

### 🌐 Live Application
The project is officially deployed on Streamlit Community Cloud.  
**You can check it out here:** [https://act02-appmultipageap.streamlit.app/](https://act02-appmultipageap.streamlit.app/)

---

## ✨ Features & Architecture

### 💎 Custom UI System (`ui.py`)
At the core of the project relies a centralized design engine `ui.py` which strips default UI bloat and enforces a rigorous design system:
- **Glassmorphism Components:** Sleek, translucent `.glass-card` elements with active `backdrop-filter: blur()`, drop shadows, and animated accent-bar hover reveals.
- **Organic "Living" Backgrounds:** Floating, animated CSS blob keyframes interacting with a subtle custom SVG dot-grid background. 
- **100% SVG Iconography:** Eliminating emojis across the board in favor of a custom 30+ library of crisp, scalable inline vector icons (Lucide-inspired).
- **Modern Typography:** Globally forced `@import` of the *Inter* font family for seamless legibility.

### 🎭 Interactions & Animations
- **Scroll Reveals:** Intersection Observers trigger smooth `<div class="reveal">` slide-ups on native DOM elements as you scroll down pages.
- **Session-Guarded Typing Hero:** A CSS-native step animation typing out `"Hi, I'm Keith"`. This runs *only* once per browser session via `st.session_state` checks to ensure UX isn't ruined by constant re-runs.
- **Dynamic Skill Bars:** Custom keyframe animations progressively fill percentage bars when navigating to the technical skills page.
- **True Theming:** Granular control over a strict palette for both Light and Dark modes. Zero cheap gradients—only solid color tokens driving the UX.

---

## 🗂️ Project Map

```text
📦 Portfolio
┣ 📂 pages
┃ ┣ 📜 2_About.py           # Developer timeline (tabs), education & interests
┃ ┣ 📜 3_Skills.py          # SVG-chip layout with animated custom progress bars
┃ ┣ 📜 4_Projects.py        # Showcases links and live builds with styled hover rows
┃ ┗ 📜 5_Contact.py         # Glassmorphism social links and messaging portal
┣ 📜 Home.py                # Main landing index with the typing hero
┗ 📜 ui.py                  # Global CSS injection, SVGs, and DOM manipulators
```

---

## 🛠️ Running Locally

If you want to view the source code locally or modify the design engine for your own app:

1. **Clone the repository**
   ```bash
   git clone https://github.com/ke1thdev/ACT02-Streamlit_Multipage_App.git
   cd ACT02-Streamlit_Multipage_App
   ```

2. **Setup virtual environment & install requirements**
   ```bash
   pip install -r requirements.txt
   # OR directly:
   pip install streamlit
   ```

3. **Launch Streamlit server**
   ```bash
   streamlit run Home.py
   ```
   *Your browser will automatically open a local instance at `http://localhost:8501`.*

<br />

<div align="center">
  <p>Designed and developed by <strong>Keith</strong>.</p>
</div>