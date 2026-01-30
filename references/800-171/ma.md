# NIST SP 800-171 Rev 3 — 03.07 Maintenance

The Maintenance family provides security requirements for performing timely maintenance on organizational systems and providing controls on the tools, techniques, mechanisms, and personnel used to conduct maintenance.

**Source:** Derived from SP 800-53 Rev 5 Maintenance (MA) family.

---

## 03.07.01 System Maintenance

Perform maintenance on organizational systems. Provide controls on the tools, techniques, mechanisms, and personnel used to conduct system maintenance.

**Mapped SP 800-53 Controls:** MA-2, MA-3, MA-3(1), MA-3(2)

**Discussion:** Maintenance includes both preventive and corrective actions. Organizations approve, control, and monitor locally and remotely executed maintenance activities. Maintenance tools are inspected for improper or unauthorized modifications, and media containing diagnostic programs are checked for malicious code. All maintenance tools are checked before use and all tools are removed after maintenance is complete.

---

## 03.07.02 Nonlocal Maintenance

Approve and monitor nonlocal maintenance and diagnostic activities. Allow the use of nonlocal maintenance only as documented in the security plan. Establish a session upon completion and terminate sessions and network connections when nonlocal maintenance is complete.

**Mapped SP 800-53 Controls:** MA-4, MA-4(3)

**Discussion:** Nonlocal maintenance is performed by individuals communicating through external networks. Organizations require strong authentication for nonlocal maintenance sessions and document credentials for remote maintenance. Sessions are terminated when maintenance is complete. Multifactor authentication may be required for nonlocal maintenance access.

---

## 03.07.03 Maintenance Personnel

Establish a process for maintenance personnel authorization. Maintain a list of authorized maintenance organizations or personnel. Verify that non-escorted personnel performing maintenance have required access authorizations. Designate organizational personnel with required access authorizations and technical competence to supervise maintenance activities of personnel who do not possess required access authorizations.

**Mapped SP 800-53 Controls:** MA-5

**Discussion:** Organizations ensure that maintenance personnel are authorized, trained, and supervised when necessary. Personnel performing maintenance on systems containing CUI must have appropriate access authorizations. Uncleared maintenance personnel are escorted and supervised by authorized individuals.

---

## 03.07.04 Timely Maintenance

Obtain maintenance support or spare parts for system components within an organization-defined time period of failure.

**Mapped SP 800-53 Controls:** MA-6

**Discussion:** Organizations define the time period for obtaining maintenance support based on the criticality of systems and the potential impact of failure. Service-level agreements with maintenance providers specify response times.

---

## References

- NIST SP 800-171 Rev 3: https://csrc.nist.gov/publications/detail/sp/800-171/rev-3/final
- NIST SP 800-53 Rev 5: Maintenance (MA) Family
- [Cross-reference: SP 800-53 to SP 800-171](../cross-references/800-53-to-800-171.md)
