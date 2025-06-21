LeetCode Notes Generator

A Python-based automation script that converts LeetCode problem text into structured Markdown notes — perfect for revision, documentation, or GitHub uploads.

Features
 Converts problem description into clean markdown
 Auto-generates headings like `Problem`, `Approach`, and `Code`
 Saves notes in organized folders

Tech Stack
 Python
 OS module, basic file handling

Setup Instructions
```bash
git clone https://github.com/prajitha18/leetcode-notes-generator.git
cd leetcode-notes-generator
python main.py
---

Why This Project?
Most students only solve problems. This tool helps me:

-   Document my solutions smartly  
-   Revise faster  
-   Share organized notes on GitHub  

> This is part of my journey toward FAANG internships (2026).

---

##  Want to Contribute?

You can help improve this by adding:

-  Web scraping from LeetCode  
-  GUI to select problems  
-  Auto-upload to GitHub  

Fork it, build it, and raise a PR!
---

## GUI Version

If you prefer a graphical interface:

### How to Use:

```bash
python gui_main.py
```

This will open a window where you can:

- Select `.txt` problem files
- Preview the content
- Convert to clean Markdown format

Make sure your `.txt` files follow this format:

```
Topic: Arrays
Problem: ...
Approach: ...
Code: ...
```

### File Example:

```
leetcode-notes-generator/
├── gui_main.py
├── main.py
├── sample_inputs/
│   └── example1.txt
├── outputs/
│   └── Arrays/
│       └── example1.md
└── README.md
```
