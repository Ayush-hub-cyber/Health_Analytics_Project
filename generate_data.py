import pandas as pd
import numpy as np

print("⚙️ Generating 100,000 patient records...")

# Generate 100,000 random realistic heights and weights
np.random.seed(42)
ids = np.arange(10001, 110001)
weights = np.random.normal(loc=70.0, scale=15.0, size=100000)
heights = np.random.normal(loc=1.65, scale=0.15, size=100000)

# Create the dataframe
df = pd.DataFrame({'Patient_ID': ids, 'Weight_kg': weights, 'Height_m': heights})

# Inject "bad data" for your pipeline to catch
df.loc[150:200, 'Weight_kg'] = np.nan
df.loc[5000:5050, 'Height_m'] = 0.0

# NEW FIX: Convert the column to 'object' (mixed types) before injecting text
df['Weight_kg'] = df['Weight_kg'].astype(object)
df.loc[99000:99010, 'Weight_kg'] = "Error"

# Save it to a massive CSV file
df.to_csv('large_patient_data.csv', index=False)
print("✅ Created 'large_patient_data.csv' (100,000 rows) successfully!")