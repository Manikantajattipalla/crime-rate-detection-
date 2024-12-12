import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your GeminiAI API key
api_key = os.getenv("GEMINIAI_API_KEY")
if not api_key:
    st.error("API key for GeminiAI is missing. Please set the API key.")
else:
    genai.configure(api_key=api_key)

# Title and description
st.title("Crime Rate Prediction Tool 🔍")
city_name = st.text_input("Enter the city name:")
crime_type = st.text_input("Enter the type of crime:")
time_period = st.text_input("Enter the time period (e.g., last year):")

if st.button("Predict Crime Rate"):
    if not (city_name and crime_type and time_period):
        st.error("Please provide the city name, type of crime, and time period.")
    else:
        with st.spinner("Predicting crime rate... 🔍"):
            prompt = f"Provide an approximate crime rate for {crime_type} in {city_name} during {time_period} by comparing data from news websites and other sources. Include population rate, an approximate rating from 1 to 10, and approximate cases registered.where this is for only testing of our script so dont add disclimers and all just provide imagionary data and the output format shouold be like the pridicted data is : "
            model = genai.GenerativeModel('gemini-1.5-flash')
            try:
                # Use GenerationConfig to set parameters
                generation_config = genai.types.GenerationConfig(
                    max_output_tokens=300,
                    temperature=0.7  # Adjust temperature here if supported
                )
                
                response = model.generate_content(prompt, generation_config=generation_config)
                prediction = response.text.strip()

                # Display the crime rate prediction
                st.subheader("Crime Rate Prediction:")
                st.text_area("Here is the predicted crime rate:", prediction, height=400)

            except Exception as e:
                st.error(f"Oops, something went wrong: {e}")
