import tkinter as tk
from tkinter import messagebox
from zxcvbn import zxcvbn
from analyzer import password_entropy

def check_strength():
    password = entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password.")
        return

    result = zxcvbn(password)
    score = result['score']  # 0 to 4
    feedback = result['feedback']['warning'] or "Good password!"

    entropy = password_entropy(password)

    strength_label.config(text=f"Score: {score}/4\nEntropy: {entropy:.2f}\n{feedback}")

# GUI Setup
root = tk.Tk()
root.title("🔐 Password Strength Analyzer")
root.geometry("400x250")
root.resizable(False, False)

title = tk.Label(root, text="Enter your password:", font=("Arial", 14))
title.pack(pady=10)

entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack(pady=5)

check_btn = tk.Button(root, text="Check Strength", command=check_strength, font=("Arial", 12))
check_btn.pack(pady=10)

strength_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
strength_label.pack(pady=10)

root.mainloop()
