### Project Overview

 Till now I have learned how to solve the linear regression and regularization problem. Now in this project, I am  going to predict the Insurance claim using logistic regression. This dataset contains information on the insurance claim. Each observation is different policyholder with various features like the age of the person, the gender of the policyholder, body mass index, providing an understanding of the body, number of children of the policyholder, smoking state of the policyholder and individual medical costs billed by health insurance.


### Learnings from the project

 After completing this project, I have a better understanding of how to build a logistic regression model. In this project, I have applied the following concepts.

Train-test split
Correlation between the features
Logistic Regression
Auc score
Roc AUC plot


### Approach taken to solve the problem

 I first did the data preprocessing like detecting the outliers if any and finding out the correlation between various features. IF there is high correlation then either we drop that feature or try to make a new features from the two or more features. Once the data is cleaned I applied the Logistics Regression model with Grid Search CV and plotted the Roc Auc curve to check its accuracy.


### Challenges faced

 As there are less features, even if there is correlation it is difficult to dtop them, because we lose essential data. Also I sturggled a bit in plotting the roc auc curve. I took the help of various resources from the web to plot it.


### Additional pointers

 Yes, We need to thorughly clean the data before applying the model. Splitting the data into train and test in an optimal way is very important especially if we have less data in our hand.


