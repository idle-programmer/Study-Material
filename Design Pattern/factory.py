"""
The Factory Method Pattern is used to create objects without exposing the instantiation logic to the client.
It defines an interface for creating an object, but allows subclasses or factories to decide which class to instantiate.
For example:
1) If we need to create multiple notification types (SMS, Email, Push), we can use a factory method to return the
appropriate notification object based on user input.
2) Payment gateways (Razorpay, Stripe, etc.)
3) Database drivers (MySQL, PostgreSQL, SQLite)
"""

class MySQLdb:
    def connect(self):
        print("Connecting to MySQL Database")


class PostgresSQLdb:
    def connect(self):
        print("Connecting to PostresSQL Database")


class DatabaseFactory:
    @staticmethod
    def get_database(db_type):
        if db_type == "mysql":
            return MySQLdb()
        elif db_type == "postgressql":
            return PostgresSQLdb()
        else:
            raise ValueError("Unsupported database type")


db = DatabaseFactory.get_database("mysql")
db.connect()
