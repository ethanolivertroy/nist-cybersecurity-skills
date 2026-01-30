# NIST SP 800-171 Rev 3 — 03.10 Physical Protection

The Physical Protection family provides security requirements for limiting physical access to systems, equipment, and operating environments to authorized individuals.

**Source:** Derived from SP 800-53 Rev 5 Physical and Environmental Protection (PE) family.

---

## 03.10.01 Physical Access Authorizations

Develop, approve, and maintain a list of individuals with authorized access to the facility where the system resides. Issue authorization credentials for facility access. Review the access list and authorization credentials periodically.

**Mapped SP 800-53 Controls:** PE-2

**Discussion:** Organizations maintain a current list of personnel authorized to access facilities where systems reside. Authorization credentials include ID badges, identification cards, and smart cards. Lists and credentials are reviewed and updated periodically and when personnel changes occur.

---

## 03.10.02 Physical Access Control

Enforce physical access authorizations at entry and exit points to the facility where the system resides by verifying individual access authorizations before granting access. Maintain physical access audit logs. Control and manage physical access devices. Escort visitors and monitor visitor activity. Secure keys, combinations, and other physical access devices.

**Mapped SP 800-53 Controls:** PE-3, PE-3(1)

**Discussion:** Physical access controls include guards, fences, turnstiles, locks, card readers, biometrics, and mantraps. Visitors are escorted in areas where CUI is processed, stored, or transmitted. Physical access audit logs capture entry and exit events. Access devices (keys, badges, combinations) are inventoried, changed, and safeguarded.

---

## 03.10.03 Access Control for Transmission

Control physical access to system distribution and transmission lines within organizational facilities.

**Mapped SP 800-53 Controls:** PE-4

**Discussion:** Physical protections applied to system distribution and transmission lines prevent unauthorized physical access to such lines, which could result in eavesdropping or physical tampering. Protections include locked wiring closets, disconnected spare jacks, and protected cabling.

---

## 03.10.04 Access Control for Output Devices

Control physical access to output from output devices to prevent unauthorized individuals from obtaining the output.

**Mapped SP 800-53 Controls:** PE-5

**Discussion:** Output devices include printers, copiers, scanners, fax machines, and audio/video devices. Controlling physical access to output prevents unauthorized individuals from viewing or obtaining CUI. Controls include placing output devices in controlled areas and requiring user authentication before printing.

---

## 03.10.05 Monitoring Physical Access

Monitor the facility where the system resides to detect and respond to physical security incidents.

**Mapped SP 800-53 Controls:** PE-6, PE-6(1)

**Discussion:** Organizations employ monitoring mechanisms such as intrusion alarms, video surveillance, security guards, and motion detectors. Physical access monitoring is coordinated with intrusion detection capabilities. Monitoring logs are reviewed regularly.

---

## 03.10.06 Visitor Access Records

Maintain visitor access records to the facility where the system resides that include name of visitor, organization, date of access, time of entry and departure, purpose of visit, and name of person visited. Review visitor access records periodically.

**Mapped SP 800-53 Controls:** PE-8

**Discussion:** Organizations document visitor access to facilities containing systems that process, store, or transmit CUI. Visitor logs include sufficient information to identify visitors and support investigations of physical security incidents.

---

## References

- NIST SP 800-171 Rev 3: https://csrc.nist.gov/publications/detail/sp/800-171/rev-3/final
- NIST SP 800-53 Rev 5: Physical and Environmental Protection (PE) Family
- [Cross-reference: SP 800-53 to SP 800-171](../cross-references/800-53-to-800-171.md)
