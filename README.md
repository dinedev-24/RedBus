________________________________________
Project Title: RedBus Data Scraping and Analysis Application
________________________________________
Project Description
This project involves scraping bus route data from RedBus, storing it in a MySQL database, and creating a Streamlit application to visualize, filter, and analyze it. The project ensures data accuracy, database efficiency, and a user-friendly interface for insights and exploration.
________________________________________
Features
•	Data Scraping: Extracts complete and accurate bus route data (route names, times, prices, ratings, etc.).
•	Database Management: Stores data in a well-designed MySQL schema.
•	Streamlit Application: Interactive data filtering, visualization, and insights.
•	Filter Options:
o	Route Name
o	Bus Type
o	Price Range
•	Visual Analytics:
o	Average price by bus type
o	Count of routes by rating
________________________________________
Installation Instructions
1.	Clone the Repository:
bash
Copy code
git clone https://github.com/your-username/RedBus-Data-Application.git
cd RedBus-Data-Application
2.	Install Required Packages:
bash
Copy code
pip install -r requirements.txt
3.	Set Up the MySQL Database:
o	Create a database named BusTransport.
o	Use the schema provided in schema.sql to set up the table.
4.	Run the Streamlit Application:
bash
Copy code
streamlit run RedBus_StreamLit_Application.py
________________________________________
Technologies Used
•	Selenium: Data scraping, cleaning, and application development.
•	MySQL: Database for storing and managing data.
•	Streamlit: Interactive web application for data analysis.
•	Pandas: Data manipulation and cleaning.
________________________________________
Project Insights
•	Challenges:
o	Handling invalid data entries during scraping.
o	Resolving errors with SQL query execution and schema design.
o	Optimizing Streamlit for large datasets.
•	Solutions:
o	Added data validation and cleaning steps before database insertion.
o	Parameterized SQL queries for error-free insertion.
o	Cached data in Streamlit to improve performance.
# RedBus
