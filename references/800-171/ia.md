# NIST SP 800-171 Rev 3 — 03.05 Identification and Authentication

The Identification and Authentication family provides security requirements for uniquely identifying and authenticating users, processes, and devices before granting access to systems containing CUI.

**Source:** Derived from SP 800-53 Rev 5 Identification and Authentication (IA) family.

---

## 03.05.01 User Identification and Authentication

Identify system users, processes acting on behalf of users, and devices. Authenticate (or verify) the identities of those users, processes, or devices as a prerequisite to allowing access to organizational systems.

**Mapped SP 800-53 Controls:** IA-2, IA-5

**Discussion:** Users are uniquely identified and authenticated before accessing systems. Common identification includes user IDs, and authentication mechanisms include passwords, tokens, biometrics, or certificates. Each user has a unique account to enable tracing of activity to individuals.

---

## 03.05.02 Multifactor Authentication

Implement multifactor authentication for access to privileged and non-privileged accounts.

**Mapped SP 800-53 Controls:** IA-2(1), IA-2(2)

**Discussion:** Multifactor authentication requires two or more different factors: something you know (password/PIN), something you have (token/smart card), or something you are (biometric). MFA is required for both local and network access to privileged accounts, and for network access to non-privileged accounts.

---

## 03.05.03 Device Identification and Authentication

Identify and authenticate devices before establishing a connection.

**Mapped SP 800-53 Controls:** IA-3

**Discussion:** Devices requiring identification and authentication include servers, workstations, laptops, printers, mobile devices, and networking devices. Methods include MAC address authentication, 802.1X, or digital certificates.

---

## 03.05.04 Identifier Management

Manage system identifiers by receiving authorization from organizational personnel to assign an individual, group, role, service, or device identifier. Select an identifier that identifies an individual, group, role, service, or device. Assign the identifier to the intended individual, group, role, service, or device. Prevent reuse of identifiers for an organization-defined time period. Disable the identifier after an organization-defined time period of inactivity.

**Mapped SP 800-53 Controls:** IA-4

**Discussion:** Identifiers include user names, account numbers, digital certificates, and other devices used to identify users, processes, and devices. Identifiers are managed throughout their lifecycle from issuance through revocation.

---

## 03.05.05 Authenticator Management

Manage system authenticators by verifying the identity of individuals, groups, roles, services, or devices receiving authenticators. Establish initial authenticator content. Establish and implement administrative procedures for initial authenticator distribution, for lost or compromised authenticators, and for revoking authenticators. Change default content of authenticators prior to system installation. Change or refresh authenticators periodically. Protect authenticator content from unauthorized disclosure and modification.

**Mapped SP 800-53 Controls:** IA-5, IA-5(1), IA-5(2), IA-5(6)

**Discussion:** Authenticators include passwords, tokens, biometrics, PKI certificates, and key cards. For password-based authentication, organizations enforce minimum password complexity, change intervals, and password history. Authenticator content is protected in storage and transmission.

---

## 03.05.06 Authenticator Feedback

Obscure feedback of authentication information during the authentication process to protect it from possible exploitation by unauthorized individuals.

**Mapped SP 800-53 Controls:** IA-6

**Discussion:** Authentication feedback — the information provided during an authentication attempt — is obscured to prevent observation by unauthorized individuals. Passwords are masked when entered, displaying asterisks or dots instead of actual characters.

---

## 03.05.07 Cryptographic Module Authentication

Implement mechanisms for authentication to a cryptographic module that meet applicable federal laws, executive orders, policies, and standards for the required authentication.

**Mapped SP 800-53 Controls:** IA-7

**Discussion:** Authentication to cryptographic modules is governed by FIPS 140 requirements. The strength of module authentication is commensurate with the level of certification (FIPS 140-2/140-3 Levels 1–4).

---

## 03.05.08 Replay-Resistant Authentication

Implement replay-resistant authentication mechanisms for access to privileged and non-privileged accounts.

**Mapped SP 800-53 Controls:** IA-2(8)

**Discussion:** Replay-resistant authentication mechanisms include protocols that use nonces or challenges (e.g., TLS, Kerberos), or one-time authenticators (e.g., time-based OTPs). These prevent adversaries from capturing and replaying authentication transactions.

---

## References

- NIST SP 800-171 Rev 3: https://csrc.nist.gov/publications/detail/sp/800-171/rev-3/final
- NIST SP 800-53 Rev 5: Identification and Authentication (IA) Family
- [Cross-reference: SP 800-53 to SP 800-171](../cross-references/800-53-to-800-171.md)
