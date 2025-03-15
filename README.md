# Car Market Analysis

This web application is designed to analyze car market data through visualizations and interactive features. It uses **Streamlit**, **Pandas**, **Plotly**, and **Matplotlib** to generate histograms, scatter plots, and other visualizations from the car advertisement dataset.

## Features

- **Price vs. Mileage**: A scatter plot showing the relationship between car prices and their mileage (odometer readings).
- **Car Price Distribution**: A histogram displaying the distribution of car prices.
- **Interactive Filters**: A checkbox to adjust visualizations based on user input.

## Technologies Used

- **Streamlit**: For building the web application interface.
- **Pandas**: For data manipulation and cleaning.
- **Plotly**: For interactive plots and visualizations.
- **Matplotlib**: For additional plotting capabilities.

## How to Run the Project Locally

1. Clone the repository:
    ```bash
    git clone https://github.com/TwyattDS/car_market_analysis.git
    ```

2. Navigate into the project directory:
    ```bash
    cd car_market_analysis
    ```

3. Set up a virtual environment:
    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:
    - On Windows:
      ```bash
      .\venv\Scripts\Activate
      ```
    - On Mac/Linux:
      ```bash
      source venv/bin/activate
      ```

5. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

7. Open the provided URL in your web browser to view the app.

## Deployment

The app is deployed on **Render** and can be accessed here: [https://car-market-analysis-t1gc.onrender.com]
