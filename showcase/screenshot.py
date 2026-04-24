"""
Automated showcase screenshot tool for Gemma 4 Data Assistant.
Requires: pip install playwright && playwright install chromium
Usage: python showcase/screenshot.py
"""

import subprocess
import time
import os

SCREENSHOTS = {
    "hero.png": "Full app view — upload a file, ask for a chart, capture the response + sidebar",
    "voice.png": "Click the mic, speak, capture the transcription preview",
    "chart.png": "Ask for a bar chart, capture it rendered in chat with code expander open",
    "excel.png": "Ask for an Excel report, capture the download button",
    "reasoning.png": 'Ask a complex question, capture the "View AI Reasoning" tab open',
    "arabic.png": "Switch to Arabic, ask a question, capture the RTL UI",
    "vision.png": "Upload an image, ask about it, capture the analysis response",
    "context.png": "Upload a large file, capture the sidebar context meter showing usage",
    "terminal.png": "Show the terminal running llama-opencode.bat with server startup output",
}

OUTPUT_DIR = os.path.dirname(__file__)

print("=" * 60)
print("  Gemma 4 Data Assistant — Screenshot Guide")
print("=" * 60)
print()
print("For each screenshot below, use Win+Shift+S to capture the window,")
print("then save it to the showcase/ folder with the specified filename.")
print()
print("Make sure the app is running:")
print("  1. Run llama-opencode.bat in one terminal")
print("  2. Run: .venv\\Scripts\\Activate.ps1 && streamlit run app.py")
print("  3. Open http://localhost:8501 in your browser")
print()
print("-" * 60)

for filename, description in SCREENSHOTS.items():
    filepath = os.path.join(OUTPUT_DIR, filename)
    status = "EXISTS" if os.path.exists(filepath) else "MISSING"
    print(f"\n  [{status}] {filename}")
    print(f"  {description}")

print()
print("-" * 60)
print(f"\n  Missing: {sum(1 for f in SCREENSHOTS if not os.path.exists(os.path.join(OUTPUT_DIR, f)))} / {len(SCREENSHOTS)}")
print()
