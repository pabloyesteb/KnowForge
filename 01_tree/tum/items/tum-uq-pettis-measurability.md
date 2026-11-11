---
id: tum-uq-pettis-measurability
source: tum-numuq
parent: uq-probability
title: Strong measurability and the Pettis criterion
type: theorem
caption: "Connects weak scalar observations and almost-separable range to Banach-valued measurable approximation."
---

# Strong measurability and the Pettis criterion

For a Banach space \(W\), Borel measurability uses \(\mathcal B(W)\), while cylindrical measurability tests inverse images through every continuous linear functional \(\ell\in W'\). Weak measurability of \(X\) means each scalar \(\ell(X)\) is measurable. Strong or Bochner measurability means almost-sure norm convergence of countably valued measurable approximations (equivalently suitable finite simple approximations). An almost-surely separable range means all values outside one null set lie in some separable subset of \(W\).

Pettis' theorem characterizes strong measurability by weak measurability plus almost-surely separable range. When \(W\) is separable the range condition is automatic, strong and weak measurability agree, and \(\operatorname{Cyl}(W)=\mathcal B(W)\). Strongly measurable variables form a vector space, which allows function-space random approximation and integration.

In general \(\operatorname{Cyl}(W)\subseteq\mathcal B(W)\), because every continuous linear functional is Borel measurable. Consequently a Borel-measurable variable is always cylindrically measurable; Remark 2.42(ii) states the opposite implication failure and is incorrect as written. The important limitation is that weak/cylindrical measurability without separable range need not imply strong measurability. In nonseparable spaces, Borel issues for sums also require care with product measurability; strong measurability supplies the stable linear framework used here. The source states Pettis' equivalence with an external proof reference.

## Source references

Archive: `00_sources/raw/tum/archives/NUMUQ (SoSe24)_20261012_1548.zip`.
- `Lecture Notes/Lecture Notes (Updated on 15.07.24)`, §2.3, Definitions 2.40–2.47, Theorem 2.48 and Remark 2.49, pp. 9–10.
- `Lecture Topics and Slides/Lecture 03 (23.04.24)`, physical pp. 10–14 (printed 24–28), definitions, literal cylindrical/Borel caution and Pettis statement.
