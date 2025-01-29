import os
import re
import ast
import difflib
import pandas as pd
import pylint.lint
import streamlit as st

class CodeReviewer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.code_files = []
        self.reports = []
    
    def load_code_files(self):
        for file in os.listdir(self.folder_path):
            if file.endswith(".py"):
                file_path = os.path.join(self.folder_path, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    code = f.read()
                self.code_files.append((file, code))
    
    def analyze_code(self):
        for file, code in self.code_files:
            errors = self.check_syntax(code)
            style_issues = self.run_pylint(file)
            self.reports.append((file, errors, style_issues))
    
    def check_syntax(self, code):
        try:
            ast.parse(code)
            return "No syntax errors"
        except SyntaxError as e:
            return f"Syntax error: {e}"
    
    def run_pylint(self, file):
        results = pylint.lint.Run([os.path.join(self.folder_path, file)], do_exit=False)
        return results.linter.stats.global_note
    
    def generate_report(self, output_file='code_review_report.csv'):
        df = pd.DataFrame(self.reports, columns=['File', 'Syntax Check', 'Pylint Score'])
        df.to_csv(output_file, index=False)
        return df

# Streamlit UI
st.title("Python Code Reviewer")

folder_path = st.text_input("Enter the folder path containing Python files:")
if folder_path:
    reviewer = CodeReviewer(folder_path)
    reviewer.load_code_files()
    reviewer.analyze_code()
    df_report = reviewer.generate_report()
    st.write("### Code Review Report")
    st.dataframe(df_report)
    st.download_button("Download Report", df_report.to_csv(index=False), file_name="code_review_report.csv", mime="text/csv")
