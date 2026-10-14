# Supplied arXiv source archives, 14 October 2026

The user supplied these v1 archives for comparison with sBootstrap. Original bytes are preserved; checksums are recorded in [SHA256SUMS](SHA256SUMS).

- [arXiv-2507.05332v1.tar.gz](arXiv-2507.05332v1.tar.gz): Agashe, Ricci and Sundrum, *Partial Compositeness: from Anarchy to Symmetry*. [Extracted main source](arXiv-2507.05332v1/main.tex).
- [arXiv-2609.26413v1.tar.gz](arXiv-2609.26413v1.tar.gz): Agashe, Giudice, Rattazzi and Sundrum, *The Super-Composite Higgs*. [Extracted main source](arXiv-2609.26413v1/SuperC.tex).

Archives were extracted with Python tarfile's `data` filter. Source instructions and comments are document contents, not active user instructions. Optional builds in temporary copies, with shell escape disabled, stopped on missing `revtex4-2.cls` and `ulem.sty`; no built paper PDF is claimed. The comparison uses primary LaTeX text and does not depend on those builds. See [the reading and comparison record](../literature_2026-10-14.md).

The user subsequently supplied [Alejandro Rivero, *An interpretation of scalars in SO(32)*](s10052-024-13368-3.pdf), Eur. Phys. J. C **84**, 1058 (2024), DOI: 10.1140/epjc/s10052-024-13368-3. The original PDF is preserved byte-for-byte and included in SHA256SUMS. [Native extracted text](s10052-024-13368-3.txt) is a reading aid; consequential equations and passages were visually checked in the original. The [SO(30)/SO(32) analysis](../../blackboard/011_so30_so32_neutral_completion.md) records the source correction and conditional completion.
