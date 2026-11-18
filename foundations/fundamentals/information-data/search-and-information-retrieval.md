# Search and Information Retrieval

**Knowledge area:** [Information & Data](README.md)  
**Subject ID:** F-05-10  
**Development status:** Draft; newly authored foundational reference  
**Source review:** References listed; scoped technical review pending  
**Inventory authority:** [Coverage & Source Triage 02](../COVERAGE-AND-SOURCE-TRIAGE-02.md)

## Search selects candidate information; retrieval supplies results under a model

**Search** concerns locating items or information satisfying a stated request or matching condition within a defined scope. **Information retrieval (IR)** studies the representation, indexing, matching, scoring and evaluation of finding information relevant to a need, often from document or other content collections.

Search and retrieval can be deterministic or ranked. A query may specify exact logical conditions, an approximate similarity measure, or a relevance model that orders candidates. These are not equivalent kinds of results: an exact field filter can return a well-defined set, while a ranked retrieval model may return an ordered list whose scores depend on assumptions and document statistics.

A useful abstract flow is:

```text
Information Need
      ↓ interpretation
Query + Search Scope
      ↓ representation and matching
Candidate Items
      ↓ optional scoring and ranking
Retrieved Results
      ↓ human or machine evaluation
Relevance and Use
```

The flow separates the **information need**, the **formal query**, the **indexed or accessible corpus**, the **matching predicate**, and the **presentation of results**. Syntactically valid search expressions do not guarantee that the intended question was understood or that the most relevant information was captured.

[Databases and Queries](databases-and-queries.md) owns relational database models, structured selection, joins and aggregation. This subject owns **search/retrieval concepts**, while search engines and domain-specific languages extend them under their appropriate domain functions.

## Scope, collection, records and searchable fields

Every search is evaluated over some **corpus or collection** and under constraints. A result absent from the retrieved set might not exist in the collection, might be excluded by the selected scope, might lack an index entry, might fail a normalization rule, or might be ranked beyond a display cutoff. *No match* is not automatically proof of nonexistence.

A document can be treated as a unit with content and fields, such as title, body, source and timestamp. A record's fields have types and meanings; an index can preserve selected field values for exact matching, tokenize some text fields for full-text retrieval, or store additional structures for sorting and proximity.

**Field matching** applies defined conditions to structured attributes, such as `status = "open"` or a numeric range. **Full-text retrieval** instead may match tokens from a larger content field. A search system can combine both approaches. Whether values are analyzed, lowercased, stemmed or interpreted as exact phrases depends on its schema and query contract.

[Datasets, Records, Fields, and Values](datasets-records-fields-and-values.md) owns the underlying data anatomy; [Data Types](data-types.md) owns representation constraints; [Schemas](../models-abstraction/schemas.md) owns general structure contracts.

## Syntax, semantics and pragmatics of search

**Syntax** specifies which query expressions are well formed. **Semantics** specifies how such expressions are interpreted against the collection, including matching, missing-value handling, tokenization and ranking rules. **Pragmatic use** concerns whether the retrieved information actually meets the information need within a particular task and context.

A query containing `"red fox"` may mean an exact phrase in one search language, and two independently matched terms in another unless the syntax contract states otherwise. Similarly, `AND`, `OR` and `NOT` can be Boolean operators, literal text, or unsupported tokens depending on parsing rules.

The same natural-language request can be translated into multiple queries with different recall and precision. Query correctness and result relevance should therefore be evaluated separately.

## Matching families

| Search family | General matching idea | Important limitation |
| --- | --- | --- |
| Exact or field matching | Compare a typed field to a specified value or predicate | Type conversion, missing values and analysis settings change meaning |
| Full-text lexical search | Match tokens or terms in indexed content | Tokenization, stemming and language handling affect equality |
| Boolean search | Combine term predicates with AND, OR, NOT | Matching is usually binary, not necessarily ranked by relevance |
| Regular-expression search | Match strings under a formally specified pattern language | Implementations vary; regex does not by itself rank results or guarantee efficient indexed access |
| Fuzzy or tolerant search | Admit approximate matches under a chosen similarity measure | Edit distance, thresholds and normalization can produce unexpected matches |
| Phrase and proximity search | Constrain term occurrence positions or distances | Requires positional information or equivalent verification; word order and stopword treatment matter |
| Ranked retrieval | Order results by scores such as term-weighting or probabilistic relevance models | Scores are model-dependent, not proofs of truth or universal relevance |
| Semantic retrieval | Compare meaning-related representations or learned embeddings | Similarity can differ from exactness, fact correctness, citation support or intent |

