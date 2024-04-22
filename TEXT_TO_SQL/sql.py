import sqlite3

#connection
connection = sqlite3.connect("student.db")

cursor = connection.cursor()


#table_info="""
#Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
#SECTION VARCHAR(25),MARKS INT);"""



#cursor.execute(table_info)

cursor.execute('''Insert Into STUDENT values('Balanarayanan','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Riswi R','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Saurav','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Harrel','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Adwaith','DEVOPS','A',35)''')


print("The isnerted records are")
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()