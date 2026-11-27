# Q1155 primary sources and scope

**Verdict, 27 November 2026.** High confidence in the match to the published restricted-family conjecture. This bounded check found the one-pair special case, the classical general pairing method and recent work for the unrestricted game. It found no earlier statement of this positive-density restricted family or of the sharp density within fixed disjoint-pair certificates. Priority has not been established. Q1154 is an attributed deduction from a published block strategy and is presented as a companion.

## Published question and previous bounds

Žarko Ranđelović, *The transversal game*, DMTCS 28(3), no. 26, published 25 November 2026. [Journal record](https://dmtcs.episciences.org/en/articles/19063) · [§3, Conjecture 7, printed and PDF p. 13](https://dmtcs.episciences.org/en/articles/19063/download#page=13) · [24 November author revision](https://arxiv.org/html/2401.16768v4#S3).

Both players have the same restricted family of transversals. The threshold g(n) is the smallest size such that every family at least that large yields a first-player forced win. A defense preventing that win is enough to give a lower bound. The paragraph before Conjecture 7 already exhibits (n−2)! transversals blocked by one common mandatory pair. Their density tends to zero. Theorem 6 gives the separately stated upper bound g(n)≤n!−mₙ+1. Here the two opposing diagonals in each 2×2 block yield order n² disjoint admissible pairs, and a compatibility count gives a strictly positive limiting coverage fraction. The upper bound for the pairing certificate relies on disjointness and makes no assertion about the best arbitrary defense.

## Closest prior work

- [A. W. Hales and R. I. Jewett, *Regularity and Positional Games*, Trans. AMS 106(2), 222–229 (1963)](https://www.jstor.org/stable/1993764) provide classical pairing strategies. The tactic of answering in the mate of a played cell is standard. The contribution here is the family defined by the block pairings and the exact/asymptotic coverage count.
- [Kevin Guan, *The transversal achievement game on a square grid*, arXiv:2608.13501, §7](https://arxiv.org/html/2608.13501#S7) improves the move bound for first-player wins in the unrestricted game. Its discussion expressly leaves f(n) and g(n) for restricted families outside its results. A fast strategy for the whole family may use transversals absent from a restricted family.
- [Ranđelović, Conjecture 5, p. 11](https://dmtcs.episciences.org/en/articles/19063/download#page=11) asks for an eventual exponential upper bound on the smallest winning family f(n). The Claim in the published Theorem 4 proof, pp. 10–11, guarantees that Maker playing second forms a transversal in a full square of any size at least five. The theorem already runs those strategies in separate blocks for the weak game. The short strong-game deduction uses one common opening cell, which prevents the opponent from completing any allowed set. The proof here credits the published strategy and accounts for moves outside the unfinished blocks using simulated Breaker moves. This is a companion deduction.

Searches checked the exact conjecture, recent restricted/unrestricted results and the disjoint-pair construction and count. The governing sources are the final journal paper and the latest authors’ public preprints.
