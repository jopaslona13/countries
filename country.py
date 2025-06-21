import sqlite3
import json
from datetime import datetime

def parse_date_safe(date_str):
    if date_str is None:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None
    
conn = sqlite3.connect("countries.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS countries (
        race INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        population TEXT,
        presidents TEXT,                                                 
        wars INTEGER,
        area INTEGER,    
        country_id INTEGER            
);
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS  gdp_inf(
    country TEXT,
    year INTEGER,
    gdp_value INTEGER,
    country_id INTEGER

               
);              
""")

with open("countries_info.json", 'r', encoding="utf-8") as f:
    countries = json.load(f)

for country in countries:
    cursor.execute("""
        INSERT INTO countries (
            race, population, wars, presidents, name, area, country_id
        )                                      
        VALUES(?, ?, ?, ?, ?, ?, ?)                     
    """, (
        country["country_name"],
        country["population"],
        country["area_km2"],
        country["race"],
        country["presidents"],
        country["wars"]
        country["id"]
    )
)
       