# FedRAMP and NIST Baseline Control Selections

## Overview

NIST SP 800-53B defines three security control baselines — Low, Moderate, and High — that correspond to the FIPS 199 impact categorization of the information system. FedRAMP (Federal Risk and Authorization Management Program) builds upon these baselines by adding controls and enhancements specific to cloud computing environments. This document covers the NIST baselines, their control composition, and FedRAMP-specific additions.

## FIPS 199 Categorization Drives Baseline Selection

The baseline selection process flows directly from FIPS 199:

```
System Information Types
    |
    v
FIPS 199 Categorization: {Confidentiality: X, Integrity: Y, Availability: Z}
    |
    v
High-Water Mark: Overall Impact Level (Low, Moderate, or High)
    |
    v
SP 800-53B: Select Corresponding Baseline (Low, Moderate, or High)
    |
    v
Tailoring: Adjust baseline per organizational needs and risk assessment
    |
    v
Final Control Set
```

### Impact Level Examples

| System Type | Typical Categorization | Overall Level |
|-------------|----------------------|---------------|
| Public website (informational) | {C: Low, I: Low, A: Low} | Low |
| Standard business system | {C: Moderate, I: Moderate, A: Low} | Moderate |
| Financial management system | {C: Moderate, I: High, A: Moderate} | High |
| Law enforcement system | {C: High, I: Moderate, A: Moderate} | High |
| National security system | Categorized per CNSSI 1253 | Varies |

## The Three NIST Baselines

### Summary

| Attribute | Low Baseline | Moderate Baseline | High Baseline |
|-----------|-------------|-------------------|---------------|
| **Approximate controls (with enhancements)** | ~135 | ~325 | ~421 |
| **Intended for** | Systems where loss would have limited adverse effect | Systems where loss would have serious adverse effect | Systems where loss would have severe or catastrophic adverse effect |
| **Examples** | Public websites, non-sensitive internal tools | Most federal systems, PII processing, financial data | Critical infrastructure controls, classified-adjacent, law enforcement |
| **FedRAMP usage** | FedRAMP Low (Li-SaaS) | FedRAMP Moderate (most common) | FedRAMP High (DoD, law enforcement, emergency services) |

### Control Counts by Family and Baseline

The following table shows approximate control counts (base controls plus selected enhancements) for each SP 800-53 Rev 5 baseline. Counts are approximate and reflect the controls specified in SP 800-53B.

| Family | Code | Low | Moderate | High | Total in Catalog |
|--------|------|-----|----------|------|-----------------|
| Access Control | AC | 17 | 37 | 50 | 90+ |
| Awareness and Training | AT | 4 | 5 | 6 | 12+ |
| Audit and Accountability | AU | 8 | 14 | 19 | 40+ |
| Assessment, Authorization, and Monitoring | CA | 6 | 9 | 11 | 20+ |
| Configuration Management | CM | 8 | 15 | 20 | 40+ |
| Contingency Planning | CP | 6 | 13 | 17 | 35+ |
| Identification and Authentication | IA | 9 | 16 | 20 | 45+ |
| Incident Response | IR | 6 | 11 | 15 | 25+ |
| Maintenance | MA | 4 | 7 | 9 | 18+ |
| Media Protection | MP | 4 | 8 | 9 | 20+ |
| Physical and Environmental Protection | PE | 11 | 17 | 22 | 50+ |
| Planning | PL | 3 | 5 | 5 | 12+ |
| Program Management | PM | 16 | 16 | 16 | 32+ |
| Personnel Security | PS | 7 | 8 | 9 | 15+ |
| PII Processing and Transparency | PT | 4 | 6 | 7 | 15+ |
| Risk Assessment | RA | 4 | 7 | 8 | 18+ |
| System and Services Acquisition | SA | 7 | 17 | 24 | 55+ |
| System and Communications Protection | SC | 8 | 20 | 32 | 60+ |
| System and Information Integrity | SI | 5 | 12 | 17 | 45+ |
| Supply Chain Risk Management | SR | 3 | 5 | 6 | 15+ |
| **Approximate Total** | | **~135** | **~325** | **~421** | **~1,000+** |

