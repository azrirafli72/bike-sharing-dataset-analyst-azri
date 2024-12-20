import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Setup Seaborn style (menambahkan beberapa gaya visualisasi)
sns.set_theme(style="whitegrid")  # Gaya background yang lebih bersih

# Load data
all_df = pd.read_csv("dashboard/main_data.csv")
all_df['dteday'] = pd.to_datetime(all_df['dteday'])
all_df.sort_values(by="dteday", inplace=True)

# Sidebar - Filter date range
min_date, max_date = all_df["dteday"].min(), all_df["dteday"].max()

with st.sidebar:
    st.image("dashboard/bike.png", use_column_width=True)
    st.title("Filter Data 📅")
    start_date, end_date = st.date_input("Select Date Range", 
                                        [min_date, max_date], 
                                        min_value=min_date, 
                                        max_value=max_date)

# Filter data based on date
main_df = all_df[(all_df['dteday'] >= pd.Timestamp(start_date)) & 
                 (all_df['dteday'] <= pd.Timestamp(end_date))]

# Aggregate data
daily_rentals_df = main_df.resample('D', on='dteday').agg({
    "registered": "sum",
    "casual": "sum",
    "cnt": "sum"
}).reset_index()

monthly_rentals_df = main_df.resample('M', on='dteday').agg({
    "registered": "sum",
    "casual": "sum",
    "cnt": "sum"
}).reset_index()

hourly_df = main_df.groupby('hr')['cnt'].sum().reset_index().rename(columns={"cnt": "total_customer"})
season_df = main_df.groupby("season")['cnt'].sum().reset_index().rename(columns={"cnt": "total_customer"})
weather_df = main_df.groupby("weathersit")['cnt'].sum().reset_index().rename(columns={"cnt": "total_customer"})

# Header
st.title("🚲 Bike Sharing Dashboard")
st.write("Analyze rental patterns of registered and casual customers | Analisis pola penyewaan sepeda.")

# Metrics
st.subheader("📊 Key Metrics / Metrik Utama")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Rentals", daily_rentals_df["cnt"].sum())

with col2:
    st.metric("Registered Customers", daily_rentals_df["registered"].sum())

with col3:
    st.metric("Casual Customers", daily_rentals_df["casual"].sum())

st.write("\n")  # Empty space for clarity

# Monthly Rentals
st.subheader("📅 Monthly Rentals / Penyewaan Bulanan")
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(monthly_rentals_df["dteday"], monthly_rentals_df["cnt"], linestyle='--',
        marker='D', label='Total Penyewaan Sepeda (cnt)', color="teal")  # Ubah warna sesuai desain
ax.set_title("Monthly Rentals | Penyewaan Bulanan", fontsize=14, weight='bold')
ax.set_xlabel("Month / Bulan", fontsize=12)
ax.set_ylabel("Total Customers / Total Pelanggan", fontsize=12)
st.pyplot(fig)

st.write("\n")

# Rentals by Season and Weather
st.subheader("🌦️ Rentals by Season and Weather / Penyewaan Berdasarkan Musim dan Cuaca")
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(9, 7))
    season_df_sorted = season_df.sort_values('total_customer', ascending=True)
    season_colors = {
    'Fall': '#8B4513',     # Coklat tua untuk musim gugur
    'Summer': '#FFA500',   # Oranye terang untuk musim panas
    'Winter': '#4682B4',   # Biru baja untuk musim dingin
    'Spring': '#32CD32'    # Hijau terang untuk musim semi
    }
    sns.barplot(x="total_customer", y="season", data=season_df_sorted, palette=season_colors, ax=ax, orient='h')
    ax.set_title("Total Rentals by Season", fontsize=14, weight='bold')
    ax.set_xlabel("Total Rentals (Total Peminjaman)", fontsize=12)
    ax.set_ylabel("Season (Musim)", fontsize=12)
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(9, 7))
    weather_df_sorted = weather_df.sort_values('total_customer', ascending=True)
    weather_colors = {
    'Clear': '#FFD700',  # Warna emas untuk cuaca cerah.
    'Cloudy': '#87CEEB',  # Biru langit terang untuk cuaca berawan.
    'Light Snow/Rain': '#D3D3D3',  # Abu-abu muda untuk salju/hujan ringan.
    'Heavy Rain/Ice Pallets': '#00008B'  # Biru tua untuk hujan deras/pellet es.
    }
    sns.barplot(x="weathersit", y="total_customer", data=weather_df, palette=weather_colors, ax=ax)  # coolwarm for weather
    ax.set_title("Total Rentals by Weather", fontsize=14, weight='bold')
    ax.set_xlabel("Weather (Cuaca)", fontsize=12)
    ax.set_ylabel("Total Rentals (Total Peminjaman)", fontsize=12)
    st.pyplot(fig)

st.write("\n\n")

# Rentals by Hour
st.subheader("⏰ Rentals by Hour / Penyewaan Berdasarkan Jam")
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x="hr", y="total_customer", data=hourly_df, color="#FF6F61", ax=ax)  # Changed color to a warmer tone
ax.set_title("Total Rentals by Hour", fontsize=14, weight='bold')
ax.set_xlabel("Hour (Jam)", fontsize=12)
ax.set_ylabel("Total Rentals (Jumlah Peminjaman)", fontsize=12)
st.pyplot(fig)

st.write("\n\n")

# Registered vs Casual - Pie Chart
st.subheader("📊 Registered vs Casual Customers / Pelanggan Terdaftar vs Kasual")
fig, ax = plt.subplots(figsize=(6, 4))
sizes = [daily_rentals_df["registered"].sum(), daily_rentals_df["casual"].sum()]
labels = ['Registered / Terdaftar', 'Casual / Kasual']
colors = ['#1f77b4', '#ff7f0e']  # Adjusted colors

ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, 
       colors=colors, wedgeprops=dict(width=0.4))
ax.set_title("Customer Distribution | Distribusi Pelanggan", fontsize=14, weight='bold')
st.pyplot(fig)

st.write("\n\n")

# Footer
st.caption("© 2024 AzriRafli03 | Built with Streamlit 🚀")
