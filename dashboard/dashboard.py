import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Setup Seaborn style
sns.set_style("whitegrid")

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
ax.plot(monthly_rentals_df["dteday"], monthly_rentals_df["cnt"], 
        marker='o', color="#6a5acd", linewidth=2)
ax.set_title("Monthly Rentals | Penyewaan Bulanan")
ax.set_xlabel("Month / Bulan")
ax.set_ylabel("Total Customers / Total Pelanggan")
st.pyplot(fig)

st.write("\n")

# Rentals by Season and Weather
st.subheader("🌦️ Rentals by Season and Weather / Penyewaan Berdasarkan Musim dan Cuaca")
col1, col2 = st.columns(2)

with col1:
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x="season", y="total_customer", data=season_df, palette="muted", ax=ax)
    ax.set_title("Total Rentals by Season")
    ax.set_xlabel("Season / Musim")
    ax.set_ylabel("Total Customers")
    st.pyplot(fig)

with col2:
    fig, ax = plt.subplots(figsize=(6, 4))
    sns.barplot(x="weathersit", y="total_customer", data=weather_df, palette="coolwarm", ax=ax)
    ax.set_title("Total Rentals by Weather")
    ax.set_xlabel("Weather / Cuaca")
    ax.set_ylabel("Total Customers")
    st.pyplot(fig)

st.write("\n")

# Rentals by Hour
st.subheader("⏰ Rentals by Hour / Penyewaan Berdasarkan Jam")
fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x="hr", y="total_customer", data=hourly_df, color="#ffb347", ax=ax)
ax.set_title("Total Rentals by Hour")
ax.set_xlabel("Hour / Jam")
ax.set_ylabel("Total Customers")
st.pyplot(fig)

st.write("\n")

# Registered vs Casual - Pie Chart
st.subheader("📊 Registered vs Casual Customers / Pelanggan Terdaftar vs Kasual")
fig, ax = plt.subplots(figsize=(6, 4))
sizes = [daily_rentals_df["registered"].sum(), daily_rentals_df["casual"].sum()]
labels = ['Registered / Terdaftar', 'Casual / Kasual']
colors = ['#66b3ff', '#ffcc99']

ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, 
       colors=colors, wedgeprops=dict(width=0.4))
ax.set_title("Customer Distribution | Distribusi Pelanggan")
st.pyplot(fig)

st.write("\n")

# Footer
st.caption("© 2024 AzriRafli03 | Built with Streamlit 🚀")