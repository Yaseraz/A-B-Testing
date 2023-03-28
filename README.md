# Comparing Conversion of Bidding Methods with A/B Testing
![Airline-AB-testing-in-action](https://user-images.githubusercontent.com/111612847/225813056-2a2d5239-f94c-4439-8979-ee2161ad58f5.jpg)



## Business Problem


Facebook recently introduced a new bidding type called "average bidding" as an alternative to the
existing "maximum bidding" bidding type. One of our clients, bombabomba.com, has decided to test this new
feature and wants to conduct an A/B test to determine whether average bidding brings more conversions than
maximum bidding. The A/B test has been running for 1 month and bombabomba.com now expects you to analyze
the results of this A/B test. The ultimate success metric for bombabomba.com is Purchase. Therefore,
the Purchase metric should be the focus of statistical tests.

## Data Set Story

This data set contains website information for a company, including the number of ads displayed and clicked,
as well as revenue information from these ads. There are two separate data sets, one for the control group
with Maximum Bidding applied, and one for the test group with Average Bidding applied, which are located on
separate pages of the ab_testing.xlsx excel file.

| Variable | Description |
| --- | --- |
| impression | Number of ad displays |
| Click | Number of clicks on the displayed ad |
| Purchase | Number of products purchased after clicking on the ad |
| Earning | Revenue generated after purchasing the products |



## Project Tasks

AB Testing (Independent Two-Sample T-Test)


1. Formulate hypotheses
2. Assumption check
- 1. Normality Assumption (shapiro)
- 2. Homogeneity of Variance (levene)
3. Application of the hypothesis test
- 1. Independent two-sample t-test if assumptions are met
- 2. Mann-Whitney U test if assumptions are not met
4. Interpret the results based on p-value
Note:
- If normality assumption is not met, go directly to step 2. If homogeneity of variance assumption is not
met, enter 1 in step 1 argument.
- Outlier analysis and correction before normality check can be useful
