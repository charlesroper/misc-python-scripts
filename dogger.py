"""
dogger.py — Query and display DNS records for a domain using the 'dog' command-line tool.

This script runs the 'dog' DNS client for a set of common record types and displays the results in a formatted table using the 'rich' library.

What is 'dog'?
----------------
'dog' is a modern command-line DNS client, similar to 'dig', but with a more user-friendly output and additional features.

Installation (Windows):
-----------------------
You can install 'dog' using either Scoop or Winget:

- Scoop:
    scoop install dog

- Winget:
    winget install ogham.dog

Ensure 'dog' is in your PATH so this script can invoke it.
"""
#!/usr/bin/env python3
import subprocess
import sys

from rich import box
from rich.console import Console
from rich.table import Table


def query_record(domain: str, record_type: str) -> str:
    """
    Runs the 'dog' command for a given domain and record type.
    Uses subprocess.Popen with start_new_session=True so that if the command
    hangs, it can be forcefully terminated after a timeout.
    """
    try:
        proc = subprocess.Popen(
            ["dog", domain, record_type],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            start_new_session=True,
        )
    except FileNotFoundError:
        return "[red]'dog' command not found. Please install it and ensure it is in your PATH.[/red]"
    except Exception as e:
        return f"[red]Error starting dog for {record_type}: {e}[/red]"

    try:
        output, _ = proc.communicate(timeout=5)
    except subprocess.TimeoutExpired:
        proc.kill()
        # Read whatever output is available
        output, _ = proc.communicate()
        return f"[red]Timeout expired for record type {record_type}[/red]"

    # Clean up the output: remove extra whitespace and replace literal "\n" with actual newlines
    output = output.strip().replace("\\n", "\n")
    if not output:
        return f"[yellow]No records found for record type {record_type}[/yellow]"
    return output


def main() -> None:
    if len(sys.argv) < 2:
        print(f"Usage: python {sys.argv[0]} <domain>")
        sys.exit(1)
    domain: str = sys.argv[1]
    record_types: list[str] = [
        "A",
        "AAAA",
        "MX",
        "CNAME",
        "TXT",
        "NS",
        "SOA",
        "SRV",
        "PTR",
        "DNSKEY",
    ]

    console: Console = Console()
    console.print(f"\n[bold underline]DNS Records for {domain}[/bold underline]\n")

    table: Table = Table(title="DNS Record Lookup", box=box.SIMPLE_HEAVY)
    table.add_column("Record Type", style="cyan", no_wrap=True)
    table.add_column("Result", style="magenta")

    for rt in record_types:
        result: str = query_record(domain, rt)
        table.add_row(f"[bold blue]{rt}[/bold blue]", result)

    console.print(table)


if __name__ == "__main__":
    main()
