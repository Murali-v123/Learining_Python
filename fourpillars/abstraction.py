# Design a Phone class with methods to call_contact and take_picture. Abstract away any internal processing details and focus on creating a user-friendly interface.


class Phone:
    def __init__(self, mobile):
        self.mobile = mobile
        # self.contact=contact

    def call_contact(self, contact):
        print(f"calling to {contact}")

    def take_picture(self):
        print("Say cheese")
        print("picture taken")


sam = Phone("Samsung")
sam.call_contact("murali")
sam.take_picture()


class Database:
    def __init__(self):
        self.__storage = {}

    def save_data(self, key, value):
        self.__storage[key] = value
        print(f"Data saved for {key}")

    def get_data(self, key):
        return self.__storage.get(key, "No data found")


db = Database()
db.save_data("user_101", {"name": "Raj", "age": 30})
print(db.get_data("user_101"))


# i = 10
# try:
#     print(i / 0)
# except Exception as e:
#     print(f"An error occurred: {e}")
# finally:
#     print("Execution completed.")

# a=10
# b=20
# c=26
# print(a) if(a>b) else print(b) if(a==b) else print(c) 