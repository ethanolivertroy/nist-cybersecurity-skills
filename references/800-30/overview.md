# NIST SP 800-30 Rev 1 — Guide for Conducting Risk Assessments

## Purpose

NIST Special Publication 800-30 Revision 1 provides guidance for conducting **risk assessments** of federal information systems and organizations. It describes the risk assessment process, the types of risk factors to consider, and how to communicate and maintain risk assessment results. Risk assessments are a key component of the Risk Management Framework (SP 800-37) and inform decisions across all RMF steps.

The publication supports all three tiers of the NIST risk management hierarchy:

- **Tier 1 — Organization Level:** Governance and strategic risk
- **Tier 2 — Mission/Business Process Level:** Risk to mission and business functions
- **Tier 3 — Information System Level:** Risk to individual information systems

Risk assessments conducted under SP 800-30 help organizations:
- Identify threats to and vulnerabilities in systems
- Determine the likelihood that threats will exploit vulnerabilities
- Determine the impact to the organization if threats are realized
- Determine overall risk and recommend appropriate responses

## Risk Assessment Process

SP 800-30 defines a four-step risk assessment process:

### Step 1: Prepare for the Assessment

Establish the context for the risk assessment before conducting it.

Key activities:
- **Identify the purpose** of the assessment (why is the assessment being conducted?)
- **Identify the scope** of the assessment (what systems, data, processes are in scope?)
- **Identify assumptions and constraints** that may affect the assessment
- **Identify sources of threat, vulnerability, and impact information** (threat intelligence feeds, vulnerability databases, organizational data)
- **Define or identify the risk model** and analytic approach to be used (quantitative, qualitative, semi-quantitative)

### Step 2: Conduct the Assessment

Produce a list of risks with associated risk levels by analyzing threats, vulnerabilities, impacts, and likelihoods.

This step involves four sub-tasks:

#### 2a. Identify Threat Sources and Events
- Identify threat sources that could adversely affect organizational operations, assets, or individuals
- Identify threat events (actions or situations) that could be produced by those sources
- Identify the relevance of the threat events to the organization

#### 2b. Identify Vulnerabilities and Predisposing Conditions
- Identify vulnerabilities in organizational systems and environments
- Identify predisposing conditions that affect the likelihood that threat events will result in adverse impacts
- Determine the severity of identified vulnerabilities

#### 2c. Determine Likelihood
- Determine the likelihood that identified threat sources would initiate threat events
- Determine the likelihood that threat events, once initiated, would result in adverse impacts
- Produce an overall likelihood determination

#### 2d. Determine Impact
- Determine the adverse impact to organizational operations, assets, and individuals
- Consider impacts to confidentiality, integrity, and availability
- Produce an overall impact determination

#### Risk Determination
- Combine likelihood and impact to determine the level of risk
- Produce a prioritized list of risks

### Step 3: Communicate Results

Share risk assessment results with decision-makers and stakeholders.

Key activities:
- Communicate risk assessment results to organizational officials (AO, CISO, system owners)
- Share information useful for risk response decisions
- Ensure risk assessment results are expressed in terms that are understandable to the audience
- Provide sufficient detail to support informed risk-based decisions

### Step 4: Maintain the Assessment

Keep the risk assessment current over time.

Key activities:
- Monitor risk factors identified in the assessment on an ongoing basis
- Update the risk assessment when changes occur to systems, threat landscape, or organizational mission
- Incorporate results from continuous monitoring activities
- Update risk assessment based on new threat intelligence or vulnerability information
- Provide updated risk assessment results to support ongoing authorization decisions

## Threat Sources and Threat Events

### Threat Source Categories

SP 800-30 categorizes threat sources into four types:

| Category | Description | Examples |
|----------|-------------|----------|
| **Adversarial** | Individuals, groups, organizations, or states that deliberately seek to exploit systems | Nation-states, hacktivists, insiders, organized crime, terrorists |
| **Accidental** | Erroneous actions by authorized users | Misconfiguration, accidental data deletion, incorrect data entry |
| **Structural** | Failures of hardware, software, or environmental controls | Hardware failure, software bugs, power failure, depletion of resources |
| **Environmental** | Natural disasters or failures of external infrastructure | Earthquakes, floods, hurricanes, power grid failure, telecommunications outage |

### Adversarial Threat Source Attributes

For adversarial threats, SP 800-30 considers:

- **Capability:** The technical sophistication and resources available to the threat source
- **Intent:** The motivation and goals of the threat source (e.g., financial gain, espionage, disruption)
- **Targeting:** Whether the threat source specifically targets the organization or is opportunistic

### Threat Events

Threat events are the specific actions or occurrences that could cause harm. Examples include:

- Conduct phishing attacks against organizational personnel
- Exploit publicly known vulnerabilities
- Conduct insider attacks
- Introduce malware into the organization
- Perform denial-of-service attacks
- Conduct supply chain attacks (compromise components prior to delivery)
- Natural disaster causes facility damage

SP 800-30 provides extensive threat event tables in its appendices (Appendix D and E) as starting points for organizations.

## Vulnerabilities and Predisposing Conditions

### Vulnerabilities

Weaknesses in information systems, security procedures, internal controls, or implementation that could be exploited by threat sources. Examples:

- Unpatched software
- Misconfigured access controls
- Weak authentication mechanisms
- Lack of encryption for data in transit
- Insufficient logging and monitoring
- Inadequate physical security

### Predisposing Conditions

Conditions that exist within the organization or environment that affect the likelihood of threat events. Examples:

