# FIPS Standards Overview — Federal Information Processing Standards

## What are FIPS?

Federal Information Processing Standards (FIPS) are standards and guidelines developed by NIST for federal computer systems. Unlike NIST Special Publications (which are generally guidance), FIPS are **mandatory for federal agencies** when approved by the Secretary of Commerce. FIPS are issued when there are compelling federal government requirements for standards and no acceptable voluntary standards exist.

Key FIPS for cybersecurity include FIPS 140-3, FIPS 199, FIPS 200, and FIPS 201.

---

## FIPS 140-3 — Security Requirements for Cryptographic Modules

### Purpose

FIPS 140-3 specifies the security requirements for cryptographic modules used within a security system to protect sensitive (but unclassified) information. It superseded FIPS 140-2 effective March 22, 2019, with a transition period. FIPS 140-3 aligns with international standards ISO/IEC 19790:2012 and ISO/IEC 24759:2017.

### Applicability

- All federal agencies that use cryptographic-based security systems to protect sensitive information
- Applies to the design and implementation of cryptographic modules (hardware, software, firmware, or hybrid)
- Private sector organizations voluntarily adopt FIPS 140-3 and often require it for products used in regulated industries (healthcare, financial services)

### Security Levels

FIPS 140-3 defines **four increasing security levels**:

| Level | Name | Description | Physical Security | Key Management |
|-------|------|-------------|-------------------|----------------|
| **Level 1** | Basic | Lowest level. At least one approved security function or algorithm. No specific physical security mechanisms required beyond basic production-grade enclosure. | Production-grade components | Basic key management |
| **Level 2** | Tamper-Evident | Adds tamper-evident coatings or seals to Level 1 requirements. Requires role-based authentication of operators. Requires running on an operating system that meets Common Criteria EAL2 (or equivalent). | Tamper-evident coatings/seals | Role-based authentication |
| **Level 3** | Tamper-Resistant | Adds tamper-detection and response mechanisms (e.g., zeroization of plaintext keys upon tamper detection). Requires identity-based authentication. Physical security prevents unauthorized access to critical security parameters. | Tamper-detection and response; strong enclosures | Identity-based authentication; key zeroization on tamper |
| **Level 4** | Highest | Provides the highest level of security. Complete envelope of protection around the cryptographic module. Detects and responds to all unauthorized physical access attempts. Designed to be resistant to environmental attacks (voltage, temperature). | Environmental failure protection (EFP) or environmental failure testing (EFT) | Automatic zeroization; environmental attack resistance |

### Cryptographic Module Validation Program (CMVP)

- CMVP is a **joint program between NIST and the Canadian Centre for Cyber Security (CCCS)**
- CMVP validates cryptographic modules against FIPS 140-3 requirements
- Testing is performed by accredited **Cryptographic and Security Testing (CST) Laboratories**
- Validated modules are listed on the NIST CMVP website with a certificate number
- Federal agencies are required to use **CMVP-validated cryptographic modules** for the protection of sensitive information
- FedRAMP requires the use of FIPS 140-2/140-3 validated cryptographic modules at all impact levels

### Approved Algorithms

Cryptographic modules must use **NIST-approved algorithms** as specified in:
- FIPS 197 (AES)
- FIPS 186 (Digital Signature Standard — DSA, RSA, ECDSA)
- FIPS 180 / FIPS 202 (Secure Hash Standard — SHA-2, SHA-3)
- SP 800-56A/B (Key Establishment)
- SP 800-90A (Random Number Generation — DRBG)
- SP 800-38 series (Block Cipher Modes of Operation — GCM, CCM, etc.)

Algorithms are validated through the **Cryptographic Algorithm Validation Program (CAVP)** before being used in CMVP-validated modules.

---

## FIPS 199 — Standards for Security Categorization of Federal Information and Information Systems

### Purpose

FIPS 199 provides a standard for categorizing federal information and information systems based on the **potential impact** of a security breach. It is the foundation of the NIST risk management approach and directly drives control selection in the RMF (SP 800-37).

### Security Objectives

FIPS 199 defines three security objectives:

