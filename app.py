from flask import Flask, request, request, render_template, jsonify
from src.pipelines.prediction_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_churn():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        data = CustomData(
            AccountWeeks = float(request.form.get('AccountWeeks')),
            ContractRenewal = request.form.get('ContractRenewal'),
            DataPlan = request.form.get('DataPlan'),
            DataUsage = float(request.form.get('DataUsage')),
            CustServCalls = request.form.get('CustServCalls'),
            DayMins = float(request.form.get('DayMins')),
            DayCalls = float(request.form.get('DayCalls')),
            MonthlyCharge = float(request.form.get('MonthlyCharge')),
            OverageFee = float(request.form.get('OverageFee')),
            RoamMins = request.form.get('RoamMins'),
        )
        
        final_new_data = data.get_data_as_dataframe()
        print('final_new_data:', final_new_data)
        predict_pipeline = PredictPipeline()
        pred = predict_pipeline.predict(final_new_data)

        results = pred[0]

        return render_template('form.html', final_result = results)
    
if __name__=="__main__":
    app.run(host="0.0.0.0")