- System exposed to the internet
- Use of legacy systems without vendor support
- High turnover of IT security personnel
- Insufficient security training
- Proximity to flood plain (environmental)
- Shared infrastructure with other tenants (cloud)

## Likelihood Determination

Likelihood is assessed based on two factors:

1. **Likelihood of initiation (adversarial)** or **likelihood of occurrence (non-adversarial):** How likely is the threat source to initiate the threat event?
2. **Likelihood of impact:** Given that the threat event is initiated, how likely is it that it will result in adverse impact (accounting for existing controls)?

SP 800-30 uses a **qualitative scale** for likelihood:

| Level | Qualitative Value | Description |
|-------|-------------------|-------------|
| 5 | Very High | Almost certain to occur; expected to occur multiple times in the assessment period |
| 4 | High | Highly likely to occur; expected to occur at least once in the assessment period |
| 3 | Moderate | Somewhat likely to occur |
| 2 | Low | Unlikely but possible |
| 1 | Very Low | Highly unlikely to occur |

## Impact Determination

Impact is assessed based on the adverse effects on organizational operations, assets, or individuals:

| Level | Qualitative Value | Description |
|-------|-------------------|-------------|
| 5 | Very High | Catastrophic adverse effect — severe degradation or loss of mission capability; major financial loss; severe harm to individuals |
| 4 | High | Significant adverse effect — significant degradation of mission capability; significant financial loss; significant harm to individuals |
| 3 | Moderate | Serious adverse effect — noticeable degradation of mission capability; noticeable financial loss; serious harm to individuals |
| 2 | Low | Limited adverse effect — minor degradation of mission capability; minor financial loss; minor harm to individuals |
| 1 | Very Low | Negligible adverse effect — negligible degradation of mission capability; negligible financial loss; negligible harm to individuals |

Impact should consider effects across all three security objectives (confidentiality, integrity, availability) consistent with FIPS 199.

## Risk Determination

Risk is determined by combining **likelihood** and **impact** using a risk matrix:

### Semi-Quantitative Risk Matrix

| | Very Low Impact (1) | Low Impact (2) | Moderate Impact (3) | High Impact (4) | Very High Impact (5) |
|---|---|---|---|---|---|
| **Very High Likelihood (5)** | 5 (Low) | 10 (Moderate) | 15 (High) | 20 (Very High) | 25 (Very High) |
| **High Likelihood (4)** | 4 (Low) | 8 (Moderate) | 12 (High) | 16 (Very High) | 20 (Very High) |
| **Moderate Likelihood (3)** | 3 (Low) | 6 (Low) | 9 (Moderate) | 12 (High) | 15 (High) |
| **Low Likelihood (2)** | 2 (Low) | 4 (Low) | 6 (Low) | 8 (Moderate) | 10 (Moderate) |
| **Very Low Likelihood (1)** | 1 (Very Low) | 2 (Low) | 3 (Low) | 4 (Low) | 5 (Low) |

### Qualitative Risk Levels

| Risk Level | Score Range | Description |
|------------|-------------|-------------|
| Very High | 20-25 | Unacceptable risk — immediate action required; AO may issue DATO |
| High | 13-19 | Significant risk — senior management attention needed; strong corrective actions required |
| Moderate | 7-12 | Manageable risk — corrective actions needed within a reasonable timeframe |
| Low | 3-6 | Acceptable risk — may require monitoring; corrective action at management discretion |
| Very Low | 1-2 | Minimal risk — generally acceptable without additional action |

## Risk Model

SP 800-30 defines a **generic risk model** with the following factors:

```
Risk = f(Threat, Vulnerability, Likelihood, Impact)
```

The risk model includes:

- **Threat Source Characteristics:** Capability, intent, targeting (adversarial); range of effects (non-adversarial)
- **Vulnerability/Predisposing Condition Severity:** How exploitable the vulnerability is and what conditions affect exploitation
- **Likelihood of Occurrence:** Probability that a given threat event will be initiated and result in impact
- **Impact Magnitude:** The level of harm expected to result
- **Risk:** The combination of likelihood and impact that characterizes the overall level of risk

Organizations may use **quantitative** (numerical/financial), **qualitative** (descriptive), or **semi-quantitative** (ordinal scales) approaches depending on data availability and organizational needs.

### Risk Assessment Approaches

| Approach | Description | Best Suited For |
|----------|-------------|-----------------|
| **Quantitative** | Uses numerical values and statistical models; expresses risk in financial or probabilistic terms | Organizations with mature data collection; scenarios where financial impact is critical |
| **Qualitative** | Uses descriptive categories (Low, Moderate, High); relies on expert judgment | Organizations with limited historical data; initial risk assessments |
| **Semi-Quantitative** | Uses ordinal scales and risk matrices (the approach primarily described in SP 800-30) | Most common approach; balances rigor with practicality |

## Relationship to Other NIST Publications

- **SP 800-37 (RMF):** Risk assessments support multiple RMF steps, particularly Prepare (Step 1), Categorize (Step 2), and Monitor (Step 7)
- **SP 800-39:** Provides the overarching risk management process at organizational, mission, and system levels — SP 800-30 implements the "risk assessment" component
- **SP 800-53:** Controls selected based on risk assessment results; risk assessment informs tailoring decisions
- **FIPS 199:** Security categorization provides initial impact assessment that feeds into detailed risk assessment

## References

- NIST SP 800-30 Rev 1: https://csrc.nist.gov/publications/detail/sp/800-30/rev-1/final
- NIST SP 800-39: Managing Information Security Risk
- NIST SP 800-37 Rev 2: Risk Management Framework
- FIPS 199: Standards for Security Categorization
