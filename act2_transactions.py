from flask import Flask, render_template, request, jsonify
from joblib import load
import pandas as pd

app = Flask(__name__)

model = load('/home/Raquelpmf/mysite/fintech (2).joblib')
model.multi_class = 'auto'

def predict_transaction(transaction_amount, sender_type, recurrence):

    data = {
        'transaction_amount': [float(transaction_amount)],
        'recurrence': [int(recurrence)],
        'sender_type_company': [int(sender_type == 'company')],
        'sender_type_crypto_exchange': [int(sender_type == 'crypto_exchange')],
        'sender_type_individual': [int(sender_type == 'individual')],
        'sender_type_marketplace': [int(sender_type == 'marketplace')]
    }

    data_df = pd.DataFrame(data)

    X = data_df[[
        'transaction_amount',
        'recurrence',
        'sender_type_company',
        'sender_type_crypto_exchange',
        'sender_type_individual',
        'sender_type_marketplace'
    ]]

    prediction = model.predict(X)[0]
    probabilities = model.predict_proba(X)[0]

    return {
        'prediction': int(prediction),
        'probability': float(max(probabilities))
    }



@app.route("/")
def index():
    return render_template("act2_transactions.html")


@app.route("/transaction/predict", methods=["POST"])
def transaction_prediction():

    try:
        result = predict_transaction(
            request.form['transaction_amount'],
            request.form['sender_type'],
            request.form['recurrence']
        )

        return render_template("act2_transactions.html", result=result)

    except (ValueError, KeyError) as error:
        return render_template(
            "act2_transactions.html", error=str(error)
        ), 400


@app.route("/api/predict", methods=["POST"])
def api_prediction():

    try:
        data = request.get_json()

        result = predict_transaction(
            data['transaction_amount'],
            data['sender_type'],
            data['recurrence']
        )

        return jsonify(result)

    except (ValueError, KeyError, TypeError) as error:
        return jsonify({'error': str(error)}), 400


if __name__ == "__main__":
    app.run(debug=False)
