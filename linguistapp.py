import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from googletrans import Translator, LANGUAGES
import random

# Setup
translator = Translator()
root = tk.Tk()
root.title("🌐 Linguist - Language Converter")
root.geometry("750x600")
root.config(bg="#FFFAF0")  # Vibrant light background

# Gradient background color options
colors = ['#FDEFF9', '#E0C3FC', '#C9FFBF', '#B5FFFC', '#FFFACD']
root.config(bg=random.choice(colors))

# ---------- Title ----------
title = tk.Label(root, text="✨ Linguist", font=("Helvetica", 32, "bold"), bg=root['bg'], fg="#333")
title.pack(pady=20)

desc = tk.Label(root, text="Your Personal Multilingual Translator", font=("Arial", 14), bg=root['bg'], fg="#444")
desc.pack()

# ---------- Language Dropdown ----------
lang_codes = {v.title(): k for k, v in LANGUAGES.items()}
lang_frame = tk.Frame(root, bg=root['bg'])
lang_frame.pack(pady=20)

lang_label = tk.Label(lang_frame, text="🌍 Select Language:", font=("Arial", 12), bg=root['bg'])
lang_label.pack(side=tk.LEFT, padx=5)

lang_dropdown = ttk.Combobox(lang_frame, values=list(lang_codes.keys()), width=30, state="readonly")
lang_dropdown.set("Choose language")
lang_dropdown.pack(side=tk.LEFT)

# ---------- Result Frame ----------
result_frame = tk.Frame(root, bg=root['bg'])
result_box = tk.Text(result_frame, height=10, width=70, font=("Arial", 12), wrap="word", bd=3, relief="ridge")

# ---------- Buttons ----------
def enter_text_popup():
    user_text = simpledialog.askstring("📝 Enter Text", "Enter the text to translate:", parent=root)
    if user_text:
        translate_text(user_text)

def translate_text(user_text):
    language = lang_dropdown.get()
    if language == "Choose language":
        messagebox.showwarning("⚠️ Oops!", "Please select a language before translating.")
        return

    try:
        translated = translator.translate(user_text, dest=lang_codes[language])
        show_translation_popup(translated.text)
    except Exception as e:
        messagebox.showerror("❌ Translation Error", str(e))

def show_translation_popup(translated_text):
    result_frame.pack(pady=15)
    result_box.delete("1.0", tk.END)
    result_box.insert(tk.END, translated_text)
    result_box.pack()
    result_box.after(100, lambda: result_box.config(bg="#e0ffe0"))  # green fade

    # Show action buttons
    try_again_btn.pack(side=tk.LEFT, padx=10)
    clear_btn.pack(side=tk.LEFT, padx=10)

def confirm_exit():
    result = messagebox.askyesno("👋 Exit Linguist", "Are you sure you want to leave?")
    if result:
        animated_exit()

def animated_exit():
    for i in range(10, 0, -1):
        root.attributes("-alpha", i/10)
        root.update()
        root.after(50)
    root.destroy()

def clear_translation():
    result_box.delete("1.0", tk.END)
    result_box.pack_forget()
    try_again_btn.pack_forget()
    clear_btn.pack_forget()
    messagebox.showinfo("✅ Cleared", "You can now enter new text to translate.")

# ---------- Button Frame ----------
btn_frame = tk.Frame(root, bg=root['bg'])
btn_frame.pack(pady=20)

enter_btn = tk.Button(btn_frame, text="✍️ Enter Text", command=enter_text_popup,
                      font=("Arial", 12, "bold"), bg="#87CEFA", fg="black", width=15)
enter_btn.pack(side=tk.LEFT, padx=10)

exit_btn = tk.Button(btn_frame, text="❌ Leave", command=confirm_exit,
                     font=("Arial", 12, "bold"), bg="#FF6B6B", fg="white", width=15)
exit_btn.pack(side=tk.LEFT, padx=10)

# ---------- Action Buttons (appear after translation) ----------
action_btn_frame = tk.Frame(root, bg=root['bg'])
action_btn_frame.pack(pady=10)

try_again_btn = tk.Button(action_btn_frame, text="🔁 Try Again", command=enter_text_popup,
                          font=("Arial", 11), bg="#FFD700", fg="black", width=15)

clear_btn = tk.Button(action_btn_frame, text="🧹 Clear Translation", command=clear_translation,
                      font=("Arial", 11), bg="#B0E0E6", fg="black", width=18)

# ---------- Run ----------
root.mainloop()
