import tkinter as tk
from tkinter import messagebox

current_question = 0
score = 0

def next_question():
    global current_question, score
    selected = answer_var.get()
    if selected == questions[current_question]["answer"]:
        score += 1
    current_question += 1
    if current_question >= len(questions):
        messagebox.showinfo("Quiz Finished", f"Your final score is {score} out of {len(questions)}.")
        window.quit()
    else:
        load_question()

questions = [
    {
        "question": "Which tool in Photoshop is used to remove blemishes and imperfections?",
        "choices": ["Clone Stamp", "Healing Brush", "Eraser", "Smudge Tool"],
        "answer": 1
    },
    {
        "question": "Which principle in design refers to equal visual weight in a composition?",
        "choices": ["Unity", "Balance", "Contrast", "Emphasis"],
        "answer": 1
    },
    {
        "question": "RGB in digital design stands for what?",
        "choices": ["Red Green Black", "Red Gold Blue", "Red Green Blue", "Raster Graphic Bitmap"],
        "answer": 2
    },
    {
        "question": "Which software is mainly used for raster image editing?",
        "choices": ["Adobe Illustrator", "Photoshop", "After Effects", "InDesign"],
        "answer": 1
    },
    {
        "question": "What does DPI stand for in digital images?",
        "choices": ["Dots Per Inch", "Depth Per Image", "Design Pixel Integration", "Data Pixel Index"],
        "answer": 0
    },
    {
        "question": "Which of these is commonly used for vector graphic design?",
        "choices": ["Photoshop", "After Effects", "Illustrator", "Premiere Pro"],
        "answer": 2
    },
    {
        "question": "What color mode is typically used for web images?",
        "choices": ["CMYK", "Grayscale", "HSB", "RGB"],
        "answer": 3
    },
    {
        "question": "Which format supports transparency?",
        "choices": ["JPG", "PNG", "TIFF", "BMP"],
        "answer": 1
    },
    {
        "question": "Which artist is known for pioneering digital glitch art?",
        "choices": ["Andy Warhol", "Rafaël Rozendaal", "Frida Kahlo", "Jackson Pollock"],
        "answer": 1
    },
    {
        "question": "What design principle refers to differences in elements to create visual interest?",
        "choices": ["Balance", "Contrast", "Repetition", "Alignment"],
        "answer": 1
    }
]

def load_question():
    q = questions[current_question]
    question_label.config(text=q["question"])
    for i, choice in enumerate(q["choices"]):
        radio_buttons[i].config(text=choice, value=i)
    answer_var.set(-1)

question_label = tk.Label(window, text="", font=("Arial", 14), wraplength=500, justify="left")
question_label.pack(pady=20)

answer_var = tk.IntVar()
radio_buttons = []
for i in range(4):
    rb = tk.Radiobutton(window, text="", variable=answer_var, value=i)
    rb.pack()
    radio_buttons.append(rb)

next_button = tk.Button(window, text="Next", command=next_question)
next_button.pack()


window = tk.Tk()
window.title("Digital Arts Trivia Quiz")
window.geometry("600x400")

window.mainloop()