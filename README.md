# 📚 Docs To Read CLI

A lightweight command-line tool for tracking documentation, guides, and articles you want to read.
Built with Python, `rich` for beautiful output, and stored locally in a JSON file.

---

## ✨ Features

- Add documentation records with **title, link, and status**
- Track progress with statuses:
  - `NOT_STARTED`
  - `IN_PROGRESS`
  - `COMPLETED`
- Automatically assigns IDs to each record
- List your documentation in a **clean, colored table**
- Data saved locally in a `data.json` file (or configurable path)

---

## 📦 Installation

Clone the repository and install in editable mode:

```bash
git clone https://github.com/yourusername/docs-to-read-cli.git
cd docs-to-read-cli
pip install -e .
```

This will install the global command:
```bash
docs
```

## 🖥️ Usage

From there you can:
- List Docs – view all saved documentation
- Add Doc – input a new title, link, and status
- Update Doc (coming soon)
- Delete Doc (coming soon)

## 🗂️ Data Storage

By default, your data is stored in:
- `data.json` inside the project root (dev mode)
- or configurable to `~/.docs_to_read.json` in your home directory for global use

You can override the database path with an environment variable:
```bash
export DOCS_DB_PATH=~/my_custom_docs.json
```

## 🛠️ Development

Install dependencies for development:
```bash
pip install -r requirements.txt
```

Run the CLI in debug mode:
```bash
python src/docs_cli/main.py
```

## 🚀 Roadmap

- Add update functionality
- Add delete functionality
- Support search/filter
- Export to CSV/Markdown
- Package to PyPI for pip install docs-to-read-cli

## 🤝 Contributing
Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to add or change.

## 📄 License
MIT License © 2025 David Martin

This gives you:
- ✅ Clear project intro
- ✅ Install & usage instructions
- ✅ Data details (since you had that question already)
- ✅ Roadmap section for “future plans”
- ✅ License placeholder

