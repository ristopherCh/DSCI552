# DSCI552
HW1: Classification
The dataset in question describes six biomechanical attributes describing the shape and orientation of the pelvis and lumbar spine of a number of individuals. Each individual is also labeled as having a “normal” bill of health, or an “abnormal” classification, which means either a disk hernia, spondylolisthesis, or any other mechanical abnormality.

The dataset was initially checked by viewing a scatterplot of all independent variables and a boxplot of the range of each variable using the Seaborn package.

The dataset was split up into training and test sets.

Then, a k-nearest neighbors classifier was implemented using the sklearn.neighbors.KNeighborsClassifier package by first training on the training data, then fitting the model to the test data and scoring the classifier. This algorithm was run through a scan of k neighbors from k = 208 to k = 1, and the score of each run was plotted to discover what the most effective parameter is.

Using the most effective value for the K neighbors parameter (k = 4) I create a confusion matrix, calculate the true positives, the precision and the F1 score. I then proceed to fail to create a Learning curve (so, please disregard (c) iii).

I then change the way the K nearest neighbors algorithm calculates the nearest neighbor by changing the calculation from Euclidean metric to Minkowski, Manhattan, Chebyshev, Mahalanobis, and others.

I also attempt KNN using a weighted decision instead of majority polling, where the distance from the point in question is considered.
