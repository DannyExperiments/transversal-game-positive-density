# Lean certificate

`TransversalPairing.all_turns` is checked using Lean 4.30.0 and its standard library.

For every disjoint matching, including one with unpaired cells, a response at its unique free mate preserves the guarding invariant at every round. With disjoint player marks the next legal first-player move cannot complete any matched pair. The certificate handles the turn before the defender replies. The enumeration of transversals, asymptotic density and optimality within the fixed-pair class remain in the paper.

[Source](Q1155Pairing.lean) · [Verification workflow](../.github/workflows/lean.yml)

To replay from the repository root with Lean 4.30.0 installed, run

```sh
lean -DwarningAsError=true formalization/Q1155Pairing.lean
```

The source requests an axiom report. The GitHub Actions workflow downloads the pinned compiler, verifies its SHA-256 and checks the source with warnings treated as errors.
