import MySQLdb
from modules import Product

class DB(object):
    def __init__(self):
        # Open database connection
        self.db = MySQLdb.connect("localhost","root","yxz1989@UTD","Storage")

    def getAllProducts(self):
        # prepare a cursor object using cursor() method
        cursor = self.db.cursor(MySQLdb.cursors.DictCursor)
        # Prepare SQL query to INSERT a record into the database.
        sql = """
            SELECT * FROM product
        """
        # Execute the SQL command
        cursor.execute(sql)
        # Commit your changes in the database
        # db.commit()
        data = cursor.fetchall()
        self.db.close()
        return data

    def addProduct(self, product):
        print(product)
        pass