# Python Utility Scripts

This repository contains standalone and somewhat random Python scripts designed for various tasks:

## dogger.py

Queries and displays DNS records for a specified domain using the [`dog`](https://github.com/ogham/dog) command-line tool. Results are shown in a formatted table using the [`rich`](https://github.com/Textualize/rich) library.

- **Features:**
  - Looks up common DNS record types (A, AAAA, MX, CNAME, TXT, NS, SOA, SRV, PTR, DNSKEY)
  - Handles errors and timeouts gracefully
  - Presents results in a visually appealing table

- **Requirements:**  
  - Python 3.7+
  - [`dog`](https://github.com/ogham/dog) DNS client (must be installed and in your PATH)
  - [`rich`](https://pypi.org/project/rich/) Python library

- **Usage:**

## inbox.py

Appends timestamped notes to a designated Obsidian inbox/scratch file. Prompts for multi-line input, timestamps the entry, and formats it as a bullet list.

- **Features:**
- Multi-line note entry with timestamp
- Appends to a configurable file (default is an Obsidian vault scratch file)
- Each note is a top-level bullet with sub-bullets for each line

- **Requirements:**  
- Python 3.7+

- **Usage:**
Follow the prompt to enter your note. End input with a blank line.

---

## License

MIT License
