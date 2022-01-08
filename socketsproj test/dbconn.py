import mysql.connector
from datetime import datetime, timedelta
import hashlib


class DBconnect:

    mydb = mysql.connector.connect(
        host="localhost",
        user="OVS",
        password="THimberland0&3"

    )
    mycursor = mydb.cursor()

    mycursor.execute("USE testdatabase")

    def insertElection(self, list):
        try:
            sql = "INSERT INTO election (id, name, type, faculty, date, starttime, stoptime, status) VALUES (%s, %s,%s,%s,%s, %s,%s,%s)"
            self.mycursor.execute(sql, list)
            self.mydb.commit()
            print("added election")
        except mysql.connector.errors.IntegrityError:
            print(f"Election {list[0]} already exist")

    def insertPositions(self, position):
        sql = "INSERT INTO positions(electionId, post) VALUES(%s,%s)"
        self.mycursor.executemany(sql, position)
        self.mydb.commit()
        print("added positions")

    def insertUsers(self, user):
        print(user)
        user[3] = hashlib.sha256(user[3].encode("utf-8")).hexdigest()
        try:
            sql = "INSERT INTO users(matricNo, department, level, password) VALUES(%s, %s, %s, %s)"
            self.mycursor.execute(sql, user)
            self.mydb.commit()
            return "Done"
        except mysql.connector.errors.IntegrityError:
            return "Duplicate id"

    def login(self, data):
        self.mycursor.execute(f"SELECT * FROM users WHERE(matricNo = '{data[0]}')")
        result = self.mycursor.fetchone()
        if hashlib.sha256(data[1].encode()).hexdigest() == result[3]:
            print(result)
            return result
        else:
            print("Invalid login details")
            return False


    def getElections(self):
        self.mycursor.execute(f"SELECT id, name, status  FROM election")
        result = self.mycursor.fetchall()
        print(f"[ALERT] {len(result)} election retrieved")
        return result

    def selectElection(self, data):
        self.mycursor.execute(f"SELECT *  FROM election WHERE(id='{data}')")
        result = self.mycursor.fetchone()
        print(f"[ALERT]:Election {data} data  retrieved!")
        return result




