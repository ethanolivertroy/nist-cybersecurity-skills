![NIST Cybersecurity Skills](nist-cyber-skills-banner.jpg)

# nist-cybersecurity-skills

A Claude Code agent skill providing comprehensive NIST cybersecurity framework reference.

## Frameworks Covered

- **SP 800-53 Rev 5** — Security and Privacy Controls (all 20 families)
- **SP 800-171 Rev 3** — Protecting Controlled Unclassified Information (CUI)
- **SP 800-53A Rev 5** — Assessment Procedures
- **CSF 2.0** — Cybersecurity Framework (6 functions, categories, subcategories)
- **SP 800-37 Rev 2** — Risk Management Framework
- **SP 800-207** — Zero Trust Architecture
- **SP 800-30 Rev 1** — Risk Assessment Guide
- **SP 800-61 Rev 3** — Incident Response
- **SP 800-63 Rev 4** — Digital Identity Guidelines
- **SP 800-161 Rev 1** — Supply Chain Risk Management
- **FIPS** — 140-3, 199, 200, 201

## Installation

### Claude Code Plugin
```bash
claude plugin install ethanolivertroy/nist-cybersecurity-skills
```

### Vercel Skills CLI
```bash
npx skills add ethanolivertroy/nist-cybersecurity-skills
```

### Local development
```bash
claude --plugin-dir ./nist-cybersecurity-skills
```

## Structure

```
.claude-plugin/plugin.json              — Plugin manifest
skills/nist-cybersecurity-skills/
  SKILL.md                              — Main entry point (framework routing, quick reference)
references/800-53/                      — SP 800-53 Rev 5 control families
references/800-171/                     — SP 800-171 Rev 3
references/800-53a/                     — SP 800-53A assessment procedures
references/csf/                         — CSF 2.0 functions
references/800-37/                      — Risk Management Framework
references/800-207/                     — Zero Trust Architecture
references/800-30/                      — Risk Assessment
references/800-61/                      — Incident Response
references/800-63/                      — Digital Identity
references/800-161/                     — Supply Chain Risk Management
references/fips/                        — FIPS standards
references/cross-references/            — Framework mappings and baselines
references/glossary.md                  — NIST cybersecurity terms
scripts/                                — Lookup utility
assets/                                 — Structured data (control families)
```

## License

MIT — see [LICENSE](LICENSE).

The scripts, SKILL.md structure, and cross-reference mappings in this repository are original work. The NIST reference content under `references/` is derived from U.S. government publications, which are in the public domain and not subject to copyright.

## Data Sources

- [`ethanolivertroy/nist-cybersecurity-training`](https://huggingface.co/datasets/ethanolivertroy/nist-cybersecurity-training) — 530,912 structured examples from 596 NIST publications
- [`ethanolivertroy/nist-publications-raw`](https://huggingface.co/datasets/ethanolivertroy/nist-publications-raw) — 596 raw PDFs
