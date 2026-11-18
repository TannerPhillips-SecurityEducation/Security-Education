# AGENTS.md | GitHub Repository Automation & Evidence Contract

**Applies to:** `.github/`, its `workflows/` directory, and related automation files.  
**Inherited authority:** [Root AGENTS.md](../AGENTS.md) governs editorial integrity, source evidence, flexible subject counts, honest approvals, and agent initiative. This document narrows those rules to repository automation; it does not override security/tool permissions.  
**Actual current automation:** [Fundamentals navigation and inventory integrity](workflows/fundamentals-internal-links.yml), [Security Foundations working architecture and area-article integrity](workflows/security-foundations-integrity.yml), and [repository-wide AGENTS/navigation integrity](workflows/repository-integrity.yml).  
**Status:** Working operational instructions, **not** a declaration of new branch protections, available secrets, completed external verification, or approval to deploy.

## 1. Mission and non-negotiable boundaries

The `.github` directory manages **mechanical verification, safe automated workflows, inspectable execution evidence and repository maintenance triggers**. Its job is to make errors visible, not to inflate manuscript maturity or infer scientific truth from a green status.

Keep automation scoped to the repository's actual approved structure. **Never** use a workflow to turn a proposed area, inventory count, article or ontology into an approved one merely because a script can parse it.

## 2. Approved structure versus automation proposals

The two current workflows are implemented and can be inspected. Any additional workflow, CI integration, dependency, secret, external deployment or required status gate is a **proposal until created and authorized** under the relevant repository governance.

Automation may verify relative links, headings, article paths, unique IDs, register state consistency, changes to source references and bounded diagnostics. **It cannot independently prove a security control is effective, a standard was followed clause by clause, a hypothesis is true, or an article deserves publication.**

Subject/area counts are *living*: validators should read current inventories rather than hardcode 120 Fundamentals articles, 96 provisional Security Foundations candidates, or any other historical denominator as permanent.

## 3. Current directory and workflow responsibilities

The physically present structure contains:

- [`workflows/fundamentals-internal-links.yml`](workflows/fundamentals-internal-links.yml): Checks Fundamentals Markdown references, tracker/ownership consistency and non-gating model/source coverage diagnostics.
- [`workflows/security-foundations-integrity.yml`](workflows/security-foundations-integrity.yml): Checks Security Foundations **provisional area README/article layout**, candidate IDs, historical pilot aliases, Markdown links and source/review states via [dynamic area validator](../foundations/security-foundations/tools/check_area_structure.py).
- [Root contributor SOP](../AGENTS.md) and three Foundations subtree contracts under [Foundations](../foundations/README.md): actual content authority and editorial gates remain in their relevant directories.

The [repository-wide integrity workflow](workflows/repository-integrity.yml) also reconciles live Foundations subject inventories and validates scoped AGENTS contracts. No other workflow, CI tool, branch protection or deployment pipeline should be described as already implemented unless inspected.

**File responsibilities:** Workflow YAML defines triggers/jobs/permissions; reference scripts own validation logic; GitHub Actions logs are run-specific evidence; a technical article review belongs in the corresponding knowledge division, not the workflow.

## 4. Operating loop: Observe → Derive → Infer → Act

1. **Observe:** Read the current workflow, scripts, relevant path tree, execution logs, triggers, event payload assumptions and actual changed files.
2. **Derive:** Determine what the test guarantees, what it doesn't, required credentials/permissions, source-of-truth files and failure impact.
3. **Infer:** Identify missing coverage, unsafe assumptions, stale hardcoded counts, incorrect regexes, false positives and unintentional privilege expansion.
4. **Act:** Make the smallest reviewable, reversible CI change; validate YAML and relevant scripts, trigger the intended run if possible and confirm the completed result.

Avoid Socratic questioning; use direct critique and transparent technical execution. Never claim a test is passing merely because a job was scheduled or a previous SHA passed.

## 5. Critical distinctions for CI and evidence

- **Workflow file / job execution / successful job / publication acceptance:** Four different artifacts and decisions.
- **Markdown target resolved / heading fragment valid / source URL reachable / citation semantically supports a claim:** Distinct levels of verification.
- **Lexical model mention / substantive conceptual coverage / correctness of model application:** A source or keyword count is not a proof of completeness.
- **Proposed subject ID / real article / reviewed article / approved canonical path:** A passing inventory count cannot collapse these states.
- **Diagnostic / mandatory gate:** A non-gating report may identify worthwhile work without blocking unrelated changes; an actual gate must fail transparently on its defined integrity errors.
- **Read-only validation / write permission / deployment permission:** Distinguish intended behavior from actual token and repository permissions.
- **Current run SHA / historical passing run SHA:** Test evidence applies to the exact code and files it examined.

## 6. Source and platform security contract

