import os
import re
from bs4 import BeautifulSoup

PATH_FILE_1 = "el.html"
PATH_FILE_2 = "en.html"
PATH_OUTPUT = "output.html"

def is_unwanted_marker(text):
    """Checks if a string is just a standalone marker (number/letter)"""

    t = text.strip()
    # Matches (1), (a), β), 1., etc. using Unicode word characters (\w)
    if re.match(r'^\([\w]+\)$', t, re.IGNORECASE) or \
       re.match(r'^[\w]+\)$', t, re.IGNORECASE) or \
       re.match(r'^[\w]+\.$', t, re.IGNORECASE) or \
       (len(t) <= 2 and t.isalnum()):
        return True
    return False

def extract_paragraphs(file_path):
    """Opens an HTML file and extracts strictly the <p> tags."""
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return []
        
    with open(file_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    text_blocks = []
    for tag in soup.find_all('p'):
        text = tag.get_text(strip=True)
        if text and not is_unwanted_marker(text):
            text_blocks.append(text)
            
    return text_blocks

def main():
    # 1. Extract text from the hardcoded paths
    text1 = extract_paragraphs(PATH_FILE_1)
    text2 = extract_paragraphs(PATH_FILE_2)
    
    if not text1 or not text2:
        return

    # 2. Generate the HTML file
    with open(PATH_OUTPUT, 'w', encoding='utf-8') as out:
        out.write("<html><head><meta charset='utf-8'><style>\n")
        out.write("body { font-family: Times New Roman, sans-serif; max-width: 800px; margin: auto; padding: 20px; line-height: 1.5; text-align: justify; }\n");
        out.write(".lang1 { color: #000; font-weight: bold; margin-top: 20px; font-size: 16px; }\n")
        out.write(".lang2 { color: #555; font-style: italic; margin-bottom: 20px; padding-bottom: 15px; border-bottom: 1px solid #eee; font-size: 15px; }\n")
        out.write("</style></head><body>\n")
        
        # 3. Zip the lists together
        for l1, l2 in zip(text1, text2):
            out.write(f'<div class="lang1">{l1}</div>\n')
            out.write(f'<div class="lang2">{l2}</div>\n')
            
        out.write("</body></html>\n")
        
    print(f"Success!")

if __name__ == "__main__":
    main()
