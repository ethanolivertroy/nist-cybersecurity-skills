# NIST SP 800-207 — Zero Trust Architecture

## Purpose

NIST Special Publication 800-207 defines **Zero Trust Architecture (ZTA)** and provides a roadmap for organizations transitioning from traditional perimeter-based security to a zero trust approach. Published in August 2020, it provides an abstract definition of ZTA, its logical components, deployment models, and use cases. The publication does not prescribe specific technologies but instead describes the principles and architectural components that any ZTA implementation should incorporate.

Zero Trust is a response to the evolving threat landscape in which traditional network perimeters are dissolving due to cloud adoption, remote work, mobile devices, and increasingly sophisticated adversaries who operate inside the network.

## Core Principles of Zero Trust

SP 800-207 is grounded in the following foundational principles:

1. **No implicit trust** — Trust is never granted implicitly based on network location, asset ownership, or physical/network location. Every access request must be evaluated.

2. **Verify explicitly** — All resource access decisions are made dynamically based on the identity of the requester, the state of the requesting device, the behavioral context, and other attributes.

3. **Least privilege access** — Access is granted with the minimum permissions necessary to perform the task, scoped to the specific resource, and limited in duration.

4. **Assume breach** — The enterprise assumes that adversaries are already present in the environment. Security is designed to limit lateral movement and minimize blast radius.

## The Seven Tenets of Zero Trust

SP 800-207 defines seven foundational tenets:

1. **All data sources and computing services are considered resources.** A network may be composed of multiple classes of devices. Small devices (e.g., IoT) may also be treated as resources needing protection.

2. **All communication is secured regardless of network location.** Network location alone does not imply trust. Communications on the enterprise LAN must meet the same security requirements as those traversing the public internet (encryption, integrity, source authentication).

3. **Access to individual enterprise resources is granted on a per-session basis.** Trust in the requester is evaluated before access is granted. Access to one resource does not automatically grant access to different resources. Authentication and authorization are discrete functions.

4. **Access to resources is determined by dynamic policy.** Policy may include observable client identity, application/service identity, requesting asset health, behavioral patterns, environmental attributes (time, location, threat intelligence), and other factors.

5. **The enterprise monitors and measures the integrity and security posture of all owned and associated assets.** No device is inherently trusted. The enterprise evaluates device security posture, applies patches, and monitors device behavior.

6. **All resource authentication and authorization are dynamic and strictly enforced before access is allowed.** The enterprise uses an identity, credential, and access management (ICAM) system that includes multifactor authentication. Continual monitoring with possible reauthentication during sessions.

7. **The enterprise collects as much information as possible about the current state of assets, network infrastructure, and communications.** The data is used to improve security posture, inform policy decisions, and support forensic analysis.

## Logical Components

SP 800-207 defines a logical architecture with key components:

### Policy Decision Point (PDP)

The PDP is the brain of ZTA, responsible for making access decisions. It consists of two sub-components:

- **Policy Engine (PE):** Makes the ultimate decision to grant, deny, or revoke access to a resource. The PE uses enterprise policy, input from external sources (threat intelligence, SIEM), and the trust algorithm to make decisions.

- **Policy Administrator (PA):** Responsible for establishing and shutting down the communication path between a subject and a resource. Generates session-specific authentication tokens or credentials. Communicates with the Policy Enforcement Point to allow or deny sessions.

### Policy Enforcement Point (PEP)

The PEP enables, monitors, and terminates connections between a subject and an enterprise resource. It is split into two logical components:

- **Client-side agent:** The component that initiates the access request (e.g., an agent on a laptop, a gateway)
- **Resource-side gateway/agent:** The component that controls access to the resource (e.g., a reverse proxy, API gateway, firewall)

The PEP is the only component that interacts directly with the data plane. It forwards requests to the PA, receives the decision, and enforces it.

### Supporting Components

| Component | Role |
|-----------|------|
| **Continuous Diagnostics and Mitigation (CDM) System** | Gathers information about the enterprise's asset state (patch level, software, configuration). Feeds data to the PE. |
| **Industry Compliance System** | Ensures the enterprise remains compliant with regulatory requirements. Feeds policy rules. |
| **Threat Intelligence Feed** | Provides external threat information (new attacks, vulnerabilities, malware). Helps the PE make informed decisions. |
| **Network and System Activity Logs** | Enterprise SIEM or similar system that aggregates logs. Provides real-time and forensic analysis. |
| **Data Access Policy** | The set of rules and attributes defining who, what, when, where, and how resources may be accessed. |
| **Enterprise Public Key Infrastructure (PKI)** | Issues and manages certificates for resources, services, and users. |
| **Identity Management System** | Creates, stores, and manages enterprise user accounts and identity records (e.g., LDAP, Active Directory, SAML/OIDC provider). |
| **Security Information and Event Management (SIEM)** | Collects security-centric information for analysis, policy refinement, and alerting. |

## Trust Algorithm

The **trust algorithm** is the process used by the PE to determine whether to grant access to a resource. Inputs to the trust algorithm include:

