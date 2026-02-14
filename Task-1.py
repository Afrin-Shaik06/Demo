
import pandas as pd
import random
from faker import Faker
import dask.dataframe as dd

fake = Faker()

# Number of rows
n = 1_000_000

print("Step 1: Generating dataset... Please wait.")

data = {
    "id": range(1, n + 1),
    "name": [fake.name() for _ in range(n)],
    "age": [random.randint(21, 60) for _ in range(n)],
    "salary": [random.randint(20000, 150000) for _ in range(n)],
    "department": [random.choice(["HR", "IT", "Sales", "Finance", "Marketing"]) for _ in range(n)]
}

df = pd.DataFrame(data)

df.to_csv("employees.csv", index=False)

print("CSV file generated successfully.\n")

print("Step 2: Loading CSV using Dask...")

ddf = dd.read_csv("employees.csv")

print("\nFirst 10 Rows of Dask DataFrame:")
print(ddf.head(10))

print("\nNumber of Partitions in Dask DataFrame:")
print(ddf.npartitions)
