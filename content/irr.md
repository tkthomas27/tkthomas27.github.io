Title: A Note on Internal Rate of Return
Date: 2017-01-24
Tags: finance, business, accounting
Category: tech
Slug: irr-note
Summary: Despite its many controversies, the IRR is a fundamental tool in financial analysis. In this note, we explore the basic formulation of IRR, what this formula looks like with multiple streams of cash, and how to solve for IRR.

# Time Value of Money

The internal rate of return (IRR) is simply the rate *r* that equates the future value of money to the present value. The actually economic interpretation of this value is highly contested.

Before getting into the IRR, lets establish the basic axioms of the time value of money that depict the relationship between present value (PV), future value (FV), and the rate of return *r* over the total number of periods ($T$):

$$
\begin{equation}
PV = \frac{FV}{(1+r)^T}
\label{basic_pv}
\end{equation}
$$

$$
\begin{equation}
FV = PV(1+r)^T
\label{basic_fv}
\end{equation}
$$

In words, Eq. $\ref{basic_pv}$ tells us that PV is equal to some FV discounted at a discount rate across the the total time period, where *T* represents the total number of time periods. The core idea is that cash now is more valuable than cash later. Therefore if I were to lend you money, I would charge you interest to make up for not having money now. This is why we compound our PV to get a FV. We simply reverse this processing by discounting to go from FV back to PV. The focus on our exposition will be on *r*, the rate of return that is used to discount/compound.

We can rearrange Eq. $\ref{basic_pv}$ into Eq. $\ref{basic_irr}$ to see the relationship between the IRR and FV and PV. Eq. $\ref{basic_irr}$ will be our final step in computing the IRR.

$$
\begin{equation}
r = \sqrt[T]{\frac{FV}{PV}}-1
\label{basic_irr}
\end{equation}
$$

# Streams of Cash

There are plenty of investments that take the form of a single payment in (a negative cash flow out of your pocketbook) followed by a single payment out (a positive cash flow into your pocketbook) after a some period of time. This, however, is a trivial example to be solved and I will instead focus on investments that take the form of multiple cashflows over several periods.

Because we are dealing with a stream of cash flows and not a single value, FV needs to be rewritten. Consider a cash flow at t=1, if the final future period is 60 periods from t=1, then we need to compute the future value of that cash flow for for 60-1 periods from that time. We can rewrite the PV and the FV of a stream of cash flows as

$$
\begin{equation}
PV = \sum_{t=1}^{t=T}\frac{CF_t}{(1+r)^{t}}
\label{pv_cf}
\end{equation}
$$

$$
\begin{equation}
FV = \sum_{t=1}^{t=T}CF_t(1+r)^{T-t}
\label{fv_cf}
\end{equation}
$$

Substituting Eq. $\ref{fv_cf}$ into Eq. $\ref{basic_pv}$ and expanding we get:

$$
\begin{equation}
PV = \frac{\sum_{t=1}^{t=T}CF_t(1+r)^{T-t}}{(1+r)^T} = \frac{CF_1(1+r)^{T-1}}{(1+r)^T} + \frac{CF_2(1+r)^{T-2}}{(1+r)^T} + ... + \frac{CF_T(1+r)^{T-T}}{(1+r)^T}
\label{pv_fv}
\end{equation}
$$

We could also modify Eq. $\ref{pv_fv}$ to read:

$$
\begin{equation}
\mathit{CF}_{t=0} = \frac{\sum_{t=1}^{t=T}CF_t(1+r)^{T-t} + \mathit{CF}_{t=T}}{(1+r)^T}
\end{equation}
$$

# Solving for Internal Rate of Return

Our primary goal is to find the *r* that solves Eq. $\ref{pv_fv}$. The most common method to do so is to treat this as a polynomial root finding exercise. For clarity, we can trivially rewrite Eq. $\ref{pv_cf}$ as

$$
\begin{equation}
PV = CF_1 (1+r)^{-1} + CF_2 (1+r)^{-2} + ... + CF_n (1+r)^{-n}
\end{equation}
$$

To find the root of this equation we need to set it to zero.

$$
\begin{equation}
0 = -PV + CF_1 (1+r)^{-1} + CF_2 (1+r)^{-2} + ... + CF_n (1+r)^{-n}
\end{equation}
$$

The root *r* that satisfies this equation is the Internal Rate of Return (IRR). There are several methods of finding this root.

## Educated Guess and Interpolation

One way of finding it is to plug and chug using the `npv` function in Excel and see which rate gives us a negative value. This would not be super precise but would give you an educated guess and allow you to use the secant method to determine a more precise IRR.

## Root Finding Algorithm
Similarly we use the `uniroot` function of R. first specify the function then use `uniroot` on it. `uniroot` uses the golden section ratio method in combination with parabolic interpolation to efficiently guess the root that satisfies the function along a specified interval.


<!-- explain excel/secant method -->
<!-- r code  for uniroot -->
<!-- latex appendix for formulas -->
