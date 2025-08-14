# Task-1
API INTEGRATION AND DATA VISUALIZATION
## 📊 Simulated Road Accident Data Visualization

This Python script generates and visualizes *mock daily road accident data* for the last 15 days.
It is useful for *data visualization practice, **API simulation, or as a **template* for projects involving time-series data plotting.

### 🚀 Features

* *API Simulation*: Mimics fetching accident data from an API without needing an actual backend.
* *Random Data Generation*: Uses random.randint() to create realistic accident counts between 100–300 per day.
* *Time-Series Plotting*: Plots the accident trend over the past 15 days using Matplotlib.
* *Clean Visualization*: Includes date labels, markers, grid lines, and automatic layout adjustment.

### 🛠 Technologies Used

* *Python* (Core language)
* *Matplotlib* (Data visualization)
* *Datetime* (Date manipulation)
* *Random* (Data simulation)

### 📂 How It Works

1. *Data Simulation*

   * The function get_mock_accident_data() creates a list of dictionaries containing:

     * date: Each day in the last 15 days.
     * accidents: A random accident count between 100 and 300.

2. *Data Extraction*

   * The script processes the simulated API response to get lists of dates and accidents.

3. *Data Visualization*

   * A *line chart* is plotted with:

     * X-axis → Dates
     * Y-axis → Accident count
     * Orange line with circular markers
     * Rotated date labels for clarity

### 📸 Example Output

The output will be a *line chart* showing daily accident counts with a visible trend over 15 days.

### ▶ How to Run

```bash
# Install dependencies
pip install matplotlib requests
