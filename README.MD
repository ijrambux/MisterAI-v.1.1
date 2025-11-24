# NordVPN Account Checker – Web Version
## Runs on Linux Distributions and Web (Render Compatible)

---

## Overview

This project allows users to check NordVPN accounts via a **web interface**.  
Users upload a combolist file (`nord.txt`) containing `username:password` pairs.  
The backend (FastAPI) processes the file and returns which accounts are valid or invalid.  
Frontend provides an easy-to-use interface for uploading files and displaying results.  

**Key Points:**
- Fully web-based – no GUI (PyQt) needed.
- Works on Linux distributions and web servers like Render.
- Designed for simplicity and easy deployment.

---

## Features

- Upload `nord.txt` combolist from the web page.
- Automatic checking of NordVPN accounts.
- Results displayed immediately in the browser.
- Headless mode and "Save Cookie" feature to be added in future updates.

---

## Installation & Run Locally

1. **Install Python 3.13+**  
2. **Clone the repository:**

```bash
git clone https://github.com/yourusername/NordVPN-Web-Checker.git
cd NordVPN-Web-Checker


