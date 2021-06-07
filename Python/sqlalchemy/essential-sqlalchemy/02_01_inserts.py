from sqlalchemy import insert
from init_db import cookies, connection

# `insert` as a table method
ins_1 = cookies.insert().values(
    cookie_name="chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50",
)
print(f"SQL Statement: {str(ins_1)}")
print(f"Params: {ins_1.compile().params}")
result = connection.execute(ins_1)

# `insert` as a free-standing function
ins_2 = insert(cookies).values(
    cookie_name="chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe.html",
    cookie_sku="CC01",
    quantity="12",
    unit_cost="0.50",
)
print(f"SQL Statement: {str(ins_2)}")
print(f"Params: {ins_2.compile().params}")

print(f"The inserted primary key is {result.inserted_primary_key}")

# `insert` as a simple statement w/ attributes passed to the execution
ins_3 = cookies.insert()
result = connection.execute(
    ins_3,
    cookie_name="dark chocolate chip",
    cookie_recipe_url="http://some.aweso.me/cookie/recipe_dark.html",
    cookie_sku="CC02",
    quantity="1",
    unit_cost="0.75",
)

# Leveraging the last practice to insert multiple items
inventory_list = [
    {
        "cookie_name": "peanut butter",
        "cookie_recipe_url": "http://some.aweso.me/cookie/peanut.html",
        "cookie_sku": "PB01",
        "quantity": "24",
        "unit_cost": "0.25",
    },
    {
        "cookie_name": "oatmeal raisin",
        "cookie_recipe_url": "http://some.okay.me/cookie/raisin.html",
        "cookie_sku": "EWW01",
        "quantity": "100",
        "unit_cost": "1.00",
    },
]
result = connection.execute(ins_3, inventory_list)
