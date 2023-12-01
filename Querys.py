import Connection

connection = Connection.create_connection("postgres", "admin", "root", "localhost", "5432")
cursor = connection.cursor()

def run_query(sql_query):
    # Підключення до бази даних і виконання запиту
    try:
        cursor.execute(sql_query)

        # Отримання результатів запиту
        records = cursor.fetchall()

        # Виведення результатів
        for record in records:
            print(record)

    except Exception as e:
        print(f"Ошибка: {e}")

# Запит 1
# -------------------------------------------------------------------
print("Відобразити всі критичні помилки. Відсортувати по коду помилки" )
sql_query = """
SELECT *
FROM Log_error
WHERE Error_level = 'Критична'
ORDER BY Code_error;
"""
run_query(sql_query)

#Запит 2
#------------------------------------------------------------
print("Порахувати кількість помилок кожного рівня (підсумковий запит)")
sql_query = """
SELECT Error_level, COUNT(*) as ErrorCount
FROM Log_error
GROUP BY Error_level;


"""
run_query(sql_query)

# Запит 3
# ------------------------------------------------------------
print("Порахувати вартість роботи програміста при виправленні кожної помилки (запит з обчислювальним полем)")

# Виконання SQL-запиту з використанням параметрів
sql_query = """

SELECT 
1000 * 3 * COUNT (*) AS Programmers_spent 
FROM Log_error;

"""
cursor.execute(sql_query)

# Отримання та виведення результату
result = cursor.fetchone()
if result:
    programmers_spent = result[0]
    print(programmers_spent)
else:
    print("Немає результатів.")

# Запит 4
# ------------------------------------------------------------
print("Відобразити всі помилки, які надійшли із заданого джерела (запит з параметром):")
sql_query = """
SELECT 
    Description_error, 
    Date_of_receipt_of_information_about_the_error, 
    Error_level, 
    functionality_categor, 
    Source
FROM Log_error
WHERE Source = 'Користувач';

"""
run_query(sql_query)

# Запит 5
# ------------------------------------------------------------
print("Порахувати кількість помилок, які надійшли від користувачів, та тестувальників:")
sql_query = """

SELECT Source, COUNT(*) AS ErrorCount
FROM Log_error
WHERE Source IN ('Користувач', 'Тестувальник')
GROUP BY Source;


"""
run_query(sql_query)

# Запит 6
# ------------------------------------------------------------
print("Порахувати кількість критичних, важливих, незначних помилок, виправлених кожним програмістом:")

sql_query = """

SELECT
    P.Programmer_Code,
    P.Programmer_Last_Name,
    COUNT(CASE WHEN LE.Error_level = 'критична' THEN 1 END) AS Critical_Errors,
    COUNT(CASE WHEN LE.Error_level = 'важлива' THEN 1 END) AS Important_Errors,
    COUNT(CASE WHEN LE.Error_level = 'незначна' THEN 1 END) AS Minor_Errors
FROM
    Programmers P
JOIN
    Error_Fixes EF ON P.Programmer_Code = EF.Programmer_Code
JOIN
    Log_error LE ON EF.Code_Error = LE.Code_Error
GROUP BY
    P.Programmer_Code, P.Programmer_Last_Name;



"""
run_query(sql_query)


# Закриття підключення
cursor.close()
connection.close()