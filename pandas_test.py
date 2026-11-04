import pandas as pd

data = {"pangalan": ["Ana", "Ben", "Cara"], "marka": [85, 92, 78]}
df = pd.DataFrame(data)
print(df)

print(df["marka"])