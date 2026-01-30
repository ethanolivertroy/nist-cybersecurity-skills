# NIST SP 800-161 Rev 1 — Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations

## Purpose

NIST Special Publication 800-161 Revision 1 provides guidance on identifying, assessing, and mitigating cybersecurity risks throughout the supply chain. It addresses the growing threat posed by supply chain compromises — where adversaries target the components, services, and processes that organizations depend on — and provides a structured approach for integrating **Cybersecurity Supply Chain Risk Management (C-SCRM)** into the broader organizational risk management framework.

Published in May 2022, Rev 1 represents a significant update that:

- Aligns with SP 800-53 Rev 5 and the NIST Cybersecurity Framework
- Integrates C-SCRM with the Risk Management Framework (SP 800-37) and Enterprise Risk Management (ERM) per OMB Circular A-123
- Responds to Executive Order 14028 (Improving the Nation's Cybersecurity) directives on software supply chain security
- Provides expanded guidance on C-SCRM for critical infrastructure sectors

## Supply Chain Risk Management Practices

C-SCRM encompasses the activities necessary to manage cybersecurity risks associated with the distributed and interconnected nature of information and communications technology (ICT) and operational technology (OT) product and service supply chains.

### Key Supply Chain Risks

| Risk Category | Description | Examples |
|---------------|-------------|----------|
| **Insertion of malicious functionality** | Adversary inserts malware, backdoors, or logic bombs into components | SolarWinds compromise, trojanized firmware |
| **Insertion of counterfeit components** | Substitution of inferior or modified components | Counterfeit integrated circuits, cloned hardware |
| **Exploitation of vulnerabilities** | Adversary exploits flaws in supply chain components | Vulnerabilities in open-source libraries (Log4j) |
| **Disruption of supply** | Interruption of component or service availability | Single-source dependency failure, geopolitical disruption |
| **Data theft or leakage** | Sensitive data exposed through supply chain partners | Third-party breach exposing customer data |
| **Unauthorized production** | Overproduction or unauthorized copies of components | Unauthorized manufacturing runs |

### Foundational C-SCRM Practices

1. **Establish C-SCRM as a priority:** Executive leadership commitment and governance
2. **Develop a C-SCRM policy:** Formalize requirements, roles, and responsibilities
3. **Identify and assess supply chain risks:** Map supply chains, identify critical suppliers, assess risks
4. **Establish requirements for suppliers:** Flow down security requirements through contracts and agreements
5. **Verify and validate:** Assess supplier compliance through audits, testing, and monitoring
6. **Plan for the full lifecycle:** Address supply chain risks from design through disposal
7. **Share information:** Participate in threat intelligence sharing (ISACs, government programs)
8. **Train and educate:** Build C-SCRM awareness across the organization

## Integration with RMF and ERM

SP 800-161 Rev 1 emphasizes that C-SCRM must be integrated with existing risk management processes, not treated as a standalone activity.

### Integration with the Risk Management Framework (SP 800-37)

C-SCRM activities map to each RMF step:

| RMF Step | C-SCRM Integration |
|----------|---------------------|
| **Prepare** | Establish C-SCRM governance, identify supply chain risk tolerance, develop C-SCRM strategy |
| **Categorize** | Consider supply chain dependencies in system categorization; identify critical supply chain components |
| **Select** | Select supply chain-specific controls (SR family from SP 800-53); incorporate C-SCRM requirements into SSP |
| **Implement** | Implement supply chain controls; flow requirements to suppliers via contracts |
| **Assess** | Assess supplier compliance; evaluate supply chain control effectiveness |
| **Authorize** | Include supply chain risks in the authorization decision; document residual supply chain risks |
| **Monitor** | Continuously monitor supply chain for changes, new vulnerabilities, and emerging threats |

### Integration with Enterprise Risk Management (ERM)

Per OMB Circular A-123, federal agencies must integrate cybersecurity risks (including supply chain risks) into their ERM process:

- **Strategic level:** C-SCRM considerations in mission and strategic planning
- **Budget level:** Resource allocation for C-SCRM activities
- **Operational level:** Day-to-day supply chain risk monitoring and management
- **Reporting level:** Supply chain risk reporting to senior leadership and oversight bodies

## C-SCRM Controls (SP 800-53 SR Family)

SP 800-161 Rev 1 leverages controls from SP 800-53 Rev 5, with primary focus on the **Supply Chain Risk Management (SR)** family. It also identifies controls from other families that are relevant to C-SCRM.

### SR Family Controls

| Control | Title | Description |
|---------|-------|-------------|
| **SR-1** | Policy and Procedures | Establish C-SCRM policy and procedures |
| **SR-2** | Supply Chain Risk Management Plan | Develop and implement a C-SCRM plan for the system |
| **SR-3** | Supply Chain Controls and Processes | Establish processes to identify and address supply chain weaknesses or deficiencies |
| **SR-4** | Provenance | Track and document the provenance of systems, components, and services |
| **SR-5** | Acquisition Strategies, Tools, and Methods | Use acquisition strategies that mitigate supply chain risk (e.g., multiple suppliers, trusted foundry) |
| **SR-6** | Supplier Assessments and Reviews | Assess and review supply chain entities (suppliers, developers, manufacturers) |
| **SR-7** | Supply Chain Operations Security | Employ OPSEC measures to protect supply chain information |
| **SR-8** | Notification Agreements | Establish agreements with suppliers for notification of supply chain compromises |
| **SR-9** | Tamper Resistance and Detection | Employ tamper-evident packaging, anti-tamper technologies, and inspection procedures |
| **SR-10** | Inspection of Systems or Components | Inspect delivered systems and components for evidence of tampering |
| **SR-11** | Component Authenticity | Develop and implement anti-counterfeit measures (e.g., verify authenticity, source from authorized distributors) |
| **SR-12** | Component Disposal | Properly dispose of components to prevent reuse or information leakage |

### Controls from Other Families Relevant to C-SCRM

SP 800-161 identifies controls across multiple SP 800-53 families that support C-SCRM:

| Family | Key C-SCRM-Relevant Controls | Focus |
|--------|-------------------------------|-------|
| **Access Control (AC)** | AC-4 (Information Flow), AC-20 (External Systems) | Controlling third-party access and data flows |
| **Audit (AU)** | AU-6 (Audit Review/Analysis), AU-13 (Monitoring for Information Disclosure) | Monitoring supply chain activities |
| **Configuration Management (CM)** | CM-2 (Baseline Configuration), CM-7 (Least Functionality), CM-8 (System Component Inventory) | Managing and tracking components |
| **Incident Response (IR)** | IR-4 (Incident Handling), IR-6 (Incident Reporting) | Supply chain incident response |
| **Maintenance (MA)** | MA-4 (Nonlocal Maintenance), MA-6 (Timely Maintenance) | Securing maintenance activities involving external parties |
| **Personnel Security (PS)** | PS-7 (External Personnel Security) | Screening and managing external personnel |
| **Risk Assessment (RA)** | RA-3 (Risk Assessment), RA-5 (Vulnerability Monitoring) | Supply chain risk and vulnerability assessment |
| **System and Services Acquisition (SA)** | SA-4 (Acquisition Process), SA-8 (Security Engineering), SA-9 (External System Services), SA-10 (Developer Configuration Management), SA-11 (Developer Testing) | Secure acquisition and development |
| **System and Communications Protection (SC)** | SC-7 (Boundary Protection), SC-18 (Mobile Code) | Protecting system boundaries from supply chain threats |
| **System and Information Integrity (SI)** | SI-7 (Software/Firmware/Information Integrity) | Verifying integrity of supplied components |

## Key Activities by Organizational Level

SP 800-161 Rev 1 organizes C-SCRM activities across three organizational levels, aligned with NIST's risk management hierarchy:

### Level 1: Enterprise / Organization Level

The executive and governance level that establishes the C-SCRM program.

**Key Activities:**
- **Establish C-SCRM governance:** Designate a C-SCRM PMO or lead; establish a C-SCRM council or working group with cross-functional representation (IT, procurement, legal, security, program management)
- **Define C-SCRM policy:** Develop enterprise-wide C-SCRM policy that defines roles, responsibilities, and authorities
- **Establish risk appetite and tolerance:** Define the organization's tolerance for supply chain risk; establish criteria for acceptable suppliers
- **Develop C-SCRM strategy:** Create a strategic plan for managing supply chain risks across the enterprise
- **Allocate resources:** Budget for C-SCRM activities, tools, and personnel
- **Establish information-sharing agreements:** Participate in ISACs, share threat intelligence, and establish agreements with government partners (CISA, sector-specific agencies)
- **Develop standard contract language:** Create template clauses for security requirements, incident notification, right-to-audit, SBOM requirements, and supply chain transparency
- **Maintain a supplier risk registry:** Track known risks associated with critical suppliers

### Level 2: Mission / Business Process Level

The mission and business process owners who translate enterprise strategy into program-level requirements.

**Key Activities:**
- **Map critical supply chains:** Identify the supply chains that support mission-critical functions; map multi-tier supplier relationships
- **Conduct supply chain risk assessments:** Assess risks specific to each mission/business process and its dependencies
- **Define mission-specific C-SCRM requirements:** Translate enterprise policy into specific acquisition and security requirements for programs
- **Evaluate supplier criticality:** Determine which suppliers are critical to mission success; identify single points of failure
- **Develop C-SCRM plans for programs:** Create program-level supply chain risk management plans
- **Coordinate across programs:** Ensure consistency in supplier requirements and risk assessments across related programs
- **Manage supplier relationships:** Oversee supplier performance, conduct periodic reviews, and manage escalations

### Level 3: Operational / System Level

The system-level activities that implement C-SCRM controls for specific information systems.

**Key Activities:**
- **Implement SR family controls:** Deploy supply chain controls as documented in the system security plan
- **Maintain a Software Bill of Materials (SBOM):** Track all software components, libraries, and dependencies in each system
- **Verify component integrity:** Inspect and validate delivered components; verify authenticity and provenance
- **Configure and harden supplied components:** Apply secure configurations before deployment; remove unnecessary functionality
- **Monitor for supply chain vulnerabilities:** Track CVEs and advisories for supply chain components; apply patches promptly
- **Conduct supplier audits and assessments:** Evaluate supplier security practices through questionnaires, audits, or third-party assessments
- **Respond to supply chain incidents:** Execute incident response procedures when supply chain compromises are detected
- **Manage component lifecycle:** Track component end-of-life, plan for replacement, and ensure secure disposal
- **Maintain system component inventory:** Keep accurate records of all components, their sources, and their current versions (supports CM-8)

## Software Supply Chain Security

Rev 1 includes expanded guidance on software supply chain security, reflecting the focus of EO 14028:

- **Software Bill of Materials (SBOM):** Organizations should require SBOMs from software suppliers to understand component composition and track vulnerabilities
- **Secure Software Development Practices:** Require suppliers to follow NIST Secure Software Development Framework (SSDF, SP 800-218)
- **Software Integrity Verification:** Verify software signatures, hashes, and provenance before deployment
- **Open-Source Software Management:** Assess and manage risks from open-source components using tools like software composition analysis (SCA)

## References

- NIST SP 800-161 Rev 1: https://csrc.nist.gov/publications/detail/sp/800-161/rev-1/final
- NIST SP 800-53 Rev 5: Security and Privacy Controls
- NIST SP 800-37 Rev 2: Risk Management Framework
- NIST SP 800-218: Secure Software Development Framework (SSDF)
- Executive Order 14028: Improving the Nation's Cybersecurity
- OMB Circular A-123: Management's Responsibility for Enterprise Risk Management and Internal Control
