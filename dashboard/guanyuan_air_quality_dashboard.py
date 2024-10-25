import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load data (example loading)
@st.cache_data
def load_data():
    # Replace this with actual data loading
    guanyuan_df = pd.read_csv('guanyuan_df.csv', parse_dates=['date'])
    return guanyuan_df

guanyuan_df = load_data()

# Set up the Streamlit app
st.title("Air Quality Analysis in Guanyuan (2013-2017)")
st.write("This dashboard presents the analysis of air quality data in Guanyuan, including pollutant levels and their correlations.")

# Plot 1: Average PM2.5 Concentration Over Years
st.subheader("Average PM2.5 Concentration (2013-2017)")
fig1, ax1 = plt.subplots(figsize=(10, 6))
guanyuan_df.groupby(guanyuan_df['date'].dt.year)['PM2.5'].mean().plot(ax=ax1)
ax1.set_title('Average PM2.5 Concentration in Guanyuan (2013-2017)')
ax1.set_xlabel('Year')
ax1.set_ylabel('PM2.5 Concentration (µg/m³)')
ax1.grid(True)
st.pyplot(fig1)

# Plot 2: Correlation Heatmap
st.subheader("Correlation Heatmap of Pollutants and Temperature")
corr_matrix = guanyuan_df[['TEMP', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].corr()

fig2, ax2 = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, linewidths=0.5, ax=ax2)
ax2.set_title('Correlation Heatmap of Temperature and Pollutants')
st.pyplot(fig2)

# Plot 3: Wind Speed and Direction vs PM2.5
st.subheader("Influence of Wind Speed and Direction on PM2.5")
fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.scatterplot(data=guanyuan_df, x='WSPM', y='PM2.5', hue='wd', ax=ax3)
ax3.set_title('Influence of Wind Speed (WSPM) and Direction (wd) on PM2.5')
ax3.set_xlabel('Wind Speed (m/s)')
ax3.set_ylabel('PM2.5 Concentration (µg/m³)')
st.pyplot(fig3)

# Plot 4: Monthly Average Pollutant Levels
st.subheader("Monthly Average Pollutant Levels (PM2.5, NO2, O3)")
guanyuan_df['month'] = guanyuan_df['date'].dt.month
pollutants = ['PM2.5', 'NO2', 'O3']

fig4, ax4 = plt.subplots(figsize=(12, 8))
for pollutant in pollutants:
    sns.lineplot(x='month', y=pollutant, data=guanyuan_df, label=pollutant, ax=ax4)

ax4.set_title('Monthly Average Pollutant Levels (PM2.5, NO2, O3)')
ax4.set_xlabel('Month')
ax4.set_ylabel('Pollutant Concentration (µg/m³)')
ax4.legend(title='Pollutant')
st.pyplot(fig4)

# Plot 5: Effect of Rainfall on PM2.5
st.subheader("Effect of Rainfall on PM2.5 Concentration")
fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.scatterplot(x='RAIN', y='PM2.5', data=guanyuan_df, ax=ax5)
ax5.set_title('Effect of Rainfall on PM2.5 Concentration')
ax5.set_xlabel('Rainfall (mm)')
ax5.set_ylabel('PM2.5 Concentration (µg/m³)')
ax5.grid(True)
st.pyplot(fig5)

# Additional customization or features can be added here
