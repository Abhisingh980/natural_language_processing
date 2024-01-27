import streamlit as st
import plotly.express as px

from nltk.sentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

list_date = [f'diary/2023-10-{item}.txt' for item in range(21, 28)]

st.title("analysis positivity and negative of diary .. [Diary Tone]")

dictionary = []
for path in list_date:
    with open(path, "r") as file:
        text = file.read()
        dictionary.append(analyzer.polarity_scores(text))


list_date = [index.strip("diary/.txt") for index in list_date]
positivity = [pos['pos'] for pos in dictionary]
negativity = [pos['neg'] for pos in dictionary]

st.subheader("Positivity")

figure = px.line(x=list_date, y=positivity, labels={"x": "Date", "y": "Positivity"})
st.plotly_chart(figure)

st.subheader("Negativity")
figure = px.line(x=list_date, y=negativity, labels={"x": "Date", "y": "Negativity"})
st.plotly_chart(figure)





