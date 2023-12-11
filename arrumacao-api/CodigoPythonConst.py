
import psutil
import time
import mysql.connector
import pyodbc

cpu = psutil.cpu_percent(interval=1)
ram = psutil.virtual_memory()

try:
    conn = pyodbc.connect(
        'Driver=ODBC Driver 17 for SQL Server;'
        'Server=ec2-34-194-127-191.compute-1.amazonaws.com;'
        'Database=PowerTechSolutions;'
        'UID=sa;'
        'PWD=myLOVEisthe0506'
    )
    cursor = conn.cursor()
    if 1 == 1:
        sql_querryCPU = f"INSERT INTO Monitoramento_RAW (Uso,FKComponente_Monitorado,FKComponente_Cadastrado) VALUES ({cpu},7,1)"
        cursor.execute(sql_querryCPU)
        conn.commit()
    if 1 == 1:
        sql_querryRAM = f'INSERT INTO Monitoramento_RAW (Total,Free,Uso,FKComponente_Monitorado,FKComponente_Cadastrado) VALUES ({ram.total},{ram.free},{ram.percent},8,2)'
        cursor.execute(sql_querryRAM)
        conn.commit()
finally:
    cursor.close()
    conn.close()

try:
    mydb = mysql.connector.connect(host = 'localhost', user = 'root',password = '@myLOVEisthe0506',database = 'PowerTechSolutions')
    if mydb.is_connected():
        db_info = mydb.get_server_info()
        mycursor = mydb.cursor()
        if 1 == 1:
            sql_querryCPU = 'INSERT INTO Monitoramento_RAW (Uso,FKComponente_Monitorado) VALUES (%s,7)'
            valCPU = [cpu]
            mycursor.execute(sql_querryCPU, valCPU)
            mydb.commit()
        if 1 == 1:
            sql_querryRAM = 'INSERT INTO Monitoramento_RAW (Total,Free,Uso,FKComponente_Monitorado) VALUES (%s,%s,%s,8)'
            valRAM = [ram.total,ram.free,ram.percent]
            mycursor.execute(sql_querryRAM, valRAM)
            mydb.commit()
finally:
    if(mydb.is_connected()):
        mycursor.close()
        mydb.close()

