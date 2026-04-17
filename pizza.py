import streamlit as st
import matplotlib.pyplot as plt

st.title("Player Pizza Chart")

player = st.text_input("Enter player name:")

def pizza_chart(values, labels, title):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.0f%%')
    ax.set_title(title)
    return fig

if st.button("Show Player"):

    player = player.lower()

    if player == "messi":
        values = [95, 92, 91]
        labels = ["Dribbling", "Shooting", "Passing"]
        fig = pizza_chart(values, labels, "Lionel Messi")
        st.pyplot(fig)

    elif player == "ronaldo":
        values = [88, 94, 93]
        labels = ["Dribbling", "Shooting", "Physical"]
        fig = pizza_chart(values, labels, "Cristiano Ronaldo")
        st.pyplot(fig)

    elif player == "mbappe":
        values = [97, 92, 89]
        labels = ["Pace", "Dribbling", "Shooting"]
        fig = pizza_chart(values, labels, "Kylian Mbappe")
        st.pyplot(fig)

    else:
        st.error("Player not found")
