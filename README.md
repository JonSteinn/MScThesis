# Automated Bijections with Combinatorial Exploration

This is my master thesis in Computer Science at Reykjavík University.

## PDF Downloads
 - [Thesis](https://github.com/JonSteinn/MScThesis/raw/main/Thesis/MScThesis%20.pdf)
 - [Defense](https://github.com/JonSteinn/MScThesis/raw/main/Defense/ThesisDefense.pdf)

## The defense
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/VYdBZf9zB44/0.jpg)](https://www.youtube.com/watch?v=VYdBZf9zB44)

## Abstract
Bijections appear in most areas of mathematics. They are of particular importance in the field of combinatorics, where they are a way of enumerating families of objects. The aim of this thesis was to develop a fully automated and domain agnostic bijection search built on top of an existing automated combinatorial specification framework. We define a binary relation on specifications that structurally associates them. When satisfied, a bijection can be constructed between their classes. This theoretical foundation is accompanied by a search algorithm for specifications satisfying this relation. The algorithm utilizes dynamic programming and backtracking. If a bijection is found it can map objects between the classes of the specifications, in both directions. The search algorithm was mainly applied to the domain of permutation patterns, where a total of 189 bijections were discovered, excluding symmetries and compositions. In many cases no previous bijections were known. Some cross-domain bijections were also discovered. As far as we know, this is the first ever fully automated bijection framework, with prior attempts requiring preliminary mathematical work. This work offers substantial structural insight into classes and can be considered a significant innovation in automated mathematics.

## Implementations
All the implementations of my work can be found in the following repositories.
- [Combinatorial Exploration](https://github.com/PermutaTriangle/comb_spec_searcher). A framework for finding specifications for combinatorial classes.
- [Tilings](https://github.com/PermutaTriangle/Tilings). An implementation of Combinatorial Exploration for the domain of permutation patterns.
- [Permuta](https://github.com/PermutaTriangle/Permuta). A general permutation library.
