class SmartDevice:
    # The Constructor method
    def __init__(self, brand, device_type):
        self.brand = brand          # Instance attribute
        self.device_type = device_type  # Instance attribute
        self.is_on = False          # Default attribute state

    # A regular method
    def info(self):
        print(f"{self.brand} {self.device_type}.")

# Creating objects (this automatically triggers __init__)
phone = SmartDevice("Apple", "iPhone")
tv = SmartDevice("Samsung", "Smart TV")

# Accessing attributes and methods
print(phone.brand)  
tv.info()  
phone.info()  