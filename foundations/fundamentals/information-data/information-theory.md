# Information Theory

**Knowledge area:** [Information & Data](README.md)  
**Approved subject heading:** Information theory  
**Development status:** Draft  
**Source review:** References listed; separate scoped claim-to-source audit pending

## Measuring uncertainty in an information source

**Information theory** develops mathematical quantities and bounds for representing and communicating information under explicitly specified probabilistic models. Its Shannon formulation concerns uncertainty in source outcomes, information gained from observations, dependencies between random variables, and limits for coding or communication through channels. **Shannon entropy is not a universal measure of semantic meaning, truth, importance, or usefulness.**

The foundational reference is [A Mathematical Theory of Communication](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf). [Probability and Statistics](../mathematics-logic/probability-and-statistics.md) supplies the probability mathematics; [Bits and Bytes](bits-and-bytes.md) covers binary representation units.

## Self-information and entropy

For a discrete event of probability `p(x)>0`, its **self-information** is:

```text
I(x) = -log₂ p(x)   bits
```

A less probable outcome has greater self-information under the stipulated distribution. Self-information is defined here for possible events with positive probability. An event assigned probability one has zero self-information.

For a discrete random variable `X` with probabilities `p(x)`, Shannon entropy is

```text
H(X) = - Σ_x p(x) log₂ p(x)
```

with the standard convention `0 log₂ 0 = 0`. Entropy is **expected self-information**, measured in bits when base-two logarithms are used. It is a property of the modeled distribution, not of a raw sample by itself.

For a fair binary source `p(0)=p(1)=1/2`, `H(X)=1` bit per symbol. For a deterministic source `p(0)=1`, `H(X)=0`. For a biased source `p(1)=1/4`, `H(X)=-(1/4)log₂(1/4)-(3/4)log₂(3/4)≈0.8113` bits per symbol.

## Entropy, capacity, and encoded length are distinct

For a finite alphabet of `m` possibilities, `0 ≤ H(X) ≤ log₂ m`, and the upper bound is reached for a uniform distribution. This upper bound concerns entropy per source symbol, not necessarily the length of each symbol's serialized representation.

An eight-bit storage field has `2^8 = 256` possible binary patterns. A uniformly distributed selection among those patterns has eight bits of entropy; a constant value in the same field has zero entropy. Compression potential depends on distribution, sequence dependencies, coding method, error requirements, and relevant practical constraints. A field's physical storage width is not its modeled Shannon entropy.

## Conditional entropy and mutual information

**Conditional entropy** `H(X|Y)` expresses the expected uncertainty of `X` after observing `Y` under their joint distribution. **Mutual information** measures information shared between `X` and `Y`:

```text
I(X;Y) = H(X) - H(X|Y)
       = H(Y) - H(Y|X)
```

For discrete variables with well-defined finite entropies, `I(X;Y) ≥ 0`; it is zero if and only if the variables are independent under the modeled joint distribution. It can be positive without implying that one variable causes the other. Causal interpretation remains with [Causality and Correlation](../scientific-analytical-reasoning/causality-and-correlation.md).

If `Y=X` exactly, the mutual information is `H(X)`. If `X` and `Y` are independent, mutual information is zero, irrespective of whether their individual entropies are high.

## Channels and coding limits

A communication channel relates transmitted and received symbols through a conditional probability model. **Channel capacity** describes the maximum mutual information per channel use after optimization over permitted input distributions, for the specified channel model. Interpreting capacity as a rate per second requires an additional channel-use rate or timing model.

Under suitable assumptions, channel coding can approach reliable transmission below capacity with increasing code block lengths and appropriate coding schemes. This is **not** a claim that every actual channel provides error-free communication or that any implementation can reach its theoretical bound without cost. The specific theorem conditions matter.

**Source coding** concerns efficient representation of source messages; **channel coding** introduces structured redundancy to help recover messages despite channel errors. These goals can pull in different directions and must not be conflated.

## Information versus meaning and evidence

A random-looking string may have high entropy yet little relevance to a particular question; a short warning may have low entropy under a source distribution but enormous practical significance. Entropy alone does not validate source honesty, observation accuracy, or the truth of any statement.

[Evidence](../scientific-analytical-reasoning/evidence.md) owns claim-relative support; [Uncertainty and Confidence](../scientific-analytical-reasoning/uncertainty-and-confidence.md) owns interpretation of knowledge limits. A high-entropy data field is not inherently more trustworthy, secure, or useful than a low-entropy one.

## Worked example: an apparently informative observation

Suppose `X` is a fair bit and `Y` is a perfect copy. Then `H(X)=1`, `H(X|Y)=0`, and `I(X;Y)=1` bit. If instead `Y` is a fresh independent fair bit, `H(X|Y)=1` and `I(X;Y)=0`.

Both `Y` fields individually have entropy one bit. Their **relationship to X** determines their mutual information. This demonstrates why independence, dependence, and information content require explicit probabilistic context.

## Sources and boundaries

- [A Mathematical Theory of Communication, foundational paper](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf).
- [MIT Mathematics for Computer Science readings](https://ocw.mit.edu/courses/6-1200j-mathematics-for-computer-science-spring-2024/pages/readings/).

**Editorial status:** Substantive draft, including original numeric examples. The numeric examples and theorem qualifications require a scoped technical review. No conflation with semantic meaning or security analytics is permitted.

[Information & Data](README.md) · [Fundamentals](../README.md) · [Development Register](../DEVELOPMENT-VERIFICATION-REGISTER.md)
