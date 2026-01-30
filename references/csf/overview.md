# NIST Cybersecurity Framework (CSF) 2.0 — Overview

## What Is the NIST CSF?

The NIST Cybersecurity Framework (CSF) is a voluntary guidance document published by the National Institute of Standards and Technology (NIST) that helps organizations understand, assess, prioritize, and communicate cybersecurity risks. Version 2.0, released in February 2024, is a major update to the original framework (v1.0, 2014) and its minor revision (v1.1, 2018).

CSF 2.0 is designed for use by **all organizations**, not just critical infrastructure. It applies regardless of sector, size, or cybersecurity maturity level. The framework is technology- and vendor-neutral, outcome-based, and meant to complement — not replace — existing cybersecurity programs and standards.

## Purpose

The CSF helps organizations:

- **Understand** their current cybersecurity posture.
- **Assess** and **prioritize** cybersecurity risks in the context of business objectives.
- **Communicate** cybersecurity expectations internally and externally (including supply chain partners).
- **Improve** cybersecurity programs over time using a repeatable, measurable approach.

## The Six Functions

CSF 2.0 organizes cybersecurity outcomes into **six high-level Functions**. These Functions represent the full lifecycle of managing cybersecurity risk and are intended to be addressed concurrently and continuously.

| Function | ID | Purpose |
|---|---|---|
| **Govern** | GV | Establish and monitor the organization's cybersecurity risk management strategy, expectations, and policy. Govern is new in CSF 2.0 and is cross-cutting — it informs how the other five Functions are carried out. |
| **Identify** | ID | Understand the organization's current cybersecurity risks by identifying assets, vulnerabilities, threats, and risk context. |
| **Protect** | PR | Use safeguards to manage cybersecurity risks to assets and operations. |
| **Detect** | DE | Find and analyze possible cybersecurity attacks and compromises. |
| **Respond** | RS | Take action regarding a detected cybersecurity incident. |
| **Recover** | RC | Restore assets and operations affected by a cybersecurity incident. |

### Function Hierarchy: Function → Category → Subcategory

Each Function is subdivided into **Categories** and then **Subcategories**:

```
Function (e.g., GOVERN — GV)
 └── Category (e.g., Risk Management Strategy — GV.RM)
      └── Subcategory (e.g., GV.RM-01: Risk management objectives are established
                              and agreed to by organizational stakeholders)
```

- **Functions** (6 total) — The broadest groupings of cybersecurity outcomes.
- **Categories** (22 total across all Functions) — Groups of related cybersecurity outcomes within a Function.
- **Subcategories** (106 total) — Specific outcome statements that provide actionable detail.

### Category Count by Function

| Function | Categories |
|---|---|
| Govern (GV) | 6 |
| Identify (ID) | 3 |
| Protect (PR) | 5 |
| Detect (DE) | 2 |
| Respond (RS) | 4 |
| Recover (RC) | 2 |

## CSF Tiers

CSF Tiers describe the **degree of rigor** in an organization's cybersecurity risk management practices. They provide context for how an organization views cybersecurity risk and the processes it has in place to manage that risk.

| Tier | Name | Description |
|---|---|---|
| **Tier 1** | Partial | Cybersecurity risk management is ad hoc or reactive. There is limited awareness of cybersecurity risk at the organizational level. Risk management practices are not formalized. |
| **Tier 2** | Risk Informed | Risk management practices are approved by management but may not be established as organization-wide policy. There is awareness of cybersecurity risk, but a consistent, organization-wide approach has not been established. |
| **Tier 3** | Repeatable | Risk management practices are formally approved, expressed as policy, and regularly updated based on changes in business requirements and the threat landscape. There is an organization-wide approach to managing cybersecurity risk. |
| **Tier 4** | Adaptive | The organization actively adapts its cybersecurity practices based on lessons learned and predictive indicators. Cybersecurity risk management is part of the organizational culture and evolves continuously from awareness of previous and current activities, including threat intelligence sharing. |

