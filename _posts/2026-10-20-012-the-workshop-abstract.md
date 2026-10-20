---
tags: workshop2026abstract
title: "The Human Petrophysicist in the Age of Agentic AI  (Kjetil Westeng, Aker BP)"
presentation_date: 2026-11-04
---
#### Presenter
**Kjetil Westeng** from Aker BP
## Abstract
Introduction

Today, LLM-based agents can retrieve subsurface data, write code, produce a complete petrophysical interpretation, and even write an elegant and convincing report at the end. But velocity is not what builds trust in the results. An interpretation must be consistent between wells, honour the different types of good-quality measured data, be tested against sparse core and test data, and be owned by someone accountable for the product.

Earlier work on automated interpretation argued that the relevant question is ‘acceptable for what?’ rather than ‘acceptable for all’ (Westeng et al., 2024). Agentic workflows add a second question, controlled by whom? The permitted use of an interpretation product should match the human control behind it.



Approach

Two properties of a task decide where agentic workflows belong today: how quickly the answers can be verified, and how much variation is tolerated (Figure 1). Software development fits both, while petrophysical interpretation is non-unique, sparsely validated (mainly in cored intervals), and has little tolerance for variation.

The same reasoning that favoured predicting interpretation parameters rather than reservoir properties directly, to keep results traceable and comparable, applies to agents, they should build and run reproducible methods in curated code, not interpret.



Observations

Agentic engineering has shortened the time from idea to working tool from months and years to days. While retaining control of the calculations through domain-owned deterministic scripts, we can now very quickly build interactive visual tools that support the petrophysicist, and update or replace them as the challenges change. The cost of maintaining a rapidly growing number of tools is a risk, but it is manageable with tests, shared libraries, and clear code owners. Succeeding with such a strategy requires access to domain expertise, software engineering expertise, and innovation skills, as well as a secure digital ecosystem.

We strive to avoid or mitigate three pitfalls: agent hallucination, agent sycophancy (the tendency to agree with what the user appears to want), and human approval fatigue.

A deterministic automatic interpretation framework has matched manual interpretation against core in earlier work and is used to screen large datasets. Raising it to decision grade requires a petrophysicist to refine the result and take ownership of it, a process that poses three challenges: (i) making the petrophysicist aware of all relevant data, in the well and in offset wells, before evaluating the automated result; (ii) making refinement easier than passive acceptance; and (iii) capturing curation status (e.g. in OSDU), so that ownership is real and felt, not merely assigned.



Conclusion

The field of AI is evolving rapidly: agent capabilities will change, but the non-uniqueness of petrophysical interpretation will not. Agents build and orchestrate, curated code computes, the petrophysicist decides and owns, and the use of each product matches the human control behind it.

Just as computerized interpretation eroded chart-book skills, agents may erode the hands-on experience that builds petrophysical judgment. How do we train petrophysicists to supervise work they no longer do themselves?




## Biography
Kjetil Westeng is an Advanced Petrophysicist