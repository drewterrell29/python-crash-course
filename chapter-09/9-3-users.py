class User:
    """A resturant"""
    def __init__(self, first_name, last_name, **attributes):
        self.first_name = first_name
        self.last_name = last_name
        self.attributes = attributes

    def describe(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Attributes:")
        for k,v in self.attributes.items():
            print(f"- {k}: {v}")

myself = User("Drew", "Terrell", height="tall", hair="red", level="strong")

myself.describe()