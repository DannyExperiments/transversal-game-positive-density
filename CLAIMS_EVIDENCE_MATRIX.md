# Claims and evidence

| Claim | Evidence |
| --- | --- |
| A positive-density family admits a pairing defense | [Theorem 1 and §2](paper/manuscript.pdf) |
| Exact family size and fixed-pair asymptotic sharpness | [§§3–4](paper/manuscript.pdf) |
| Small board family sizes and explorer membership | [Replay](verification/results/replay.txt) |
| Exponential winning family via published blocks | [Companion deduction](proof/companion-q1154.md) |
| Source and scope of the conjectures | [Primary-source comparison](audits/public_safe_reports/LITERATURE.md) |

### Scoped Lean result

For every disjoint matching, including one with unpaired cells, a response at its unique free mate preserves the guarding invariant at every round. With disjoint player marks the next legal first-player move cannot complete any matched pair. The certificate handles the turn before the defender replies. The enumeration of transversals, asymptotic density and optimality within the fixed-pair class remain in the paper. [Declaration and replay](formalization/README.md)