Consult the [GitHub Actions documentation](https://docs.github.com/en/actions) and official syntax/action requirements before changing workflow behavior or permissions. Verify action major versions, current deprecations and security notes where they matter.

Use **least privilege** by default, as existing workflows do with `permissions: contents: read`. Preserve scoped `push`, `pull_request` and `workflow_dispatch` triggers unless a justified workflow change requires otherwise. Avoid untrusted shell interpolation from pull-request titles, attacker-controlled inputs, arbitrary artifacts or unchecked data.

Do not echo credentials, API tokens, private records or secrets to logs. Do not add a deploy/publish or external-write step without explicit authorization, security review and actual tool support. Do not assume a secret or repository/environment permission exists.

## 7. Authoring or revising automation

A useful workflow or script should specify the **claim it checks**, scope/path filters, input files, success/failure conditions, environment requirements, and limitations.

Keep scripts deterministic and as simple as the task allows. Parse **current registered content**, not a permanently fixed subject total. For a novel parser, test both expected-valid and expected-invalid fixture examples, including duplicate IDs, missing files, stale status strings, changed headings and optional content.

A meaningful CI result reports actual files or paths checked, broken references and review states when applicable. New diagnostics should not be disguised as mandatory publication approval.

## 8. Inventory growth, schema and structural changes

Changes in knowledge architecture are **owned by the relevant content division**. A CI tool can detect discrepancies and document them, but it cannot authorize a new category, canonical directory, ontology predicate, publisher version, or technical-review status.

When the inventory expands/contracts, reconcile validation logic to the adopted file conventions and prior IDs. A structural integrity failure may reveal a **legitimate new editorial state** or a parser bug; inspect before assuming the content is wrong.

Avoid disabling checks merely to attain a green result. If current rules are too rigid, update them with a documented explanation and tests that retain the intended guarantee.

## 9. Directory navigation and file scope

- [`.github/AGENTS.md`](AGENTS.md): This automation-specific operating contract.
- [Root AGENTS.md](../AGENTS.md): Global technical/editorial constraints and review states.
- [Root README](../README.md): Approved navigation and public repository scope.
- [Fundamentals CI workflow](workflows/fundamentals-internal-links.yml): Mechanical checks for actual Fundamentals files.
- [Security Foundations CI workflow](workflows/security-foundations-integrity.yml): Mechanical checks for working Security Foundations files.

Future tools, workflows, releases or CI reports need only be added when there is actual content or measurable validation value. Keep the repository free of decorative placeholder workflows.

## 10. Development, review and acceptance states

Treat **workflow implemented**, **workflow tested**, **commit-specific validation passed**, **claim sources checked**, **content Reviewed**, **content Verified**, and **Published** as separate facts.

A model-assisted editorial audit belongs in a technical review ledger, not as an assertion inferred from CI. A syntax validator cannot prove the technical claims in a networking, cloud, physical control or cryptography article.

Automated merges, releases and publishing must respect project authorization and distinct editorial acceptance gates. No workflow should silently promote articles to Published merely because all links resolve.

## 11. Safety, security and test validation

Before committing workflow edits, check: YAML structure, actual script paths, action versions, event filters, path globs, job permissions, shell quoting, failure handling, expected exit codes, dependency availability and untrusted input handling.

After a commit, inspect the corresponding GitHub Actions run and relevant job logs. A **passing run must be completed and match the tested commit**. On a failure, find the first meaningful error, correct its cause and rerun. Describe a missing/unsupported test accurately.

Validate cross-subtree agent links and navigation only after creating the actual targets. Avoid writing CI that recursively creates a new directory or rewrites the subject inventory to match expected counts.

## 12. Change control and evidence reporting

Use current blob SHA for GitHub updates. Avoid overlapping writes to the same path, undeclared secret use, unreviewed new external actions and breaking changes to CI contracts.

When reporting automation work, provide the changed workflow or script, actual run URL, outcome, checked metrics, limitations and outstanding technical/publication gates. Distinguish automated static checks from empirical model or implementation tests.

If code must run with more permissions, describe the reason and risk; do not infer authorization from general collaboration instructions.

## 13. Next-agent handoff checklist

1. Read [root SOP](../AGENTS.md), current [workflow files](workflows/fundamentals-internal-links.yml) and associated validation scripts before editing.
2. Confirm the actual intended validation claim, scope and current path/approval state in the affected content division.
3. Make a minimal, deterministic, least-privilege change with explicit failure semantics.
4. Check YAML and test scripts against changed conventions, including dynamic inventory counts.
5. Commit, inspect the **completed commit-matched run**, and correct any real failure.
6. Report exactly what automation demonstrated and what it could not demonstrate.
7. Do not equate a green structural run with source-Verified, expert-reviewed or Published material.

**Governing principle:** Automation supports evidence; it cannot manufacture it. Fail visibly, protect credentials, keep counts dynamic and publish only with explicit authorization.
