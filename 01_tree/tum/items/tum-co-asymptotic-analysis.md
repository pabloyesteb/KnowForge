---
id: tum-co-asymptotic-analysis
source: tum-combinatorial-optimization
parent: co-foundations
title: Asymptotic bounds and input-sensitive running-time analysis
type: method
caption: "Uses eventual inequalities, encoding size and tight best/worst-case examples to compare algorithmic costs."
---

# Asymptotic bounds and input-sensitive running-time analysis

For nonnegative functions, \(f=O(g)\) means \(f(x)\le Cg(x)\) beyond some threshold with fixed \(C>0\); \(f=\Omega(g)\) reverses the inequality, and \(f=\Theta(g)\) requires both. Ratios establish or disprove these relations. For \(f(n)=n^2+10n\) and \(g(n)=n^3/3+n\), \(f/g\to0\), so \(f=O(g)\) and not \(\Omega(g)\). Their logarithms both have order \(\log n\), even though the polynomials have different degrees. Similarly \(3^n=\Omega(2^n)\) but not \(O(2^n)\), while \(\log(3^n)\) and \(\log(2^n)\) are both \(\Theta(n)\). The solution's nested logarithm in its polynomial-log comparison is a typographical error; leading logarithmic terms are \(2\log n+o(1)\) and \(3\log n-\log3+o(1)\).

Count elementary operations such as arithmetic, comparisons and assignments, and state the size parameter. Binary encoding of an integer \(a\) uses \(O(1+\log(1+|a|))\) bits, including sign; numeric magnitude is not its bit length. A bound polynomial in a large numeric value need not be polynomial in the encoded input length. Growth rates explain why a constant-factor hardware speedup has limited benefit for exponential or factorial algorithms.

The sheet's insertion-sort pseudocode inserts \(L[j]\) into the already sorted prefix by shifting larger entries. It maps \([4,7,9,2,1]\) to \([1,2,4,7,9]\). In decreasing order, iteration \(j\) shifts \(j-1\) entries, for \(\sum_{j=2}^n(j-1)=\Theta(n^2)\) work, proving a tight worst-case bound rather than merely an upper bound. Already sorted input performs no shifts but still traverses the outer loop and checks each insertion, giving \(\Theta(n)\) best-case time. The official solution swaps the names of its loops in the best-case explanation; the outer loop still executes \(n-1\) times.

## Source references

Archive: `00_sources/raw/tum/archives/Combinatorial O 950730014 (S24)_20261012_1548.zip`.
- `Lecture Notes/lecture notes.pdf`, §1.1, pp. 6–7, Definition 1.10, encoding and running-time comparison tables.
- `Lecture Notes/class notes for 19 April.pdf`, printed slides 22–25 (physical pp. 35–38).
- `Problem Sheets/Exercise Sheet 1/exercise_sheet_1.pdf`, Exercises 1–2, p. 1; `Problem Sheets/Exercise Sheet 1 - solutions/exercise_sheet_1 - sol.pdf`, corresponding solutions, pp. 1–2.
