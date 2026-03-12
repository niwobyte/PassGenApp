# 🌐 Web-Based Password Generator

A modern password generator with a sleek web interface (HTML/CSS/JS) and a powerful Python backend.

## 📸 Instructions
<p align="center">
  <img src="assets/index.png" width="45%" />
  <img src="assets/journal.png" width="45%" />
</p>
<p align="center">
  <img src="assets/settings.png" width="45%" />
  <img src="assets/txt.png" width="45%" />
</p>

## 🛡️ Security
- **CSPRNG**: To ensure cryptographically secure generation of random numbers, the `window.crypto.getRandomValues()` method is used.
- **100% Offline**: No data ever leaves your device. No cloud, no leaks.

## ⚠️ Security Notice
*   **Confidentiality:** If you save passwords to a `.txt` file, treat it as sensitive data. **Do not share this file with anyone.**
*   **Protection:** It is highly recommended to move generated passwords to a dedicated password manager or encrypt the file if you are on a shared computer.

## ✨ Key Features
- **Modern UI**: Clean and intuitive web interface.
- **Journal**: Track and manage your generated passwords.
- **Settings**: Customizable generation rules.
- **Cross-Platform**: Runs in your favorite browser via Python.

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/niwobyte/PassGenApp.git
   cd PassGenApp
   pip install -r requirements.txt
   python PassGenApp.py
