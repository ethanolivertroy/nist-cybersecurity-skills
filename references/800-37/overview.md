# NIST SP 800-37 Rev 2 — Risk Management Framework for Information Systems and Organizations

## Purpose

NIST Special Publication 800-37 Revision 2 provides guidelines for applying the **Risk Management Framework (RMF)** to information systems and organizations. The RMF provides a disciplined, structured, and flexible process for managing security and privacy risk that includes:

- Information security categorization
- Control selection, implementation, and assessment
- System and common control authorization
- Continuous monitoring

Rev 2 expanded the RMF from six steps to seven by adding the **Prepare** step, and incorporated privacy risk management alongside security risk management. It also aligned the RMF with the NIST Cybersecurity Framework (CSF) and integrated supply chain risk management concepts.

The RMF is mandatory for federal agencies under FISMA and is widely adopted by contractors and organizations operating on behalf of the federal government.

## The Seven RMF Steps

### Step 1: Prepare

**Purpose:** Carry out essential activities at the organization and system levels to help prepare the organization to manage its security and privacy risks using the RMF.

Key tasks:
- Assign key RMF roles (AO, ISSO, ISSM, system owner)
- Establish a risk management strategy and organizational risk tolerance
- Conduct organization-level and system-level risk assessments
- Identify common controls available to the organization
- Develop an organization-wide strategy for continuous monitoring
- Define the system boundary and identify system stakeholders
- Establish a system-level strategy for control implementation
- Register the system in organizational tracking systems (e.g., eMASS)

The Prepare step was added in Rev 2 to ensure organizations complete necessary prerequisites before beginning the traditional RMF process. It reduces the overall cost and increases the effectiveness of subsequent steps.

### Step 2: Categorize

**Purpose:** Categorize the system and the information processed, stored, and transmitted by the system based on an impact analysis.

Key tasks:
- Categorize the system using **FIPS 199** criteria (confidentiality, integrity, availability)
- Assign impact levels (Low, Moderate, High) for each security objective
- Determine the overall system categorization (based on the high-water mark)
- Document the categorization decision in the system security plan (SSP)
- Obtain approval of the categorization from the AO or designated representative

The categorization drives all subsequent control selection. A system categorized as Moderate impact, for example, would use the Moderate baseline from SP 800-53.

**Key Reference:** FIPS 199 (Standards for Security Categorization), NIST SP 800-60 (Guide for Mapping Types of Information and Information Systems to Security Categories)

### Step 3: Select

**Purpose:** Select, tailor, and document the controls necessary to protect the system and organization commensurate with risk.

Key tasks:
- Select the initial control baseline from **FIPS 200** and **SP 800-53** based on the system categorization
- Apply **tailoring** activities to adjust the baseline:
  - Identify and designate common controls (inherited from the organization or other systems)
  - Apply scoping considerations (remove controls that are not applicable)
  - Select compensating controls where standard controls cannot be implemented
  - Assign organization-defined parameter values
  - Supplement the baseline with additional controls based on risk assessment
- Document control selections in the SSP

**Key Reference:** SP 800-53 Rev 5, FIPS 200, CNSSI 1253 (for national security systems)

### Step 4: Implement

**Purpose:** Implement the controls as specified in the security and privacy plans.

Key tasks:
- Implement selected controls consistent with organizational architecture and deployment environments
- Document the control implementation in the SSP, describing:
  - How each control is implemented
  - The functional description of the control implementation
  - Expected behavior and actual inputs, outputs, and interfaces
- Ensure common controls are implemented by the responsible entity and available to inheriting systems

### Step 5: Assess

**Purpose:** Assess the controls to determine if they are implemented correctly, operating as intended, and producing the desired outcome.

Key tasks:
- Develop a **Security Assessment Plan (SAP)** — defines scope, methodology, assessment procedures, and team
- Conduct the assessment using procedures from **SP 800-53A Rev 5** (examine, interview, test)
- Document findings in a **Security Assessment Report (SAR)**
- Identify control deficiencies and determine risks
- Develop a **Plan of Action and Milestones (POA&M)** for deficiencies
- Conduct remediation actions to address deficiencies where possible
- Reassess remediated controls as needed

The assessment may be performed by the organization (self-assessment), an independent assessor, or a third-party assessment organization (3PAO) depending on the authorization type (e.g., FedRAMP requires 3PAO).

**Key Reference:** SP 800-53A Rev 5

### Step 6: Authorize

**Purpose:** Authorize the system or common controls based on a determination that the risk to organizational operations, assets, individuals, other organizations, and the Nation is acceptable.

Key tasks:
- Compile the **authorization package**, which includes:
  - System Security Plan (SSP)
  - Security Assessment Report (SAR)
  - Plan of Action and Milestones (POA&M)
  - Executive summary / risk determination
- Submit the package to the **Authorizing Official (AO)**
- The AO reviews the package, considers the overall risk posture, and makes a risk-based decision:
  - **Authorization to Operate (ATO):** System is authorized to operate — risk is acceptable
  - **Common Control Authorization:** Common controls are authorized for use by inheriting systems
  - **Denial of Authorization to Operate (DATO):** Risk is unacceptable — system must not operate
  - **Interim ATO (IATO):** Temporary authorization with conditions and a defined timeline

The authorization decision is documented with the terms, conditions, and any limitations of the authorization.

### Step 7: Monitor

**Purpose:** Maintain ongoing situational awareness about the security and privacy posture of the system and organization.