1. **Access request:** The subject requesting access and the resource being requested
2. **Subject identity and attributes:** User identity, role, group membership, authentication assurance level
3. **Asset state:** Device health, patch level, presence of required software (e.g., EDR), certificate validity
4. **Behavioral patterns:** Historical access patterns, deviations from normal behavior, time of access, geolocation
5. **Environmental context:** Current threat level, network posture, time-based policies
6. **Threat intelligence:** Known indicators of compromise, active campaigns, vulnerability disclosures

The trust algorithm may operate in two modes:

- **Criteria-based:** Uses a set of weighted criteria (e.g., score-based). Each factor contributes to an overall trust score. Access is granted if the score exceeds a threshold.
- **Singular:** A single factor can deny access regardless of other factors (e.g., a compromised credential immediately blocks access).

Most implementations use a hybrid approach.

## Deployment Models

SP 800-207 describes three primary approaches to ZTA deployment:

### 1. Enhanced Identity Governance

- Uses the **identity of the actor** as the primary policy component
- Enterprise resource access is gated by identity verification and access policies
- Relies heavily on identity providers, directory services, and MFA
- Best suited for environments with strong identity infrastructure
- Example technologies: IAM platforms, SAML/OIDC, conditional access policies

### 2. Micro-Segmentation

- Uses **network micro-segmentation** to place resources on individual (or small group) network segments protected by gateway devices
- The PEP acts as a gateway/firewall controlling access to each segment
- Infrastructure-centric approach — places protection at the network level
- Best suited for environments with diverse infrastructure (on-premise, cloud, legacy)
- Example technologies: Software-defined networking (SDN), next-generation firewalls, micro-segmentation platforms

### 3. Software Defined Perimeters (SDP)

- Uses **network infrastructure** to implement zero trust — the network is overlaid with software-based controls
- The PA acts as a network controller, setting up and tearing down communication paths
- Resources are hidden from unauthorized users — not even visible on the network unless access is approved (concept of a "dark cloud")
- Example technologies: SDP solutions (based on Cloud Security Alliance SDP specification), overlay networks

Most real-world ZTA deployments **combine elements** of all three approaches.

## Migration Approaches

SP 800-207 recommends a **phased approach** to ZTA migration:

### Phase 1: Identify Actors and Assets
- Identify all subjects (users, services, machines) and resources on the network
- Catalog data flows and determine which resources are most critical
- Understand current access patterns and dependencies

### Phase 2: Identify Business Processes and Workflows
- Map business processes to the subjects and resources they require
- Identify the risk associated with each process
- Determine risk tolerance for each workflow

### Phase 3: Policy Formulation
- Develop access policies for each resource based on identity, device health, context, and risk
- Define the trust algorithm criteria
- Identify candidate ZTA solutions

### Phase 4: Deploy in Monitoring Mode
- Deploy ZTA components alongside existing perimeter-based security (not replacing it)
- Monitor policy decisions but do not enforce — collect data to refine policies
- Identify false positives and false negatives

### Phase 5: Expand ZTA Coverage
- Gradually shift enforcement from perimeter-based controls to ZTA components
- Start with low-risk resources and expand to higher-risk resources
- Decommission legacy perimeter components as confidence grows

The migration is **iterative** — organizations continuously refine policies, expand coverage, and improve trust algorithms. ZTA is not a single product deployment but an ongoing architectural shift.

## Threats to ZTA

SP 800-207 identifies several threats and concerns specific to ZTA implementations:

| Threat | Description |
|--------|-------------|
| **Subversion of the PDP/PEP** | If the PE or PA is compromised, an attacker can authorize access to any resource. The PDP/PEP must be the most hardened components. |
| **Denial of Service (DoS)** | If the PA or PEP is disrupted, legitimate users cannot access resources. Redundancy and resilience are critical. |
| **Stolen Credentials** | Compromised user credentials could be used to gain access. MFA and behavioral analytics mitigate this risk. |
| **Insider Threat** | Authorized users may abuse their access. Least privilege, behavioral monitoring, and anomaly detection help mitigate. |
| **Visibility on the Network** | If the enterprise cannot monitor all traffic (e.g., encrypted traffic), the PE may lack data to make informed decisions. |
| **Storage of System and Network Information** | ZTA components collect and store extensive data. This data becomes a high-value target. |
| **Reliance on Proprietary Data Formats** | Vendor lock-in and interoperability challenges. Open standards and APIs mitigate this risk. |
| **Use of Non-Person Entities (NPEs)** | Service accounts, automated processes, and IoT devices may not support MFA or behavioral analytics. Special policies are needed. |

## Relationship to Executive Order 14028

Executive Order 14028 (May 2021) on Improving the Nation's Cybersecurity directed federal agencies to adopt zero trust architectures. CISA's Zero Trust Maturity Model and OMB Memorandum M-22-09 further operationalized this requirement, using SP 800-207 as the foundational reference.

## References

- NIST SP 800-207: https://csrc.nist.gov/publications/detail/sp/800-207/final
- CISA Zero Trust Maturity Model: https://www.cisa.gov/zero-trust-maturity-model
- OMB M-22-09: Moving the U.S. Government Toward Zero Trust Cybersecurity Principles
- Executive Order 14028: Improving the Nation's Cybersecurity