| Objective | Definition |
|-----------|-----------|
| **Confidentiality** | Preserving authorized restrictions on information access and disclosure, including means for protecting personal privacy and proprietary information |
| **Integrity** | Guarding against improper information modification or destruction, and includes ensuring information non-repudiation and authenticity |
| **Availability** | Ensuring timely and reliable access to and use of information |

### Impact Levels

For each security objective, FIPS 199 defines three levels of potential impact:

| Impact Level | Definition |
|-------------|-----------|
| **Low** | The loss of confidentiality, integrity, or availability could be expected to have a **limited adverse effect** on organizational operations, organizational assets, or individuals. A limited adverse effect means: degradation in mission capability to an extent and duration that the organization is able to perform its primary functions but with noticeably reduced effectiveness; minor damage to organizational assets; minor financial loss; or minor harm to individuals. |
| **Moderate** | The loss of confidentiality, integrity, or availability could be expected to have a **serious adverse effect** on organizational operations, organizational assets, or individuals. A serious adverse effect means: significant degradation in mission capability to an extent and duration that the organization is able to perform its primary functions but with significantly reduced effectiveness; significant damage to organizational assets; significant financial loss; or significant harm to individuals that does not involve loss of life or serious life-threatening injuries. |
| **High** | The loss of confidentiality, integrity, or availability could be expected to have a **severe or catastrophic adverse effect** on organizational operations, organizational assets, or individuals. A severe or catastrophic adverse effect means: severe degradation or loss of mission capability to an extent and duration that the organization is not able to perform one or more of its primary functions; major damage to organizational assets; major financial loss; or severe or catastrophic harm to individuals involving loss of life or serious life-threatening injuries. |

### Security Categorization Formula

The security categorization of an information system is expressed as:

```
SC (Information System) = {(Confidentiality, impact), (Integrity, impact), (Availability, impact)}
```

Example:
```
SC (Financial System) = {(Confidentiality, Moderate), (Integrity, High), (Availability, Moderate)}
```

### High-Water Mark

The **overall system categorization** is determined by the **high-water mark** — the highest impact level among the three security objectives. In the example above, the system would be categorized as **High** because integrity is rated High.

The high-water mark determines which SP 800-53 baseline is applied:
- Low impact system -> Low baseline
- Moderate impact system -> Moderate baseline
- High impact system -> High baseline

### Guidance for Categorization

NIST SP 800-60 (Guide for Mapping Types of Information and Information Systems to Security Categories) provides detailed guidance and recommended categorizations for common information types (e.g., financial, health, law enforcement, defense).

---

## FIPS 200 — Minimum Security Requirements for Federal Information and Information Systems

### Purpose

FIPS 200 specifies **minimum security requirements** for federal information and information systems across 17 security-related areas. It is the bridge between FIPS 199 (categorization) and SP 800-53 (control selection).

### The 17 Security Areas

FIPS 200 defines minimum security requirements in the following areas:

1. **Access Control (AC)**
2. **Awareness and Training (AT)**
3. **Audit and Accountability (AU)**
4. **Certification, Accreditation, and Security Assessments (CA)** (now Assessment, Authorization, and Monitoring)
5. **Configuration Management (CM)**
6. **Contingency Planning (CP)**
7. **Identification and Authentication (IA)**
8. **Incident Response (IR)**
9. **Maintenance (MA)**
10. **Media Protection (MP)**
11. **Physical and Environmental Protection (PE)**
12. **Planning (PL)**
13. **Personnel Security (PS)**
14. **Risk Assessment (RA)**
15. **System and Services Acquisition (SA)**
16. **System and Communications Protection (SC)**
17. **System and Information Integrity (SI)**

### How It Works

1. The organization categorizes the system per **FIPS 199**
2. **FIPS 200** mandates that the organization meet minimum security requirements by applying SP 800-53 controls
3. The organization selects the appropriate **SP 800-53 baseline** (Low, Moderate, or High) corresponding to the FIPS 199 categorization
4. The organization **tailors** the baseline as needed per SP 800-53 and SP 800-37 guidance
5. The resulting set of controls satisfies the FIPS 200 minimum security requirements

### Mandatory Applicability

