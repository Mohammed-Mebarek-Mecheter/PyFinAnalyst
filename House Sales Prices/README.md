# House Sales Analysis

## Overview

RealAgents is a real estate company aiming to optimize house listing prices by predicting sale prices based on property characteristics. The project involves analyzing house sales data to understand factors influencing sale prices, geographic trends, and seasonal patterns. Predictive modeling techniques are employed to develop accurate price prediction models.

## Data

The dataset contains records of previous houses sold in the area. The columns and criteria for data cleaning are as follows:

- house_id: Nominal. Unique identifier for houses.

- city: Nominal. The city in which the house is located. One of 'Silvertown', 'Riverford', 'Teasdale', and 'Poppleton'. Replace missing values with "Unknown".

- sale_price: Discrete. The sale price of the house in whole dollars. Values can be any positive number greater than or equal to zero. Remove missing entries.

- sale_date: Discrete. The date of the last sale of the house. Replace missing values with 2023-01-01.

- months_listed: Continuous. The number of months the house was listed on the market prior to its last sale, rounded to one decimal place. Replace missing values with the mean number of months listed, rounded to one decimal place.

- bedrooms: Discrete. The number of bedrooms in the house. Any positive values greater than or equal to zero. Replace missing values with the mean number of bedrooms, rounded to the nearest integer.

- house_type: Ordinal. One of "Terraced" (two shared walls), "Semi-detached" (one shared wall), or "Detached" (no shared walls). Replace missing values with the most common house type.

- area: Continuous. The area of the house in square meters, rounded to one decimal place. Replace missing values with the mean, to one decimal place.


## Analysis Overview

1. **Time-to-Sale Analysis**:
    - Calculate average time-to-sale for different property types.
    - Use the Kaplan-Meier estimator to visualize survival curves.

2. **Temporal Analysis**:
    - Explore temporal trends in sale prices and transaction volume.

3. **Geographic Trends**:
    - Analyze average sale prices and correlations by city.

4. **House Sales Price Factors**:
    - Investigate factors influencing sale prices using descriptive statistics and regression analysis.

5. **Market Segmentation**:
    - Segment the housing market based on specific criteria.

6. **Predictive Modeling**:
    - Develop machine learning models (Linear Regression, Random Forest Regressor, Gradient Boosting Regressor, XGBoost Regressor) to predict sale prices.
    - Perform hyperparameter tuning using grid search.
    - Evaluate model performance using mean squared error.

## Implementation Details

The project code is organized into Jupyter Notebooks for each analysis step:
- Time-to-Sale Analysis.ipynb
- Temporal Analysis.ipynb
- Geographic Trends.ipynb
- House Sales Price Factors.ipynb
- Market Segmentation.ipynb
- Predictive Modeling.ipynb

The notebooks contain detailed explanations, code, visualizations, and results for each analysis step.

## Results

The project demonstrates the effectiveness of predictive modeling techniques in accurately predicting house sale prices. Each analysis step provides valuable insights for optimizing listing prices and improving sales strategies.

## Author

- **Mohammed Mebarek Mecheter**
- **Contact**: mohammedmecheter@gmail.com
- **LinkedIn**: [Mohammed Mebarek Mecheter](https://www.linkedin.com/in/mohammed-mecheter/)

## Contributing

Contributions to the project are encouraged. For issues or suggestions, please open an issue or submit a pull request. Your feedback is valued and appreciated.

