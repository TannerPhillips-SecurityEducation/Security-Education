# Administrative Editorial Passes | Readability and Detailed Understanding

**Working edition:** v0.3 · November 19, 2026  
**Stage:** Active editorial program, with **Security Foundations new drafting paused** after its Technical Review 11.  
**Scope:** Existing knowledge-reference manuscripts and their navigation, starting with **Fundamentals** as the established structural baseline; expand to other non-paused divisions on actual evidence. Existing Security Foundations references can receive source corrections or narrowly scoped maintenance without reopening a new drafting wave.  
**Governing contracts:** [Root AGENTS](AGENTS.md) · [Foundations AGENTS](foundations/AGENTS.md) · [Fundamentals AGENTS](foundations/fundamentals/AGENTS.md) · [Security Foundations AGENTS](foundations/security-foundations/AGENTS.md)

## 1. Purpose and quality proposition

**Administrative pass** means a deliberate editorial improvement cycle across already-authored knowledge. It does not mean mass formatting, low-effort paraphrase, or an automatic article status upgrade.

The objective is that a reader can **read**, **understand**, **explain**, **apply**, and **critically evaluate** a concept without needing to infer a missing step. Technical rigor and accessibility are mutually reinforcing when claims, notation, examples and boundaries are well constructed.

**Principle:** *Readability is not simplification of reality. Depth is not accumulation of words. Detail is the amount of explanation needed to make the mechanism intelligible.*

All changes must preserve author/source distinctions, provisional taxonomies, file ownership, historical review evidence, and GitHub navigation. Never rewrite a subtle technical distinction into a false equivalence merely to shorten the article.

## 2. Distinct administrative pass types

| Pass | Primary objective | Accepted evidence of improvement | Guardrail |
| --- | --- | --- | --- |
| **A0. Baseline and gap inventory** | Identify actual readability, depth, source and relationship gaps in existing articles | Per-article observed problems with section/claim location, consequence and proposed fix | No invented ratings or “all articles checked” claims |
| **A1. Readability and narrative coherence** | Strengthen section order, transitions, referents, terminology and explanatory progression | Before/after passages that resolve ambiguity, reduce needless repetition, improve direct definitions | Preserve necessary precision and domain language |
| **A2. In-depth conceptual understanding** | Explain mechanisms, conditions, assumptions, internal structures and consequences | A missing derivation supplied, counterexample clarified, boundary relation made explicit | **Material technical additions need claim-level source/model review** |
| **A3. Worked demonstration and reasoning** | Make abstract ideas concrete through inspectable examples, diagrams and equations | Recomputed figures, complete assumptions, interpretations and countertests | Invented data explicitly marked; no fabricated experiments |
| **A4. Relationships and navigation** | Strengthen prerequisites, canonical-owner links, headings and navigation to neighboring concepts | Resolved links, unique homes, meaningful in/out relationships and a demonstrated reader pathway | Do not create duplicate bodies or silently ratify taxonomy |
| **A5. Editorial and evidence quality** | Improve citations, source attribution, logical consistency, definitions and uncertainty language | Claim-to-source matrix, corrected edition, unsupported claim weakened or removed | **Source-Verified is a separate gate**; mere links do not verify |
| **A6. Presentation and publication readiness** | Inspect legibility, tables, formulas, mobile readability, image placeholders and release wording | Render inspection where possible, controlled front matter, remaining publication blockers | Never label Published or independently peer-reviewed without actual approval |

**Passes are lenses, not a mandatory seven-stage bureaucracy.** Combine them for coherent articles, record the actual scope, and prioritize depth problems over superficial consistency. Do not impose fixed article, sentence, word, heading, table, or visual counts.

## 3. Readability without loss of rigor

For substantive concepts, provide only what the concept actually requires:

- **Distinction:** What is the concept, and what is it not? Avoid defining a term solely through a neighboring term.
- **Anatomy:** Which entities, relationships, states, variables or boundaries make up the phenomenon?
- **Mechanism:** How does it operate? Explain the transition from prerequisites through behavior to result.
- **Conditions:** Under what assumptions is the claim true, false, limited or unknown?
- **Worked reasoning:** Where material, show the calculation or observed-to-derived argument without skipping the controlling step.
- **Counterexample:** Include a meaningful case where a tempting generalization fails.
- **Connection:** Explain both prerequisites and what downstream knowledge the concept enables.
- **Evidence:** Distinguish primary-source claims, editor-authored models, hypothetical examples, and actually validated claims.

Not every article requires every element or the same depth. A precise two-paragraph concept can be complete; a hard concept may warrant several interrelated models and multiple worked cases. **Do not optimize for uniformity.**

**Preferred prose:** Direct technical narrative with meaningful paragraphs. Start from the reader's immediate conceptual need, not meta-commentary about the document or repeated declarations that it is a working artifact. Use headings when they make retrieval easier; avoid a heading for every sentence. Put caveats next to the claims they limit. Tables should clarify relationships, not substitute for necessary explanation.

