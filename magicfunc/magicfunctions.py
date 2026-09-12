class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def __str__(self):
        return f"{self.name}-{self.id}"

    def __len__(self):
        return len(self.name)

    def __repr__(self):
        return f"Employee('{self.name}', {self.id})"