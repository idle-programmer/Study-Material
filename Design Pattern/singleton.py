"""
Singleton pattern is a design pattern which restricts a class to instantiate its multiple objects.
It is nothing but a way of defining a class. Class is defined in such a way that only one instance
of the class is created in the complete execution of the program/project (during runtime).
Example:
1) Database Connection Pool
2) Logging
"""

class ControlTower:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            print("Initializing Control Tower!")
        return cls.__instance


tower1 = ControlTower()
tower2 = ControlTower()
print(tower1 is tower2)


class DatabasePool:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.pool = []  # simulate a connection pool
            cls.__instance.max_size = 5
            print("DB Pool created")
        return cls.__instance
    
db1 = DatabasePool()
db2 = DatabasePool()
print(db1 is db2)