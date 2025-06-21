import os

INPUT_FOLDER = "sample_inputs"
OUTPUT_FOLDER = "outputs"

def read_input(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def split_sections(text):
    try:
        topic = text.split("Topic:")[1].split("Problem:")[0].strip()
        problem = text.split("Problem:")[1].split("Approach:")[0].strip()
        approach = text.split("Approach:")[1].split("Code:")[0].strip()
        code = text.split("Code:")[1].strip()
        return topic, problem, approach, code
    except Exception as e:
        print("Error: Could not split input properly.", e)
        return "", "", "", ""

def write_markdown(file_name, topic, problem, approach, code):
    md = f"# Problem\n\n{problem}\n\n---\n\n## Approach\n\n{approach}\n\n---\n\n## Code\n\n```python\n{code}\n```"
    topic_folder = os.path.join(OUTPUT_FOLDER, topic)
    os.makedirs(topic_folder, exist_ok=True)
    output_path = os.path.join(topic_folder, file_name.replace(".txt", ".md"))
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(md)
    print(f"Converted: {file_name} → {topic}/{file_name.replace('.txt', '.md')}")

if __name__ == "__main__":
    for file_name in os.listdir(INPUT_FOLDER):
        if file_name.endswith(".txt"):
            file_path = os.path.join(INPUT_FOLDER, file_name)
            text = read_input(file_path)
            topic, problem, approach, code = split_sections(text)
            if topic and problem and approach and code:
                write_markdown(file_name, topic, problem, approach, code)
            else:
                print(f"Skipped: {file_name} due to missing or incomplete sections.")