Note: The PM (Program Management) family is included at all baselines with the same count because PM controls are organizational-level controls applied regardless of system impact level. Actual counts vary slightly based on how enhancements are counted.

### How Baselines Build on Each Other

The baselines are **cumulative** — each higher baseline includes all controls from the lower baselines plus additional controls and enhancements:

```
Low Baseline (~135 controls)
    |
    + Additional controls/enhancements
    |
    v
Moderate Baseline (~325 controls) — includes all Low controls
    |
    + Additional controls/enhancements
    |
    v
High Baseline (~421 controls) — includes all Moderate controls
```

### Key Controls Added at Moderate (Not in Low)

| Control | Title | Why Added at Moderate |
|---------|-------|---------------------|
| AC-4 | Information Flow Enforcement | More stringent data flow controls needed |
| AC-5 | Separation of Duties | Prevents single-person fraud/error |
| AC-6(1-10) | Least Privilege (enhancements) | Granular privilege management |
| AU-6(1)(3) | Audit Review enhancements | Automated audit analysis |
| CM-3 | Configuration Change Control | Formal change management |
| CP-7 | Alternate Processing Site | Disaster recovery capability |
| IA-2(1)(2)(8)(12) | MFA enhancements | Multi-factor authentication required |
| IR-4(1) | Incident Handling — Automated Handling | Automated incident processing |
| SC-7(3)(4)(5)(7)(8) | Boundary Protection enhancements | More granular network boundary controls |
| SC-8 | Transmission Confidentiality and Integrity | Encryption in transit |
| SC-28 | Protection of Information at Rest | Encryption at rest |
| SI-4 | System Monitoring (expanded) | Comprehensive monitoring |

### Key Controls Added at High (Not in Moderate)

| Control | Title | Why Added at High |
|---------|-------|------------------|
| AC-3(2) | Dual Authorization | Two-person integrity for critical actions |
| AC-6(8) | Privilege Levels for Code Execution | Restricts code execution privileges |
| AU-10 | Non-Repudiation | Proof of data origin and delivery |
| CP-6(1)(2)(3) | Alternate Storage Site enhancements | Geographic separation, accessibility |
| IA-5(2)(3) | PKI-Based Authentication, In-Person Registration | Stronger authentication mechanisms |
| PE-3(1) | Physical Access Control — System Access | Alarm systems |
| SC-3 | Security Function Isolation | Isolate security functions from non-security |
| SC-7(10)(18)(21) | Boundary Protection — advanced enhancements | Exfiltration prevention, fail-secure |
| SC-12(1) | Cryptographic Key — Availability | Key availability for critical systems |
| SI-6 | Security and Privacy Function Verification | Verify security functions operate correctly |

## FedRAMP-Specific Additions Beyond NIST Baselines

FedRAMP builds upon the NIST baselines by adding controls, parameters, and requirements specific to cloud service environments. These additions address cloud-specific risks and federal requirements.

### FedRAMP Additional Controls and Parameters

FedRAMP does not simply adopt the NIST baselines as-is. It customizes them by:

1. **Adding controls not in the NIST baseline** — FedRAMP selects additional controls from the SP 800-53 catalog
2. **Specifying FedRAMP-defined parameter values** — Where SP 800-53 allows organization-defined parameters (ODPs), FedRAMP specifies mandatory values
3. **Requiring additional documentation** — FedRAMP requires specific artifacts beyond the standard RMF package

### Key FedRAMP Additions (Moderate Baseline Example)

