# Projec-+b741b
# b Name : Popular Movies of IMDB.com

# Importing required modules
import pandas as pd
import numpy as np 
import time
import sqlalchemy
import matplotlib.pyplot as plt

# Imported Data frame
df = pd.DataFrame()
csv_file = "D:\Python\March\Popular_movies\imbd_updated.CSV"

def read_csv_file():
    df = pd.read_csv(csv_file)
    print(df)

# Function to clear output screen
def clear():
    for x in range(65):
        print()

def data_analysis_menu():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print("\n\nData Analysis MENU ")
        print('_' * 100)
        print("1.  Show whole Dataframe")
        print("2.  Show Columns ")
        print("3.  Show Top Rows")
        print("4.  Show Bottom Rows")
        print("5.  Show Specific Column\n")
        print("6.  Add a New Record\n")
        print("7.  Add a New Column\n")
        print("8.  Delete a Column\n")
        print("9.  Delete a Record\n")
        print("10. Update a Record\n")
        print("11. Rating Wise Report\n")
        print("12. Language Wise Report\n")
        print("13. Data Summery\n")
        print("14. Exit to Main Menu\n")

        ch = int(input("Enter your choice: "))

        if ch == 1:
            print(df)
            wait = input()
        elif ch == 2:
            print(df.columns)
            wait = input()
        elif ch == 3:
            n_head = int(input("Enter total rows you want to see: "))
            print(df.head(n_head))
            wait = input()
        elif ch == 4:
            n_tail = int(input("Enter total rows you want to see: "))
            print(df.tail(n_tail))
            wait = input()
        elif ch == 5:
            print(df.columns)
            col_name = input("Enter Column name that you want to print: ")
            print(df[col_name])
            wait = input()
        elif ch == 6:
            index = input("Enter Index number: ")
            movie = input("Enter new movie name: ")
            overview = input("Enter movie overview: ")
            lang = input("Enter movie language: ")
            count = int(input("Enter vote count: "))
            average = int(input("Enter vote average: "))

            data = {'index' : index,
                    'title' : movie,
                    'overview' : overview,
                    'language' : lang,
                    'vote_count' : count,
                    'vote_average' : average
                    }
            df.append(data, ignore_index=True)
            print(df)
            wait = input()
        elif ch == 7:
            col_name = input("Enter new column name: ")
            col_value = int(input("Enter deafult column value: "))
            df[col_name] = col_value
            print(df)
            print("\n\n\nPress any key to continue....")
            wait = input()
        elif ch == 8:
            col_name = input("Enter column name to delete: ")
            del df[col_name]
            print(df)
            print("\n\n\nPress any key to continue....")
            wait = input()
        elif ch == 9:
            index_no = int(input("Enter the Index Number that you want to delete: "))
            df = df.drop(df.index[index_no])
            print(df)
            print('\n\n\nPress any key to continue....')