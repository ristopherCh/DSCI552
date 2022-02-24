# DSCI 552 HW6: Active Learning Using Support Vector Machines

Part 2

(see homework-6-chrishanson folder for Part 1: Supervised, Semi-Supervised, and Unsupervised Learning)

The dataset in question is the UCI banknote authentication data set, in which data were extracted from images that were taken from genuine and forged banknote-like specimens, describing the variance, skewness, and curtosis of the wavelet transformed image, the entropy of the image, and the class of the image.

A SVM was trained with a pool of (at first just) 10 randomly selected data points from the training set using linear kernel and L1 penalty. Then, this process was repeated by adding 10 other randomly selected data points, until all 900 points were used. This is an example of passive learning.

Similarly, a SVM was trained with a pool of (at first just, again) 10 randomly selected data points from the training set using linear kernel and L1 penalty. Then, the 10 closest data points in the training set to the hyperplane of the SVM were added to the pool, and a new SVM was trained, repeating this process until all 900 points were used. This is active learning.

Learning curves of the passive and active learning processes are plotted together to compare the superiority of active learning to passive learning.
