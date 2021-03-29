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
            wait  = input()
        elif ch == 10:
            index_no = int(input(
                "Enter the Index number that you want to update: "
            ))
            df = df.drop(df.index[index_no])
            print(df)
            print("\n\n\nPress any key to continue....")
            wait = input()
        elif ch == 11:
            g = df.sort_values(by = ["vote_average", "vote_count"], ascending = False)
            clear()
            print("Top 20 Movies Based on Rating")
            print("-" * 120)
            print(g.head(20))

            print("\n\n\nPress any key to continue...")
            wait = input()
        elif ch == 12:
            dfl = df.language.unique()
            print("Available Languages: ", dfl + '\n\n')
            langl = input("Enter Language Type: ")
            dfl = df[df.language == langl]
            clear()
            print("Top 20 Movies Based on Rating | Language: ", langl)
            print("-" * 120)
            print(dfl.sort_values(by = 'vote_average', ascending = False).head(20))
            print("\n\n\nPress any key to continue....")
            wait = input()
        elif ch == 13:
            print(df.describe())
            print("\n\n\nPress any key to continue....")
            wait  = input()
        elif ch == 14:
            break

# Function to generate export menu
def export_menu():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print("\n\nEXPORT MENU")
        print("_" * 100)
        print()
        print('''
              1. CSV File
              2. Excel File
              3. MYSQL TABLE
              3. Exit to Main Menu
              ''')
        ch = int(input("Enter your choice: "))

        if ch == 1:
            df.to_csv(R"D:\Python\March\Popular_movies\newMovies.CSV")
            print("\n\nCheck your new file 'newMovies.csv' at D:/Python/March/Popular_movies/")
            wait = input()
        elif ch == 2:
            df.to_excel(R"D:\Python\March\Popular_movies\newMovies.xlsx")
            print("\n\nCheck your new file 'newMovies.xlsx' at D:\Python\March\Popular_movies\\")
            wait = input()
        elif ch == 3:
            engine = sqlalchemy.create_engine(
                "mysql+pymysql://root:@localhost:3306/Punit_Choudhary")
            df.to_sql(name = 'movies', con = engine,
                      index = False, if_exists = 'replace')
            print("\n\nCheck your Database for movies table.....")
            wait = input()
        if ch == 4:
            break

# Function to generate Graph menu
def graph():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print("\nGRAPH MENU")
        print("_" * 100)
        print("1.  Whole Data LINE Graph")
        print("2.  Whole Data Bar Graph")
        print("3.  Whole Data Bar Graph Horizontal")
        print("4.  Whole Data Scatter Graph")
        print("5.  Exit to Main menu\n")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            g = df.groupby('language')
            x = df['language'].unique()
            y = g['language'].count()
            plt.xticks(rotation = 'vertical')
            plt.xlabel("Language")
            plt.ylabel("Total Movies")
            plt.title("Language wise movies count")
            plt.grid(True)
            plt.plot(x, y)
            plt.show()
        elif ch == 2:
            g = df.groupby('language')
            x = df['language'].unique()
            y = g['language'].count()
            plt.xlabel("Language")
            plt.ylabel("Total Movies")
            plt.title("Language wise movies count")
            plt.bar(x, y)
            plt.grid(True)
            plt.show()
        elif ch == 3:
            g = df.groupby('language')
            x = df['language'].unique()
            y = g['language'].count()
            plt.xlabel("Language")
            plt.ylabel("Total Movies")
            plt.title("Language wise movies count")
            plt.barh(x, y)
            plt.grid(True)
            plt.show()
        elif ch == 4:
            g = df.groupby('language')
            x = df['language'].unique()
            y = g['language'].count()
            plt.xlabel("Language")
            plt.ylabel("Total Movies")
            plt.title("Language wise movies count")
            plt.grid(True)
            plt.scatter(x, y)
            plt.show()
            wait = show()
        elif ch == 5:
            break


def main_menu():
    clear()
    while True:
        clear()
        print("MAIN MENU")
        print("_" * 100)
        print()
        print('''
              1. Read CSV File
              2. Data Analysis Menu
              3. Graph Menu
              4. Export Data
              5. Exit
              ''')
        choice = int(input("Enter your choice: "))

        if choice == 1:
            read_csv_file()
            Wait = input()
        elif choice == 2:
            data_analysis_menu()
            Wait = input()
        elif choice == 3:
            graph()
            wait = input()
        elif choice == 4:
            export_menu()
            wait = input()
        elif choice == 5:
            break
    clear()


# Calling main function
main_menu()