Tiers are **not maturity levels**. An organization does not need to reach Tier 4 in every area — the appropriate tier depends on the organization's risk appetite, mission, and threat environment.

## CSF Profiles

A **CSF Profile** describes an organization's cybersecurity posture in terms of the CSF outcomes (subcategories) that are relevant to it. There are two types:

- **Current Profile** — Describes the cybersecurity outcomes the organization is currently achieving.
- **Target Profile** — Describes the desired cybersecurity outcomes the organization aims to achieve.

Comparing a Current Profile to a Target Profile reveals **gaps** that can be prioritized and addressed through an action plan. Profiles can also be used for:

- **Community Profiles** — A set of CSF outcomes tailored for a particular sector, technology, or threat type (e.g., a profile for ransomware readiness, or for small businesses).
- **Communication** — Conveying cybersecurity requirements to suppliers or partners.
- **Due Diligence** — Assessing the cybersecurity posture of third parties.

## Relationship to NIST SP 800-53

NIST SP 800-53 ("Security and Privacy Controls for Information Systems and Organizations") provides a **comprehensive catalog of security and privacy controls**. The CSF and SP 800-53 are complementary:

| Aspect | CSF 2.0 | SP 800-53 Rev. 5 |
|---|---|---|
| **Nature** | Outcome-based framework | Prescriptive control catalog |
| **Granularity** | High-level outcomes (subcategories) | Detailed controls and control enhancements |
| **Use** | Risk communication, prioritization, assessment | Implementation guidance, compliance (e.g., FISMA) |
| **Audience** | All organizations | Primarily federal agencies and their contractors, but widely used |

NIST provides **Informative References** that map CSF subcategories to SP 800-53 controls (and to many other standards such as ISO 27001, CIS Controls, and COBIT). These mappings help organizations that use the CSF identify specific SP 800-53 controls they can implement to achieve a desired outcome.

For example:
- CSF Subcategory **PR.AA-01** ("Identities and credentials for authorized users, services, and hardware are managed by the organization") maps to SP 800-53 controls such as **IA-1**, **IA-2**, **IA-4**, **IA-5**, **IA-8**, and others.

## How Organizations Use the CSF

1. **Scope** — Determine which systems, processes, and assets are in scope.
2. **Gather Information** — Identify relevant threats, vulnerabilities, requirements, and current practices.
3. **Create a Current Profile** — Assess which CSF outcomes are currently being achieved and to what extent.
4. **Conduct Risk Assessment** — Analyze risks to determine their likelihood and potential impact.
5. **Create a Target Profile** — Determine desired CSF outcomes based on risk assessment, business objectives, and regulatory requirements.
6. **Gap Analysis** — Compare Current and Target Profiles to identify gaps.
7. **Develop an Action Plan** — Prioritize and plan actions to close the gaps.
8. **Implement and Monitor** — Execute the plan and continuously monitor progress, updating profiles as the risk environment changes.

## Key Changes from CSF 1.1 to CSF 2.0

- **Govern Function added** — Elevates governance from a category within Identify to a standalone, cross-cutting Function.
- **Broadened scope** — Explicitly designed for all organizations, not just critical infrastructure.
- **Improved guidance on profiles** — More detail on how to create and use Current, Target, and Community Profiles.
- **Supply chain risk management** — Expanded coverage through the new GV.SC category.
- **Continuous improvement** — The Identify Function now includes an Improvement (ID.IM) category.
- **Updated references** — Informative References are now maintained online through the NIST Cybersecurity and Privacy Reference Tool (CPRT) rather than embedded in the document.

## References

- NIST CSF 2.0: [https://csf.tools/reference/nist-cybersecurity-framework/v2-0/](https://csf.tools/reference/nist-cybersecurity-framework/v2-0/)
- NIST SP 800-53 Rev. 5: [https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final](https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final)
- NIST CPRT (Informative References): [https://csrc.nist.gov/projects/cprt](https://csrc.nist.gov/projects/cprt)
