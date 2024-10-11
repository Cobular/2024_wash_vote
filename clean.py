import re
from typing import List, Tuple
import glob
import os

def process_markdown(content: str) -> str:
    lines: List[str] = content.split('\n')
    first_h1_found: bool = False
    processed_lines: List[str] = []
    
    for line in lines:
        if line.strip().startswith('# '):
            if not first_h1_found:
                processed_lines.append(line)
                first_h1_found = True
        else:
            processed_lines.append(line)
    
    return '\n'.join(processed_lines)

def process_file(file_path: str) -> None:
    with open(file_path, 'r', encoding='utf-8') as file:
        content: str = file.read()
    
    processed_content: str = process_markdown(content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(processed_content)

def process_files(glob_pattern: str) -> None:
    for file_path in glob.glob(glob_pattern):
        process_file(file_path)
        print(f"Processed and updated: {file_path}")

def main() -> None:
    glob_pattern: str = 'src/pages/measures/*.md'
    process_files(glob_pattern)

if __name__ == "__main__":
    main()