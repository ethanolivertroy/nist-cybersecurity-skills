#!/usr/bin/env python3
"""
NIST Control Lookup Helper.

Quickly look up controls, definitions, or cross-references from the
generated reference files.

Usage:
    python scripts/lookup.py control AC-2
    python scripts/lookup.py control "AC-2(1)"
    python scripts/lookup.py family AC
    python scripts/lookup.py search "access control"
    python scripts/lookup.py baseline moderate AC
    python scripts/lookup.py map csf PR.AC
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REFERENCES_DIR = REPO_ROOT / "references"
ASSETS_DIR = REPO_ROOT / "assets"


def load_control_families():
    """Load control family metadata from assets."""
    families_path = ASSETS_DIR / "control-families.json"
    if families_path.exists():
        with open(families_path) as f:
            return json.load(f)
    return {}


def lookup_control(control_id):
    """Look up a specific control by ID (e.g., AC-2, AC-2(1))."""
    match = re.match(r"^([A-Z]{2})-(\d+)(?:\((\d+)\))?$", control_id.upper())
    if not match:
        print(f"Invalid control ID format: {control_id}")
        print("Expected format: XX-N or XX-N(N), e.g., AC-2 or AC-2(1)")
        return

    family_code = match.group(1)
    control_num = match.group(2)
    enhancement = match.group(3)

    family_file = REFERENCES_DIR / "800-53" / f"{family_code.lower()}.md"
    if not family_file.exists():
        print(f"Family file not found: {family_file}")
        return

    content = family_file.read_text()

    # Build the heading pattern to search for
    if enhancement:
        search_id = f"{family_code}-{control_num}({enhancement})"
    else:
        search_id = f"{family_code}-{control_num}"

    # Find the section for this control
    lines = content.split("\n")
    found = False
    output_lines = []
    current_depth = 0

    for line in lines:
        if found:
            # Check if we've hit the next control at same or higher level
            if line.startswith("#"):
                heading_depth = len(line) - len(line.lstrip("#"))
                if heading_depth <= current_depth:
                    break
            output_lines.append(line)
        elif search_id in line and line.startswith("#"):
            found = True
            current_depth = len(line) - len(line.lstrip("#"))
            output_lines.append(line)

    if output_lines:
        print("\n".join(output_lines).strip())
    else:
        print(f"Control {search_id} not found in {family_file}")


def lookup_family(family_code):
    """Show overview of a control family."""
    family_code = family_code.upper()
    families = load_control_families()

    if family_code in families:
        info = families[family_code]
        print(f"{family_code} — {info['name']}")
        print(f"Controls: {info['control_range']}")
        print(f"Reference: {info['reference_file']}")
    else:
        print(f"Unknown family code: {family_code}")
        print(f"Valid codes: {', '.join(sorted(families.keys()))}")


def search_references(query):
    """Search across all reference files for a query string."""
    query_lower = query.lower()
    results = []

    for md_file in REFERENCES_DIR.rglob("*.md"):
        content = md_file.read_text()
        lines = content.split("\n")
        for i, line in enumerate(lines):
            if query_lower in line.lower():
                rel_path = md_file.relative_to(REPO_ROOT)
                results.append((str(rel_path), i + 1, line.strip()))

    if results:
        print(f"Found {len(results)} matches for '{query}':\n")
        for path, line_num, text in results[:50]:  # Limit to 50 results
            print(f"  {path}:{line_num}")
            print(f"    {text[:120]}")
            print()
    else:
        print(f"No matches found for '{query}'")


def lookup_baseline(level, family_filter=None):
    """Show controls in a specific baseline, optionally filtered by family.

    Reads baselines from the 800-53 markdown files (looking for **Baselines:** tags).
    """
    level = level.capitalize()
    if level not in ("Low", "Moderate", "High"):
        print(f"Invalid baseline level: {level}")
        print("Valid levels: low, moderate, high")
        return

    families = load_control_families()
    refs_dir = REFERENCES_DIR / "800-53"
    results = {}  # family_code -> [(control_id, baselines_str)]

    for md_file in sorted(refs_dir.glob("*.md")):
        if md_file.name == "overview.md":
            continue

        family_code = md_file.stem.upper()
        if family_filter and family_code != family_filter.upper():
            continue

        content = md_file.read_text()
        lines = content.split("\n")

        current_control = None
        for line in lines:
            heading = re.match(r"^## ([A-Z]{2}-\d+)[:\s](.+)$", line)
            if heading:
                current_control = heading.group(1)
                current_title = heading.group(2).strip().rstrip(":")
            elif line.startswith("**Baselines:**") and current_control:
                baselines_str = line.replace("**Baselines:**", "").strip()
                if level in baselines_str:
                    if family_code not in results:
                        results[family_code] = []
                    results[family_code].append(
                        (current_control, current_title, baselines_str)
                    )

    if not results:
        if family_filter:
            print(f"No {level} baseline controls found in family {family_filter.upper()}")
        else:
            print(f"No {level} baseline controls found")
        return

    total = sum(len(v) for v in results.values())
    if family_filter:
        print(f"{level} baseline controls in {family_filter.upper()} ({total}):\n")
    else:
        print(f"{level} baseline controls ({total} total):\n")

    for fam_code in sorted(results.keys()):
        fam_name = families.get(fam_code, {}).get("name", fam_code)
        controls = results[fam_code]
        print(f"  {fam_code} — {fam_name} ({len(controls)} controls)")
        for ctrl_id, title, baselines in controls:
            print(f"    {ctrl_id}: {title}  [{baselines}]")
        print()


def map_csf(csf_id):
    """Map a CSF 2.0 function/category to SP 800-53 controls.

    Reads references/cross-references/800-53-to-csf.md and extracts
    matching sections.
    """
    csf_file = REFERENCES_DIR / "cross-references" / "800-53-to-csf.md"
    if not csf_file.exists():
        print(f"Cross-reference file not found: {csf_file}")
        return

    content = csf_file.read_text()
    csf_id_upper = csf_id.upper()

    # CSF functions: GV, ID, PR, DE, RS, RC
    csf_functions = {
        "GV": "GOVERN",
        "ID": "IDENTIFY",
        "PR": "PROTECT",
        "DE": "DETECT",
        "RS": "RESPOND",
        "RC": "RECOVER",
    }

    # Check if user passed a function code (e.g., "PR") or category (e.g., "PR.AC")
    lines = content.split("\n")
    found_sections = []
    in_section = False
    section_lines = []
    section_depth = 0

    for line in lines:
        if line.startswith("#"):
            # Check if this heading matches our search
            heading_text = line.lstrip("#").strip()
            heading_depth = len(line) - len(line.lstrip("#"))

            if in_section:
                # End previous section if we hit same or higher level heading
                if heading_depth <= section_depth:
                    found_sections.append("\n".join(section_lines))
                    section_lines = []
                    in_section = False

            # Match by CSF ID in heading (e.g., "GV.OC", "PR.AA")
            # Or match by function name (e.g., "GOVERN", "PROTECT")
            matches = False
            if "." in csf_id_upper:
                # Category match: look for exact category ID like "PR.AA" or "DE.CM"
                if csf_id_upper in heading_text.upper():
                    matches = True
            elif csf_id_upper in csf_functions:
                # Function-level match: match the function heading (### DETECT)
                func_name = csf_functions[csf_id_upper]
                if heading_text.upper().startswith(func_name):
                    matches = True

            if matches:
                in_section = True
                section_depth = heading_depth
                section_lines = [line]
                continue

        if in_section:
            section_lines.append(line)

    if in_section and section_lines:
        found_sections.append("\n".join(section_lines))

    if found_sections:
        print(f"CSF 2.0 mappings for '{csf_id}':\n")
        for section in found_sections:
            print(section.strip())
            print()
    else:
        print(f"No CSF 2.0 mappings found for '{csf_id}'")
        print("Try: GV, ID, PR, DE, RS, RC (functions) or PR.AA, DE.CM, etc. (categories)")


def main():
    parser = argparse.ArgumentParser(description="NIST Control Lookup Helper")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # control subcommand
    ctrl_parser = subparsers.add_parser("control", help="Look up a specific control")
    ctrl_parser.add_argument("control_id", help="Control ID (e.g., AC-2, AC-2(1))")

    # family subcommand
    fam_parser = subparsers.add_parser("family", help="Show control family info")
    fam_parser.add_argument("family_code", help="Family code (e.g., AC, SI)")

    # search subcommand
    search_parser = subparsers.add_parser("search", help="Search references")
    search_parser.add_argument("query", help="Search query")

    # baseline subcommand
    baseline_parser = subparsers.add_parser(
        "baseline", help="Show controls in a baseline (low/moderate/high)"
    )
    baseline_parser.add_argument("level", help="Baseline level (low, moderate, high)")
    baseline_parser.add_argument(
        "family", nargs="?", default=None,
        help="Optional family code filter (e.g., AC, SI)",
    )

    # map subcommand
    map_parser = subparsers.add_parser(
        "map", help="Map between frameworks (e.g., map csf PR.AC)"
    )
    map_parser.add_argument(
        "framework", choices=["csf"],
        help="Target framework to map to",
    )
    map_parser.add_argument("identifier", help="Framework identifier (e.g., PR.AC, DE)")

    args = parser.parse_args()

    if args.command == "control":
        lookup_control(args.control_id)
    elif args.command == "family":
        lookup_family(args.family_code)
    elif args.command == "search":
        search_references(args.query)
    elif args.command == "baseline":
        lookup_baseline(args.level, args.family)
    elif args.command == "map":
        if args.framework == "csf":
            map_csf(args.identifier)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
