# Contributing to Gemma Data Assistant

Thank you for your interest in contributing! Here's how to get started.

## Development Setup

1. Fork and clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Start llama-server: `./start_llama_server.bat`
5. Run the app: `streamlit run app.py`

## Pull Request Process

1. Create a feature branch (`git checkout -b feature/amazing-feature`)
2. Make your changes
3. Test with both CSV and Excel files
4. If adding UI text, update `translations.py` for both English and Arabic
5. Commit with a clear message (`git commit -m 'feat: add amazing feature'`)
6. Push and open a Pull Request

## Translation Guidelines

When adding new UI strings:

1. Add an English key to the `"en"` dictionary in `translations.py`
2. Add the Arabic translation to the `"ar"` dictionary
3. Use `t("key_name", lang=lang)` in `app.py` instead of hardcoded strings
4. Test both English and Arabic modes

## Code Style

- Follow PEP 8
- Add docstrings to new functions
- Keep `app.py` as a single file (architecture decision)
- No external CDN dependencies (100% offline operation)

## Reporting Bugs

Use the bug report template with:
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- Your OS and Python version