| Area | FedRAMP Requirement | NIST Baseline |
|------|---------------------|---------------|
| **Continuous Monitoring** | Monthly OS/database vulnerability scanning, annual penetration testing, annual assessment of 1/3 of controls | NIST does not specify frequencies at this level |
| **Vulnerability Scanning (RA-5)** | Monthly OS scans, monthly web application scans, annual penetration test. High-risk vulnerabilities remediated within 30 days, moderate within 90 days, low within 180 days. | General vulnerability monitoring and scanning |
| **Configuration Scanning** | Monthly automated configuration scans against FedRAMP benchmarks (DISA STIGs, CIS Benchmarks) | General configuration management |
| **Incident Response (IR-6)** | Report incidents to FedRAMP and CISA within 1 hour of determination | General incident reporting |
| **Access Control (AC-2)** | Specific parameter values for account review frequency, inactivity period, etc. | Organization-defined parameters |
| **Multi-Factor Authentication** | Required for all privileged and non-privileged user access to the cloud environment. FedRAMP specifies phishing-resistant MFA for privileged users. | MFA required but parameters less specific |
| **Encryption** | FIPS 140-2/3 validated modules required for all cryptographic functions. TLS 1.2+ required. | General cryptographic protection |
| **Boundary Protection (SC-7)** | Specific requirements for cloud boundary definition, customer isolation, and multi-tenancy | General boundary protection |
| **Data Location** | Data must be stored and processed within the United States (for most FedRAMP authorizations) | No geographic requirement |

### FedRAMP Control Parameter Examples

| Control | Parameter | FedRAMP Value |
|---------|-----------|---------------|
| AC-2(3) | Disable inactive accounts after | 90 days (or less) |
| AC-7 | Number of consecutive invalid logon attempts | Not more than 3 |
| AC-7 | Time period for lockout | At least 15 minutes or until unlocked by administrator |
| AC-11 | Session lock after inactivity | 15 minutes (or less) |
| AU-6 | Frequency of audit review | At least weekly |
| IA-5(1) | Password minimum length | 12 characters (or more) |
| RA-5 | Frequency of vulnerability scanning | Monthly for OS, monthly for web app, annually for penetration test |
| SI-2 | Timeframe for flaw remediation | 30 days (High), 90 days (Moderate), 180 days (Low) |

### FedRAMP Authorization Levels

| Level | Based On | Typical Use |
|-------|----------|-------------|
| **FedRAMP Low** | NIST Low baseline + FedRAMP additions | Low-impact SaaS (Li-SaaS) for non-sensitive data |
| **FedRAMP Moderate** | NIST Moderate baseline + FedRAMP additions | Most federal cloud deployments — handles CUI and sensitive PII |
| **FedRAMP High** | NIST High baseline + FedRAMP additions | Law enforcement, emergency services, financial, health, and other high-impact data |

### FedRAMP Rev 5 Transition

FedRAMP has transitioned its baselines to align with SP 800-53 Rev 5 and SP 800-53B. Key changes include:

- Incorporation of new Rev 5 control families (PT, SR)
- Updated parameter values
- Alignment with NIST's updated control baselines
- Enhanced supply chain requirements
- Updated continuous monitoring requirements

## Tailoring the Baseline

Both NIST and FedRAMP allow tailoring of the baseline, though FedRAMP imposes stricter constraints:

### NIST Tailoring Activities
- Identify and designate **common controls** (inherited from the organization)
- Apply **scoping considerations** (remove non-applicable controls)
- Select **compensating controls** (alternative controls when standard controls cannot be implemented)
- Assign **organization-defined parameters** (fill in ODP values)
- **Supplement** the baseline with additional controls based on risk assessment

### FedRAMP Tailoring Constraints
- FedRAMP **rarely permits removal** of baseline controls
- FedRAMP specifies many parameter values — CSPs cannot choose less restrictive values
- **Alternative implementations** require documented justification and FedRAMP approval
- Additional controls can always be added but baseline controls generally cannot be removed or weakened

## References

- NIST SP 800-53B: Control Baselines: https://csrc.nist.gov/publications/detail/sp/800-53b/final
- NIST SP 800-53 Rev 5: https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final
- FIPS 199: https://csrc.nist.gov/publications/detail/fips/199/final
- FIPS 200: https://csrc.nist.gov/publications/detail/fips/200/final
- FedRAMP: https://www.fedramp.gov/
- FedRAMP Rev 5 Baselines: https://www.fedramp.gov/baselines/
