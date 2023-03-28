#####################################################
# Comparison of AB Test and Conversion of Bidding Methods
#####################################################

#####################################################
# Task 1: Preparing and Analyzing Data
#####################################################

# Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_1samp, shapiro, \
    levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, \
    f_oneway, kruskal

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

control_group = pd.read_excel("datasets/ab_testing.xlsx", usecols=[0, 1, 2, 3], sheet_name="Control Group")
test_group = pd.read_excel("datasets/ab_testing.xlsx", usecols=[0, 1, 2, 3], sheet_name="Test Group")


def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe().T)


check_df(control_group)
check_df(test_group)

# Step 3: After the analysis process, combine the control and test group data using the concat method.
df = pd.concat([control_group, test_group], axis=0, ignore_index=True)

df.head()

###################################################
# Task 2: Define A/B Test Hypothesis
###################################################

# Step 1: Define the hypothesis.
# H0 : M1 = M2 There is no difference between the purchasing averages of the two groups.
# H1 : M1!= M2 There is a difference between the purchase averages of the two groups.

# Step 2: Analyze the purchase (gain) averages for the control and test group
control_group["Purchase"].mean()
test_group["Purchase"].mean()

###################################################
# TASK 3: Performing Hypothesis Testing
###################################################

##################################################
# AB Testing (Independent Two Sample T Test)
##################################################

# Step 1: Check the assumptions before testing the hypothesis. These are Assumption of Normality and Homogeneity of Variance.

# Test separately whether the control and test groups comply with the normality assumption via the Purchase variable.

# H0: Normal distribution assumption is provided.
# H1:..not provided.

test_stat, pvalue = shapiro(control_group["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Test Stat = 0.9773, p-value = 0.5891
# p-value>0.05 H0 cannot be rejected

test_stat, pvalue = shapiro(test_group["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Test Stat = 0.9589, p-value = 0.1541
# p-value>0.05 H0 cannot be rejected

# When we applied the normality assumption test in both groups, the P value values showed that we provided the normality assumption.

#######################################
# Assumption of Variance Homogeneity
#######################################

# H0: Variances are Homogeneous
# H1: Variances Are Not Homogeneous
test_stat, pvalue = levene(test_group["Purchase"],
                           control_group["Purchase"].dropna())
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# Test Stat = 2.6393, p-value = 0.1083
# p-value>0.05 H0 cannot be rejected. Variances are homogeneously distributed.

# Step 2: Select the appropriate test according to the Normality Assumption and Variance Homogeneity results
# We will apply parametric test as it provides the assumption of Normality and Homogeneity of Variance.

test_stat, pvalue = ttest_ind(test_group["Purchase"],
                              control_group["Purchase"],
                              equal_var=True)  # We would do the Welch test if variance homogeneities were not provided (it would be equal_var=False)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
# Test Stat = 0.9416, p-value = 0.3493

# Step 3: Purchasing control and test groups, taking into account the p_value obtained as a result of the test
# Comment if there is a statistically significant difference between the # means.

# p-value>0.05 H0 cannot be rejected. It showed that there was no difference between the two groups.
# Observes that there is no statistically significant difference

############################################################
# TASK 4 : Analysis of Results
############################################################

# Step 1: Which test did you use, give reasons.
# We applied Shapiro test for normality assumption for Control and Test group. We also applied Levene test for variance homogeneity.
# We saw that the two test results provided the assumptions. Therefore, we applied parametric test. (Independent two-sample t-test)
# The p-value obtained after applying the Independent Two Sample T Test was examined. H0 hypothesis could not be rejected because our value was not less than 0.05.
# Even if there is a difference between the means of the control and test groups, it has been determined as a result of the analyzes that this is not statistically significant.

# Step 2: Advise the customer according to the test results you have obtained.
# In line with these results, it may be advisable not to suggest any changes to the customer and to preserve the current situation.
# However, it may be useful to do more analysis and perhaps perform different tests to give a more precise result.
# Or we can test again by increasing the number of samples.