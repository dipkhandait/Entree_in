import sqlite3

connection = sqlite3.connect("Project.db")
cursor = connection.cursor()
S_user = cursor.execute(f"SELECT * FROM Current_login WHERE No = '{1}'")
record = S_user.fetchone()
user = record[0]
print(user)

try:
    Spl_user = cursor.execute(f"SELECT * FROM Col_Pref_list where Username = '{user}'")
    recordpl = Spl_user.fetchone()
    userpl = recordpl[0]
    print(userpl)
    print("SUCCESSFULL")
except Exception as e:
    print("Unsuccessful")
    print(e)