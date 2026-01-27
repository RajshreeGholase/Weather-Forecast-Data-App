import streamlit as st
import plotly.express as px
from backend import get_data

# Add title, text input, slider, selectbox, and subheader
st.title("Weather Forecast For The Next Days")
place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5,
                 help="Select the number of forecasted days")

option = st.selectbox("Select data to view",
              ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
   # get the temperature/sky data
   try:
      filtered_data = get_data(place, days, option)

      if option == "Temperature":
          temperatures = [dict["main"]["temp"] / 10 for dict in filtered_data]
          dates = [dict["dt_txt"] for dict in filtered_data]
          # create a  temperature plot
          figure = px.line(x=dates, y=temperatures, labels={"x": "Date", "y": "Temperature (Celsius)"})
          st.plotly_chart(figure) # here plotly is a famous data visualization

      if option == "Sky":
          images = {"Clear": "Images/clear.png","Clouds": "Images/cloud.png",
                 "Rain": "Images/rain.png","Snow": "Images/snow.png"}
          sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
          image_paths = [images[condition] for condition in sky_conditions]
          st.image(image_paths, width=115)

   except KeyError:
       st.write("That place does not exist")