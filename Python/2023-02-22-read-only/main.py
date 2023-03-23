class User:
    """
    User class
    
    It has some methods and properties to simulate the functions
    of a regular class.
    """
    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def reversed_email(self):
        return self.email[::-1]

    def __str__(self):
        return f"User: {self.email}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @full_name.setter
    def full_name(self, value):
        self.first_name, self.last_name = value.split(" ")

    

class ReadOnlyUser:
    def __init__(self, *args, **kwargs):
        self._user = User(*args, **kwargs)
    
    def __getattr__(self, name):
        return getattr(self._user, name)
    
    def __setattr__(self, name, value):
        if name == "_user":
            super().__setattr__(name, value)
        else:
            raise RuntimeError("This instance is read-only.")


reg_user_1 = User("Joseph", "Test",  "test@test.com", "123456")

fixtured_user = ReadOnlyUser("Fixed", "Test!", "fixed@test.com", "123456")

reg_user_2 = User("James", "Test", "another_test@test.com", "123456")

print("Reading initial values:")
print(reg_user_1.email)
print(fixtured_user.email)
print(reg_user_2.email)

print(" ")
print("Changing values:")
reg_user_1.email = "new_email1@test.com"
reg_user_2.email = "new_email2@test.com" 
try:
    fixtured_user.email = "should not work"
except RuntimeError:
    print("Correctly raised RuntimeError!")
else:
    print("Should not be printed!")

print(" ")
print("Reading values after changes:")
print(reg_user_1.email)
print(fixtured_user.email)
print(reg_user_2.email)

print(" ")
print("Changing values with setters...")
reg_user_1.full_name = "New Name"
try:
    fixtured_user.full_name = "New Name"
except RuntimeError:
    print("Correctly raised RuntimeError!")
else:
    print("Should not be printed!")
reg_user_2.full_name = "New Name 2"

print(" ")
print("Reading values after changes:")
print(reg_user_1.full_name)
print(fixtured_user.full_name)
print(reg_user_2.full_name)