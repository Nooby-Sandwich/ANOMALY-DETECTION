
from flask import Flask, render_template, request
import pandas as pd
from  your_anomaly_detection_module  import AnomalyDetectionModel

app = Flask(__name__)

# Load your dataset
data = pd.read_csv('Aircraft_data.csv')


model = AnomalyDetectionModel()

model.train(data)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':

        x_attribute = request.form['x-axis']
        y_attribute = request.form['y-axis']


        selected_data = data[[x_attribute, y_attribute]]

        anomalies = model.detect_anomalies(data)

        anomaly_plot = model.plot_anomalies(selected_data, anomalies, x_attribute, y_attribute)

        return render_template('index.html', anomaly_plot=anomaly_plot)

    # Render the initial form
    return render_template('index.html')

@app.route('/check_plane', methods=['GET', 'POST'])
def check_plane():
    attribute_names = list(data.columns)  # Retrieve attribute names from the dataset

    if request.method == 'POST':
        attributes = []
        for name in attribute_names:
            attributes.append(float(request.form[name]))

        plane_data = pd.DataFrame([attributes])

        anomalies = model.detect_anomalies(plane_data)

        if any(anomalies):
            result = "Anomalous"
        else:
            result = "Non-Anomalous"

        return render_template('check_plane.html', result=result, attribute_names=attribute_names)

    return render_template('check_plane.html', attribute_names=attribute_names)

if __name__ == '__main__':
    app.run(debug=True)
