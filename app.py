import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Player Search", layout="centered")

st.title("Player Search Dashboard")

# ========================
# FAKE DATA (možeš kasnije menjati)
# ========================
players = {
    "Messi": [90, 85, 92, 88, 95],
    "Ronaldo": [85, 90, 80, 87, 89],
    "Mbappe": [88, 78, 85, 90, 91]
}

labels = ["Pace", "Shooting", "Passing", "Dribbling", "Physical"]

# ========================
# SEARCH
# ========================
player_name = st.text_input("Enter player name:")

# ========================
# BUTTON
# ========================
if st.button("Show Player"):
    if player_name in players:

        values = players[player_name]

        # pizza chart
        fig, ax = plt.subplots()
        ax.pie(values, labels=labels, autopct='%1.1f%%')
        ax.set_title(player_name)

        st.pyplot(fig)

    else:
        st.error("Player not found")
