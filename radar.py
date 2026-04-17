import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("Radar Chart")

player = st.text_input("Enter player name:")

def radar_chart(values, labels, title):
    angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False)

    values = np.concatenate((values, [values[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    fig, ax = plt.subplots(subplot_kw={'polar': True})

    ax.plot(angles, values)
    ax.fill(angles, values, alpha=0.3)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    ax.set_title(title)

    return fig

if st.button("Show Player"):

    player = player.lower()

    if player == "messi":
        values = np.array([95, 92, 91])
        labels = ["Dribbling", "Shooting", "Passing"]
        fig = radar_chart(values, labels, "Lionel Messi")
        st.pyplot(fig)

    elif player == "ronaldo":
        values = np.array([88, 94, 93])
        labels = ["Dribbling", "Shooting", "Physical"]
        fig = radar_chart(values, labels, "Cristiano Ronaldo")
        st.pyplot(fig)

    elif player == "mbappe":
        values = np.array([97, 92, 89])
        labels = ["Pace", "Dribbling", "Shooting"]
        fig = radar_chart(values, labels, "Kylian Mbappe")
        st.pyplot(fig)

    else:
        st.error("Player not found")
