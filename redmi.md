# Crime Rate Prediction Tool

This project is a web application that predicts crime rates based on user inputs. It uses Streamlit for the web interface and Google's Generative AI for generating predictions.

## Setup

1. Clone the repository.
2. Install the required packages:
    ```bash
    pip install streamlit google-generativeai
    ```
3. Set your GeminiAI API key in the `app.py` file:
    ```python
    api_key = "YOUR_API_KEY_HERE"
    ```

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```
2. Open the web browser and navigate to the local Streamlit URL.
3. Enter the city name, type of crime, and time period in the input fields.
4. Click the "Predict Crime Rate" button to get the prediction.

## Code Overview

### app.py

- **Imports**: The necessary libraries are imported, including Streamlit and Google's Generative AI.
- **API Key Configuration**: The GeminiAI API key is set up.
- **User Inputs**: The app takes user inputs for city name, type of crime, and time period.
- **Prediction**: When the "Predict Crime Rate" button is clicked, a prompt is generated and sent to the Generative AI model to get the prediction.
- **Display**: The predicted crime rate is displayed in a text area.

