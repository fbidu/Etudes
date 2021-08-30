import capnp  # noqa: F401
import addressbook_capnp as addressbook  # noqa

# Creating a new addressbook
addresses = addressbook.AddressBook.new_message()

# Alice's Data
alice = addressbook.Person.new_message(name="Alice")
alice.id = 1
alice.email = "alice@ali.ce"

# Alice's Phone
alice_phone = alice.init("phones", 1)[0]
alice_phone.type = "mobile"
alice.employment.school = "MIT"

# Bob's Data
bob = addressbook.Person.new_message(name="Bob")
people = addresses.init("people", 2)

people[0] = alice
people[1] = bob

# Dump to disk
f = open("adresses.bin", "w+b")
addresses.write(f)

# Read from disk
f = open("adresses.bin", "rb")
addresses = addressbook.AddressBook.read(f)
print(addresses)
print(addresses.people[0].name)
