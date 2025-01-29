AI Code Reviewer

Overview

The AI Code Reviewer is a Python-based tool that analyzes Python code files for syntax errors and coding style issues using Pylint. It provides a Streamlit UI where users can input a folder path, review Python files, and download a detailed CSV report of the code analysis.

Features

✅ Syntax Error Detection – Identifies and reports Python syntax errors.✅ Pylint Score Calculation – Evaluates code quality using Pylint.✅ Batch File Processing – Reviews all .py files in a specified folder.✅ Streamlit UI – User-friendly interface for easy code review.✅ Downloadable CSV Report – Exports results for further analysis.

Installation

1. Clone the Repository

 git clone https://github.com/YadneshR/ai-code-reviewer.git
 cd ai-code-reviewer

2. Install Dependencies

pip install streamlit pandas pylint

Usage

Run the Streamlit App

streamlit run ai_code_reviewer.py

Steps to Use the App

Enter the folder path containing .py files.

Click Analyze to review the files.

View the Code Review Report in the UI.

Download the CSV report for reference.

Example Output

File Name

Syntax Check

Pylint Score

script.py

No syntax errors

8.5

app.py

Syntax error: Unexpected EOF

6.2

Contributing

Feel free to fork the repository, submit issues, and contribute enhancements!

License

This project is open-source under the MIT License.

