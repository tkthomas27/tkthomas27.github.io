Title: Chain of Thought: Norm
Date: 2017-02-08
Tags: linear-algebra, regression
Category: tech
Slug: cot-norm
Summary: Chain of Thought: starting with regularization techniques of ridge regression and lasso we move to what is a norm while covering optimization, Moore-Penrose Pseudoinverse matrix, and Lagrangian multiplier.


# Ridge Regression and the Lasso

While working through [Introduction to Statistical Learning](http://timothykylethomas.me/islr.html#islr) (ISLR), I became intrigued by the lecture on [subset selection](https://lagunita.stanford.edu/c4x/HumanitiesScience/StatLearning/asset/model_selection.pdf). Subset selection is the process of reducing linear models to only those features (viz. independent variables) that are most relevant. Old standbys in this field are piecewise forward and backward selection. The hot topic now, however, are the shrinkage methods ridge regression and lasso.

This two methods are popular now because of the explosion of higher dimensional data (i.e., where there are more features than observations). Piecewise selection frequently becomes intractable where there are many features. Shrinkage methods solve this method by building in a penalty to OLS estimation that automatically pushes coefficients to zero (you should read the above notes on subset selection for more details, here we are just plowing ahead with my chain of thought). The point of having less features and lower coefficients is the reduction in the overall variance of the model.

Let's briefly overview OLS estimation and the changes the ridge and lasso make. With a vector $b$ of responses and a matrix $A$ of features, we seek to find the vector $x$ that makes $Ax = b$.[^1] Using standard terms for OLS, $b$ is the dependent variable $y$, $A$ is our observations $X$, and $x$ is the vector of $\beta$s giving use the formula $X \beta = y$ (note that the order of $X$ and $\beta$ is important). The simplest way to express is from a geometric perspective: we want to choose a $\beta$ vector that minimizes the distance between $X$ and $y$ (the bars $||$ tell us that this is a  euclidean norm --- a fancy way of saying a distance):

$$\hat{\beta} = \min_{\beta} ||y - X\beta||. $$

The OLS way to do this is to minimize the sum of the squared residuals (RSS). There are many ways to express the minimization of RSS (a la the geometric version above), but here we will use the version presented in ISLR to remain consistent.

First, the RSS we seek to minimize is:

$$ RSS = \sum_{i=1}^n (y_i - \beta_0 - \sum_{j=1}^p \beta_j x_{ij})^2 .$$

This is probably the most complicated way to present OLS, but in doing so, it quite exactly tells you what is happening.

For ridge regression we add a shrinkage penalty with tuning parameter $\lambda$ to the criterion:

$$ RSS + \lambda \sum_{j=1}^p \beta^2_j .$$

Now, instead of just trying to minimize RSS, we are trying to minimize a larger number: RSS plus the shrinkage penalty. This will force the model to prefer $\beta$s that are smaller and closer to zero thus helping to reduce the variance of the model (you will often end up with very small coefficients and not ones exactly equal to zero).

The $\sum \beta^2$ part of the penalty is also known as the $\ell_2$ penalty and can be written in its geometric form as $||\beta|\vert_2$.

A newer sibling of the ridge regression that is becoming increasingly more popular is the lasso:

$$ RSS + \lambda \sum_{j=1}^p |\beta_j |$$

By recasting the penalty as an $\ell_1$ norm (alternatively $||\beta|\vert_1$), the minimization can take coefficients to zero (not just close to zero as in ridge regression). The result is feature selection: only those coefficients that are non-zero are kept. The disadvantage of the lasso is that it requires computationally intensive numerical searching algorithms.

So the difference between ridge and lasso is the nature of this penalty: ridge uses the $\ell_2$ norm while the lasso uses the $\ell_1$ norm (the $\LaTeX$ code for $\ell$ is `\ell`). So what are these norms?



# Norm

When researching norms --- particularly in the context of optimization problems like those used in subset selection --- I came across this helpful [blog post](https://rorasa.wordpress.com/2012/05/13/l0-norm-l1-norm-l2-norm-l-infinity-norm/).

There is a lot to unpack from this post and many avenues of thoughts. One could easily start exploring the nature of Euclidean space and its alternatives (i.e., [hyperbolic space](https://en.wikipedia.org/wiki/Hyperbolic_space)) and the variety of [norms](https://en.wikipedia.org/wiki/Norm_(mathematics)). However, I decided to keep to the $\ell_1$ and $\ell_2$ norms, their optimization, and their application to the statistical issues presented above.

A simple way to think of a norm is a distance or size in a p-dimensional space. As the author of the blog writes, the general form of a norm is:

$$||x|\vert_p = \sqrt[p]{\sum_i |x_i|^p} $$

The $\ell_1$ norm ends up simply being the sum of the absolute value of each element, while the $\ell_2$ norm is the square root of the sum of the squared elements.

You may remember from grade school the formula for the distance ($d$) between two points on the 2-dimensional plane $(x_1,y_2)$ and $(x_2,y_2)$:

$$ d = \sqrt{(x_1-x_2)^2 + (y_1 - y_2)^2} $$

Which we can rewrite as:

$$|| y - x|\vert_2 = \sqrt{\sum (y - x)^2} $$

Does the above remind you of our minimization problem $\hat{\beta} = \min_{\beta} ||y - X\beta||$ or the RSS formula? It should because, as stated above, the OLS optimization is simply trying to find the $\beta$s that minimizes the distance between $X$ and $y$. In other words, OLS wants the vector of $\beta$s that makes the $\ell_2$ norm $||y - X\beta||$ the smallest. OLS is just a more multi-faceted version of something you have been doing all along.

# Norm Optimization

To tie it together: regular OLS is simply minimizing an $\ell_2$ norm, ridge regression is minimizing an $\ell_2$ norm plus an $\ell_2$ penalty, and the lasso is minimizing an $\ell_2$ norm plus an $\ell_1$ norm.

Minimizing the $\ell_1$ norm (or any optimization problem involving the $\ell_1$ norm) requires the use of various numerical analysis [algorithms](https://www.cs.ubc.ca/~schmidtm/Documents/2005_Notes_Lasso.pdf). These were computationally unfeasible until recent developments in computing power.

Minimizing the $\ell_2$ norm is a more simple prospect. The author of the blog presents a way of doing this involving Lagrangian multipliers that ultimately dumps us off in OLS land. First, note that our objective function is

$$ \min ||x|\vert_2 \text{ s.t. } Ax = b  $$

The Lagrangian for this is:

$$ ||x||^2_2 + \lambda' (Ax - b)$$

After solving[^2], the minimized estimate of x is $A' (AA')^{-1} b$. The 'a-ha' moment for me, was recognizing that this is in fact the same as $\hat{\beta} = (X'X)^{-1}X'y$. The $(X'X)^{-1}X'$ is known as the [Moore-Penrose Pseudoinverse Matrix](https://en.wikipedia.org/wiki/Moore–Penrose_pseudoinverse).





[^1]: [Tikhonov Regularization](https://en.wikipedia.org/wiki/Tikhonov_regularization)
[^2]: The mechanics of this process in the context of OLS (called constrained least squares) can be seen [here](http://stanford.edu/class/ee103/lectures/constrained-least-squares/constrained-least-squares_slides.pdf)
