# NIST SP 800-171 Rev 3 — 03.08 Media Protection

The Media Protection family provides security requirements for protecting system media containing CUI, both in digital and non-digital forms, and for limiting access to CUI on system media to authorized users.

**Source:** Derived from SP 800-53 Rev 5 Media Protection (MP) family.

---

## 03.08.01 Media Access

Restrict access to CUI on system media to authorized users.

**Mapped SP 800-53 Controls:** MP-2

**Discussion:** System media includes digital media (e.g., flash drives, CDs, DVDs, external hard drives) and non-digital media (e.g., paper, microfilm). Organizations restrict access to media containing CUI through physical controls, encryption, or both.

---

## 03.08.02 Media Marking

Mark system media indicating the distribution limitations, handling caveats, and applicable security markings of the information.

**Mapped SP 800-53 Controls:** MP-3

**Discussion:** Organizations mark media to indicate CUI designation, distribution limitations, handling instructions, and applicable security markings. Marking is done in accordance with CUI marking guidance from the National Archives.

---

## 03.08.03 Media Storage

Physically control and securely store system media containing CUI within controlled areas.

**Mapped SP 800-53 Controls:** MP-4

**Discussion:** Organizations physically control and securely store media containing CUI. Controlled areas include locked rooms, safes, or areas with access control mechanisms. Digital media may be secured through encryption as an alternative or complement to physical controls.

---

## 03.08.04 Media Transport

Protect and control system media containing CUI during transport outside of controlled areas.

**Mapped SP 800-53 Controls:** MP-5, MP-5(3)

**Discussion:** Organizations protect media during transport using encryption for digital media and physical protections (e.g., locked containers) for both digital and non-digital media. Controlled transport includes hand-carrying media, using bonded courier services, or encrypted digital transmission. The use of cryptographic mechanisms (e.g., FIPS-validated encryption) protects the confidentiality of CUI during transport.

---

## 03.08.05 Media Sanitization

Sanitize system media containing CUI prior to disposal, release out of organizational control, or release for reuse.

**Mapped SP 800-53 Controls:** MP-6, MP-6(1)

**Discussion:** Organizations sanitize media using methods commensurate with the sensitivity of the information and the type of media. Methods include clearing (overwriting), purging (degaussing), or destroying (shredding, incineration). NIST SP 800-88 provides guidance on media sanitization. Organizations review, approve, track, document, and verify sanitization actions.

---

## 03.08.06 CUI on Portable Storage Devices

Prohibit the use of portable storage devices when such devices have no identifiable owner. Implement restrictions on the use of portable storage devices containing CUI on external systems.

**Mapped SP 800-53 Controls:** MP-7, AC-19

**Discussion:** Organizations control the use of portable storage devices (USB drives, external hard drives, etc.) to prevent unauthorized exfiltration of CUI. Devices without identifiable owners may contain malicious code and are prohibited. Encryption is required for CUI on portable storage devices.

---

## References

- NIST SP 800-171 Rev 3: https://csrc.nist.gov/publications/detail/sp/800-171/rev-3/final
- NIST SP 800-53 Rev 5: Media Protection (MP) Family
- [Cross-reference: SP 800-53 to SP 800-171](../cross-references/800-53-to-800-171.md)
