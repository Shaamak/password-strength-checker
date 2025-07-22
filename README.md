# 🔐 Password Strength Analyzer with Custom Wordlist Generator

A Python-based cybersecurity tool that analyzes the strength of user passwords and generates custom wordlists for penetration testing or auditing weak password practices.

## 🚀 Features

- ✅ **Password Strength Analysis** using custom entropy calculations and/or `zxcvbn`
- ✅ **Custom Wordlist Generation** using user inputs (e.g., name, date, pet name)
- ✅ **Leetspeak Variants** and pattern generation (e.g., `p@ssw0rd123`)
- ✅ **Export Wordlist** in `.txt` format (for tools like Hydra, John, etc.)
- ✅ **Command-Line Interface (CLI)** using `argparse`
- ✅ Optional GUI with `tkinter` 

---

## 🛠 Tech Stack

- **Python 3.8+**
- `argparse` – for CLI
- `nltk` – for text manipulation
- `zxcvbn-python` – for password scoring
- `tkinter` *(optional GUI)*
- `itertools`, `re`, `string` – standard Python libs

---
