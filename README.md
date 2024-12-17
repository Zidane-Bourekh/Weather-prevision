# Weather Data Visualization Project  

## Description  
This project aims to retrieve and visualize weather data while serving as a foundation for future **AI-based weather predictions**.  
In its current version, the project fetches historical weather data for a specified location and date range using the **Meteostat API**, processes it with **Pandas**, and displays it as a clean temperature graph using **Matplotlib** 
it is set for Paris in January 2024 but can be changed if needed please see the tutorial i made below.  

The final goal of this project is to integrate **Artificial Intelligence** models that will predict weather trends for the upcoming days based on historical data. 

The initial development was done in a **Jupyter Notebook** for rapid prototyping and testing. The final code has been consolidated into a standalone **Python script** for clean execution and sharing.

---

## Features  
- Retrieve weather data via **Meteostat API**  
- Process and format data with **Pandas**  
- Display temperature trends using **Matplotlib**  
- Customizable date ranges and cities  

---

## Technical Choices  

### 1. **Jupyter Notebook for Prototyping**  
The development started in a **Jupyter Notebook** to:  
- Explore and test the API while avoiding repetitive API calls.  
- Visualize the results step by step.  

The final code has been moved to a **Python script** (`weather.py`) for better readability and usability.  

### 2. **Use of `.gitignore`**  
To protect sensitive data and keep the repository clean:  
- The `config.py` file containing the **API key** is excluded using `.gitignore`.  
- The working Jupyter Notebook was excluded to keep the repository lightweight.  

---

## Requirements  
To run this project, you need:  
- **Python 3.8+**  
- Python libraries: `requests`, `pandas`, `matplotlib`  
- A free API key from [Meteostat]

---

## Installation  

Follow these steps to set up and run the project:

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/YourUsername/your-repo-name.git
   cd your-repo-name

2. **Create a `config.py` file for your API key**:
   Create a config.py file for your API key:
   API_KEY = "your_api_key_here"

3. **Install the required dependencies**:
   pip install requests pandas matplotlib

4. **Run the script**:
   python weather.py




## How to Customize the Dates and City

Locate this section in the code:
querystring = {
    "lat": "48.8566",       # Latitude for Paris
    "lon": "2.3522",        # Longitude for Paris
    "alt": "35",            # Altitude in meters
    "start": "2024-01-01",  # Start date (YYYY-MM-DD)
    "end": "2024-01-31"     # End date (YYYY-MM-DD)
}

Update the "start" and "end" values with your desired dates.

## Change the City

To fetch data for a different city, update the "lat" (latitude) and "lon" (longitude) values.


## Project structure

weather-data-visualization/  
│  
├── weather.py               # Main Python script
├── weather.ipynb            #Jupyter notebook
├── .gitignore               # Excludes config.py and Jupyter Notebook  
├── config.py                # API key (excluded from repository)  
└── README.md                # Project documentation  

## Future Improvements

This project is a starting point and will be expanded with the following features:

AI-powered predictions for weather trends using Machine Learning
More graphics 
Building a simple user interface for better accessibility


