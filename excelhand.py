import pandas as pd

def handle_excel_command(file_path: str):
    try:
        xl = pd.ExcelFile(file_path)
        return f"✅ Found sheets: {xl.sheet_names}"
    except Exception as e:
        return f"❌ Error reading Excel: {str(e)}"