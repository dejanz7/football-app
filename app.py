import streamlit as st

st.title("Player Search Dashboard")

player = st.text_input("Enter player name:")

if st.button("Show Player"):

    player = player.lower()

    if player == "messi":
        st.success("Lionel Messi")
        st.write("Dribbling: 95")
        st.write("Shooting: 92")
        st.write("Passing: 91")

    elif player == "ronaldo":
        st.success("Cristiano Ronaldo")
        st.write("Dribbling: 88")
        st.write("Shooting: 94")
        st.write("Physical: 93")

    elif player == "mbappe":
        st.success("Kylian Mbappe")
        st.write("Pace: 97")
        st.write("Dribbling: 92")
        st.write("Shooting: 89")

    else:
        st.error("Player not found")
