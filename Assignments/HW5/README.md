# DSCI 552 HW5: Multi-Class and Multi-Label Classification Using Support Vector Machines, and K-Means Clustering on a Multi-Class and Multi-Label Data Set

The dataset in question for this assignment is the UCI Anuran Calls (MFCCs) Data Set, which contains acoustic features extracted from syllables of anuran (frogs) calls, including the family, the genus, and the species labels. It is a multilabel dataset, containing 60 audio records belonging to 4 different families, 8 genus, and 10 species.

First, a support vector machine (SVM) classifier is trained on each of the labels (binary relevance). 10 fold cross validation is used to determine the weight of the SVM penalty and the with of the Gaussian Kernel. This is then repeated using L1 penalized SVMs with standardized attributes. Finally, it is repeated using SMOTE to remedy class imbalance.

Next, a Monte-Carlo simulation is performed by repeating the k-means clustering procedure 50 times, and reporting the average and STD of the 50 Hamming Distances calculated.

Finally, the average Hamming score and Hamming loss is calculated between the true labels and the majority label triplet (family, genus, species) assigned by the k means clustering.
