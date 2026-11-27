# Reproducibility

Run from the repository root with Python 3.11 or later.

    python3 -I scripts/verify_repository.py
    python3 -I verification/src/replay.py

Direct enumeration checks the inclusion–exclusion count on boards of sizes four through nine. The replay also checks all 24 transversals and their complete pairs on the four-by-four worked board. [Recorded replay](verification/results/replay.txt).

Extract the [offline explorer](visualization/paired-grid-explorer.zip) and open index.html. The [GIF renderer](visualization/render.py) uses Python and Pillow with supplied font paths. [Build the paper](paper/BUILD.md).
