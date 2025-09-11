import os
import json
from json import JSONDecodeError
from rich.table import Table
from rich.console import Console
from .documentation_class import Documentation

# Resolve path to data.json inside the package root
PACKAGE_DIR = os.path.dirname(__file__)
DATABASE = os.path.join(PACKAGE_DIR, "..", "..", "data.json")
DATABASE = os.path.abspath(DATABASE)

console = Console()

def _load_all():
    try:
        with open(DATABASE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data if isinstance(data, list) else []
    except (FileNotFoundError, JSONDecodeError):
        return []

def _load_one(target_doc_id: int):
    existing_data = _load_all()
    return next((doc for doc in existing_data if doc.get("doc_id") == target_doc_id), None)

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
        print("⚠️ Invalid status. Defaulting to NOT_STARTED.")
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

def update_documentation():
    try:
        doc_to_update_id = int(input("Enter the ID you would like to update: "))
    except ValueError as e:
        print(f"❌  Invalid Input: {e}. Please enter a valid ID.")
        return

    existing_data = _load_all()
    doc_to_update = next((doc for doc in existing_data if doc.get("doc_id") == doc_to_update_id), None)

    if doc_to_update is None:
        print(f"❌ Unable to find document with ID: {doc_to_update_id}")
        return

    title_update = input(f"Update your title [{doc_to_update['title']}]: ").strip() or doc_to_update["title"]
    link_update = input(f"Update your link [{doc_to_update['link']}]: ").strip() or doc_to_update["link"]
    status_update = input(f"Update your status [{doc_to_update['status']}]: ").strip().upper() or doc_to_update["status"]

    if status_update not in Documentation.VALID:
        print("⚠️ Invalid status. Defaulting to NOT_STARTED.")
        status = "NOT_STARTED"

    """Apply updates"""
    doc_to_update["title"] = title_update
    doc_to_update["link"] = link_update
    doc_to_update["status"] = status_update

    _save_all(existing_data)

    print(f"✅ Updated document {doc_to_update_id}: {title_update} ({status_update})")

def delete_documentation():
    try:
        doc_to_delete_id = int(input("Enter the ID you would like to delete: "))
    except ValueError as e:
        print("❌ Invalid Input. Please enter a valid numeric ID.")
        return

    existing_data = _load_all()

    # Filter out the record with the matching ID
    new_data = [doc for doc in existing_data if doc.get("doc_id") != doc_to_delete_id]

    if len(new_data) < len(existing_data):
        _save_all(new_data)
        print(f"✅ Document with ID {doc_to_delete_id} has been removed.")
    else:
        print(f"❌ Unable to find document with ID: {doc_to_delete_id}")
