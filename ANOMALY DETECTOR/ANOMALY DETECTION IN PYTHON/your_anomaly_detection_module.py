from sklearn.ensemble import IsolationForest
from sklearn.svm import OneClassSVM
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.metrics import recall_score
import matplotlib.pyplot as plt

class AnomalyDetectionModel:
    def __init__(self):
        self.models = []

    def train(self, data):
        # Add different anomaly detection models
        self.models.append(('Isolation Forest', IsolationForest(contamination='auto', random_state=42)))
        self.models.append(('One-Class SVM', OneClassSVM()))
        self.models.append(('K-Means', KMeans(n_clusters=2)))

        # Train all models
        for name, model in self.models:
            model.fit(data)

    def detect_anomalies(self, data, threshold=0.5):
        # Detect anomalies using all models
        predicted_anomalies = {}
        for name, model in self.models:
            anomalies = model.predict(data)
            predicted_anomalies[name] = anomalies

        # Combine the predictions from different models
        combined_anomalies = sum(predicted_anomalies.values()) / len(self.models)

        # Determine anomalies based on the threshold
        anomalies = combined_anomalies > threshold

        return anomalies

    def plot_anomalies(self, selected_data, anomalies, x_attribute, y_attribute):
        plt.figure(figsize=(10, 6))
        plt.scatter(selected_data[x_attribute], selected_data[y_attribute], c=anomalies, cmap='viridis')
        plt.xlabel(x_attribute)
        plt.ylabel(y_attribute)
        plt.title('Anomaly Detection')
        plt.show()
