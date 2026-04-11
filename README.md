# EUR-Lex Bilingual Parallel Generator

This project provides a lightweight, universal Python command-line tool that processes official HTML publications from **EUR-Lex** (such as the EU AI Act, GDPR, etc.) and generates a clean, maind bilingual document. 

It is designed to facilitate the cross-checking of precise terminology and phrasing between any two EU languages, paragraph by paragraph.

## Features
* **Universal Language Support:** Uses smart Regular Expressions (Regex) that automatically detect and filter out formatting noise (like list letters `(a), (β), (ö)` or numbers `(140)`) across all EU languages, preventing alignment drift.
* **Direct HTML Parsing:** Reads directly from raw EUR-Lex HTML files.
* **Command-Line Interface (CLI):** Easily specify your input files and custom output names directly from the terminal without editing the code.
* **Print-Ready HTML:** Generates a lightweight HTML file styled for readability, which can be instantly printed to PDF via any web browser.

## Project Structure
```text
lex-aligner/
├── main.py                 # main Python parsing script
├── requirements.txt        # python dependencies (BeautifulSoup4)
└── README.md               # project documentation
```

## Installation & Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/sofilip/lex-aligner
   cd lex-aligner/   
   ```

2. Create a virtual environment (Recommended):
   ```bash
   python -m venv lex-aligner-venv
   source lex-aligner-venv/bin/activate  # On Windows use: lex-aligner-venv\Scripts\activate
   ```

3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

**Step 1: Download your source files**
Go to [EUR-Lex](https://eur-lex.europa.eu/homepage.html) and download the HTML, webpage-only versions of your desired document in two languages. Save them to your project folder (e.g., `el.html` and `en.html`).

**Step 2: Run the script via the terminal**
```bash
python3 main.py el.html en.html -o output.html
```

## Converting to PDF
Once the script finishes, open your generated HTML file in any modern web browser (Chrome, Edge, Firefox). Press `Ctrl+P` (or `Cmd+P` on Mac) and select **"Save as PDF"** for a perfectly formatted, offline legal document.