## 4. Deep-understanding test

An article is a **candidate for deeper treatment** when any of these observations are true:

1. It names a mechanism but leaves its input, output or decisive transformation unexplained.
2. It asserts a relationship without stating prerequisites or the direction of implication.
3. It uses a mathematical quantity without defining population, units, model and interpretation.
4. It provides an example but omits why the example validates or contradicts the general claim.
5. It conflates observable activity, stored representations, inference and intention.
6. It invokes a framework without identifying its unit of analysis, source edition or known boundary.
7. It describes a control/objective but omits how failure, bypass or partial coverage affects it.
8. It jumps from general abstraction to specialized implementation without a bridging explanation.
9. It uses repeated disclaimers as a substitute for a precise source or evidentiary scope.
10. It assumes the reader has knowledge not yet established by linked prerequisites.

A proposed improvement must identify the **specific gap** and show which inference, application or explanation becomes possible after the change. More text is justified only when that improvement is real.

## 5. Evidence and maturity protection

Keep the following independent:

**Observed source** → **drafted explanation** → **model-assisted technical review** → **claim-level source verification** → **independent qualified acceptance** → **publication**.

An A1 wording correction that does not change a material claim may preserve the existing audit record with a documented editorial delta. A new equation, changed threat condition, revised security property, material counterexample or disputed standards interpretation must receive a **new scoped technical check** and provenance before it is presented as supported.

GitHub Actions test structure, link targets and registered states. A successful run does **not** prove that an article's content is right, understandable or ready for publication.

## 6. One inspectable batch

For each actual administrative batch, record:

**Before:** Documents inspected, their editorial state, a bounded list of observed gaps, and why these changes matter.

**Action:** Exact files and passages edited, change type (clarity/depth/model/source/navigation), and new examples or diagrams when justified.

**Verification:** Re-read the changed explanation, check claims and formulas, evaluate at least one relevant counterexample, run repository integrity validation, and record links to the commit and review where applicable.

**After:** Observable improvements, residual gaps, sources not inspected, and which adjacent topics would benefit next. Do not report “complete corpus audit” on the basis of a sample.

Administrative passes may target several articles within a coherent cluster. Individual documentation records remain useful even when one shared editorial ledger describes the entire batch.

## 7. First focus: Fundamentals

**Initial priority:** Inspect a cross-section of existing [Fundamentals](foundations/fundamentals/README.md) articles for explanation gaps in **mathematics/logic, systems engineering, scientific reasoning, models/abstraction, and information/data**. This is a preliminary coverage lens, not an inventory commitment or a new authoring batch.

Apply **A0 (baseline/gap inventory)** first. Where a low-risk A1 clarification is justified, make the edit and verify it. For complex A2/A3 improvements, retain explicit source/model review requirements rather than quietly upgrading an internally Reviewed document.

Potential substantive focus includes: deriving an equation from its assumptions; linking a formal definition to its operational meaning; explaining a failure mode and its boundaries; replacing an unsupported universal statement with a scoped one; and adding an honest worked example where the inference is otherwise invisible.

**Security Foundations pause:** No new SF Drafts, candidate expansions, or editorial changes that silently alter its approved review state. Its 39 Reviewed manuscripts, 57 un-authored candidates and 262 bounded claim groups remain the paused baseline until a deliberate future resume or correction.

## Completed administrative passes

- [Fundamentals Administrative Editorial Pass 01](foundations/fundamentals/ADMINISTRATIVE-EDITORIAL-PASS-01.md) (November 19, 2026): bounded A0 inspection of ten existing Fundamentals articles, with A2/A3 in-depth revisions to two Systems & Engineering articles (Reliability and Failure; Queueing and Service-System Models). Added source-scoped, independently recalculated examples and explanations. This is not a complete corpus audit or publication acceptance.

- [Fundamentals Administrative Editorial Pass 02](foundations/fundamentals/ADMINISTRATIVE-EDITORIAL-PASS-02.md) (November 19, 2026): targeted A0–A5 improvement of four existing Fundamentals articles in Dependencies, Abstraction, Conceptual and Formal Models, and Databases and Queries. Nine bounded material claim groups, recalculated toy cases, formal reachability counterexample, and scoped primary-source checks; Security Foundations drafting pause and prior review gates unchanged.

## 8. Completion criteria

An administrative pass is **completed** only when the intended change is inspectable: changed article or ledger, link and CI checks, explicit source/model limitations, and a truthful account of what was actually inspected. A document merely saying “next pass planned” is a **program record**, not a completed editorial pass.

**Governing goal:** A living technical reference that makes reasoning visible, preserves useful complexity and empowers independent understanding. Depth follows the concept; evidence governs the claim; administrative polish never becomes fictitious publication approval.
