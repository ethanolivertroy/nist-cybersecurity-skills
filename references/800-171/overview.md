# NIST SP 800-171 Rev 3 — Protecting Controlled Unclassified Information in Nonfederal Systems and Organizations

## Purpose

NIST Special Publication 800-171 Revision 3 provides federal agencies with recommended security requirements for protecting the confidentiality of Controlled Unclassified Information (CUI) when it resides in nonfederal systems and organizations. It establishes a set of security requirements that nonfederal organizations must implement when they process, store, or transmit CUI on behalf of federal agencies.

The publication was developed in response to Federal Information Security Modernization Act (FISMA) requirements and Executive Order 13556, which established the CUI program to standardize the way the executive branch handles unclassified information that requires safeguarding.

## Who It Applies To

SP 800-171 applies to **nonfederal organizations** that handle CUI, including:

- **Defense contractors** and subcontractors operating under DFARS clause 252.204-7012
- **Government contractors** across all federal agencies
- **Universities and research institutions** receiving federal grants involving CUI
- **State, local, and tribal governments** handling federal CUI
- **Any nonfederal entity** that processes, stores, or transmits CUI pursuant to a federal contract, grant, or agreement

Federal agencies themselves are governed directly by FIPS 200 and SP 800-53, not 800-171.

## Relationship to SP 800-53

SP 800-171 security requirements are **derived from the NIST SP 800-53 Moderate baseline**. The derivation process involved:

1. Starting with the SP 800-53 Moderate baseline controls
2. **Removing controls that are uniquely federal** — controls that address responsibilities of the federal government (e.g., federal-specific security training requirements, federal incident reporting to US-CERT)
3. **Removing controls related to public access systems** — not relevant to CUI protection
4. **Removing controls expected to be met by nonfederal organizations without specification** — controls that are routinely satisfied by nonfederal organizations through standard business practices (e.g., having a policy document)
5. Tailoring the remaining controls into a set of security requirements expressed in language appropriate for nonfederal organizations

Rev 3 aligns the requirements more directly with SP 800-53 Rev 5 controls, making traceability more explicit.

## The 17 Control Families

SP 800-171 Rev 3 organizes its security requirements into **17 families** (expanded from the 14 families in Rev 2):

| Family ID | Family Name | Description |
|-----------|-------------|-------------|
| 03.01 | Access Control (AC) | Limit system access to authorized users and transactions |
| 03.02 | Awareness and Training (AT) | Ensure personnel are aware of security risks and trained in responsibilities |
| 03.03 | Audit and Accountability (AU) | Create, protect, and retain audit records for monitoring and investigation |
| 03.04 | Configuration Management (CM) | Establish and maintain baseline configurations and inventories |
| 03.05 | Identification and Authentication (IA) | Identify and authenticate users, devices, and processes |
| 03.06 | Incident Response (IR) | Establish incident handling capabilities |
| 03.07 | Maintenance (MA) | Perform timely maintenance on systems |
| 03.08 | Media Protection (MP) | Protect system media containing CUI |
| 03.09 | Personnel Security (PS) | Screen individuals and protect CUI during personnel actions |
| 03.10 | Physical Protection (PE) | Limit physical access to systems and facilities |
| 03.11 | Planning (PL) | Develop and implement security plans |
| 03.12 | Risk Assessment (RA) | Assess risk to operations, assets, and individuals |
| 03.13 | System and Communications Protection (SC) | Monitor and protect communications and system boundaries |
| 03.14 | System and Information Integrity (SI) | Identify, report, and correct system flaws in a timely manner |
| 03.15 | Security Assessment and Monitoring (CA) | Assess, monitor, and correct deficiencies in security controls |
| 03.16 | Supply Chain Risk Management (SR) | Manage supply chain risks to systems and components |
| 03.17 | Personally Identifiable Information Processing and Transparency (PT) | Manage PII processing and transparency obligations |

Note: Rev 2 had 14 families. Rev 3 added Planning (PL), Supply Chain Risk Management (SR), and Personally Identifiable Information Processing and Transparency (PT) to align with SP 800-53 Rev 5.

## Relationship to CMMC

The **Cybersecurity Maturity Model Certification (CMMC) 2.0** program, administered by the Department of Defense, is directly built on SP 800-171:

- **CMMC Level 1 (Foundational):** 15 basic safeguarding requirements from FAR 52.204-21 (a subset of 800-171)
- **CMMC Level 2 (Advanced):** Requires implementation of **all SP 800-171 Rev 2 requirements** (110 security requirements). Assessed by C3PAOs (Certified Third-Party Assessment Organizations) for prioritized acquisitions, or self-assessed for non-prioritized acquisitions
- **CMMC Level 3 (Expert):** Includes all 800-171 requirements plus a subset of SP 800-172 enhanced security requirements, assessed by DIBCAC (Defense Industrial Base Cybersecurity Assessment Center)

Organizations must achieve the appropriate CMMC level to be eligible for DoD contracts involving CUI. A Plan of Action and Milestones (POA&M) is permitted for some requirements, but certain requirements are non-negotiable for certification.

## Key Differences from SP 800-53

| Aspect | SP 800-53 | SP 800-171 |
|--------|-----------|------------|
| **Audience** | Federal agencies and systems | Nonfederal organizations handling CUI |
| **Scope** | Comprehensive catalog (1,000+ controls) | Focused subset (~110 requirements in Rev 2, reorganized in Rev 3) |
| **Structure** | Controls with enhancements, organized by family | Security requirements organized by family |
| **Baselines** | Three baselines (Low, Moderate, High) | Single set of requirements (derived from Moderate) |
| **Federal controls** | Includes federal-specific controls | Federal-specific controls removed |
| **Flexibility** | Tailoring guidance for agencies | Organizations can use alternative but equally effective means |
| **Assessment** | Assessed per SP 800-53A | Assessed per SP 800-171A or CMMC assessment guides |
| **Control enhancements** | Extensive enhancements per control | Some enhancements folded into requirements; no separate enhancement structure |
| **Policy requirements** | Explicit policy and procedure controls (XX-1) | Policy and procedures expected but not specified as individual requirements |
| **Terminology** | "Controls" and "control enhancements" | "Security requirements" and "organization-defined parameters (ODP)" |

## Rev 3 Changes from Rev 2

Key changes introduced in Revision 3 include:

- **Direct mapping to SP 800-53 Rev 5:** Each requirement now explicitly maps to one or more SP 800-53 Rev 5 controls, improving traceability
- **Organization-Defined Parameters (ODPs):** Requirements now include ODPs that organizations must define, replacing the more generic language of Rev 2
- **Additional families:** Three new families (PL, SR, PT) added to align with 800-53 Rev 5
- **Withdrawn requirements:** Some Rev 2 requirements were withdrawn or consolidated
- **Enhanced specificity:** Requirements are more precisely stated to reduce ambiguity in implementation and assessment

## References

- NIST SP 800-171 Rev 3: https://csrc.nist.gov/publications/detail/sp/800-171/rev-3/final
- NIST SP 800-171A: Assessment procedures for 800-171
- NIST SP 800-172: Enhanced Security Requirements for CUI (beyond 800-171)
- CMMC Program: https://www.acq.osd.mil/cmmc/
