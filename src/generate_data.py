import pandas as pd
import numpy as np

# Same random values generate karne ke liye
np.random.seed(42)

# 100 records ke liye advertising budget generate karna
tv = np.random.uniform(10, 300, 100)
radio = np.random.uniform(1, 50, 100)
newspaper = np.random.uniform(1, 100, 100)

# Advertising budget ke basis par sales calculate karna
noise = np.random.normal(0, 2, 100)

sales = (
    3
    + 0.045 * tv
    + 0.18 * radio
    + 0.006 * newspaper
    + noise
)

# DataFrame create karna
df = pd.DataFrame({
    "TV": tv,
    "Radio": radio,
    "Newspaper": newspaper,
    "Sales": sales
})

# CSV file save karna
df.to_csv("data/advertising_data.csv", index=False)

print("Dataset created successfully!")
print("Dataset shape:", df.shape)
print(df.head())