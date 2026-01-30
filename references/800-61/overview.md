# NIST SP 800-61 Rev 3 — Incident Response Recommendations and Considerations for Cybersecurity Risk Management

## Purpose

NIST Special Publication 800-61 Revision 3, published in 2024, provides recommendations for organizations on planning, executing, and improving their incident response (IR) capabilities. Rev 3 represents a significant shift from prior revisions by reframing incident response as an integral part of cybersecurity risk management rather than a standalone operational activity.

Rev 3 moves away from the prescriptive, step-by-step playbook approach of Rev 2 and instead emphasizes:

- Integrating incident response into the NIST Cybersecurity Framework (CSF) 2.0
- Treating incident response as a cross-cutting function that supports Govern, Identify, Protect, Detect, Respond, and Recover functions
- Aligning incident response with organizational risk management and governance
- Supporting evolving threats including ransomware, supply chain compromise, and cloud-specific incidents

## Incident Response Lifecycle

While Rev 3 restructures its guidance around CSF 2.0 functions, it retains and builds upon the foundational IR lifecycle phases established in earlier revisions:

### Phase 1: Preparation

Preparation establishes the capability to respond to incidents before they occur.

Key activities:
- **Establish incident response policy and plan:** Define the organization's approach to incident handling, including roles, responsibilities, communication procedures, and escalation criteria
- **Build and train the incident response team:** Staff and train a team with appropriate technical and communication skills
- **Acquire tools and resources:** Deploy and maintain IR tools (forensic workstations, network monitoring, log aggregation, ticketing systems)
- **Conduct exercises and training:** Perform tabletop exercises, simulations, and red team/blue team exercises to test readiness
- **Establish relationships:** Pre-establish working relationships with law enforcement, CISA, ISACs, legal counsel, and communications teams
- **Implement preventive controls:** While not strictly IR, preventive controls (patching, network segmentation, MFA) reduce the frequency and impact of incidents

### Phase 2: Detection and Analysis

Detection identifies potential security events; analysis determines whether they constitute incidents and assesses their scope and severity.

Key activities:
- **Monitor indicators of compromise (IOCs):** Use SIEM, EDR, NDR, and other monitoring tools to detect anomalous activity
- **Analyze precursors and indicators:** Precursors signal a possible future incident (e.g., new exploit announced); indicators signal that an incident may be occurring or has occurred (e.g., anomalous network traffic, alerts from IDS)
- **Correlate and validate events:** Combine data from multiple sources to reduce false positives and confirm genuine incidents
- **Categorize and prioritize incidents:** Assess the functional impact, information impact, and recoverability to determine response priority
- **Document findings:** Maintain detailed records from the moment detection begins (timestamps, actions taken, evidence collected)
- **Notify appropriate stakeholders:** Escalate to management, legal, PR, and external parties as required by policy and regulation

### Phase 3: Containment, Eradication, and Recovery

Once an incident is confirmed, the organization works to limit damage, remove the threat, and restore operations.

**Containment:**
- Implement short-term containment to stop the immediate threat (e.g., isolate affected systems, block malicious IPs)
- Implement long-term containment to maintain operations while preparing for eradication (e.g., apply temporary patches, redirect traffic)
- Collect and preserve forensic evidence before making changes
- Decision criteria for containment strategy include: potential damage, need for evidence preservation, service availability requirements, resource requirements, and time needed

**Eradication:**
- Identify and eliminate the root cause of the incident
- Remove malware, close exploited vulnerabilities, disable compromised accounts
- Rebuild affected systems from known-good media if necessary
- Verify that eradication was complete — threat actors often maintain multiple persistence mechanisms

**Recovery:**
- Restore systems to normal operation
- Confirm that systems are functioning normally and monitoring is in place
- Implement additional monitoring for recurrence
- Gradually restore services, beginning with highest-priority systems
- Validate that business processes are operating correctly

### Phase 4: Post-Incident Activity

Learning from incidents improves future response capabilities.

Key activities:
- **Conduct a lessons-learned meeting:** Hold a retrospective within a defined time after incident closure (often within 2 weeks) involving all stakeholders
- **Document the incident:** Compile a complete incident report including timeline, actions taken, impact assessment, and root cause analysis
- **Update IR plans and procedures:** Revise policies, playbooks, and procedures based on lessons learned
- **Identify control improvements:** Recommend changes to preventive, detective, and corrective controls
- **Share information:** Share anonymized or sanitized incident information with ISACs, CISA, and other trusted partners to improve collective defense
- **Collect and retain evidence:** Ensure evidence is retained per organizational policy and legal requirements
- **Calculate incident metrics:** Track metrics such as time-to-detect, time-to-contain, time-to-recover, and total incident cost

## Incident Categories

SP 800-61 Rev 3 and its predecessors define several incident categories. Organizations should develop a taxonomy appropriate to their environment. Common categories include:

