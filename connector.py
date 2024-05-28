import mysql.connector 

class Connector:
    db = mysql.connector.connect (
        host ="localhost",
        user="root",
        password="",
        db="student_information system")
    cursor = db.cursor()