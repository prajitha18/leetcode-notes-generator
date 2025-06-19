import os

INPUT_FOLDER = "sample_inputs"
OUTPUT_FOLDER = "outputs"

def read_input(file_name):
    input_path = os.path.join(INPUT_FOLDER, file_name)
    print(f"Reading from: {input_path}")
    with open(input_path, 'r', encoding='utf-8') as f:
        return f.read()

def split_sections(text):
    try:
        problem_part = text.split("Problem:")[1].split("Approach:")[0].strip()
        approach_part = text.split("Approach:")[1].split("Code:")[0].strip()
        code_part = text.split("Code:")[1].strip()
        print("Input split successful")
        return problem_part, approach_part, code_part
    except Exception as e:
        print("Error: Failed to split the input properly.", e)
        return "", "", ""

def write_markdown(file_name, problem, approach, code):
    md = f"# Problem\n\n{problem}\n\n---\n\n## Approach\n\n{approach}\n\n---\n\n## Code\n\n```python\n{code}\n```"
    output_path = os.path.join(OUTPUT_FOLDER, file_name.replace(".txt", ".md"))
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"Markdown written to: {output_path}")

if __name__ == "__main__":
    file_name = "example1.txt"
    text = read_input(file_name)
    print(f"File content:\n{text}\n---")
    problem, approach, code = split_sections(text)
    write_markdown(file_name, problem, approach, code)
