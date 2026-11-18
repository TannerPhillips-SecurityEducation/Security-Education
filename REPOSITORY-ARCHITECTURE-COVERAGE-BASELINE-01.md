# Security Knowledge | Architecture and Content Coverage Baseline 01

**Snapshot date:** November 18, 2026  
**Scope:** Default-branch repository directory and file presence, approved/proposed governance, canonical article inventories and bounded development evidence.  
**Evidence:** Full recursive GitHub tree (`truncated=false`), [repo-wide link and contract validator](tools/check_repository_integrity.py), [dynamic coverage report](tools/report_knowledge_coverage.py), [Fundamentals register](foundations/fundamentals/DEVELOPMENT-VERIFICATION-REGISTER.md) and [Security Foundations pilot register](foundations/security-foundations/pilots/README.md).  
**Status:** **Working, versioned evidence baseline**, not a publication certificate, completeness percentage, ratification of internal proposals, or assertion that every source passage has been verified.

## 1. Actual repository topology

The observed root directory structure contains `.github/`, `tools/`, `foundations/` and the seven specialized domains:

- [Fundamentals](foundations/fundamentals/README.md), [Security Foundations](foundations/security-foundations/README.md) and [Operational Foundations](foundations/operational-foundations/README.md) are three **approved divisions** under [Foundations](foundations/README.md).
- [Network](network/README.md), [Endpoint](endpoint/README.md), [Application](application/README.md), [Cloud](cloud/README.md), [Industrial](industrial/README.md), [IoT](iot/README.md) and [Identity](identity/README.md) are the seven **approved specialized knowledge domains**.
- [Root AGENTS.md](AGENTS.md), [Foundations AGENTS.md](foundations/AGENTS.md) and all their domain/division counterparts supply scoped instructions. [Automation AGENTS.md](.github/AGENTS.md) governs mechanical checks.

**Current checked counts:**

| Evidence unit | Observed count | What is actually being counted |
| --- | ---: | --- |
| Markdown files repository-wide | **297** | Navigation, articles, decision histories, reviews, AGENTS and other Markdown combined |
| Root + top-level + Foundation division AGENTS contracts | **13** | 1 root, 9 top-level, 3 division-specific |
| Specialized domain child navigation READMEs | **76** | Function and secondary indexes, **not** 76 substantive articles |
| GitHub Actions workflow files | **3** | Fundamentals, Security Foundations and repository-wide integrity |
| Fundamentals canonical article files registered | **120** | Current authored subject references, distinct from navigation and audit files |
| Security Foundations substantive pilot articles | **14** | Working pilots with current scoped reviews, **not** ratified permanent canonical locations |
| Operational Foundations substantive references | **0** | Division scope README/AGENTS exist; no internal taxonomy or article corpus |
| Specialized domain substantive function/implementation articles | **0** | Their READMEs currently define scope and navigation only |

The numbers above are **a dated observation**. They are neither targets, permanent inventory sizes nor evidence of the conceptual completeness of a domain.

## 2. Architecture authority and editorial maturity

| Layer | Navigational architecture | Actual content | Technical-review state | Approval and publication limitation |
| --- | --- | --- | --- | --- |
| **Fundamentals** | Approved twelve area identities; living subject inventory | 120 canonical references | 120 internally **Reviewed (model-assisted)** under documented scoped waves | Full source-Verified and independently Published **not** claimed; subjects remain add/split/merge/retire eligible |
| **Security Foundations** | Division approved; twelve areas and 96 subjects are **working proposed counts**, both flexible | 14 substantive pilot articles across proposed areas | 14 **Reviewed (model-assisted)**; three scoped pilot audits with 70 material claim groups | Internal taxonomy not ratified; permanent canonical placement, complete source verification and publication pending |
| **Operational Foundations** | Division approved; internal taxonomy unapproved | README and tailored AGENTS only | No authored subject corpus to review | Must distinguish operational method from general security concept and implementation |
| **Seven specialized domains** | Function-first navigation approved; secondary OS/application/provider views where relevant | 76 child navigation READMEs, no substantive function/implementation articles | No function/implementation corpus to review yet | Deeper subject taxonomy and implementation placements require separate decisions |

The repository supports **hierarchy for navigation, knowledge graph through relationships**, with **Domain → Function → Implementation** in specialized domains. One coherent concept has one general canonical owner. A folder name, source framework heading or link count cannot imply complete coverage or an ontological subclass.

## 3. Integrity evidence and limits

