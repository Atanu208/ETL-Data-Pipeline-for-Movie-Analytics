# 🎬 ETL Data Pipeline for Movie Analytics  

## 📌 Project Overview  
This project is an **offline ETL (Extract, Transform, Load) pipeline** built using **Python and MySQL**.  
It processes a dataset of 4,000+ movies (`movies.csv`) by extracting the data, cleaning and transforming it, and loading it into a MySQL database for analysis.  

The goal of this project is to demonstrate **data engineering fundamentals** such as ETL, automation, logging, and analytics — without using cloud tools.  

---

## ⚙️ Features  
- **Extract**: Reads raw movie data from a CSV file.  
- **Transform**: Cleans missing values, standardizes data types, and removes duplicates.  
- **Load**: Inserts transformed data into a MySQL database (`movies_db`).  
- **Logging**: Tracks pipeline runs and errors for debugging.  
- **Automation**: ETL pipeline can be scheduled with Windows Task Scheduler.  
- **Analytics**: Run SQL queries to find top-rated movies, genre-based stats, or budget vs gross analysis.  

---

## 🗂 Dataset  
The dataset contains movie information such as:  

- `name`  
- `rating`  
- `genre`  
- `year`  
- `released`  
- `score`  
- `votes`  
- `director`  
- `writer`  
- `star`  
- `country`  
- `budget`  
- `gross`  
- `company`  
- `runtime`  

Sample entry:  

```csv
"The Shining";"R";"Drama";1980;"June 13 1980 (United States)";8.4;927000.0;"Stanley Kubrick";"Stephen King";"Jack Nicholson";"United Kingdom";19000000;"46998772.0";"Warner Bros.";146.0
🚀 Tech Stack

Language: Python
Database: MySQL
Libraries: Pandas, SQLAlchemy, Logging
Tools: Windows Task Scheduler (for automation)

📂 Project Structure
<img width="971" height="268" alt="image" src="https://github.com/user-attachments/assets/c872da63-870c-40fa-8bc5-1e5d8b2b6ddd" />

⚡ How to Run

Clone Repository
<img width="949" height="63" alt="image" src="https://github.com/user-attachments/assets/66ad54a2-16ef-47c2-9007-6bb5a8fcb752" />

Install Requirements
pip install pandas sqlalchemy mysql-connector-python

Update Database Config
Edit db_config.py with your MySQL credentials. Example:

DB_USER = "root"
DB_PASSWORD = "yourpassword"
DB_HOST = "localhost"
DB_NAME = "movies_db"

Run ETL Script
python etl_pipeline.py

Verify in MySQL
USE movies_db;
SELECT * FROM movies_data LIMIT 5;

📊 Example Queries

Top 5 Movies by Rating
SELECT name, score 
FROM movies_data 
ORDER BY score DESC 
LIMIT 5;

Movies Released After 2015
SELECT name, year, score 
FROM movies_data 
WHERE year > 2015;


🔮 Future Improvements
Add unit tests for data validation.
Support multiple input sources (CSV, Excel, API).
Create dashboards using Power BI or Tableau.

