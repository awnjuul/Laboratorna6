import Connection

# Підключення до Бази даних
connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
cursor = connection.cursor()

try:
    # Створення таблиці Помилки
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Log_error (
    Code_error INT PRIMARY KEY,
    Description_error TEXT,
    Date_of_receipt_of_information_about_the_error DATE,
    Error_level VARCHAR(15),
    functionality_categor VARCHAR(30),
    Source VARCHAR(20)
);

    """
    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f" Помилка створення таблиці Помилка: {e}")

try:
    # Створення таблиці програмістів відповідальних за виправлення помилки


    create_table_query = """
    CREATE TABLE IF NOT EXISTS Programmers(
        Programmer_Code INT PRIMARY KEY,
        Programmer_Last_Name VARCHAR(50),
        Programmer_First_Name VARCHAR(50),
        Programmer_Phone VARCHAR(15)
    );
        """

    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці програмістів відповідальних за виправлення помилки: {e}")

try:
        # Створення таблиці виправлення помилок


    create_table_query = """
  CREATE TABLE IF NOT EXISTS Error_Fixes (
       Fix_Code INT PRIMARY KEY,
       Code_Error INT,
       Fix_Start_Date DATE,
       Fix_Duration INT,
       Programmer_Code INT,
       Work_Cost_Per_Day DECIMAL(10, 2),
       FOREIGN KEY (Code_Error) REFERENCES Log_error(Code_error),
       FOREIGN KEY (Programmer_Code) REFERENCES Programmers(Programmer_Code)
    );
        """

    cursor.execute(create_table_query)
    connection.commit()
except Exception as e:
    print(f"Помилка при створенні таблиці виправлення помилок: {e}")

    cursor.close()
    connection.close()
