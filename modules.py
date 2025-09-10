import json
from json import JSONDecodeError
from rich.table import Table
from rich.console import Console
from documentation_class import Documentation

DATABASE = "data.json"

console = Console()

def _load_all():
    try:
        with open(DATABASE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, JSONDecodeError):
        return []

def _save_all(docs):
    with open(DATABASE, "w", encoding="utf-8") as file:
        json.dump(docs, file, indent=4, ensure_ascii=False)

def next_id(existing_data):
    """Handle records that might not have an id yet"""
    ids = [doc.get("doc_id") for doc in existing_data if isinstance(doc, dict) and isinstance(doc.get("doc_id"), int)]
    return (max(ids) + 1) if ids else 1

def list_documentation():
    data = _load_all()
    if not data:
        console.print("[bold red]No docs are listed yet. Go ahead and add one![/]")
        return

    table = Table(title="Documentation To Read")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Status", style="green")
    table.add_column("Link", style="blue")

    for doc in data:
        table.add_row(
            str(doc.get("doc_id", "?")),
            doc.get("title", "(no title)"),
            doc.get("status", "NOT_STARTED"),
            doc.get("link", "")
        )

    console.print(table)

def create_documentation():
    title = input("Input the title: ").strip()
    link = input("Input the link: ").strip()
    status = input("Input the status (NOT_STARTED, IN_PROGRESS, COMPLETED): ").strip().upper()

    if status not in Documentation.VALID:
        print("Invalid status. Defaulting to NOT_STARTED")
        status = "NOT_STARTED"

    existing_data = _load_all()
    doc_id = next_id(existing_data)

    """Create new documentation object with an ID"""
    new_doc = Documentation(doc_id, title, link, status)

    """Append serialized dict"""
    existing_data.append(new_doc.to_dict())
    _save_all(existing_data)

    print(f"📄 New document created: [{new_doc.doc_id}] {new_doc.title} ({new_doc.status})")
    return new_doc


