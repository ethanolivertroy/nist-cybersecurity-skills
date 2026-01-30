# NIST SP 800-171 Rev 3 — 03.04 Configuration Management

The Configuration Management family provides security requirements for establishing and maintaining baseline configurations and inventories of organizational systems, and for managing changes to those configurations.

**Source:** Derived from SP 800-53 Rev 5 Configuration Management (CM) family.

---

## 03.04.01 Baseline Configuration

Establish and maintain baseline configurations and inventories of organizational systems (including hardware, software, firmware, and documentation) throughout the system development life cycle.

**Mapped SP 800-53 Controls:** CM-2, CM-6

**Discussion:** Baseline configurations serve as a basis for future builds, releases, or changes to systems. Organizations establish baseline configurations and maintain them under configuration control. Inventories include hardware, software, firmware, and documentation.

---

## 03.04.02 Configuration Settings

Establish and enforce security configuration settings for information technology products employed in organizational systems.

**Mapped SP 800-53 Controls:** CM-6, CM-6(1)

**Discussion:** Configuration settings are the parameters that can be changed on hardware, software, or firmware components that affect security posture. Organizations establish mandatory configuration settings based on the most restrictive mode consistent with operational requirements, such as CIS Benchmarks or STIGs.

---

## 03.04.03 Configuration Change Control

Track, review, approve or disapprove, and log changes to organizational systems. Control and monitor user-installed software.

**Mapped SP 800-53 Controls:** CM-3, CM-5, CM-11

**Discussion:** Configuration change control involves the systematic proposal, justification, implementation, testing, review, and disposition of changes to the system. Changes include modifications to hardware, software, firmware, and documentation. User-installed software is controlled to prevent unauthorized or malicious software installation.

---

## 03.04.04 Impact Analysis

Analyze changes to the system to determine potential security impacts prior to change implementation.

**Mapped SP 800-53 Controls:** CM-4

**Discussion:** Organizations analyze changes to systems to determine potential security impacts. Security impact analyses are conducted before changes are made and include consideration of the security requirements for the system, potential side effects, and cascading effects on other system components.

---

## 03.04.05 Access Restrictions for Change

Define, document, approve, and enforce physical and logical access restrictions associated with changes to organizational systems.

**Mapped SP 800-53 Controls:** CM-5

**Discussion:** Changes to the hardware, software, or firmware components of systems can potentially have significant effects on the security of the systems. Organizations limit access to change functions to only qualified and authorized individuals. Access restrictions include both physical access (e.g., server rooms) and logical access (e.g., privileged accounts).

---

## 03.04.06 Least Functionality

Configure the system to provide only essential capabilities. Restrict or disable the use of non-essential functions, ports, protocols, and services.

**Mapped SP 800-53 Controls:** CM-7, CM-7(1), CM-7(2)

**Discussion:** Organizations review the system to identify unnecessary functions, ports, protocols, and services and disable or restrict them. This includes removing or disabling unused software, closing unnecessary ports, and enabling only required protocols. Application whitelisting or deny-by-exception may be employed.

---

## 03.04.07 Authorized Software — Allow-by-Exception

Identify software programs authorized to execute on the system and employ a deny-all, permit-by-exception policy to restrict execution of unauthorized software.

**Mapped SP 800-53 Controls:** CM-7(5)

**Discussion:** Allow-by-exception (application whitelisting) identifies authorized software and denies execution of all other software. Organizations maintain a list of approved software and use technical controls (e.g., application whitelisting tools) to enforce the policy.

---

## 03.04.08 System Component Inventory

Develop and document an inventory of system components that accurately reflects the system, includes all components within the system boundary, is at the appropriate level of granularity, and is maintained and reviewed periodically.

**Mapped SP 800-53 Controls:** CM-8, CM-8(1)

**Discussion:** Organizations maintain an accurate, complete, and up-to-date inventory of system components. Components include hardware, software, firmware, and documentation. Automated mechanisms are used to maintain current, complete, and accurate inventories.

---

## 03.04.09 Information Location

Identify and document the location of CUI and the system components on which CUI is processed, stored, or transmitted.

**Mapped SP 800-53 Controls:** CM-12

**Discussion:** Organizations identify where CUI resides within the system to ensure appropriate protections are applied. Understanding CUI location supports data flow analysis, access control, incident response, and data loss prevention.

---

## References

- NIST SP 800-171 Rev 3: https://csrc.nist.gov/publications/detail/sp/800-171/rev-3/final
- NIST SP 800-53 Rev 5: Configuration Management (CM) Family
- [Cross-reference: SP 800-53 to SP 800-171](../cross-references/800-53-to-800-171.md)
