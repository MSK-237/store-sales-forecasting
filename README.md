# Store Sales Forecasting

## Project Overview

This project predicts future store sales using the Kaggle Store Sales - Time Series Forecasting dataset. Store information, product families, promotions, transaction counts, and date-based features were combined to build a machine learning forecasting model.

Several date-based features such as year, month, day, day of week, and weekend indicators were engineered during preprocessing. Multiple machine learning algorithms were evaluated, and the Random Forest model achieved the best overall performance.

---

## Dataset

The project uses the Kaggle Store Sales - Time Series Forecasting competition dataset.

Main files:

* train.csv
* test.csv
* stores.csv
* transactions.csv
* holidays_events.csv
* oil.csv

---

## Feature Engineering

The following features were created:

* Year
* Month
* Day
* Day of Week
* Weekend Indicator
* Store Transaction Statistics

Categorical variables were encoded before model training.

---

## Models Evaluated

| Model             | MAE    | R²     |
| ----------------- | ------ | ------ |
| Random Forest     | 60.09  | 0.9304 |
| Gradient Boosting | 191.59 | 0.7797 |

Random Forest achieved the strongest performance and was selected as the final model.

---

## Results

* MAE: 60.09
* R² Score: 0.9304
* Kaggle Public Score: 0.69777

---

Live Demo

🚀 **[Live Demo](https://huggingface.co/spaces/MSK34/store-sales-forecasting)**

Kaggle Notebook

📊 **[Kaggle Notebook](https://www.kaggle.com/code/mhskaya/store-sales-forecasting)**

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Joblib
* Streamlit

---

## Project Structure

```text
store-sales-forecasting/
│
├── src/
│   ├── app.py
│
├── requirements.txt
├── README.md
└── Store_Sales_Forecasting.ipynb
```

## Model File

The trained model file is not included in this repository because it exceeds GitHub's file size limit. The complete application, including the trained model, is available on the Hugging Face Space linked above.

---

## Conclusion

This project demonstrates how machine learning can be applied to retail sales forecasting. By combining store information, promotions, transaction statistics, and temporal features, the Random Forest model achieved strong predictive performance and generated competitive results on the Kaggle Store Sales competition.
