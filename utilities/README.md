# 🛠️ Utilities

This directory contains **practical, task-based Python scripts** designed to automate or simplify everyday workflows.  
Each utility serves a focused purpose, from extracting data to transforming files or interacting with external systems.

These scripts are typically:
- Small and self-contained
- Built for reusability or one-off tasks
- Focused on **real-world usefulness** rather than deep language exploration

---

## 📁 Example Use Cases

| Script | Description |
|--------|-------------|
| `extract_subtitles.py` | Download subtitles from a YouTube video using `pytube` or similar libraries |
| `db_to_excel.py` | Connect to a database and export a query result to Excel using `pymysql` and `openpyxl` |
| `rename_files.py` | Batch rename files in a directory based on a pattern |
| `fetch_weather.py` | Pull weather data from an open API and save it as JSON or CSV |
| `json_cleaner.py` | Pretty-print or normalize large JSON files for inspection or comparison |

---

## 📦 Structure Suggestions

Each utility can live in its own subdirectory if needed:

```

utilities/
├── extract\_subtitles/
│   ├── extract\_youtube.py
│   └── requirements.txt
├── export\_db\_to\_excel/
│   ├── export.py
│   └── config.json
├── rename\_files/
│   └── rename\_batch.py

````

---

## 🧰 How to Use

- Most scripts can be run directly with `python script.py`
- Some may require dependencies listed in `requirements.txt`
- You can create virtual environments per subdirectory if needed

```bash
cd utilities/extract_subtitles
python extract_youtube.py
````

---

## ✏️ Contributing

This is a personal space, but feel free to adapt or extend the scripts.
If you want to structure your own utilities, follow the same pattern:
*Keep it simple, self-contained, and well-documented.*

---

## 📜 License

MIT License — feel free to reuse and adapt these utilities for personal or professional use.
