import subprocess
import datetime
import os
import tkinter as tk
from tkinter import filedialog, messagebox

INPUT_FOLDER = "sample_inputs"
OUTPUT_FOLDER = "outputs"

def split_sections(text):
    try:
        topic = text.split("Topic:")[1].split("Problem:")[0].strip()
        problem = text.split("Problem:")[1].split("Approach:")[0].strip()
        approach = text.split("Approach:")[1].split("Code:")[0].strip()
        code = text.split("Code:")[1].strip()
        return topic, problem, approach, code
    except Exception as e:
        return "", "", "", ""

def write_markdown(file_name, topic, problem, approach, code):
    md = f"# Problem\n\n{problem}\n\n---\n\n## Approach\n\n{approach}\n\n---\n\n## Code\n\n```python\n{code}\n```"
    topic_folder = os.path.join(OUTPUT_FOLDER, topic)
    os.makedirs(topic_folder, exist_ok=True)
    output_path = os.path.join(topic_folder, file_name.replace(".txt", ".md"))
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)
    return output_path

def browse_file():
    filepath = filedialog.askopenfilename(initialdir=INPUT_FOLDER, title="Select Input File", filetypes=[("Text Files", "*.txt")])
    if filepath:
        file_label.config(text=filepath)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        text_preview.delete(1.0, tk.END)
        text_preview.insert(tk.END, content)
        convert_button.config(state=tk.NORMAL)

def convert_file():
    filepath = file_label.cget("text")
    if not filepath.endswith(".txt"):
        messagebox.showerror("Error", "Please select a .txt file")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    topic, problem, approach, code = split_sections(content)
    if not all([topic, problem, approach, code]):
        messagebox.showerror("Format Error", "One or more sections are missing.")
        return

    filename = os.path.basename(filepath)
    output_path = write_markdown(filename, topic, problem, approach, code)
    messagebox.showinfo("Success", f"Markdown created at:\n{output_path}")

def push_to_github():
    try:
        commit_message = f"Auto: Add notes - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}"
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        messagebox.showinfo("Success", "Changes pushed to GitHub!")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Git Error", f"Failed to push:\n{e}")

# GUI Setup
root = tk.Tk()
root.title("LeetCode Notes Generator")
root.geometry("700x500")

title_label = tk.Label(root, text="LeetCode Notes Generator (GUI)", font=("Arial", 16))
title_label.pack(pady=10)

browse_button = tk.Button(root, text="Browse .txt File", command=browse_file)
browse_button.pack()

file_label = tk.Label(root, text="No file selected", wraplength=600)
file_label.pack(pady=5)

text_preview = tk.Text(root, height=15, width=80)
text_preview.pack(pady=10)

convert_button = tk.Button(root, text="Convert to Markdown", command=convert_file, state=tk.DISABLED)
convert_button.pack()

push_button = tk.Button(root, text="Push to GitHub", command=push_to_github)
push_button.pack(pady=5)

root.mainloop()
# Verified commit identity for prajitha18
