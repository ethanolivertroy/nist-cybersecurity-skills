# NIST SP 800-63 Rev 4 — Digital Identity Guidelines

## Purpose

NIST Special Publication 800-63 Revision 4 provides technical requirements and guidelines for federal agencies implementing digital identity services. It covers the full identity lifecycle: identity proofing, authentication, and federation. Rev 4 (published 2024) introduces significant updates including the addition of a fourth volume on threats and security considerations, updated requirements for phishing-resistant authenticators, expanded equity and usability guidance, and alignment with evolving threats.

The publication applies to digital transactions between individuals and federal systems, but is widely adopted by the private sector as a de facto standard for digital identity.

## Document Structure — Four Volumes

SP 800-63 Rev 4 consists of a parent document and four volumes:

| Volume | Title | Scope |
|--------|-------|-------|
| **SP 800-63-4** | Digital Identity Guidelines (Parent) | Overall framework, assurance levels, risk assessment, selecting assurance levels |
| **SP 800-63A-4** | Identity Proofing and Enrollment | Identity proofing requirements at IAL1, IAL2, IAL3 |
| **SP 800-63B-4** | Authentication and Lifecycle Management | Authenticator requirements at AAL1, AAL2, AAL3 |
| **SP 800-63C-4** | Federation and Assertions | Federation protocols and assertion requirements at FAL1, FAL2, FAL3 |
| **SP 800-63D-4** | Threats and Security Considerations | Threat analysis for identity systems (new in Rev 4) |

## Identity Assurance Levels (IAL)

IAL specifies the degree of confidence in the identity proofing process — that the person claiming an identity is in fact that person.

### IAL1 — No Identity Proofing Required

- No requirement to link the applicant to a specific real-world identity
- Self-asserted attributes may be collected but are not verified
- Appropriate when the activity does not require knowing who the person is
- Example: Anonymous access to public-facing government information, low-risk account creation

### IAL2 — Remote or In-Person Identity Proofing

