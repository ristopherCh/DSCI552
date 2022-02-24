# DSCI 552 HW3: Time Series Classification with Logistic Regression

The dataset in question is a set of time series representing instances of humans performing certain activities: bending, cycling, lying, sitting, standing, and walking. The goal of this assignment is to use this data to train an classifier algorithm to determine which of these activities is being performed in an unlabeled time series.

First, the features that will be used to train and test the algorithm are extracted from the time series: minimum, maximum, mean, median, STD, quartiles.

A 90% bootstrap confidence interval for the standard deviation of each feature is calculated, and from these results it’s decided that the algorithm will be trained only on the mean, median, and STD features.

The first algorithm to be trained is a binary logistic regression classifier which will differentiate between bending and all other activities. 5 fold cross validation is used to determine the most precise classifier available, when comparing classifiers trained on datasets that are either one full length dataset or broken up into many smaller time series of equal length.

At this point, I struggle in an infinite void of confusion. Days pass; perhaps years pass. I forget my name. Presumably, I then find the correct method. When I retire I will go back through this code and smile.

The ROC curve and the area under the ROC curve (AUC) are calculated for both the train and test data.

L1 penalized logistic regression is performed and the method of using L1 regularization for variable selection is found to perform better than selection using p-values.

Finally, an L1-penalized multinomial regression model is built to classify all activities in the training set.
