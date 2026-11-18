# Security Foundations | Pilot Technical Review 05: Side Channels, Covert Channels, and Information Leakage

**Review date:** November 18, 2026  
**Scope:** [SF-04-08, Side Channels, Covert Channels, and Unintended Information Leakage](weaknesses-vulnerabilities-exposure/side-channels-covert-channels-and-unintended-information-leakage.md). One substantive area-first working Draft, **10 material claim groups**, with source/version review, logical counterexamples, formal-model checks and corrections.  
**Method:** A separate model-assisted second pass after the preceding Draft stage. Compared the manuscript with official NIST and MITRE definitions, directly inspected NIST SP 800-53 Rev. 5 **SC-31** in the rendered primary PDF, inspected the derivation of binary-symmetric-channel capacity in Stanford EE376A course notes, recomputed formulas and examined overlapping canonical ownership.  
**Disposition:** The revised SF-04-08 manuscript satisfies this **bounded model-assisted technical review**. It may advance to **Reviewed (model-assisted) / Core claims checked**, not source-Verified, independently peer-reviewed, taxonomically approved or Published. Earlier [Reviews 01–04](pilots/README.md) retain their independent historical scope. No new candidate ID or area category is adopted.

## Claim-led technical review

| Group | Claim or mechanism checked | Evidence, review finding, and important limit |
| --- | --- | --- |
| 05-01 | **Side-channel definition and source scope** | [NIST CSRC side-channel glossary](https://csrc.nist.gov/glossary/term/side_channel) explicitly attributes its definition to **NIST AI 100-2e2025** and describes observation of nonfunctional characteristics, such as execution-time, memory and physical effects. **Pass with correction:** label the source context; do not represent that glossary entry as a universal formal classification of every side channel. |
| 05-02 | **Covert channel requires policy context and cooperating entities in its classical definition** | [NIST covert-channel glossary](https://csrc.nist.gov/glossary/term/covert_channel) draws from **CNSSI 4009-2022 / RFC 4949** and SP 800-53 Rev. 5: locally authorized operations can collectively transfer information in violation of policy. **Pass.** Whether an action violates a particular policy remains a system-specific question. |
| 05-03 | **Storage and timing channels are distinct but related** | [NIST covert storage](https://csrc.nist.gov/glossary/term/covert_storage_channel) and [covert timing](https://csrc.nist.gov/glossary/term/covert_timing_channel) definitions distinguish writing/reading shared state from modulating resource use and observed response time. [MITRE CWE-515](https://cwe.mitre.org/data/definitions/515.html) and [CWE-385](https://cwe.mitre.org/data/definitions/385.html) describe corresponding weakness classes. **Pass.** A shared resource is not automatically an exploited channel. |
| 05-04 | **CWE terminology overlaps without forming a disjoint side/covert ontology** | [MITRE CWE-208](https://cwe.mitre.org/data/definitions/208.html) covers observable timing discrepancy. [CWE-385](https://cwe.mitre.org/data/definitions/385.html) is placed under CWE-514, but its technical descriptions also mention external observation of secret-dependent operations. **Pass after correction:** the article warns that CWE catalog relationships and examples are not a proof that all timing leaks involve a cooperating sender. |
| 05-05 | **Leakage vs a timing anomaly, direct disclosure, and compromised state** | A timing variation can depend only on public input size; an unauthorized explicit response can disclose a secret with no side channel; observing a candidate leak does not demonstrate exploitation or attribution. **Pass with clarification:** a supported leakage claim must identify protected property, forbidden flow, observer model and an evidentiary connection. These are conceptual counterexamples, not measurements or a new external standard. |
| 05-06 | **SC-31 analysis, estimation, testing and actual measurement are separate** | Directly visually inspected [NIST SP 800-53 Rev. 5](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf), **SC-31 in Chapter 3, printed page 320, PDF index 346**. Base control identifies potential storage/timing pathways and estimates maximum bandwidth. Enhancements (1)–(3) separately address exploitability tests, maximum-bandwidth reduction, and operational bandwidth measurement. **Pass after explicit correction** of source scope. NIST [CPRT](https://csrc.nist.gov/projects/cprt/catalog) lists **5.2.0 (August 2025)**; the inspected PDF reflects the older Rev. 5 text, not a complete independently diffed copy of 5.2.0. |
| 05-07 | **Conditional mutual information is an observation-relative quantity** | The standard identity \(I(S;Y\mid L)=H(S\mid L)-H(S\mid Y,L)\) applies to the declared jointly distributed random variables where these entropies are defined. Zero conditional mutual information means no additional *statistical* information within this observation/distribution model, not absence of all physical leakage, causal influence or exploitation possibilities. **Pass**, with explicit model limitations already preserved in the manuscript. |
| 05-08 | **Binary symmetric channel capacity formula and numeric values** | [Stanford EE376A Lecture 8 (2018), printed pp. 1–2, PDF index 1](https://web.stanford.edu/class/ee376a/files/2017-18/lecture_8.pdf) derives \(C=1-H_2(p)\) for a memoryless binary symmetric channel, achieved by equally likely inputs. Independently recomputed \(H_2(0.1)=0.4689955935892812\) bits; \(C=0.5310044064107188\) bits/use; \(4C=2.124017625642875\) bits/s. **Pass.** Values rounded to six decimals in the article. |
| 05-09 | **Four symbols per second do not imply an unconditional 2.124018 bits/s bound** | The rate multiplication is valid *under the article's constrained fixed-slot model*, including no information encoded by idle slots, omitted symbols, or slot timing. **Pass after material correction:** made the fixed four-slots-per-second, bounded signaling, memoryless noise and no-extra-timing-channel assumptions explicit. If an independent timing/absence channel exists, the single binary-channel calculation does not bound the combined system. |
| 05-10 | **Mitigation and canonical ownership limits** | The article correctly treats constant-time intent, isolation, output normalization, and rate limits as threat-model-specific techniques rather than universal prevention proofs. [SC-31(2)](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) observes that eliminating covert channels can significantly affect performance. **Pass.** SF-04-08 explains leakage mechanisms; [SF-08-09](secure-design-architecture/information-flow-security-and-noninterference.md) retains information-flow policy/noninterference; [SF-04-02](weaknesses-vulnerabilities-exposure/vulnerabilities-and-exploitability.md) retains general vulnerability conditions; concrete domain implementations and operational testing keep their separate owners. |

## Recomputed model and independent countertests

Under the hypothetical binary symmetric channel, set \(p=0.1\). For \(0<p<1\):

\[
H_2(p)=-p\log_2(p)-(1-p)\log_2(1-p).
\]

Then

\[
H_2(0.1)=0.4689955935892812,\qquad
C_{\mathrm{use}}=1-H_2(0.1)=0.5310044064107188\ \mathrm{bits/use}.
\]

For **four predefined signaling slots per second**, with at most one channel use per slot and no independent information in slot timing or omission:

\[
C_{\mathrm{rate}}\leq 4C_{\mathrm{use}}
=2.124017625642875\ \mathrm{bits/s}.
\]

Three independent logical tests bound the interpretation:

1. **No bit errors:** \(p=0\) implies \(H_2(p)=0\) by the continuous endpoint convention, so \(C=1\) bit/use, a ceiling of 4 bits/s at four fixed slots/s.
2. **Independent output:** \(p=0.5\) implies \(H_2(p)=1\), so \(C=0\), even when the sender emits symbols. The observation has no capacity to distinguish their values in this binary model.
3. **Additional covert timing:** If the sender may signal through the timing or absence of the four slots themselves, the assumed alphabet and channel-use bound are incomplete; the claimed 2.124018-bit/s ceiling **does not bound the combined channel**. The article explicitly excludes such a second carrier.

These are mathematical properties of an *assumed* channel. They are not measurements of an actual application, a prediction of attack duration, evidence of malicious intent, or certification of information-flow security.

## Corrections applied to the substantive article

The review introduced nine bounded editorial improvements: (1) scoped the NIST AI-sourced side-channel definition; (2) documented CWE-385's overlap with ordinary timing-side-channel observations; (3) tightened the evidentiary requirements for claiming leakage; (4) separated SC-31 bandwidth estimation from optional operational measurement and exploitability testing; (5) made signaling slots fixed and excluded extra slot-timing/omission symbols; (6) added the Stanford source for Shannon capacity and the equal-prior maximization condition; (7) qualified the four-slots-per-second bound as asymptotic rather than measured throughput; (8) added precise NIST SC-31 source-page/version caveats; and (9) added the independent information-theory lecture reference to the source register.

**Review outcome:** No need to split or merge the working SF-04-08 subject was demonstrated. Retain the article's provisional area placement, promote its **development** to Reviewed (model-assisted) and its **source review** to Core claims checked, and leave all broader architecture, source-Verified, independent expert acceptance and Published gates open.

## Source and verification boundaries

The review inspected rendered pages in the NIST Rev. 5 PDF and Stanford teaching reference and compared official NIST CSRC and MITRE CWE HTML entries. It did **not** inspect all 800-53 Release 5.2.0 OSCAL/JSON material clause by clause, run physical side-channel tests, measure a real covert channel, prove every application of the formal information-theory model, or validate every source claim in the whole Security Foundations corpus. The reviewed examples are conceptual or mathematically stipulated, not experimental results.

**Independent review remains outstanding.** Structural CI success verifies register/path/link consistency, not scientific truth or publication readiness.

[Security Foundations](README.md) · [Working article register](pilots/README.md) · [Development/Verification Register](DEVELOPMENT-VERIFICATION-REGISTER.md) · [Working ownership](CANONICAL-OWNERSHIP-REGISTER.md)