FIPS 200 is **mandatory for all federal agencies** and applies to all information and information systems that support federal operations and assets (excluding national security systems, which are covered by CNSS standards).

---

## FIPS 201 — Personal Identity Verification (PIV) of Federal Employees and Contractors

### Purpose

FIPS 201 (currently FIPS 201-3) specifies requirements for a **Personal Identity Verification (PIV) system** for federal employees and contractors. It was mandated by Homeland Security Presidential Directive 12 (HSPD-12), which required a government-wide standard for secure and reliable identification.

### What is a PIV Card?

The PIV card is a **smart card** that provides:
- **Physical access** to federal facilities (via contactless interface)
- **Logical access** to federal information systems (via contact interface and PKI certificates)
- **Digital signature** capability
- **Encryption** capability

### PIV System Components

| Component | Description |
|-----------|-------------|
| **PIV Card** | Smart card with a contact interface (ISO 7816) and contactless interface (ISO 14443). Contains PKI certificates, biometric data (fingerprints, facial image), and card authentication keys. |
| **PIV Issuance System** | Processes for identity proofing, background investigation, card issuance, and lifecycle management. |
| **PIV Middleware** | Software that enables operating systems and applications to interface with the PIV card. |
| **Card Management System** | Backend infrastructure for issuing, managing, and revoking PIV cards. |
| **PKI Infrastructure** | Certificate authorities (CAs) that issue and manage the certificates stored on PIV cards. Federal PKI (FPKI) serves as the trust framework. |

### Authentication Mechanisms

FIPS 201-3 defines several authentication mechanisms at varying assurance levels:

| Mechanism | Assurance Level | Description |
|-----------|----------------|-------------|
| **PKI-AUTH** | High (AAL3) | PKI-based authentication using the PIV Authentication certificate. Requires PIN to unlock the private key. |
| **PKI-CAK** | Medium | Card Authentication Key — contactless authentication without PIN. For physical access and moderate-assurance logical access. |
| **BIO** | High | Biometric (fingerprint or iris) comparison performed on-card or off-card. Used with another factor. |
| **BIO-A** | High | Attended biometric — biometric comparison performed under supervision. |
| **OCC-AUTH** | Varies | On-Card Comparison — biometric verification performed by the card itself. |
| **SYM-CAK** | Low-Medium | Symmetric Card Authentication Key — for legacy contactless access. |
| **VIS** | Lowest | Visual inspection of the card's physical features. Not suitable for logical access. |

### Derived PIV Credentials

FIPS 201-3 supports **derived PIV credentials** — credentials issued based on proof of possession of a valid PIV card. These are used on mobile devices and other platforms that cannot accommodate a physical smart card reader. Derived credentials can be:
- PKI-based certificates stored in device secure elements
- FIDO2/WebAuthn credentials derived from PIV identity proofing

### Key Requirements

- All federal employees and contractors requiring long-term access must be issued PIV cards
- Identity proofing must meet specified requirements (aligned with SP 800-63A IAL3)
- Background investigation (National Agency Check with Inquiries or Tier 1) is required before PIV issuance
- Cards must be revoked upon employee separation or when eligibility criteria are no longer met
- PIV cards have a maximum lifetime of **6 years**

## Relationship Among FIPS Standards

```
FIPS 199 (Categorize System)
    |
    v
FIPS 200 (Minimum Security Requirements)
    |
    v
SP 800-53 (Select Controls Based on Impact Level)
    |
    v
FIPS 140-3 (Cryptographic Module Requirements for SC/IA Controls)
FIPS 201 (PIV Card Requirements for IA/PE Controls)
```

## References

- FIPS 140-3: https://csrc.nist.gov/publications/detail/fips/140/3/final
- FIPS 199: https://csrc.nist.gov/publications/detail/fips/199/final
- FIPS 200: https://csrc.nist.gov/publications/detail/fips/200/final
- FIPS 201-3: https://csrc.nist.gov/publications/detail/fips/201/3/final
- CMVP Validated Modules: https://csrc.nist.gov/projects/cryptographic-module-validation-program
- SP 800-60: Guide for Mapping Types of Information and Information Systems to Security Categories
- HSPD-12: Policy for a Common Identification Standard for Federal Employees and Contractors