The [initial repository-wide GitHub Actions run](https://github.com/TannerPhillips-SecurityEducation/Security-Education/actions/runs/44311290978) successfully checked:

| Mechanical check | Result |
| --- | ---: |
| Markdown documents read | **297** |
| Local Markdown targets resolved | **4,341** |
| Internal heading fragments checked | **79** |
| Top-level instruction contracts present | **9** |
| Foundations division contracts present | **3** |
| Mechanical repository integrity errors | **0** |

The same workflow invokes existing Fundamentals and Security Foundations inventory/state validators. A [live non-gating coverage diagnostic](tools/report_knowledge_coverage.py) was then added to report article and candidate inventories without hard-coding their current counts.

**Limitations:** The link validator does **not** test remote URL availability, source-text passage relevance, technical truth, semantic relationship correctness, manuscript quality, actual deployment security, independent expert review or publication. Future checks must not overstate their claims.

## 4. Current conceptual coverage and known deficits

### Fundamentals

The [current development register](foundations/fundamentals/DEVELOPMENT-VERIFICATION-REGISTER.md) reconciles 120 authored, scoped Reviewed articles. Previous 109 and 116 numbers belong to historical waves. [Wave H](foundations/fundamentals/WAVE-H-TECHNICAL-REVIEW-01.md) separately reviewed the four newest subjects: calculus/differential equations, stochastic processes, information retrieval, and queueing.

**Remaining:** Complete claim-to-passage verification across the corpus, further numerical/optimization depth analysis, model/architecture consistency, current external source maintenance, and qualified publication acceptance. A technically plausible and internally Reviewed article is not necessarily Verified or Published.

### Security Foundations

The [working candidate inventory](foundations/security-foundations/SUBJECT-INVENTORY-PROPOSAL.md) has 96 active proposed subjects within twelve proposed areas, based on explicit source/ownership adjudication. **Neither count is fixed.** The [pilot register](foundations/security-foundations/pilots/README.md) contains 14 articles, each with scoped [reviews 01](foundations/security-foundations/PILOT-TECHNICAL-REVIEW-01.md), [02](foundations/security-foundations/PILOT-TECHNICAL-REVIEW-02.md), or [03](foundations/security-foundations/PILOT-TECHNICAL-REVIEW-03.md). The [source crosswalk](foundations/security-foundations/ESTABLISHED-MODEL-CROSSWALK.md) and [ownership boundaries](foundations/security-foundations/OWNERSHIP-BOUNDARIES.md) are research records, not permanent canonical ontologies.

**82 current candidate headings lack a pilot**. That is an *article-coverage count*, not proof that every remaining heading is necessary, sufficient, or worth a separate page. The [gap review](foundations/security-foundations/COVERAGE-AND-GAPS-REVIEW-03.md) prioritizes recovery objectives/trusted restoration, side and covert channels, evidentiary confidence/attribution, compliance versus effective security, key lifecycle, threat-behavior models and harm.

**Immediate development direction:** Continue authoring and scoped reviewing substantive pilots, evaluate merges and subject ownership through actual prose, then seek explicit internal-architecture ratification before migrating approved canonical pages. **Do not falsely call pilot manuscripts Published or impose the 96 number as a quota.**

### Operational Foundations and specialized domains

Operational Foundations needs a substantive, evidence-based internal architecture proposal and method pilots; no subject inventory is approved. The specialized domains need actual function/implementation references rather than further decorative indexes. Their sources and implementations should link to general Foundations concepts incrementally.

## 5. Source and knowledge relationship quality

A source-linked article and a source-Verified article are different. A control catalog cannot certify control effectiveness; a model cannot certify a deployment; a valid log is not automatically a truthful attribution. Record these distinctions in every relevant review.

**Relationship coverage** is evaluated by semantic ownership and actual useful links, not a minimum links-per-article or links-per-domain quota. A missing cross-domain link may reflect an unwritten implementation rather than an absent general concept.

**Content variability:** No frozen numbers of articles, topics, examples, subsections, references, diagrams or words. Depth follows complexity and evidence. If source work shows a subject duplicates another, **contract** the inventory; if a distinct concept lacks a home, **expand** it with traceable rationale.

## 6. Execution priorities toward parity

1. **Infrastructure verified:** All 13 scoped AGENTS contracts; reconciled Fundamentals active navigation/status documents; root-wide CI and a dynamic coverage report.
2. **Security Foundations content deepening:** Expand the source-led pilot corpus across the proposed coverage areas, starting with the already identified high-value unpiloted security concepts. Maintain rigorous claim-group review and current source editions.
3. **Architecture acceptance:** Use the developed pilots to decide which Security Foundations areas and subjects should be ratified, split, merged, or relocated. Never infer approval from volume alone.
4. **Promotion path:** After approved canonical placement, move or link existing pilots into real canonical subject locations, reconcile all trackers, and validate the entire corpus.
5. **Verification path:** Claim-to-passage support, external reference freshness, editorial consistency, conceptual relations and qualified independent expert review are separate gates for both Foundations corpora.
6. **Later cross-domain integration:** Operational Foundations and the seven function-first domains acquire substantive content, with real dependencies linked as that content is developed.

**Parity is a maturity standard, not a numeric target.** A Security Foundations corpus comparable to Fundamentals would have approved canonical ownership, substantive navigable articles for the justified inventory, per-article scoped technical evidence, mechanical integrity and clear remaining source/publication gates. It need **not** have exactly twelve areas or 120 subjects.

[Root SOP](AGENTS.md) · [Foundations SOP](foundations/AGENTS.md) · [Repository integrity workflow](.github/workflows/repository-integrity.yml) · [Coverage diagnostic](tools/report_knowledge_coverage.py)
