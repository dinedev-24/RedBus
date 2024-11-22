import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus
import matplotlib.pyplot as plt

# Database configuration
db_user = 'root'
db_password = 'Portal@77'
db_host = 'localhost'
db_name = 'bustransport'

# Initialize database connection
engine = create_engine(f"mysql+pymysql://{db_user}:{quote_plus(db_password)}@{db_host}/{db_name}")

# Load data function
@st.cache_data
def load_data():
    query = "SELECT * FROM bus_routes"
    return pd.read_sql(query, con=engine)

data = load_data()

# Title and Description
st.title("BusTransport Data Viewer")
st.markdown("""
This application allows you to explore, filter, and analyze bus route data interactively.
""")

# Sidebar Filters
st.sidebar.title("Filters")
bus_name_filter = st.sidebar.selectbox("Filter by Bus Name", options=["All"] + data['bus_name'].dropna().unique().tolist())
route_name_filter = st.sidebar.selectbox("Filter by Route Name", options=["All"] + data['route_name'].dropna().unique().tolist())
min_price = st.sidebar.number_input("Minimum Price", value=float(data['price'].min()))
max_price = st.sidebar.number_input("Maximum Price", value=float(data['price'].max()))

# Apply filters
filtered_data = data[
    ((data['bus_name'] == bus_name_filter) if bus_name_filter != "All" else True) &
    ((data['route_name'] == route_name_filter) if route_name_filter != "All" else True) &
    (data['price'] >= min_price) &
    (data['price'] <= max_price)
]

# Display filtered data
st.subheader("Filtered Data")
if filtered_data.empty:
    st.write("No results match the selected criteria.")
else:
    st.write(filtered_data)

# Add analysis and charts
if not filtered_data.empty:
    # Bar Chart: Average Price by Bus Name
    st.subheader("Average Price by Bus Name")
    avg_price_by_bus_name = filtered_data.groupby('bus_name')['price'].mean().reset_index()
    st.bar_chart(avg_price_by_bus_name.set_index('bus_name'))
    
    # Line Chart: Price Trend by Route
    st.subheader("Price Trend by Route")
    price_trend = filtered_data.groupby(['route_name', 'bus_name'])['price'].mean().reset_index()
    st.line_chart(price_trend.pivot(index='route_name', columns='bus_name', values='price'))
    
    # Area Chart: Seats Availability by Route
    st.subheader("Seats Availability by Route")
    seats_by_route = filtered_data.groupby('route_name')['seats_available'].sum().reset_index()
    st.area_chart(seats_by_route.set_index('route_name'))

    # Pie Chart: Distribution of Bus Types
    st.subheader("Distribution of Bus Types")
    bus_type_distribution = filtered_data['bus_type'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(bus_type_distribution, labels=bus_type_distribution.index, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')  # Equal aspect ratio ensures that the pie chart is circular.
    st.pyplot(fig)

    # Scatter Plot: Price vs. Star Rating
    st.subheader("Price vs. Star Rating")
    scatter_data = filtered_data[['price', 'star_rating']].dropna()
    fig, ax = plt.subplots()
    ax.scatter(scatter_data['price'], scatter_data['star_rating'], alpha=0.7, edgecolors='w', s=100)
    ax.set_xlabel("Price")
    ax.set_ylabel("Star Rating")
    ax.set_title("Price vs. Star Rating")
    st.pyplot(fig)

else:
    st.write("No data available for further analysis.")