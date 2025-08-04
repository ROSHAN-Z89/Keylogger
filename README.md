<h1 align="center">🕵️‍♂️ Keylogger</h1>

<p align="center">
  <img src="https://img.shields.io/badge/Version-1.0-blue?style=for-the-badge">
  <br>
  <img src="https://img.shields.io/badge/Author-ROSHAN--Z89-green?style=flat-square">
  <img src="https://img.shields.io/badge/Open%20Source-Yes-cyan?style=flat-square">
  <img src="https://img.shields.io/badge/Written%20In-Python-blue?style=flat-square">
</p>

---

## 🧠 Description

**Python Keylogger** is a lightweight, cross-platform keylogger script built using `pynput`. It captures all keystrokes, including modifier combinations like `CTRL+K`, and logs them to a timestamped file. Ideal for educational purposes, penetration testing, or behavior analysis.

> ⚠️ **Disclaimer:** This tool is for educational and ethical hacking purposes only. Do **not** use it without proper authorization.

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| ⌨️ Multi-Key Detection | Logs combo keys like `CTRL+C`, `ALT+F4`, `SHIFT+A`. |
| 🗂️ Timestamped Logs | Saves logs in uniquely named files based on date and time. |
| 🔒 Modifier Handling | Detects and tracks `CTRL`, `SHIFT`, `ALT` properly. |
| 🧠 Smart Character Capture | Supports both character keys and special keys. |
| 🧾 Lightweight | Pure Python, no external dependencies beyond `pynput`. |
| 📦 Cross-Platform | Runs on Windows, Linux, Mac (anywhere `pynput` works). |

---

## 📦 Installation

🧪 Works best on Python 3.8 or above

```bash
git clone https://github.com/ROSHAN-Z89/python-keylogger
cd Keylogger
pip install -r requirements.txt
python keylogger.py
