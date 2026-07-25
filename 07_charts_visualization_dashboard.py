import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import altair as alt

st.set_page_config(
    page_title="Charts & Visualization Dashboard",
    layout="wide"
)

st.title("Charts & Visualization Dashboard")

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150,170, 160, 210, 250],
    "Profit": [25, 30, 35, 32, 45, 50]
})

st.header("1. Line Chart")
st.line_chart(df.set_index("Month")["Sales"])

st.header("2. Area Chart")
st.area_chart(df.set_index("Month")[["Sales", "Profit"]])

st.header("3. Bar Chart")
st.bar_chart(df.set_index("Month")["Sales"])

st.header("4. Scatter plot (Matplotlib)")
fig, ax = plt.subplots()
ax.scatter(df["Sales"], df["Profit"])
ax.set_xlabel("Sales")
ax.set_ylabel("Profit")
st.pyplot(fig)

st.header("5. Altair Chart")
alt_chart = alt.Chart(df).mark_line(point=True).encode(
    x="Month",
    y="Sales",
    tooltip=["Month", "Sales"]
)
st.altair_chart(alt_chart, use_container_width=True)

st.header("6. plotly Chart")
plotly_fig = px.line(df, x="Month", y="Sales", markers=True)
st.plotly_chart(plotly_fig, use_container_width=True)

st.header("7. Matplotlib Line Chart")
fig2, ax2 = plt.subplots()
ax2.plot(df["Month"], df["Profit"], marker="o")
ax2.set_title("Monthly Profit")
st.pyplot(fig2)

st.header("9. Pie Chart")
fig4, ax4 = plt.subplots()
ax4.pie(
    df["Sales"],
    labels=df["Month"],
    autopct="%1.1f%%",
    startangle=90
)
ax4.set_title("Sales Contribution")
st.pyplot(fig4)

st.header("10. Histogram")
random_data = np.random.normal(100, 15, 500)
fig5, ax5 = plt.subplots()
ax5.hist(random_data, bins=20)
ax5.set_title("Sales Distribution")
st.pyplot(fig5)