- Evidence of real-world identity is collected and verified
- Supports both **remote** and **in-person** proofing processes
- Requires presentation of identity evidence (e.g., driver's license, passport) and verification that the evidence is genuine and belongs to the applicant
- Evidence strength requirements: At least one piece of SUPERIOR or STRONG evidence, or two pieces of STRONG evidence, or one STRONG plus two FAIR pieces of evidence
- Biometric verification (e.g., selfie match to photo ID) may be used for remote proofing
- Address confirmation is required
- Example: Creating an account at a federal benefits portal, healthcare identity verification

### IAL3 — In-Person or Supervised Remote Identity Proofing

- Requires **in-person** proofing or **supervised remote** proofing with a trained operator
- Physical presence of the applicant before a trusted agent, or supervised remote session with equivalent controls
- Strongest evidence requirements: Must include at least one SUPERIOR evidence
- Biometric collection is required for future authentication binding
- Example: Obtaining a federal PIV card, high-assurance identity for national security systems

### Key IAL Concepts in Rev 4

- **Evidence strength tiers:** UNACCEPTABLE, WEAK, FAIR, STRONG, SUPERIOR — based on document security features, verification methods, and issuing authority rigor
- **Equity considerations:** Rev 4 emphasizes that identity proofing must accommodate individuals who may lack traditional identity documents
- **Fraud mitigation:** Requirements for detecting fraudulent documents and impostor attempts

## Authenticator Assurance Levels (AAL)

AAL specifies the confidence in the authentication process — that the person accessing the system is the same person who enrolled.

### AAL1 — Single-Factor Authentication

- Requires at least **one authentication factor** (something you know, have, or are)
- Permits a wide range of authenticator types including passwords (memorized secrets), OTP devices, and single-factor cryptographic devices
- Reauthentication required at least every **30 days** (or per policy)
- Example: Username and password for a low-risk government application

### AAL2 — Multi-Factor Authentication

- Requires **two different authentication factors**
- Acceptable combinations include:
  - Multi-factor cryptographic device (single device providing two factors)
  - Memorized secret + single-factor OTP device
  - Memorized secret + single-factor cryptographic device or software
  - Single-factor cryptographic device + memorized secret
- Reauthentication required at least every **12 hours**, with 30-minute inactivity timeout
- **Phishing-resistant authenticators are recommended** at AAL2 in Rev 4
- Example: Password plus hardware OTP token for federal agency systems

### AAL3 — Hardware-Based Multi-Factor Authentication

- Requires a **hardware-based authenticator** and a verifier impersonation-resistant (phishing-resistant) authentication protocol
- The authenticator must provide a cryptographic proof of possession through a secure protocol
- Requires a **hardware cryptographic authenticator** (e.g., FIDO2 security key, PIV smart card)
- Reauthentication required at least every **12 hours**, with 15-minute inactivity timeout
- Example: PIV card authentication for classified systems, FIDO2 security key for high-value transactions

### Authenticator Types Defined in SP 800-63B

| Type | Description | Factor(s) |
|------|-------------|-----------|
| **Memorized Secret** | Password or PIN | Something you know |
| **Look-Up Secret** | Pre-printed codes, recovery codes | Something you have |
| **Out-of-Band Device** | Push notification or code sent to a separate device (e.g., SMS, app-based) | Something you have |
| **Single-Factor OTP Device** | Hardware or software token generating time-based (TOTP) or event-based (HOTP) codes | Something you have |
| **Multi-Factor OTP Device** | OTP device that requires a second factor (PIN/biometric) to activate | Something you have + know/are |
| **Single-Factor Cryptographic Software** | Software-based cryptographic key (e.g., certificate on a device) | Something you have |
| **Single-Factor Cryptographic Device** | Hardware device with embedded cryptographic key | Something you have |
| **Multi-Factor Cryptographic Software** | Software-based key activated by a second factor | Something you have + know/are |
| **Multi-Factor Cryptographic Device** | Hardware device activated by a second factor (e.g., PIV card with PIN) | Something you have + know/are |

### Phishing-Resistant Authenticators

Rev 4 places significant emphasis on **phishing-resistant authenticators** — those that cryptographically bind the authentication to the specific relying party and are resistant to verifier impersonation attacks:

- **FIDO2/WebAuthn:** Public key cryptography bound to the relying party origin. The authenticator signs a challenge that includes the relying party's domain, preventing phishing.
- **PKI/PIV Smart Cards:** Certificate-based authentication using mutual TLS or challenge-response. The server's identity is validated by the client.

OMB Memorandum M-22-09 requires federal agencies to use phishing-resistant MFA for agency staff, contractors, and partners.

## Federation Assurance Levels (FAL)

FAL specifies the confidence in federated identity assertions — the security of the token or assertion passed between an Identity Provider (IdP) and a Relying Party (RP).

### FAL1 — Bearer Assertion

- The assertion (e.g., SAML assertion, OIDC ID token) is a **bearer token** — whoever possesses it can use it
- The assertion is signed by the IdP and verified by the RP
- Channel protections (TLS) are required to prevent interception
- No holder-of-key proof required
- Example: Standard SAML SSO or OIDC flow for low-risk applications

### FAL2 — Holder-of-Key Assertion

- The assertion includes a reference to a **cryptographic key held by the subscriber**
- The RP verifies that the presenter of the assertion also controls the referenced key (proof of possession)
- Protects against assertion theft — even if the assertion is intercepted, it cannot be used without the key
- Example: OIDC with DPoP (Demonstration of Proof-of-Possession), SAML with holder-of-key profile

### FAL3 — Holder-of-Key Assertion with Direct Presentation

- Requires all FAL2 properties plus the assertion is presented directly from the IdP to the RP through the subscriber (no intermediary stores or caches the assertion)
- Cryptographic authentication of the subscriber to the RP at the time of assertion presentation
- Highest assurance for federated transactions
- Example: Cryptographic proof at both the assertion layer and the subscriber-to-RP channel

### Federation Protocols

SP 800-63C addresses several federation protocols:

- **SAML 2.0:** XML-based assertion standard widely used in government. Supports web browser SSO and back-channel attribute queries.
- **OpenID Connect (OIDC):** JSON/REST-based identity layer on OAuth 2.0. Increasingly preferred for modern applications.
- **Kerberos:** Ticket-based authentication commonly used in enterprise Windows environments.

## Volume D: Threats and Security Considerations (New in Rev 4)

SP 800-63D is a new addition in Rev 4 that provides a comprehensive threat analysis for each stage of the digital identity lifecycle:

### Identity Proofing Threats
- **Fraudulent identity evidence:** Forged or counterfeit documents
- **Synthetic identity fraud:** Combining real and fabricated identity attributes
- **Social engineering:** Manipulating the proofing process or operators
- **Deepfakes:** Using AI-generated images or video to defeat biometric verification

### Authentication Threats
- **Phishing and verifier impersonation:** Tricking users into providing credentials to fake sites
- **Credential stuffing:** Using breached credentials from other sites
- **Man-in-the-middle:** Intercepting and relaying authentication sessions
- **Authenticator theft or duplication:** Physical theft or cloning of hardware tokens
- **Session hijacking:** Stealing authenticated session tokens

### Federation Threats
- **Assertion theft/replay:** Intercepting and reusing federation assertions
- **IdP compromise:** Compromise of the identity provider affects all relying parties
- **Assertion injection:** Forging or modifying assertions
- **Cross-site request forgery (CSRF):** Exploiting federation flows

### Mitigation Strategies
SP 800-63D maps specific mitigations to each threat, guiding organizations in selecting appropriate IAL, AAL, and FAL levels based on their threat model.

## Selecting Assurance Levels

The parent document (SP 800-63-4) provides guidance for selecting appropriate IAL, AAL, and FAL levels based on risk:

1. **Identify potential harms** — Consider harms to the individual, the organization, and the public if identity is falsely claimed or authentication is defeated
2. **Map harms to impact categories** — Inconvenience, financial loss, agency reputation, unauthorized disclosure of sensitive information, civil or criminal violations, personal safety
3. **Assess impact levels** — Low, Moderate, High for each harm category
4. **Select the highest applicable assurance level** — The highest impact across all categories determines the minimum assurance level

## References

- NIST SP 800-63 Rev 4: https://csrc.nist.gov/publications/detail/sp/800-63/4/final
- NIST SP 800-63A Rev 4: Identity Proofing and Enrollment
- NIST SP 800-63B Rev 4: Authentication and Lifecycle Management
- NIST SP 800-63C Rev 4: Federation and Assertions
- NIST SP 800-63D Rev 4: Threats and Security Considerations
- OMB M-22-09: Moving the U.S. Government Toward Zero Trust Cybersecurity Principles
- FIDO Alliance: https://fidoalliance.org/
