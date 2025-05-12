import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk 
from PIL import ImageFilter, ImageEnhance, ImageDraw

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

current_question = 0
score = 0

def load_question():
    q = questions[current_question]
    question_label.config(text=q["question"])
    for i, choice in enumerate(q["choices"]):
        radio_buttons[i].config(text=choice, value=i)
    answer_var.set(-1)

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

def main():
    global window, question_label, answer_var, radio_buttons

    window = tk.Tk()
    window.title("Digital Arts Trivia Quiz")
    window.geometry("600x400")

    bg_image = Image.open("background.jpg")  
    bg_image = bg_image.resize((600, 400), Image.Resampling.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = tk.Label(window, image=bg_photo)
    bg_label.image = bg_photo
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

    question_label = tk.Label(
        window, text="", font=("Arial", 14), wraplength=500, justify="left", bg="#ffffff", padx=10, pady=10
    )
    question_label.place(x=50, y=30)

    answer_var = tk.IntVar()
    radio_buttons = []
    for i in range(4):
        rb = tk.Radiobutton(
            window, text="", variable=answer_var, value=i, font=("Arial", 12),
            bg="#ffffff", activebackground="#f7cfe3", anchor="w"
        )
        rb.place(x=70, y=100 + i * 30)
        radio_buttons.append(rb)

    next_button = tk.Button(
        window,
        text="Next",
        command=next_question,
        font=("Arial", 12, "bold"),
        bg="#f7cfe3",  
        activebackground="#f4b9d7",
        relief="raised",
        borderwidth=2,
        padx=10,
        pady=5
    )
    next_button.place(x=250, y=270)

    load_question()
    window.mainloop()

if __name__ == "__main__":
    main()