# DSCI 552 HW6: Supervised, Semi-Supervised, and Unsupervised Learning

Part 1

The dataset in question is the UCI Breast Cancer Wisconsin (Diagnostic) Data Set, in which features are computed from a digitized image of a fine needle aspirate of a breast mass. They describe characteristics of the cell nuclei (radius, texture, area, etc.) present in the image. These are then labeled as malignant or benign.

First, a Monte-Carlo Simulation is performed by performing 30 iterations each of supervised, unsupervised, and semi-supervised learning, with train and test data chosen randomly.

Supervised learning is enacted by training an L1 penalized SVM to classify the data. 5x cross validation is used to choose the penalty parameter, and the data is normalized before training. All of the standard calculations (ROC, AUC, F1, accuracy, etc) are done on both the training and test data.

Semi-supervised learning is performed by selecting 50% of each of the positive and negative classes in the training set as the labeled data and the rest as the unlabeled data. An L1 penalized SVM is used to classify the labeled data. Then, the unlabeled data point that is farthest from the decision boundary of the SVM is labeled and added to the labeled data, and the SVM is retrained. The process is continued until all unlabeled data are used.

Unsupervised learning is performed by running k-means algorithm on the whole data set, ignoring the labels of the data, with k=2. The clusters are classified via majority polling, and these labels are compared to the true labels to determine the accuracy of the unsupervised training algorithm.

Finally, Spectral Clustering (based on kernels) is performed. An RBF kernel with gamma=1 is used.

To nobody’s surprise, supervised learning is more accurate than semi or unsupervised learning, although those performed better than I expected.
