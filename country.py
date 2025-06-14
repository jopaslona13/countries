import sqlite3
import json
from datetime import datetime

def parse_date_safe(date_str):
    if date_str is None:
        return None
    try:
        return datetime.strftime(date_str, %Y-%m-%d).date()
    except ValueError:
        return None
    
conn = sqlite3.connect("countries.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foregin_keys = ON;") 

cursor.execute("""
    CREATE TABLE IF NOT EXISTS countries (
        race INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        population TEXT,
        presidents TEXT,                                                 
        wars INTEGER,           
               
               
               
);
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS presidents (
        country TEXT,
        first_name TEXT,            
        last_name TEXT,
        years_reign INTEGER,
               
);              
""")

with open(
    "", 'r', encoding="utf-8"
) as f:
    countries = json.load(f)

for country in countries:
    cursor.execute("""
        INSERT INTO countries(
            race, population, wars, presidents, name)
    )                                      
        VALUES(?,?,?,?,?,?,?)                     
    """,(
        name,
        purse_of_safe(student.get("enrollment_date"))
        purse_of_safe(student.get("graduation_date")) 
    ))   