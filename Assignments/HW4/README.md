# DSCI 552 HW4: The LASSO and Boosting for Regression & Tree-Based Methods
The dataset in question is the UCI Communities and Crime Data Set, which combines socio-economic data from the 1990 US Census, law enforcement data from 1990, and crime data from 1995. The features describe the community (race, age, household size, etc.) and are labeled with a value for per capita violent crimes.

First, missing values are imputed with a strategy of ‘mean.’  Non-predictive features are filtered out of the dataset. A correlation matrix for the features of the dataset is plotted, and the coefficient of variation for each feature is calculated.

Then, a linear model is fit to the training set using least squares, and test error is reported as calculated by both the statsmodels and sklearn packages.

A ridge regression model is fit on the training set, with lambda chosen by cross-validation. A LASSO model is fit on the training set, with alpha chosen by cross validation. It’s found that un-standardized samples provide a lower mean square error than do standardized samples.

Principal component regression, a technique based on principal component analysis, is used to fit a model on the training set, with the number of principal components chosen by cross-validation.

A boosting tree is fit to the data using L1 penalized regression at each node to build a multivariate regression tree. The regularization term is determined using cross-validation.

Next, a new data set is introduced: APS failure at Scania Trucks dataset. It consists of data collected from heavy Scania trucks in everyday usage. The system in focus is the air pressure system, and the classified feature is whether failure in the truck is a part of the air pressure system or not. The data being used to classify the failure are proprietary attributes of the truck, as measured by systems within the truck.

Many of the same initial investigative techniques are performed on this dataset as were performed in part 1 above.

A random forest classifier is trained on the data set, first without compensating for class imbalance in the data set. A confusion matrix and other measures of the success of the classifier are reported.

Next, I compensate for class imbalance in my random forest, and noticed an improvement in the precision of the classifier trained.

I then fail to complete the assignment in a fit of exhaustion.
