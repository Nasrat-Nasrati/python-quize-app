import tkinter as tk
from tkinter import messagebox
import json
import random
from quiz_logic import calculate_score

# Load questions
with open("real_questions.json", "r") as file:
    all_questions = json.load(file)

selected_questions = random.sample(all_questions, 30)
question_vars = []  # لیست متغیرهای ذخیره‌کننده انتخاب کاربر

# تنظیم پنجره اصلی
window = tk.Tk()
window.title("Benefits Exam Application")

# حالت تمام‌صفحه
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f"{screen_width}x{screen_height}")

# ایجاد اسکرول‌بار و کانواس
canvas = tk.Canvas(window)
scrollbar = tk.Scrollbar(window, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

def complete_exam():
    selected_answers = [var.get() for var in question_vars]
    score, max_score = calculate_score(selected_questions, selected_answers)
    messagebox.showinfo("Exam Completed", f"Final Score: {score:.2f} / {max_score}")

# ایجاد سوالات (بدون انتخاب پیش‌فرض)
for idx, question in enumerate(selected_questions):
    frame = tk.Frame(scrollable_frame)
    frame.pack(anchor="w", pady=5, padx=10)

    tk.Label(
        frame,
        text=f"{idx+1}. {question['question']}",
        wraplength=screen_width - 100,
        justify="left",
        font=("Arial", 14)
    ).pack(anchor="w")

    var = tk.StringVar(value="")  # مقدار اولیه خالی
    question_vars.append(var)

    for option in question["options"]:
        if not option.strip():  # رد کردن گزینه‌های خالی
            continue
        tk.Radiobutton(
            frame,
            text=option,
            variable=var,
            value=option,
            font=("Arial", 12)
        ).pack(anchor="w")

# دکمه ارسال
submit_btn = tk.Button(
    scrollable_frame,
    text="Complete Exam",
    command=complete_exam,
    bg="green",
    fg="white",
    font=("Arial", 13)
)
submit_btn.pack(pady=30)

window.mainloop()