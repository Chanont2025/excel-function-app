# 📊 Excel Function Explorer App (v1.0.1)

A secure, searchable, and extendable Streamlit app for exploring Microsoft Excel functions.

## 🔧 Features
- 🔐 Admin-only CSV upload
- 📁 Secure CSV loading from Google Drive using `gdown`
- 🔎 Search and filter Excel functions
- ✅ Designed for Streamlit Cloud deployment

## 🚀 How to Deploy

1. Clone this repo to Streamlit Cloud.
2. Set your `secrets.toml` with:
```toml
admin_mode = true
admin_password = "your_password"
[remote_file]
gdrive_file_id = "your_file_id_here"
```
3. File path: `excel_function_app/streamlit_app.py`

## 📦 Requirements
```
streamlit
pandas
gdown
```