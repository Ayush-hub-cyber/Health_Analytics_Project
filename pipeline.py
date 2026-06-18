import pandas as pd

print("🚀 Starting Health Data Pipeline...")

# --- PHASE 1: Data Ingestion ---
try:
    # Load the raw CSV file into a Pandas "DataFrame" (think of it like a virtual Excel sheet)
    df = pd.read_csv('large_patient_data.csv')
    print(f"✅ Loaded {len(df)} raw patient records.")
except FileNotFoundError:
    print("❌ Error: 'patient_data.csv' not found. Please make sure it is saved in this folder.")
    exit()

# --- PHASE 2: Data Cleaning ---
# Force everything to be a number. 'coerce' takes words like "Error" and turns them into NaN (Not a Number)
df['Weight_kg'] = pd.to_numeric(df['Weight_kg'], errors='coerce')
df['Height_m'] = pd.to_numeric(df['Height_m'], errors='coerce')

# Drop any rows that have missing data (NaN) or where height is 0 (to prevent math errors)
df = df.dropna()
df = df[df['Height_m'] > 0]
print(f"🧹 Cleaned data: {len(df)} valid records remain.")

# --- PHASE 3: Data Processing (The Engine) ---
# Calculate BMI for thousands of rows instantly using vectorized math
df['BMI'] = df['Weight_kg'] / (df['Height_m'] ** 2)
df['BMI'] = df['BMI'].round(2)

# Define our categorization logic
def get_category(bmi):
    if bmi < 18.5: return "Underweight"
    elif 18.5 <= bmi < 24.9: return "Normal weight"
    elif 25 <= bmi < 29.9: return "Overweight"
    else: return "Obese"

# Apply the logic to every single row in the dataset
df['Category'] = df['BMI'].apply(get_category)

# --- PHASE 4: Data Export ---
output_filename = 'clean_patient_report.csv'
df.to_csv(output_filename, index=False)

print(f"💾 Pipeline complete! Successfully exported to: {output_filename}")