Key tasks:
- Monitor the system and its environment of operation for changes that affect control effectiveness
- Conduct **ongoing assessments** of controls per the continuous monitoring strategy
- Analyze and respond to the output of continuous monitoring activities
- Report the security and privacy posture to the AO and other stakeholders
- Manage changes to the system through a **configuration management process**
- Update the SSP, SAR, and POA&M on an ongoing basis
- Conduct ongoing authorization or reauthorization as determined by the AO

Effective continuous monitoring reduces the need for complete reassessments and supports near-real-time risk management.

**Key Reference:** SP 800-137 (Information Security Continuous Monitoring)

## Key RMF Roles

| Role | Abbreviation | Responsibilities |
|------|-------------|------------------|
| **Authorizing Official** | AO | Senior official with authority to accept risk and issue ATO/DATO decisions. Accountable for the system's security posture. May delegate to a Designated Authorizing Representative. |
| **Information System Security Officer** | ISSO | Responsible for the day-to-day security of the information system. Implements and maintains security controls, monitors the system, and supports the AO. |
| **Information System Security Manager** | ISSM | Manages the information security program for an organization or major component. Oversees ISSOs and ensures consistent security practices across systems. |
| **System Owner** | SO | Responsible for procuring, developing, integrating, modifying, operating, maintaining, and disposing of the system. Ensures the system is operated according to the SSP. |
| **Common Control Provider** | CCP | Responsible for implementing, assessing, and monitoring common controls inherited by other systems. Documents common controls and makes them available. |
| **Chief Information Officer** | CIO | Responsible for IT planning, budgeting, and performance, including information security. Designates the Senior Agency Information Security Officer (SAISO). |
| **Senior Agency Information Security Officer** | SAISO/CISO | Carries out CIO responsibilities under FISMA. Oversees the agency-wide information security program. Often titled Chief Information Security Officer (CISO). |
| **Risk Executive (Function)** | RE | Ensures risk-related considerations for individual systems are consistent with the organization's risk management strategy and risk tolerance. |
| **Security Control Assessor** | SCA | Conducts independent assessments of security controls. May be internal or external (3PAO). |

## Relationship to SP 800-53 and FIPS 199/200

The RMF depends on several foundational NIST publications:

### FIPS 199 — Security Categorization
- Used in **Step 2 (Categorize)** to classify the system based on potential impact (Low, Moderate, High) to confidentiality, integrity, and availability
- The system's overall categorization is the **high-water mark** of the three impact values
- Example: A system categorized as {Confidentiality: Moderate, Integrity: Moderate, Availability: Low} has an overall Moderate categorization

### FIPS 200 — Minimum Security Requirements
- Used in **Step 3 (Select)** to determine the minimum security requirements for the system based on its FIPS 199 categorization
- Specifies that organizations must meet minimum security requirements by employing the security controls from SP 800-53

### SP 800-53 — Security and Privacy Controls
- Provides the comprehensive catalog of controls used in **Step 3 (Select)**
- Defines three control baselines (Low, Moderate, High) corresponding to FIPS 199 impact levels
- Controls are implemented in **Step 4**, assessed in **Step 5** using SP 800-53A, and monitored in **Step 7**

### Flow
```
FIPS 199 (Categorize) --> FIPS 200 (Minimum Requirements) --> SP 800-53 (Select Controls)
                                                                      |
                                                              SP 800-53A (Assess Controls)
```

## The ATO Process

The Authorization to Operate (ATO) process is the culmination of RMF Steps 1-6:

```
1. Prepare    --> Establish context, roles, boundaries
2. Categorize --> FIPS 199 impact analysis
3. Select     --> Choose controls from SP 800-53 baseline + tailoring
4. Implement  --> Deploy and configure controls
5. Assess     --> Independent assessment per SP 800-53A
6. Authorize  --> AO reviews package and issues ATO/DATO
7. Monitor    --> Continuous monitoring sustains ATO
```

### Authorization Package Components

| Document | Purpose |
|----------|---------|
| **System Security Plan (SSP)** | Comprehensive description of the system, its boundary, environment, and how each control is implemented |
| **Security Assessment Report (SAR)** | Results of the independent assessment, findings, and risk determinations |
| **Plan of Action and Milestones (POA&M)** | Tracks control deficiencies, planned remediation, milestones, and responsible parties |
| **Risk Assessment** | Analysis of threats, vulnerabilities, and risk to the organization |
| **Authorization Decision Letter** | Formal letter from the AO documenting the authorization decision and conditions |

### Types of Authorization

- **System ATO:** Standard authorization for an individual system (typically 3 years, or ongoing with continuous monitoring)
- **Common Control Authorization:** Authorization of controls that can be inherited by multiple systems
- **Type Authorization:** Authorization of a common system deployed in multiple locations
- **Facility Authorization:** Authorization of physical/environmental controls for a facility
- **FedRAMP ATO:** Authorization for cloud services (Provisional ATO from JAB or Agency ATO)
- **Ongoing Authorization:** Continuous authorization based on continuous monitoring instead of periodic reauthorization

## References

- NIST SP 800-37 Rev 2: https://csrc.nist.gov/publications/detail/sp/800-37/rev-2/final
- FIPS 199: https://csrc.nist.gov/publications/detail/fips/199/final
- FIPS 200: https://csrc.nist.gov/publications/detail/fips/200/final
- NIST SP 800-53 Rev 5: https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final
- NIST SP 800-53A Rev 5: https://csrc.nist.gov/publications/detail/sp/800-53a/rev-5/final
- NIST SP 800-137: Information Security Continuous Monitoring