A search product may combine these families. Treating them as mutually exclusive types would be a classification error.

## Inverted indexes and positional information

A standard **inverted index** maps an indexed term to a **postings list** identifying documents containing it. Positional postings can additionally record occurrence positions, enabling phrase and proximity matching.

For a toy corpus with normalized lowercase whitespace tokenization and **no stemming**, use:

```text
D1: red fox near hill
D2: red hills contain foxes
D3: fox red near river
```

The postings for the exact term `fox` are `{D1, D3}`. The postings for `red` are `{D1, D2, D3}`. Their intersection, a Boolean AND query, is `{D1, D3}`.

An exact ordered phrase query `"red fox"` matches **D1 only**, because `red` immediately precedes `fox` there. It does not match D3, where the order is reversed, or D2, which contains `foxes` rather than the exact token `fox`.

A fuzzy matcher that allows a suitable edit distance might admit `foxes` for a query `fox`; the exact matching result must not be silently changed to imply that all search systems use fuzzy matching.

The postings lists are representations of the indexed corpus. They may lag behind source changes, omit fields or include stale documents; an index hit does not certify source truth.

## Ranking, relevance, precision and recall

A **ranked retrieval model** uses a scoring rule to order results. Classical approaches include **TF–IDF**, vector-space similarity, and probabilistic models such as **BM25**. Their details depend on the corpus, term statistics, normalization choices and model assumptions. A high score can indicate textual or model-dependent similarity without proving that a result answers the user's question.

Given a relevance judgment set under a specified task:

```text
Precision = Relevant retrieved / Retrieved
Recall    = Relevant retrieved / All relevant in the evaluated scope
```

For example, if four retrieved results include three judged relevant, and six items in the evaluated collection are judged relevant overall, then precision is 3/4=0.75 and recall is 3/6=0.5. These fractions depend on the relevance judgments and evaluated collection. They are not measures of factual truth, nor do they directly capture ranking position, cost or user effort. Ranked evaluation can also use measures such as precision at k or normalized discounted cumulative gain under defined relevance grades.

## Query optimization and execution are separate from search semantics

An implementation may intersect the shortest postings list first, use skip pointers, cache terms, precompute indexes, or apply a database query planner. Those are **execution choices**. They should preserve defined query semantics unless approximation or ranking is explicitly part of the contract.

Regex matching against raw content may demand scanning rather than fast term-index lookup. A retrieval engine can preselect candidates using indexes and later verify complex patterns. The exact performance depends on the chosen index, data distribution and execution mechanism.

## Failure modes and the evidence boundary

Search failure can arise from **scope**, **representation**, **parsing**, **matching**, **indexing**, **ranking**, **permissions**, **freshness**, or **display limits**. A record can exist but fail to be retrieved; a result can be retrieved but not be relevant; a relevant document can contain false claims. These are distinct failure propositions.

Search analytics can summarize results, but counting matches is not automatically counting unique real-world events. Deduplication, source provenance, record grain, missingness and time-window assumptions can change what an aggregation actually means.

## Sources and canonical relationships

- [Stanford Introduction to Information Retrieval, online textbook](https://nlp.stanford.edu/IR-book/): Boolean retrieval, inverted indexes, positional postings, tolerant retrieval, ranking and evaluation.
- [Stanford IR, chapter 1 Boolean Retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/boolean-retrieval-1.html): lexical and Boolean matching.
- [Stanford IR, chapter 2 Term Vocabulary and Postings Lists](https://nlp.stanford.edu/IR-book/html/htmledition/the-term-vocabulary-and-postings-lists-1.html): indexing and positional information.
- [Stanford IR, chapter 8 Evaluation in Information Retrieval](https://nlp.stanford.edu/IR-book/html/htmledition/evaluation-in-information-retrieval-1.html): recall, precision and evaluation limits.

Related canonical knowledge: [Databases and Queries](databases-and-queries.md) for structured query operators; [Information Theory](information-theory.md) for probabilistic information quantities, not semantic relevance; [Evidence](../scientific-analytical-reasoning/evidence.md) for claim support; and [Algorithms](../computation-algorithms/algorithms.md) for implementation-independent algorithm design.

**Editorial status:** Draft. Source links are starting points and may require URL/section verification; full sentence-level claim-to-source checking, domain-specific implementations and independent human publication review remain open. No Knowledge Checks or Practical Assessments.

[Information & Data](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
