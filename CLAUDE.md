# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A Claude Code plugin that provides structured NIST cybersecurity framework references (SP 800-53, 800-171, CSF 2.0, 800-53A, and more). The 79 markdown reference files in `references/` are generated from NIST OSCAL catalogs and a HuggingFace dataset of 530,912 examples from 596 NIST publications.

## Architecture

```
HuggingFace dataset + NIST OSCAL catalogs
    ↓ (local/scripts/)
Structured markdown reference files (references/)
    ↓
SKILL.md routing table → Claude reads relevant reference files
    ↓
User gets framework-specific answers
```

**Data pipeline runs in order (scripts in `local/scripts/`, gitignored):**
1. `local/scripts/generate-references.py` — generates initial markdown from HuggingFace dataset
2. `local/scripts/enrich-from-oscal.py` — adds Related Controls from NIST OSCAL (authoritative, 100% coverage)
3. `local/scripts/tag-baselines.py` — adds FedRAMP baseline tags (Low/Moderate/High)

**Plugin entry point:** `skills/nist-cybersecurity-skills/SKILL.md` — contains the framework routing table that maps user queries to reference files.

**Plugin manifest:** `.claude-plugin/plugin.json` (v1.1.0)

## Key Commands

```bash
# Install Python deps for data generation (local/scripts/)
pip install datasets huggingface_hub

# Regenerate all reference files (local dev scripts, gitignored)
python local/scripts/generate-references.py
python local/scripts/enrich-from-oscal.py
python local/scripts/tag-baselines.py

# CLI lookup tool (stdlib only, no external deps)
python scripts/lookup.py control AC-2
python scripts/lookup.py control "AC-2(1)"
python scripts/lookup.py family AC
python scripts/lookup.py search "access control"
python scripts/lookup.py baseline moderate
python scripts/lookup.py baseline moderate AC
python scripts/lookup.py map csf PR.AC

# Install as Claude plugin
claude plugin install ethanolivertroy/nist-cybersecurity-skills
```

## Key Directories

- `references/800-53/` — 20 control family files (AC, AT, AU, CA, CM, CP, IA, IR, MA, MP, PE, PL, PM, PS, PT, RA, SA, SC, SI, SR)
- `references/800-53a/` — assessment procedures per family
- `references/800-171/` — CUI protection requirements
- `references/csf/` — CSF 2.0 functions (GV, ID, PR, DE, RS, RC)
- `references/cross-references/` — framework mappings and baseline definitions
- `assets/` — Structured data (control families JSON)
- `scripts/` — Lookup utility (`lookup.py`, stdlib only)
- `local/` — Dev-only scripts and cached data (gitignored)

## Development Notes

- Reference files are **generated artifacts** — edit the scripts in `local/scripts/`, not the markdown files directly
- `scripts/lookup.py` uses only Python stdlib; the generation scripts in `local/scripts/` need `datasets` and `huggingface_hub`
- OSCAL data is cached in `local/assets/` to avoid repeated downloads; delete cached files to force re-download
- Control IDs follow the pattern: `XX-N` for base controls, `XX-N(M)` for enhancements (e.g., `AC-2(1)`)
- Baseline inheritance: High ⊃ Moderate ⊃ Low (each higher baseline includes all controls from lower ones)
