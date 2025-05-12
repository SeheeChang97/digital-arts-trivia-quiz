import tkinter as tk

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

window = tk.Tk()
window.title("Digital Arts Trivia Quiz")
window.geometry("600x400")

window.mainloop()