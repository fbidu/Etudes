from init_db import cookies, connection
from sqlalchemy import select

# Select as a 'free-standing' function
s = select([cookies])

print(s)
rp = connection.execute(s)  # rp = ResultProxy

results = rp.fetchall()
print(results)

# Select as a table attribute
s = cookies.select()
rp = connection.execute(s)

print(f"{rp.fetchone()=}")
print(f"{rp.keys()=}")

print("*" * 80)
# A bunch of column selects
first = rp.first()
print(f"{first[1]=}")
print(f"{first.cookie_name=}")
print(f"{first[cookies.c.cookie_name]=}")
