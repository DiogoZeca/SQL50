# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# | referee_id  | int     |
# +-------------+---------+
# In SQL, id is the primary key column for this table.
# Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.

 

# Find the names of the customer that are not referred by the customer with id = 2.

# Return the result table in any order.


import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    df = customer[(customer['referee_id']!=2) | (customer['referee_id'].isnull())]
    return(df['name'].to_frame())