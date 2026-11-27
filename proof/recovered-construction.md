# Q1155: a positive-density family the first player cannot win

**Result.** Conjecture 7 of the cited paper is false. More precisely, liminf as n→∞ of g(n)/n! is at least 1−exp(−1/2), approximately 0.393469. This bound is asymptotically best among the particular certificates that require every allowed transversal to contain a complete pair from a fixed disjoint pairing of cells. No optimal value of g(n) is claimed.

## Exact source and rules

Žarko Ranđelović, *The transversal game*, DMTCS 28(3), article 26, 2026. [Publisher's final PDF, §3, Conjecture 7, printed and PDF p. 13](https://dmtcs.episciences.org/en/articles/19063/download#page=13): Its statement is g(n)=o(n!). The final PDF and [author's latest revision, arXiv:2401.16768v4, §3](https://arxiv.org/html/2401.16768v4#S3) were checked, as was the [pinned catalog entry](https://github.com/10m-u/open-problems-catalog/blob/ca8d4d44ba3db527f19f28928c240168f545ecfe/problems/mathematics/combinatorics-graph-theory-part-1.md#q1155). The [journal record](https://dmtcs.episciences.org/en/articles/19063) gives 25 November 2026 as publication date; arXiv lists v4 as its latest.

Players X and O alternate marking previously unoccupied cells of an n×n grid, X first. Both players have the same prescribed family F of winning sets, each a transversal (a permutation matrix's support). Completing any member wins. If no one does, play can end in a draw. The threshold g(n) is the least integer such that for every family of at least that size X can force a win. Preventing X from winning suffices; it is immaterial whether O wins or draws.

## 1. A pairing defense

Put m=⌊n/2⌋. Pair the first 2m rows into consecutive pairs and likewise the first 2m columns. Each resulting 2×2 block contributes its two diagonal pairs of opposite cells. All these pairs are disjoint; cells outside the blocks can remain unpaired. Define F to be the transversals containing both cells of at least one of the prescribed pairs.

After X marks a paired cell, O marks its mate if free. Otherwise O moves anywhere legal. Thus X can never own both cells of any pair: the first claimed by X is either followed immediately by O's reply or already has an O-marked mate. This argument also rules out X winning immediately on its move, because in any complete pair in a newly completed transversal the first cell must have been marked by X on a strictly earlier move. Unpaired cells and a game that ends before a reply create no exception. Consequently g(n)>|F|.

## 2. Exact count and limiting density

Use a uniform random permutation of n columns and count Z, the number of marked pairs contained in its transversal. Put S_k=E[binom(Z,k)] and (n)_j=n(n−1)…(n−j+1). For 1≤k≤m,

    S_k = binom(m,k)^2 k! 2^k / (n)_{2k}.

To verify the coefficient, a feasible k-set of marked pairs has k distinct row-pair blocks and k distinct column-pair blocks. Choose those two k-element sets, match them by a bijection, and select the diagonal in each matched block in two ways. The resulting 2k prescribed cells have distinct rows and columns; the probability of finding all of them in the random permutation is 1/(n)_{2k}. No other k-set can occur. Thus the exact family size is the inclusion–exclusion sum n! times ∑_{k=1}^m (−1)^{k+1}S_k.

For fixed k, as n grows, m/n→1/2, hence S_k→(1/2)^k/k!. Bonferroni bounds P(Z≥1) between its alternating partial sums of even and odd order. For every fixed order pass to the limit in n; then let the order grow. Both bounds converge to 1−exp(−1/2). There is no interchange of an unbounded sum and a limit. This gives the claimed lower bound on g(n)/n! along all integers n→∞.

## 3. Optimal limiting density within this fixed-pair certificate

For any disjoint pairing, ignore the pairs in a single row or column: they cannot occur in a transversal. Let q_n be the number of remaining pairs, so q_n≤n²/2. Fix k. A given pair is incompatible with at most 4n other distinct pairs, since those must meet at least one of its two rows or two columns and each cell belongs to at most one pair. Therefore among all q_n^k ordered k-tuples, at most O_k(n^{2k−1}) have two incompatible or repeated pairs (choose the two positions, the first pair, its conflicting partner, and the other entries). A compatible set appears in k! orders and fixes 2k values of the permutation. It follows that on any subsequence with q_n/n²→a, each S_k→a^k/k!. The same fixed-order Bonferroni argument gives limiting density 1−exp(−a)≤1−exp(−1/2). Every subsequence has a further subsequence where a exists, proving the claimed upper bound on limsup. Our construction has q_n=2⌊n/2⌋². This upper bound is only for the fixed-pair certificate, not for all possible defensive strategies.
