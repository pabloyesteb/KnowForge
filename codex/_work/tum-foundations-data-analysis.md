# Tree extraction — tum-foundations-data-analysis

## TreeNodes

- Linear algebra and Hilbert-space geometry
- SVD, low-rank approximation and dimensional coordinates
- Probability and high-dimensional concentration
- Random projections and dimension reduction
- Convex analysis and optimization

## Batches

[Source profile / file index](../../00_sources/source_profiles/tum-foundations-data-analysis.md).
Archive: `00_sources/raw/tum/archives/Foundations in 950732430 (S24)_20261012_1529.zip`.
B = `Introduction and general information/Booklet of Exercises FDA.pdf` (79 physical pages).
E<n>/S<n> = numbered weekly task/solution pair; N<n> = corresponding `All you... math` review (extensionless PDF), using the profile's exact weekly paths. Read each full pair/review once; later overlaps extend existing Items.

| # | Original boundaries | Status |
|---|---|---|
| 1 | B front matter and Chapter 1, pp. 1–15; entire E0–E1/S0–S1; N1–N2 | Partial: B/E0/E1 done; S0/S1/N1/N2 unread |
| 2 | B Chapter 2, pp. 16–40; E2–E6/S2–S6; N3–N7; `6. Mai - 12. Mai/peppers.png`, `20. Mai - 26. Mai/Erratum Exercise 4.1`, `3. Juni - 9. Juni/Code for Exercise 6.2` | Pending; subdivide at exercise groups as needed |
| 3 | B Chapter 3, pp. 41–56; E7–E8/S7–S8; N8–N9 | Pending |
| 4 | B Chapter 4, pp. 57–61; E9/S9; N10–N11 | Pending |
| 5 | B Chapter 5, pp. 62–76; E10–E11/S10–S11; N12; reuse N11 | Pending |
| 6 | B Chapter 6 through end, pp. 77–79; E12/S12; N13; both `Introduction and general information/` sample-exam PDFs; archive index; reconciliation | Pending |

## Progress

- Completed Sources: `tum-functional-analysis` (54 Items/7 nodes; all 13 chapters, supplement, 14 sheet pairs, tutorial, mock exam); `tum-nonlinear-optimization` (20 Items/4 nodes; all 7 supplied sheet pairs/index). Source-wide reconciliation and production/example validation passed; completed plans removed.
- Current Source: B pp. 1–15 and entire E0/E1 read; 6 Items, 1 node, covering all Chapter 1 exercises and further exercises. S0/S1/N1/N2 contain effectively no mathematical selectable text and remain unread; do not count them as covered.
- Next: batch 1, `22. April - 28. April/Solution of Exercise Sheet 0.pdf`, its single tall physical page from the top, then entire `29. April - 5. Mai/Solution Sheet 1.pdf`, N1 and N2. Render readable consecutive vertical crops; extend existing Items for complementary evidence. Do not reread B/E0/E1 unnecessarily.

## Open issues

- Reviews/solutions contain handwritten, tall pages: inspect visually; booklet/profile cannot substitute for their originals.
- Archive contains `Code for Exercise 6.2`, absent from the profile's file list: inspect as text only, do not execute. Verify file format and scope in batch 2.
- Read E12's convex-analysis content with Chapter 6; reconcile back to Chapter 5 without duplicate Items.
- Relocated CLI resolves the repository root incorrectly. Existing `scripts/tree.py` API with explicit repository root validates safely; leave infrastructure unchanged.
- Completed NLO Source remains limited to supplied material: lecture definitions/constructions and Moodle tests unavailable. Items retain the MFCQ/CQ2 limits; original barrier condition is closure of strict interior, unlike the profile's lost overbar.
