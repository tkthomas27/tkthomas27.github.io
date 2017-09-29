Title: Blog Log
Date: 2017-09-22
Tags: anything
Category: tech, not-tech
Slug: log
Summary: A streaming repo of consciousness


---
September 28, 2017

When interpreting regression results it is valuable to remember that the *ceteris peribus* interpretation is due to the coefficients being partial derivatives. A derivative is simply defined as

$$
\frac{\Delta y}{\Delta x} = \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}
$$

In words, if $y=f(x)$ the change in y ($\Delta y$) per change in x ($\Delta x$) is how much how much a function changes ($f(x_0 + \Delta x) - f(x_0)$) given a change in x ($\Delta x$). Hence we get the standard derivative notation:

$$
\frac{dy}{dx} \equiv f'(x) \equiv \lim_{\Delta x \rightarrow 0} \frac{\Delta y}{\Delta x}
$$

In both simple and multiple regression, we interpret $\beta$s in similar ways: a unit change in $x$ results in a $\beta$ amount of change in $y$. But how can we ignore other coefficients in multiple regression? Because they are partial derivatives where one variable is held constant while the other is allowed to vary. For example, the derivative of $f(x,y)$ while holding $x$ constant can be written as

$$
f_x'(y) = \frac{\partial f(x,y)}{\partial x}
$$

*Napoleon: A Life*: punishment should be infrequent but severe; "truth is so precious she should be surrounded by a bodyguard of lies"

*Philosopher's Toolkit*: Richard Dawkins' "selfish gene" is an example of a failed intuition pump---doesn't mean at all what people think it does (he is referring to how genes optimize locally instead of globally for the organism)

---
September 22, 2017

*Napoleon: A Life*: notorious micromanager; emo youth---wrote excessively Romantic letters on suicide and his 1st wife Josephine; lived frugally when younger---only ate once a day; more concerned by mulberry nursery than revolution; "We have them now"

[Petrozavodsk Phenomenon](http://www.wikiwand.com/en/Petrozavodsk_phenomenon): an unusual and unexplained atmospheric phenomenon. Never heard of this until recently

[Pythagorean Expectation](http://www.wikiwand.com/en/Pythagorean_expectation): way of computing expected wins. Pro football uses exponent of 2.67, [Redditor](https://www.reddit.com/r/nfl/comments/6rkmbv/introduction_to_pythagorean_expectation/) says this doesn't make sense due to [VC Dimension issues](http://www.wikiwand.com/en/VC_dimension). Some [more](https://www.quora.com/Explain-VC-dimension-and-shattering-in-lucid-Way) on VC dimensions.

IgNobel Award Winner: Elisabeth Oberzaucher and Karl Grammer, for trying to use mathematical techniques to determine whether and how Moulay Ismael the Bloodthirsty, the Sharifian Emperor of Morocco, managed, during the years from 1697 through 1727, to father 888 children

---
September 21, 2017

L1 norm for accuracy---less bias; L2 norm gives parsimony---less variance <|||> New favorite military title: 1st Sea Lord <|||> Ada Lovelace thought of using punch cards after being inspired by weaving loom <|||> 37% optimal stopping problems and Secretary problem

Jeremy Bentham referred to natural rights as "nonsense on stilts"---similar sentiment from other Enlightenment thinkers <|||> John Adams thought the idea that "all mean are created equal" was absurd

[Strassen’s Subcubic Matrix Multiplication Algorithm](http://www.wikiwand.com/en/Strassen_algorithm): a divide-conquer-combine strategy that is completely non-obvious but hugely important because it saves on recursive calls.
