Stock Price Trend Predictor-A machine learning-based web application that predicts the trend of a stock price using historical stock market data.

## Project Overview
The Stock Price Trend Predictor is a Django web application integrated with a machine learning model.
The application takes stock-related input data such as:
- Open price
- High price
- Low price
- Closing price
- Trading volume
and predicts the expected stock price trend.

##  Technologies Used
- **Python**
- **Django**
- **Machine Learning**
- **Scikit-learn**
- **Pandas**
- **HTML**
- **CSS**



## Machine Learning Model

The project uses a Random Forest Classifier to classify the stock price trend.

The trained model is stored as:
`stock_model.pkl`
The dataset used for training contains historical stock information including:
- Open
- High
- Low
- Close
- Volume

## Project Structure
Stock-Price-Trend-Predictor/
├── manage.py
├── model.py
├── s.csv
│
├── stockapp/
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   └── stock_model.pkl
│
├── stockproject/
│   ├── settings.py
│   └── urls.py
│
└── templates/
    └── index.html

How to Run the Project

1. Clone the repository
git clone https://github.com/saritha2106/Stock-Price-Trend-Predictor.git

2. Open the project directory
cd Stock-Price-Trend-Predictor

3. Create and activate a virtual environment
python -m venv venv

Windows:
venv\Scripts\activate

4.Install dependencies
pip install django pandas scikit-learn

5. Run the Django server
python manage.py runserver

6. Open the application
Open the local URL shown in the terminal, usually:
http://127.0.0.1:8000/

Features
Django-based web interface
Machine learning-based stock trend prediction
Historical stock data processing
Random Forest classification
Simple user-friendly interface

Future Improvements

Use larger and more recent datasets
Add real-time stock market data
Compare multiple machine learning models
Add interactive stock price charts
Improve prediction performance
Deploy the application online


Disclaimer
This project is developed for educational and demonstration purposes. Stock market predictions are not guaranteed and should not be considered financial advice.
