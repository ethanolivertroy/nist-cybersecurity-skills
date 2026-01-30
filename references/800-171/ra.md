# NIST SP 800-171 Rev 3 — 03.12 Risk Assessment

The Risk Assessment family provides security requirements for assessing risk to organizational operations, assets, and individuals resulting from the processing, storage, or transmission of CUI.

**Source:** Derived from SP 800-53 Rev 5 Risk Assessment (RA) family.

---

## 03.12.01 Risk Assessment

Periodically assess the risk to organizational operations (including mission, functions, image, or reputation), organizational assets, and individuals resulting from the operation of organizational systems and the associated processing, storage, or transmission of CUI.

**Mapped SP 800-53 Controls:** RA-3

**Discussion:** Organizations assess risks from the operation of systems containing CUI. Risk assessments consider threats, vulnerabilities, likelihood, and impact. Results inform risk responses, security control selections, and other risk management decisions. Assessments are updated when significant changes occur to systems or environments.

---

## 03.12.02 Vulnerability Monitoring and Scanning

Monitor and scan for vulnerabilities in the system and hosted applications. Remediate vulnerabilities in accordance with risk assessments. Update vulnerability scanning tools and databases.

**Mapped SP 800-53 Controls:** RA-5, RA-5(2), RA-5(5)

**Discussion:** Organizations scan for vulnerabilities using automated tools (e.g., network scanners, web application scanners) and manual techniques. Vulnerabilities are remediated based on risk priority. Scanning tools and vulnerability databases are kept current. Privileged access scanning provides more comprehensive vulnerability identification.

---

## 03.12.03 Vulnerability Disclosure

Establish a public vulnerability disclosure policy. Implement procedures for receiving and responding to vulnerability reports.

**Mapped SP 800-53 Controls:** RA-5(11)

**Discussion:** Vulnerability disclosure supports the identification of vulnerabilities by external researchers and other parties. Organizations establish channels for receiving vulnerability reports and processes for analyzing, validating, and remediating reported vulnerabilities.

---

## References

- NIST SP 800-171 Rev 3: https://csrc.nist.gov/publications/detail/sp/800-171/rev-3/final
- NIST SP 800-53 Rev 5: Risk Assessment (RA) Family
- [Cross-reference: SP 800-53 to SP 800-171](../cross-references/800-53-to-800-171.md)
