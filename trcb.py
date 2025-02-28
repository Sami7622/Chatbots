import streamlit as st # type: ignore
import google.generativeai as genai # type: ignore



genai.configure(api_key='Your_api_key_here')


st.title('Travel Recommendation Bot')
st.write('Welcome to the Travel Recommendation Bot! Please answer the following questions to get a travel recommendation.')

with st.form('my_form'):
    city = st.text_input('What city are you traveling to?')
    start_date = st.date_input('When are you planning to travel?')
    end_date = st.date_input('When are you planning to return?')
    places = st.text_input('What are some places you would like to visit?(like beaches, museums, etc.)')
    submit = st.form_submit_button('Submit')
    if submit:
        instruction = f"Consider the {start_date} and {end_date} for the vacation in the city {city} and generate an itenary to cover most popular places in the city. Never forget to include mentioned places {places}."
        system_instruction = "You are an expert Travel recommendation Bot. "

        try:
            model = genai.GenerativeModel(
                "models/gemini-1.5-flash",
                system_instruction=system_instruction,
            )
            response = model.generate_content(instruction)
            st.write(response.text)
        except Exception as e:
            st.error(f"An error occurred: {e}")







