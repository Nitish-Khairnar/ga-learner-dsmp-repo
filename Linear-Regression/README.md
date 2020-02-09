### Project Overview

 This project is about the world famous game set company 'LEGO'.We have to predict the price of the new lego product set. We have the dataset directly from the official website.Each observation is a different lego set with various features like how many pieces in the set, rating for the set, number of reviews per set etc. Here our aim is to build a linear regression model to predict the price of a set.


### Learnings from the project

 I got a better understanding of how to build the Linear Regression model. With the follwoing concept got even more clear, namely how to split the data in Training and Testing, what shall be the ratio.
Finding out the correlation between the features with the target variable and removing those which are highly correlated. I also learnt about the evaluation metrics like the MSE and R-square


### Approach taken to solve the problem

 Firstly I loaded the dataset on our learning platform, and then decided in what ratio to split the given data into training and testing.
I notices that few columns were categorical in nature, they needed to encoded first. Also I realised that the age column was mentioned in range format and not as a specific number, so even that had to be converted before building our model


### Challenges faced

 Encoding was new concept for me, so I had to learn it and also deciding which one to opt for, be it one hot ro label encoding. Then after finding out the accuracy, we had to cross verify whether it correct or not, so Cross validation technique had also to be learnt.


### Additional pointers

 Yes, I belive we should not get diverted looking at the huge dataset. Also the framework for every data science problem differs, there is always something common, and that is Data Exploration. We need to look for any outliers, if encoding is required, missing values have to be dropped or imputed, findout out the correlation. This all are the basic steps and we must adhere to the guidelines before jumping on our models.


