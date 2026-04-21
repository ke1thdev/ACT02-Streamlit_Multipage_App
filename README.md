<div align="center">
  <img src="https://user-images.githubusercontent.com/7164864/217935870-c0bc60a3-6fc0-4047-b011-7b4c59488c91.png" alt="Streamlit Logo" width="80" />
  <h1>Modern Streamlit Portfolio</h1>
  <p>A highly customized, premium portfolio web application built with Streamlit and modern CSS.</p>
</div>

---

## 🚀 About The Project

This project demonstrates how far you can push a standard Python Streamlit application. Moving away from standard, generic dashboard aesthetics, this application implements a complete custom design system using injected CSS, SVG iconography, and dynamic scroll animations to create a responsive, modern, and beautiful developer portfolio. 

## ✨ Key Features

- **Glassmorphism Design System:** Custom `.glass-card` CSS components with sleek backdrop-blur effects and accent-bar hover reveals.
- **Scroll-Triggered Animations:** Custom `IntersectionObserver` JavaScript logic injected into Streamlit to trigger staggered slide-up reveals as the user scrolls.
- **Living Background:** A dynamic UI featuring a subtle SVG dot-grid overlay combined with floating organic background shapes animated via CSS keyframes.
- **High-Fidelity Typography & Icons:** Standardized on the beautiful *Inter* font. Zero emojis are used—everything from social links to skills chips relies on a custom repository of 30+ inline, scalable SVG icons (Lucide-inspired).
- **Session-Guarded Keyframes:** Smooth CSS-driven typing animations for the hero section that reliably check `st.session_state` to prevent obnoxious re-animations upon user interaction.
- **Strict Theme Controls:** Complete command over Light and Dark mode rendering with carefully curated, solid-color design tokens (zero cheap gradients).

## 🗂️ Project Structure

```text
📦 Portfolio App
┣ 📂 pages
┃ ┣ 📜 2_About.py           # Developer timeline, education, and achievements
┃ ┣ 📜 3_Skills.py          # SVG-chip layout with animated custom progress bars
┃ ┣ 📜 4_Projects.py        # Showcases tools/web-apps with hover project rows
┃ ┗ 📜 5_Contact.py         # Glassmorphism info cards and quick message UI
┣ 📜 Home.py                # Main landing page with typing hero and interest highlights
┣ 📜 ui.py                  # The core design engine (CSS styling, SVGs, Helper Functions)
┗ 📜 README.md
```

## 🛠️ Built With

* **[Streamlit](https://streamlit.io/)** — The core Python web framework.
* **Modern CSS3** — For custom styling, flexbox layouts, media queries, and keyframe animations.
* **Vanilla JS** — For `IntersectionObserver` scroll-reveal hooks.
* **Python 3.10+**

## 💻 Running Locally

To run this application locally, ensure you have Python and `streamlit` installed.

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ke1thdev/ACT02-Streamlit_Multipage_App.git
   cd ACT02-Streamlit_Multipage_App
   ```

2. **Install Requirements:**
   *(If you are utilizing a virtual environment, activate it prior to proceeding)*
   ```bash
   pip install streamlit
   ```

3. **Launch the App:**
   ```bash
   streamlit run Home.py
   ```
   *The application will automatically pop open in your default browser at `http://localhost:8501/`.*

## 📄 License & Attribution

Designed and developed by **Keith**.  