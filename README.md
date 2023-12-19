# Aircraft Anomaly Detection

This is a web application for aircraft anomaly detection using Flask and various anomaly detection models such as Isolation Forest, One-Class SVM, and K-Means. The application allows users to visualize anomalies in a dataset, as well as check if a specific set of aircraft attributes is anomalous.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python (3.6 or higher)
- Flask
- pandas
- scikit-learn
- matplotlib

Install the required Python packages using the following command:

```bash
pip install Flask pandas scikit-learn matplotlib

Installing
Clone the repository to your local machine:
bash
Copy code
git clone https://github.com/your-username/aircraft-anomaly-detection.git
Change into the project directory:
bash
Copy code
cd aircraft-anomaly-detection
Run the Flask application:
bash
Copy code
python main.py
The application will be accessible at http://127.0.0.1:5000/ in your web browser.

Usage
Visit the homepage (/) to plot graphs and visualize anomalies in the dataset.
Click on "Check Your Plane" to input specific aircraft attributes and check if the plane is anomalous.
Files and Directories
main.py: The main Flask application.
your_anomaly_detection_module.py: Anomaly detection module containing the AnomalyDetectionModel class.
Aircraft_data.csv: Sample dataset for aircraft attributes.
templates/: HTML templates for rendering web pages.
static/: Static files such as CSS stylesheets and images.
Contributing
Feel free to contribute to this project by opening issues or submitting pull requests. Please follow the Contributing Guidelines.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
This project was inspired by the need for anomaly detection in aircraft attribute datasets.
Special thanks to the contributors and the open-source community.
