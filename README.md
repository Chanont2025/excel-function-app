
# 📊 Excel Function Explorer

A user-friendly web app to **explore Excel functions interactively**. Built with [Streamlit](https://streamlit.io), this app enables users to search Excel formulas, view categorized lists, see syntax and examples, and follow step-by-step tutorials.

## 🚀 Features

- 🔍 Real-time search with autocomplete
- 📂 Browse functions by category
- ⭐ Bookmark your favorite functions (future version)
- 📘 View descriptions, syntax, examples, and tutorials
- 📤 Upload your own CSV file with function data

## 📁 Project Structure

```
excel_function_app/
├── streamlit_app.py          # Main Streamlit app
├── load_data.py              # Functions to load default/uploaded CSV
├── utils.py                  # Utilities for search and filtering
├── components.py             # UI rendering logic
├── requirements.txt          # Python dependencies
└── Excel_functions_EN.csv    # Sample dataset
```

## 📄 CSV Format

Your CSV file must follow this structure:

| Function Name | Description | Syntax | Example | Category | Tutorial |
|---------------|-------------|--------|---------|----------|----------|
| TEXT          | Converts a value to text | TEXT(value, format_text) | TEXT(1234.567, "0.00") | Text Functions | Step-by-step instructions... |

- The `Tutorial` column supports multi-line text separated by `\n`

## 🧪 Installation & Usage

1. Clone the repository:
```bash
git clone https://github.com/your-username/excel-function-app.git
cd excel-function-app
```

2. Install the dependencies:
```bash
pip install -r requirements.txt
```

3. Run the app:
```bash
streamlit run streamlit_app.py
```

## 🖼️ Screenshot

> _(Add a screenshot of the app UI here)_

## 📦 Dependencies

- streamlit
- pandas
- pyperclip


## 🪪 License

This project is licensed under the MIT License.
