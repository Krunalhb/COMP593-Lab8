"""
Description:
 Generates a CSV reports containing all married couples in
 the Social Network database.

Usage:
 python marriage_report.py
"""
import os
import sqlite3
from create_relationships import db_path
import pandas as pd

def main():
    # Query DB for list of married couples
    married_couples = get_married_couples()

    # Save all married couples to CSV file
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'married_couples.csv')
    save_married_couples_csv(married_couples, csv_path)

def get_married_couples():
    """Queries the Social Network database for all married couples.

    Returns:
        list: (name1, name2, start_date) of married couples 
    """
    # TODO: Function body
con = sqlite3.connect(db_path)
cur = con.cursor()

    #SQL query to get married couples:
married_couples_query= """ 
SELECT person1.name, person2.name, start_date, type 
FROM relationships  
JOIN people person1 ON person1_id = person1.id;
JOIN people person2 ON person2_id = person2.id
WHERE rel_type = 'partner'
"""

# Execute the query and get all results
cur.execute(married_couples_query)
married_couples = cur.fetchall()

con.close()
 
def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """
    # TODO: Function body
    df = pd.Dataframe(married_couples, columns=['start_date', 'person1', 'person2'])
    df.to_csv(csv_path, index=False)
    
if __name__ == '__main__':
   main()