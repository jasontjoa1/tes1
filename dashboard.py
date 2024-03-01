import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

def display_correlation_matrix(df, title):
    correlation = df[['temp', 'atemp', 'hum', 'windspeed', 'cnt']].corr()
    st.subheader(f"Matriks Korelasi Berdasarkan {title}")
    plt.figure(figsize=(10, 6))
    sns.heatmap(correlation, annot=True, cmap='coolwarm', fmt=".2f")
    st.pyplot(plt)

day_df = pd.read_csv("https://raw.githubusercontent.com/jasontjoa1/tes1/main/day.csv")
hour_df = pd.read_csv("https://raw.githubusercontent.com/jasontjoa1/tes1/main/hour.csv")

st.set_page_config(
    page_title="Bike Rentals Dashboard",
)

with st.sidebar:
    st.title("Bike Rentals Dashboard")
    st.write("Selamat datang di Bike Rentals Dashboard! Silahkan melihat data-data berikut.")
    st.subheader("Sample Data 'Day'")
    st.write(day_df.head())
    st.subheader("Sample Data 'Hour'")
    st.write(hour_df.head())

st.title("Bike Rentals Dashboard")

hourly_peak_hours = hour_df.groupby('hr')['cnt'].sum().sort_values(ascending=True)
st.subheader("Jumlah Penyewa Sepeda Setiap Jam")
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(hourly_peak_hours.index, hourly_peak_hours.values, color='skyblue')
ax.set_xlabel('Jam')
ax.set_ylabel('Jumlah Penyewa')
st.pyplot(fig)

selected_df = st.radio("Pilih Data yang Ingin Dilihat:", ('Data "Day"', 'Data "Hour"'))
if selected_df == 'Data "Day"':
    current_df = day_df
else:
    current_df = hour_df
display_correlation_matrix(current_df, selected_df)

day_df['dteday'] = pd.to_datetime(day_df['dteday'])
monthly_rentals_df = day_df.resample(rule='M', on='dteday').agg({
    "cnt": "sum"
})
st.subheader("Tren Penyewaan Sepeda dalam Dua Tahun")
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(monthly_rentals_df.index, monthly_rentals_df['cnt'], marker='o', linewidth=2, color="#72BCD4")
ax.set_xlabel("Bulan")
ax.set_ylabel("Jumlah Penyewa")
st.pyplot(fig)

st.caption('Copyright (c) Jason Tjoa 2024')