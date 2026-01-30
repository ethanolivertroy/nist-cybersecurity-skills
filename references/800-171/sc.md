# NIST SP 800-171 Rev 3 — 03.13 System and Communications Protection

The System and Communications Protection family provides security requirements for monitoring, controlling, and protecting communications at external and key internal boundaries of systems processing CUI.

**Source:** Derived from SP 800-53 Rev 5 System and Communications Protection (SC) family.

---

## 03.13.01 Boundary Protection

Monitor and control communications at the external managed interfaces of the system and at key internal managed interfaces within the system. Implement subnetworks for publicly accessible system components that are physically or logically separated from internal organizational networks.

**Mapped SP 800-53 Controls:** SC-7, SC-7(5), SC-7(7)

**Discussion:** Boundary protection includes the use of routers, firewalls, gateways, intrusion detection/prevention systems, and DMZ architectures. External boundary protections are implemented at the Internet boundary and at connections to other external systems. Internal boundary protection segments networks containing CUI from other networks. Organizations deny network communications by default and allow by exception.

---

## 03.13.02 Cryptographic Protection

Implement cryptographic mechanisms to prevent unauthorized disclosure of CUI during transmission and while in storage.

**Mapped SP 800-53 Controls:** SC-8, SC-8(1), SC-28, SC-28(1)

**Discussion:** Organizations protect the confidentiality of CUI during transmission using FIPS-validated cryptography (e.g., TLS, IPsec, S/MIME) and during storage using full-disk encryption, file-level encryption, or database encryption. Cryptographic mechanisms comply with applicable laws, executive orders, directives, and regulations.

---

## 03.13.03 Denial-of-Service Protection

Protect against or limit the effects of denial-of-service attacks on organizational systems.

**Mapped SP 800-53 Controls:** SC-5

**Discussion:** Organizations implement protective measures against denial-of-service attacks including monitoring, filtering, and increasing bandwidth capacity. Detection mechanisms identify attacks and enable response actions.

---

## 03.13.04 Collaborative Computing Devices and Applications

Prohibit remote activation of collaborative computing devices and applications with exceptions defined by the organization. Provide an explicit indication of use to users physically present at the devices.

**Mapped SP 800-53 Controls:** SC-15

**Discussion:** Collaborative computing devices include networked whiteboards, cameras, and microphones. Organizations prohibit remote activation of these devices to prevent unauthorized monitoring. Visual or auditory indicators inform users when devices are active.

---

## 03.13.05 Cryptographic Key Establishment and Management

Establish and manage cryptographic keys when cryptography is employed within the system.

**Mapped SP 800-53 Controls:** SC-12

**Discussion:** Cryptographic key management includes key generation, distribution, storage, access, use, rotation, and destruction. Organizations manage keys in accordance with applicable requirements and standards (e.g., NIST SP 800-57).

---

## 03.13.06 Mobile Code

Define and enforce restrictions on the use of mobile code and mobile code technologies.

**Mapped SP 800-53 Controls:** SC-18

**Discussion:** Mobile code technologies include Java, JavaScript, ActiveX, and VBScript. Organizations define acceptable and unacceptable mobile code and technologies. Implementation controls include preventing the download and execution of prohibited mobile code.

---

## 03.13.07 Voice over Internet Protocol

Establish usage restrictions and implementation guidance for Voice over Internet Protocol (VoIP) technologies. Authorize the use of VoIP within the system.

**Mapped SP 800-53 Controls:** SC-19

**Discussion:** VoIP may introduce additional security risks including eavesdropping and denial of service. Organizations establish restrictions and guidance addressing VoIP traffic separation, encryption, and monitoring.

---

## 03.13.08 Session Authenticity

Protect the authenticity of communications sessions.

**Mapped SP 800-53 Controls:** SC-23

**Discussion:** Session authenticity protections guard against man-in-the-middle attacks and session hijacking. Mechanisms include TLS mutual authentication, session tokens, and unique session identifiers.

---

## 03.13.09 Protection of Information at Rest

Protect the confidentiality of CUI at rest.

**Mapped SP 800-53 Controls:** SC-28, SC-28(1)

**Discussion:** Information at rest refers to the state of information when it is not being transmitted or processed. Protection mechanisms include full-disk encryption, file-level encryption, database encryption, and hardware-based encryption. Organizations use FIPS-validated cryptographic mechanisms.

---

## 03.13.10 Process Isolation

Maintain a separate execution domain for each executing system process.

**Mapped SP 800-53 Controls:** SC-39

**Discussion:** Systems provide separate execution domains to prevent processes from interfering with each other. Execution domain separation is implemented through hardware and software mechanisms such as address spaces, kernel/user mode separation, and virtualization.

---

## 03.13.11 Network Segmentation

Implement network segmentation to separate CUI from non-CUI networks where appropriate.

**Mapped SP 800-53 Controls:** SC-7, SC-7(21)

**Discussion:** Organizations logically or physically segment networks to isolate CUI processing from general-purpose networks. Segmentation reduces the attack surface and limits lateral movement by adversaries.

---

## References

- NIST SP 800-171 Rev 3: https://csrc.nist.gov/publications/detail/sp/800-171/rev-3/final
- NIST SP 800-53 Rev 5: System and Communications Protection (SC) Family
- [Cross-reference: SP 800-53 to SP 800-171](../cross-references/800-53-to-800-171.md)
