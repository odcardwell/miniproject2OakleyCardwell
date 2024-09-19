# miniproject2OakleyCardwell
### INF601 Advanced Programming with Python
### Oakley Cardwell

## Project Description
This project analyzes the trend of global temperatures over the last century (1923 - 2023) using data from NASA's Goddard Institute for Space Studies (GISS).

### Data Explanation
This project analyzes global average temperature anomalies over the last century to understand the trend of global temperatures. A temperature anomaly represents the difference between the observed temperature and a reference (baseline) temperature. Using anomalies instead of absolute temperatures allows for a more accurate assessment of temperature changes over time and across different regions.

### Key Points

- Temperature Anomalies: Indicate how much warmer or cooler a given year was compared to the baseline period.
- Baseline Period: The reference period against which anomalies are calculated, often a multi-decade average.
- Data Visualization: The graph plots annual average temperature anomalies from 1923 to 2023, revealing trends in global temperature changes.
- Trend Analysis: A linear trend line is included to highlight the overall increase in global temperatures over the past century.

### Understanding the Graph

The upward trend in the graph illustrates that global temperatures have been increasing over the last 100 years.
This trend is a clear indication of global warming, largely attributed to human activities like burning fossil fuels and deforestation.
The graph serves as a visual representation of climate change, emphasizing the urgency for environmental action.

### Data Source

- **NASA GISTEMP Team**: [GISS Surface Temperature Analysis (GISTEMP v4)](https://data.giss.nasa.gov/gistemp/)
- **Data File**: [GLB.Ts+dSST.csv](https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/odcardwell/miniproject2OakleyCardwell.git
    ```

2. Navigate to the project folder:
    ```bash
    cd /miniproject2OakleyCardwell
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Run the script:
```bash
python temperature_trend.py
```

The temperature trend plot will be saved in the charts directory as global_temperature_trend.png.

## Requirements

### `requirements.txt`

To generate this file, run the following command in your project directory:

```bash
pip freeze > requirements.txt