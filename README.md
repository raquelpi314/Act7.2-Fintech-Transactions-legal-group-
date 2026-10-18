# Act7.2-Fintech-Transactions-legal-group-
Activity 7.2 introducing LLM to make predictions on our issue, in this case regarding the origin category of transactions. The app uses a Logistic Regression model to classify transactions. May enter transaction info through a HTML and get a prediction and the estimated prob.
The project uses three input variables:
  transaction_amount: Amount involved in the transaction
  sender_type: Type of sender
  recurrence: the recurrence value of the transaction
It predicts origin_category presented by numbers 1-5
We used a .joblib file and it receives the transaction information, predicts an origin category and calculates the prob associated with the prediction

The app developed with Python and Flask, can be accessed through a HTML 
Website: https://raquelpmf.pythonanywhere.com/
API included that allows other apps to request predictions

The project requires the elements listed in requirements.txt. 

Limitations: Model based on model financial transactions' data and is meant for educational purposes only. Predictions not validated for real-world decisions or circumstances. (university activity for fintech).
  
Training: 
Create a python code for a multinomial logistic regression using a three columns data frame, for Monkeypr, a RegTech app that helps users aged 16–25 in Spain justify the origin of funds received on their bank accounts. Each row is an incoming transaction (credit) on a linked bank account. First column transaction amount as a continuous variable in euros, second column sender type as a categorical variable (company, individual, crypto exchange, marketplace), third column recurrence as a discrete variable (number of similar credits from the same sender in the last 6 months). Name all variables using Python style, small cap with underscore for spaces. Target variable origin category with 5 classes, as confirmed by the user in the app: 1 salary/scholarship, 2 family gift, 3 resale/marketplace, 4 crypto, 5 other. Generate all variables randomly using numpy, making the target depend on sender type and recurrence. Set the seed so that all variables always get the same value. Save the data to an excel named fintech.xlsx without index. One-hot encode the categorical variable, split the data into train and test. Validate the model using classification report in both train and test data. Dump the model into a file using joblib, call the file fintech.joblib.
