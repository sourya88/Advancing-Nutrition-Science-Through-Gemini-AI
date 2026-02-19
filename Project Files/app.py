

import streamlit as st
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
import os


API_KEY = "Google_StudioAI_Key"

genai.configure(api_key=API_KEY)

llm = GoogleGenerativeAI(
    model="gemini-2.5-flash",  
    google_api_key=API_KEY,
    temperature=0.7
)

nutritional_info_template = PromptTemplate(
    input_variables=["food_items"],
    template="""Provide detailed nutritional information for the following food items: {food_items}.
Include macronutrients (protein, fat, carbohydrates), micronutrients (vitamins, minerals), and calorie content."""
)

def get_food_items_input():
    with st.form("food_items_input_form"):
        food_items = st.text_area("Enter Food Items (comma separated)")
        submitted = st.form_submit_button("Get Nutritional Information")
        if submitted:
            return {"food_items": food_items}

def get_nutritional_info_response(input_data):
    prompt = nutritional_info_template.format(**input_data)
    return llm.invoke(prompt)

st.title("NutriAI - Instant Nutritional Information")

input_data = get_food_items_input()

if input_data:
    with st.spinner("Fetching nutritional information..."):
        response = get_nutritional_info_response(input_data)
        st.subheader("Nutritional Information")
        st.write(response)

