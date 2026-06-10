import streamlit as st
import pandas as pd
import joblib

# Model dosyasını yüklüyoruz
model_bilgileri = joblib.load("store_sales_model.pkl")

model = model_bilgileri["model"]
columns = model_bilgileri["columns"]

family_encoder = model_bilgileri["family_encoder"]
city_encoder = model_bilgileri["city_encoder"]
state_encoder = model_bilgileri["state_encoder"]
type_encoder = model_bilgileri["type_encoder"]

store_transaction_median = model_bilgileri["store_transaction_median"]
general_transaction_median = model_bilgileri["general_transaction_median"]

st.title("Store Sales Forecasting")

st.write(
    "Bu uygulama, mağaza ve ürün bilgilerine göre tahmini satış miktarını hesaplar. "
    "Model Kaggle Store Sales veri seti kullanılarak eğitilmiştir."
)

store_nbr = st.number_input(
    "Mağaza Numarası",
    min_value=1,
    max_value=54,
    value=1
)

family = st.selectbox(
    "Ürün Ailesi",
    list(family_encoder.classes_)
)

city = st.selectbox(
    "Şehir",
    list(city_encoder.classes_)
)

state = st.selectbox(
    "Eyalet / Bölge",
    list(state_encoder.classes_)
)

store_type = st.selectbox(
    "Mağaza Tipi",
    list(type_encoder.classes_)
)

cluster = st.number_input(
    "Cluster",
    min_value=1,
    max_value=17,
    value=1
)

onpromotion = st.number_input(
    "Promosyondaki Ürün Sayısı",
    min_value=0,
    value=0
)

tarih = st.date_input("Tahmin Tarihi")

year = tarih.year
month = tarih.month
day = tarih.day
dayofweek = tarih.weekday()
is_weekend = 1 if dayofweek in [5, 6] else 0

transactions = store_transaction_median.get(
    store_nbr,
    general_transaction_median
)

girdi = pd.DataFrame({
    "store_nbr": [store_nbr],
    "family": [family_encoder.transform([family])[0]],
    "onpromotion": [onpromotion],
    "year": [year],
    "month": [month],
    "dayofweek": [dayofweek],
    "city": [city_encoder.transform([city])[0]],
    "state": [state_encoder.transform([state])[0]],
    "type": [type_encoder.transform([store_type])[0]],
    "cluster": [cluster],
    "transactions": [transactions],
    "day": [day],
    "is_weekend": [is_weekend]
})

# Modelin beklediği kolon sırasına getiriyoruz
for col in columns:
    if col not in girdi.columns:
        girdi[col] = 0

girdi = girdi[columns]

if st.button("Satış Tahmini Yap"):
    tahmin = model.predict(girdi)[0]
    tahmin = max(0, tahmin)

    st.success(f"Tahmini Satış Miktarı: {tahmin:.2f}")