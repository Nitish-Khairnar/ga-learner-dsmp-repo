### Project Overview

 We have a housing dataset problem from Melbourne City.Here each observation is a different house attribute with various features, like the number of properties that exist in the suburb, land size, building size, governing council for the area, real estate agent, price of the house, etc. Like any other housing dataset problem, here too we have to predict the saleprice of the house.


### Learnings from the project

 I got the learn Train-Test split, Correlation between features, Linear and polynomial regression, the types of Regularization i.e. Lasso and Ridge and the evaluation matrics R2


### Approach taken to solve the problem

 First thing first was to look at the dataset and its features. Lot of them were in Textual form, so they need to be encoded first. Then I splitted the data in test and training. After splitting I found out the correlation between various features. I predicted the housing price using Linear Regression, only to find out the accuracy not upto the mark.
Then I applied Lasso, ridge and cross validation techniques to improve the accuracy, but that didnt help here in this case.
So finally I applied the Polynomial Regressor to generate the second degree polynomial features and the accuracy increased to a great extent.


### Challenges faced

 Intuitively I was able to get the problem statement, but to code it down was little tricky for my side. So I underwent a lot of coding practice, solved wuite a number of assignments and then I found it relatively easy to code.


### Additional pointers

 Before directly assuming any concept, we need to check it. As I was under this impression that regularization with L1 or L2 helps, but it was nit true for this data set. So we need to look back at the concept often and get our ideas clarified rather than just assuming from our side.