| Category | Description | Examples |
|----------|-------------|----------|
| **Unauthorized Access** | Gaining logical or physical access without permission | Exploitation of vulnerability, use of stolen credentials, social engineering |
| **Denial of Service (DoS/DDoS)** | Disrupting availability of systems or networks | Volumetric attacks, application-layer attacks, resource exhaustion |
| **Malicious Code** | Execution of malware on systems | Ransomware, trojans, worms, spyware, cryptominers |
| **Improper Usage** | Violation of acceptable use policies | Unauthorized software installation, misuse of privileges, policy violations |
| **Web-Based Attack** | Attacks targeting web applications or services | SQL injection, cross-site scripting (XSS), web shell deployment |
| **Email-Based Attack** | Attacks delivered through email | Phishing, spear-phishing, business email compromise (BEC) |
| **Supply Chain Compromise** | Compromise through a trusted vendor or supplier | Trojanized software update, compromised hardware, third-party breach |
| **Insider Threat** | Threat originating from within the organization | Data theft by employee, sabotage, unintentional exposure |

### Incident Severity and Prioritization

Organizations should prioritize incidents based on:

- **Functional Impact:** The effect on business functionality (None, Low, Medium, High)
- **Information Impact:** The effect on confidentiality and integrity of data (None, Privacy Breach, Proprietary Breach, Integrity Loss)
- **Recoverability:** The level of effort needed to recover (Regular, Supplemented, Extended, Not Recoverable)

## CISA Reporting Requirements

Federal agencies and critical infrastructure organizations have reporting obligations to the **Cybersecurity and Infrastructure Security Agency (CISA)**:

### Federal Agencies (FISMA)
- Required to report incidents to CISA (formerly US-CERT) in accordance with FISMA and OMB directives
- Reporting timelines vary by incident severity and category
- CISA provides the Federal Incident Notification Guidelines specifying reporting formats and timelines
- Major incidents (as defined by OMB) must be reported within **1 hour** of determination

### Cyber Incident Reporting for Critical Infrastructure Act (CIRCIA)
- Signed into law in 2022; CISA issued the final rule for implementation
- **Covered entities** in critical infrastructure sectors must report:
  - Covered cyber incidents within **72 hours** of reasonably believing the incident occurred
  - Ransomware payments within **24 hours** of payment
- Reports must include information about the incident, affected systems, vulnerabilities exploited, and attacker techniques

### What to Report
- Description of the incident and affected systems
- Date and time of the incident and discovery
- Indicators of compromise
- Impact assessment
- Actions taken in response
- For ransomware: amount demanded, amount paid, payment instructions

## Incident Response Team Models

SP 800-61 describes several organizational models for IR teams:

### Central Incident Response Team
- A single IR team handles incidents for the **entire organization**
- Best for small to medium organizations
- Provides consistency in incident handling
- May lack local knowledge of diverse environments

### Distributed Incident Response Teams
- Multiple IR teams, each responsible for a specific **logical or physical segment** of the organization (e.g., by business unit, geographic region, or system)
- A central coordination entity provides oversight and ensures consistent practices
- Best for large or geographically dispersed organizations
- Provides local expertise and faster response

### Coordinating Team
- Provides guidance, best practices, and coordination services to other IR teams but **does not have direct authority** over them
- Functions as an advisory body
- Common in decentralized organizations or sector-level coordination (e.g., ISACs)

### Hybrid Model
- Combines elements of the above models
- Central team handles high-severity incidents; distributed teams handle routine incidents
- Most common in large enterprises

### Outsourced IR Services
- Some or all IR functions are outsourced to a **managed security service provider (MSSP)** or incident response retainer firm
- May provide 24/7 coverage, specialized expertise, and surge capacity
- Requires clear contracts, SLAs, and data handling agreements
- Organization retains overall accountability for incident response

## Integration with CSF 2.0

Rev 3 aligns IR activities with all six CSF 2.0 functions:

| CSF Function | IR Integration |
|-------------|----------------|
| **Govern (GV)** | Establish IR governance, policy, roles, and integration with ERM |
| **Identify (ID)** | Understand assets, risks, and dependencies that affect IR readiness |
| **Protect (PR)** | Implement controls that prevent or limit incidents |
| **Detect (DE)** | Deploy monitoring, alerting, and analysis capabilities |
| **Respond (RS)** | Execute containment, analysis, reporting, and communication |
| **Recover (RC)** | Restore services, implement improvements, communicate recovery status |

## References

- NIST SP 800-61 Rev 3: https://csrc.nist.gov/publications/detail/sp/800-61/rev-3/final
- NIST CSF 2.0: https://www.nist.gov/cyberframework
- CISA Federal Incident Notification Guidelines: https://www.cisa.gov/incident-notification-guidelines
- CIRCIA: Cyber Incident Reporting for Critical Infrastructure Act of 2022
