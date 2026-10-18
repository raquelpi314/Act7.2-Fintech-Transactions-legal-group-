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
  
