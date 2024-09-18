# miniproject2OakleyCardwell
### INF601 Advanced Programming with Python
### Oakley Cardwell

## Project Description
This project analyzes the trend of global temperatures over the last century (1923 - 2023) using data from NASA's Goddard Institute for Space Studies (GISS).

## Data Source

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
- Python 3.x
- yfinance
- numpy
- matplotlib

### `requirements.txt`

To generate this file, run the following command in your project directory:

```bash
pip freeze > requirements.txt