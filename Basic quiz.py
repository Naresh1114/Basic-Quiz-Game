import tkinter as tk
from tkinter import messagebox

# Questions and Answers
questions = {
    "What is your name?": "naresh",
    "What is 2 + 2?": "4",
    "What is your age?": "24",
    "what is your fevarate subject'?": "python",
    "What is the boiling point of water?": "100"
}

# Initialize score and question index
score = 0
question_index = 0

# Function to check the answer
def check_answer():
    global score, question_index
    
    user_answer = answer_entry.get().strip()
    
    if user_answer.lower() == questions[current_question].lower():
        score += 1
        messagebox.showinfo("Result", "Correct!")
    else:
        messagebox.showinfo("Result", f"Wrong! The correct answer is {questions[current_question]}.")

    question_index += 1
    if question_index < len(questions):
        ask_question()
    else:
        messagebox.showinfo("Quiz Finished", f"Your final score is {score}/{len(questions)}.")
        root.quit()

# Function to display the current question
def ask_question():
    global current_question
    current_question = list(questions.keys())[question_index]
    question_label.config(text=current_question)
    answer_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Quiz Game")

# Create and place widgets
question_label = tk.Label(root, text="", wraplength=300)
question_label.pack(pady=50)

answer_entry = tk.Entry(root)
answer_entry.pack(pady=30)

submit_button = tk.Button(root, text="Submit Answer", command=check_answer)
submit_button.pack(pady=50)

# Start the quiz by asking the first question
ask_question()

# Run the application
root.mainloop()