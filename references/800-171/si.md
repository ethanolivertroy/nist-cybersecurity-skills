# NIST SP 800-171 Rev 3 — 03.14 System and Information Integrity

The System and Information Integrity family provides security requirements for identifying, reporting, and correcting system flaws in a timely manner, and for protecting systems from malicious code and monitoring system security alerts.

**Source:** Derived from SP 800-53 Rev 5 System and Information Integrity (SI) family.

---

## 03.14.01 Flaw Remediation

Identify, report, and correct system flaws in a timely manner. Test software and firmware updates related to flaw remediation for effectiveness and potential side effects before installation. Install security-relevant software and firmware updates within an organization-defined time period of the release of updates.

**Mapped SP 800-53 Controls:** SI-2, SI-2(2)

**Discussion:** Organizations identify system flaws, report them, and correct them. Flaw remediation includes installing patches, service packs, and hotfixes. Updates are tested before deployment to prevent adverse effects. Automated mechanisms centrally manage flaw remediation processes.

---

## 03.14.02 Malicious Code Protection

Implement malicious code protection mechanisms at system entry and exit points. Update malicious code protection mechanisms as new releases are available. Perform periodic scans of the system and real-time scans of files from external sources.

**Mapped SP 800-53 Controls:** SI-3, SI-3(4)

**Discussion:** Organizations employ anti-malware tools that detect and eradicate malicious code. Protection mechanisms are updated with the latest signatures and heuristics. Both real-time scanning and periodic full-system scans are performed. Malicious code protection addresses both known and emerging threats.

---

## 03.14.03 Security Alerts, Advisories, and Directives

Receive and respond to system security alerts, advisories, and directives from external organizations on an ongoing basis.

**Mapped SP 800-53 Controls:** SI-5

**Discussion:** Organizations monitor security alerts, advisories, and directives from sources such as CISA, US-CERT, vendors, and industry groups. Alerts are analyzed, prioritized, and acted upon in accordance with organizational risk management processes.

---

## 03.14.04 System Monitoring

Monitor the system to detect attacks and indicators of potential attacks, unauthorized local, network, and remote connections, and anomalous behavior. Identify unauthorized use of the system.

**Mapped SP 800-53 Controls:** SI-4, SI-4(4), SI-4(5)

**Discussion:** Organizations monitor systems using intrusion detection systems, intrusion prevention systems, audit record monitoring, and other monitoring tools. Monitoring includes inbound and outbound communications, internal system activity, and unusual or unauthorized activities. Alerts are generated when indicators of compromise are detected.

---

## 03.14.05 Information Input Validation

Check the validity of organization-defined information inputs to the system.

**Mapped SP 800-53 Controls:** SI-10

**Discussion:** Organizations identify and validate information inputs to systems, including checking for accuracy, completeness, validity, and authenticity. Input validation protects against injection attacks and other input-based exploits.

---

## 03.14.06 Error Handling

Reveal error messages only to authorized personnel and not expose CUI or sensitive system information in error messages displayed to general users.

**Mapped SP 800-53 Controls:** SI-11

**Discussion:** Organizations configure systems to provide error messages that do not reveal sensitive system information (e.g., stack traces, database queries, internal network paths) to unauthorized users. Detailed error information is logged for authorized administrators.

---

## 03.14.07 Information Handling and Retention

Handle and retain CUI within the system and information output from the system in accordance with applicable laws, executive orders, directives, policies, regulations, standards, and operational requirements.

**Mapped SP 800-53 Controls:** SI-12

**Discussion:** Organizations manage CUI throughout its lifecycle in accordance with applicable requirements. This includes handling during processing, storage, transport, and disposition. Retention policies are consistent with organizational and legal requirements.

---

## References

- NIST SP 800-171 Rev 3: https://csrc.nist.gov/publications/detail/sp/800-171/rev-3/final
- NIST SP 800-53 Rev 5: System and Information Integrity (SI) Family
- [Cross-reference: SP 800-53 to SP 800-171](../cross-references/800-53-to-800-171.md)
