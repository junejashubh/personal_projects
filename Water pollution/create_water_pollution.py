import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Define parameters
countries_cities = {
    'USA': ['New York', 'Los Angeles'],
    'India': ['Mumbai', 'Delhi'],
    'China': ['Beijing', 'Shanghai'],
    'Brazil': ['Rio de Janeiro', 'São Paulo'],
    'Germany': ['Berlin', 'Munich']
}
water_sources = ['River', 'Lake', 'Bay', 'Canal']

# Date range
start_date = datetime(2019, 1, 1)
end_date = datetime(2023, 12, 31)
date_range = pd.date_range(start=start_date, end=end_date)

# Function to generate realistic pollution patterns
def generate_pollution_data(city, date):
    # Introduce seasonality (more pollution during summer months)
    month = date.month
    is_summer = month in [6, 7, 8]
    
    # Introduce patterns based on city
    if city in ['New York', 'Berlin']:
        base_pollution = 30  # Cleaner cities
    elif city in ['Mumbai', 'Beijing']:
        base_pollution = 60  # More industrial areas
    else:
        base_pollution = 45  # Intermediate
    
    pollution_index = base_pollution + random.uniform(-10, 10)
    if is_summer:
        pollution_index += 10  # Higher pollution in summer
    
    # Generate other parameters based on pollution index
    ph = round(7.0 + random.uniform(-0.5, 0.5), 2)
    dissolved_oxygen = round(max(2, 10 - (pollution_index / 10)), 2)
    bod = round(random.uniform(2, 10) + (pollution_index / 10), 2)
    cod = round(bod * 2, 2)
    nitrates = round(random.uniform(5, 20) * (pollution_index / 100), 2)
    phosphates = round(random.uniform(0.1, 1) * (pollution_index / 100), 3)
    lead = round(random.uniform(0.01, 0.1) * (pollution_index / 100), 3)
    mercury = round(random.uniform(0.001, 0.01) * (pollution_index / 100), 4)
    
    return ph, dissolved_oxygen, bod, cod, nitrates, phosphates, lead, mercury, pollution_index

# Generate dataset
data = []

for date in date_range:
    for country, cities in countries_cities.items():
        for city in cities:
            water_source = random.choice(water_sources)
            ph, dissolved_oxygen, bod, cod, nitrates, phosphates, lead, mercury, pollution_index = generate_pollution_data(city, date)
            data.append([date, country, city, water_source, ph, dissolved_oxygen, bod, cod, nitrates, phosphates, lead, mercury, pollution_index])

# Create DataFrame
columns = ['Date', 'Country', 'City', 'Water Source', 'pH Level', 'Dissolved Oxygen (mg/L)', 'Biological Oxygen Demand (BOD)', 
           'Chemical Oxygen Demand (COD)', 'Nitrates (mg/L)', 'Phosphates (mg/L)', 'Lead (mg/L)', 'Mercury (mg/L)', 'Pollution Index']
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('water_pollution_dataset.csv', index=False)

print("Dataset generated and saved as 'water_pollution_dataset.csv'")
