# DSCI 552 HW2: Linear and Multiple Regression

The dataset for this assignment is drawn from 6 years of the operation of a combined cycle power plant, describing the temperature, ambient pressure, relative humidity, and exhaust vacuum features of the plant. These indicators can be used to describe the net hourly electrical energy output of the plant using linear regression.

First the dataset is loaded and explored. Scatterplots are created to view any possible relationships between the variables, and statistical calculations are performed on each feature.

A linear regression is fit using each individual predictor by using the statsmodels.regression.linear_model.OLS package, and regression results are displayed.

A multiple regression model is created to predict the response using all predictors. Univariate and multiple regression coefficients are compared.

The possibility of nonlinear responses is tested for each feature, and all of the features prove to have some nonlinear response, in the X^2 and/or X^3 values.

A test is performed to determine whether there is evidence of association of interactions of predictors with the response. Many predictor interactions prove to be statistically significant.

Using what was learned about nonlinear and associated interactions, an optimized multiple regression is performed using the significant nonlinear and associated features, with insignificant variables removed as determined by their p-values.

Finally, k nearest neighbors regression is run on the dataset and is compared to linear regression. In this case, KNN was found to be slightly more accurate.
