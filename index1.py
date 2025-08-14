import requests
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random

# Step 1: Simulate API data for last 15 days
def get_mock_accident_data():
    today = datetime.now()
    data = []
    for i in range(15):
        date = (today - timedelta(days=14 - i)).strftime("%Y-%m-%d")
        accidents = random.randint(100, 300)  # Simulating accident numbers
        data.append({"date": date, "accidents": accidents})
    return {"status": "success", "data": data}

# Step 2: Fetch data (simulate API response)
response = get_mock_accident_data()
dates = [entry['date'] for entry in response['data']]
accidents = [entry['accidents'] for entry in response['data']]

# Step 3: Visualize data
plt.figure(figsize=(12, 6))
plt.plot(dates, accidents, marker='o', linestyle='-', color='orange')
plt.title("Simulated Daily Road Accidents (Last 15 Days)")
plt.xlabel("Date")
plt.ylabel("Number of Accidents")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()