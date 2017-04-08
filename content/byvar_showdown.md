Title: Variables by Group: Stata v R v Python
Date: 2017-03-18
Tags: data science, python, stata, r
Category: tech
Slug: byvar_showdown
Summary: Summary statistics by subgroups are a quick way to get a sense of the variation in your data. In this post, we look at how to generate simple summary stats of WRDS financial data by different groups using Stata, R, and Python.

# Overview

**The Challenge**: We want to create three different summary statistics by three different groups using Stata, R, and Python. Specifically, we want to calculate:

* `firm_div`: total dividends by firm
* `year_repo`: average share repurchases by year
* `sec_ni`: median net income by GICs Sector

**The Data**
We will be using select SP500 data from the CRSP-Compustat merged database found at WRDS. Our variables are:

* `year` is the year of the firm's financial data; our data ranges over the 10 year period from 2005-2014
* `permno` is a unique identifier for each firm
* `gsector` is the 2-digit GICS industrial sector assigned to each firm
* `repo` is the share repurchases made by each firm each year. This number is calculated using Compustat data following Kahle (2002)
* `totdiv_adj` is the CRSP total dividends adjusted for stock splits
* `ni` is the Compustat net income (loss) number

# Stata

For Stata, we will be relying on the `bysort` and the `egen` functions.

* `bysort` will sort the data and then carryout the function by whatever group is specified: permno, year, gsector.

* `egen` is a more powerful version of the standard `generate` function and allows to compute sums (using the `total` function), `mean`, and `median`.

```stata
* total dividends by firm
bysort permno : egen firm_div = total(totdiv_adj)

* average repurchases by year
bysort year : egen year_repo = mean(repo)

* median net income by GICs Sector
bysort gsector : egen sec_ni = median(ni)
```

# R

For R, we will be using the base `aggregate` function. The form it takes is `aggregate(x, group, fun)`. This will apply function `fun` to `x` by `group`. Our `x`s will be dividends, repurchases, and net income. Our `group`s will be firm, year, and GICs sector. And our `fun`s will be total, mean, and median

```r
# total dividends by firm
firm_div <- aggregate(sp500_dat$totdiv_adj, list(Firm=sp500_dat$permno), sum)

# average repurchases by year
year_repo <- aggregate(sp500_dat$repo, list(Year=sp500_dat$year), mean)

# median net income by GICs Sector
sec_ni <- aggregate(sp500_dat$ni, list(Sector=sp500_dat$gsector), median)
```

# Python

For Python, one of the easiest ways to compute summary statistics by groups is to use Pandas. To do so, first read in the data as a Pandas dataframe. Now we can use the following syntax: `data.groupby(group)[x].fun()`. Like the R example, our `x`s will be dividends, repurchases, and net income; our `group`s will be firm, year, and GICs sector; and our `fun`s will be total, mean, and median

```python
# read in data as a pandas dataframe
import pandas as pd
sp500_dat = pd.read_csv("sp500_dat.csv")

# total dividends by firm
sp500_dat.groupby('permno')['totdiv_adj'].sum()

# average repurchases by year
sp500_dat.groupby('year')['repo'].mean()

# median net income by GICs Sector
sp500_dat.groupby('gsector')['ni'].median()
```

# Conclusion

Given the simplicity of the functions, performance is not really issue. R is clearly the wordiest with the need to specify `data$var` for each variable. By leveraging Pandas, Python is the most succinct. The most "natural" would be Stata in that the code reads very much like how you would describe the variable (which is funny given Python's emphasis on things being "Pythonic").
