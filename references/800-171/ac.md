# NIST SP 800-171 Rev 3 — 03.01 Access Control

The Access Control family provides security requirements to limit system access to authorized users, processes acting on behalf of authorized users, and devices. It addresses both logical and physical access, remote access, and the use of external systems.

**Source:** Derived from SP 800-53 Rev 5 Access Control (AC) family.

---

## 03.01.01 Account Management

Manage system accounts, including establishing conditions for group and role membership, identifying authorized users, and managing account lifecycle (creation, modification, disabling, removal).

**Mapped SP 800-53 Controls:** AC-2

**Discussion:** Organizations define account types, assign account managers, and establish processes for creating, enabling, modifying, disabling, and removing accounts. This includes reviewing accounts periodically and establishing conditions for group and role membership.

---

## 03.01.02 Access Enforcement

Enforce approved authorizations for logical access to systems and information in accordance with applicable access control policies.

**Mapped SP 800-53 Controls:** AC-3

**Discussion:** Access enforcement mechanisms include access control lists, access control matrices, and role-based access control. The system enforces approved authorizations at the application and service level in addition to the OS level.

---

## 03.01.03 Information Flow Enforcement

Enforce approved authorizations for controlling the flow of CUI within the system and between connected systems.

**Mapped SP 800-53 Controls:** AC-4

**Discussion:** Information flow control regulates where CUI can travel within systems and between interconnected systems. This includes boundary protections, filtering, and content-checking mechanisms.

---

## 03.01.04 Separation of Duties

Separate the duties of individuals to reduce the risk of malevolent activity without collusion.

**Mapped SP 800-53 Controls:** AC-5

**Discussion:** Separation of duties addresses the potential for abuse of authorized privileges and helps reduce the risk of malicious activity. Examples include dividing mission/business functions and support functions, and ensuring different individuals perform system support functions.

---

## 03.01.05 Least Privilege

Employ the principle of least privilege, including for specific security functions and privileged accounts.

**Mapped SP 800-53 Controls:** AC-6, AC-6(1), AC-6(2), AC-6(5), AC-6(7), AC-6(9), AC-6(10)

**Discussion:** Organizations employ least privilege for specific duties and systems. This includes authorizing access only to security functions that users need, requiring non-privileged accounts for nonsecurity functions, restricting privileged accounts, auditing privileged function use, and preventing non-privileged users from executing privileged functions.

---

## 03.01.06 Unsuccessful Logon Attempts

Enforce a limit on consecutive invalid logon attempts by a user during an organization-defined time period and automatically lock the account or delay next logon when the maximum is exceeded.

**Mapped SP 800-53 Controls:** AC-7

**Discussion:** Organizations define the maximum number of unsuccessful logon attempts and the time period in which the attempts occur. The system can automatically lock the account for a specified time period, lock the account until released by an administrator, or delay the next logon prompt.

---

## 03.01.07 System Use Notification

Display a system use notification message before granting system access informing users of applicable monitoring, recording, and usage conditions.

**Mapped SP 800-53 Controls:** AC-8

**Discussion:** System use notification messages can be implemented using logon banners. The content and format of the notification are determined by the organization, but typically include notices regarding authorized use, monitoring, and potential consequences of unauthorized use.

---

## 03.01.08 Session Lock

Prevent further access to the system by initiating a session lock after an organization-defined time period of inactivity or upon receiving a request from a user. Retain the session lock until the user reestablishes access using established identification and authentication procedures.

**Mapped SP 800-53 Controls:** AC-11, AC-11(1)

**Discussion:** Session locks are temporary actions taken when users stop work and move away from the immediate vicinity of systems but do not want to log out because of the temporary nature of their absences. The session lock conceals information previously visible on the display with a publicly viewable image (pattern-hiding display).

---

## 03.01.09 Session Termination

Automatically terminate a user session after organization-defined conditions or trigger events.

**Mapped SP 800-53 Controls:** AC-12

**Discussion:** Conditions or trigger events requiring automatic session termination include organization-defined periods of user inactivity, targeted responses to certain types of incidents, and time-of-day restrictions on system use.

---

## 03.01.10 Permitted Actions Without Identification or Authentication

Identify user actions that can be performed on the system without identification or authentication consistent with organizational mission and business functions.

**Mapped SP 800-53 Controls:** AC-14

**Discussion:** Specific user actions may be permitted without identification or authentication if organizations determine that identification or authentication is not required. Organizations may allow a limited number of user actions without identification or authentication, such as accessing a public website or other publicly accessible information.

---

## 03.01.11 Remote Access

Establish usage restrictions, configuration requirements, and connection requirements for each type of remote access allowed. Authorize each type of remote access prior to establishing the connection. Route remote access via managed access control points.

**Mapped SP 800-53 Controls:** AC-17, AC-17(1), AC-17(2), AC-17(3), AC-17(4)

**Discussion:** Remote access is access to systems by users communicating through external networks (e.g., the Internet). Types of remote access include VPNs, dial-up, broadband, and wireless. Organizations use encrypted VPNs to protect confidentiality of remote connections. Managed access control points include proxies, gateways, routers, firewalls, and encrypted tunnels.

---

## 03.01.12 Wireless Access

Establish configuration requirements, connection requirements, and implementation guidance for wireless access. Authorize wireless access prior to allowing connections. Protect wireless access using authentication and encryption.

**Mapped SP 800-53 Controls:** AC-18, AC-18(1)

**Discussion:** Wireless technologies include microwave, packet radio, 802.11x, and Bluetooth. Organizations use authentication protocols and encryption to protect wireless access. Wireless networking capabilities represent a significant potential vulnerability.

---

## 03.01.13 Access Control for Mobile Devices

Establish configuration requirements, connection requirements, and implementation guidance for organization-controlled mobile devices. Authorize the connection of mobile devices to organizational systems.

**Mapped SP 800-53 Controls:** AC-19, AC-19(5)

**Discussion:** Mobile devices include laptops, tablets, smartphones, and similar devices. Organizations apply full-device encryption or container-based encryption on mobile devices. Access control for mobile devices addresses device identification and authentication, configuration management, implementation of mandatory protective software, and scanning devices for malicious code.

---

## 03.01.14 Use of External Systems

Establish terms and conditions for authorized individuals to access the system from external systems. Establish terms and conditions for processing, storing, or transmitting CUI using external systems.

**Mapped SP 800-53 Controls:** AC-20, AC-20(1), AC-20(2)

**Discussion:** External systems are systems that are not organizationally owned or operated. Terms and conditions address the types of applications that can be accessed from external systems, maximum security categorization of information that can be processed, stored, or transmitted, and the use of organizationally controlled portable storage devices on external systems. Organizations restrict or prohibit the use of personally owned devices.

---

## 03.01.15 Information Sharing

Facilitate information sharing by enabling authorized users to determine whether access authorizations assigned to a sharing partner match the access restrictions on the information.

**Mapped SP 800-53 Controls:** AC-21

**Discussion:** Information sharing applies to information that may be restricted in some manner based on policy, regulation, or organizational directive. Organizations establish the conditions under which CUI can be shared, including with external partners.

---

## References

- NIST SP 800-171 Rev 3: https://csrc.nist.gov/publications/detail/sp/800-171/rev-3/final
- NIST SP 800-53 Rev 5: Access Control (AC) Family
- [Cross-reference: SP 800-53 to SP 800-171](../cross-references/800-53-to-800-171.md)
