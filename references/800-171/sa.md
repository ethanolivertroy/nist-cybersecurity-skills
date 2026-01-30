# NIST SP 800-171 Rev 3 — 03.16 System and Services Acquisition (Supply Chain Risk Management)

The Supply Chain Risk Management family provides security requirements for managing supply chain risks to systems and components used to process, store, or transmit CUI. Note: In the SP 800-171 Rev 3 numbering, this family is numbered 03.16 and maps to both SP 800-53 Supply Chain Risk Management (SR) and System and Services Acquisition (SA) families.

**Source:** Derived from SP 800-53 Rev 5 System and Services Acquisition (SA) and Supply Chain Risk Management (SR) families. This file covers SA-derived requirements; see also [sr.md](sr.md) for SR-specific requirements.

---

## 03.16.01 Security Engineering Principles

Apply security engineering principles in the specification, design, development, implementation, and modification of the system and system components.

**Mapped SP 800-53 Controls:** SA-8

**Discussion:** Organizations apply security engineering principles to protect the confidentiality of CUI. These principles include defense-in-depth, least privilege, minimized trust surfaces, fail-safe defaults, separation of duties, and modularity. Applying these principles reduces security vulnerabilities.

---

## 03.16.02 External System Services

Require external providers of system services to comply with organizational security requirements and employ appropriate security controls. Define and document organizational oversight and user roles and responsibilities with regard to external system services. Monitor security control compliance by external service providers on an ongoing basis.

**Mapped SP 800-53 Controls:** SA-9, SA-9(2)

**Discussion:** External system services include services provided by cloud service providers, managed security service providers, and other external entities. Organizations require external providers to comply with CUI protection requirements through contracts, service-level agreements, and monitoring.

---

## 03.16.03 Developer Configuration Management

Require the developer of the system, system component, or system service to perform configuration management during system development, integration, and operation.

**Mapped SP 800-53 Controls:** SA-10

**Discussion:** Configuration management during system development ensures that changes are tracked, controlled, and documented. This includes tracking changes to the system during development, maintaining documentation, and ensuring only authorized changes are made.

---

## 03.16.04 Developer Security and Privacy Testing

Require the developer of the system, system component, or system service to create and implement a security assessment plan, produce evidence of execution of the plan, and implement a verifiable flaw remediation process.

**Mapped SP 800-53 Controls:** SA-11

**Discussion:** Developer testing verifies that security functions work as intended. Testing includes unit testing, integration testing, system testing, and regression testing of security functions. Flaw remediation processes address vulnerabilities discovered during testing.

---

## References

- NIST SP 800-171 Rev 3: https://csrc.nist.gov/publications/detail/sp/800-171/rev-3/final
- NIST SP 800-53 Rev 5: System and Services Acquisition (SA) Family
- [Cross-reference: SP 800-53 to SP 800-171](../cross-references/800-53-to-800-171.md)
