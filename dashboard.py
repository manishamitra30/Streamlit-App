import streamlit as st
import plotly.graph_objects as go
import requests
import random

st.set_page_config(page_title="Persona Cloak Command Center", layout="wide")

# ---- CONFIG ----
USE_BACKEND = False   # change to True when Poonam gives API
BACKEND_URL = "http://localhost:8000/generate_bait_profile"


# ---- MOCK FUNCTION (FOR NOW) ----
def mock_api():
    bio_list = [
        "I enjoy cooking, exploring new hiking trails, and reading sci-fi.",
        "Tech enthusiast who loves building apps and drinking too much coffee.",
        "Creative writer who spends weekends painting and gaming."
    ]
    return {
        "bio": random.choice(bio_list),
        "personality": {
            "openness": round(random.uniform(0.2, 0.9), 2),
            "conscientiousness": round(random.uniform(0.2, 0.9), 2),
            "extraversion": round(random.uniform(0.2, 0.9), 2),
            "agreeableness": round(random.uniform(0.2, 0.9), 2),
            "neuroticism": round(random.uniform(0.2, 0.9), 2)
        }
    }


# ---- CALL BACKEND OR MOCK ----
def get_bait_profile():
    if USE_BACKEND:
        response = requests.post(BACKEND_URL)
        return response.json()
    else:
        return mock_api()
# ---- UI ----
st.title("🛡 Persona Cloak — Command Center Dashboard")
st.write("Generate and visualize bait profiles used for adversarial personality cloaking.")

if st.button("Generate Bait Profile"):
    data = get_bait_profile()

    st.subheader("Generated Bio")
    st.info(data["bio"])

    st.subheader("Personality Scores")
    traits = data["personality"]
    st.json(traits)

    # Radar Chart
    st.subheader("Radar Chart (Big Five Traits)")

    labels = list(traits.keys())
    values = list(traits.values())

    labels += labels[:1]    # close loop
    values += values[:1]

    fig = go.Figure(
        data=[go.Scatterpolar(
            r=values,
            theta=[label.capitalize() for label in labels],
            fill='toself'
        )],
        layout=go.Layout(
            polar=dict(radialaxis=dict(range=[0, 1], visible=True)),
            showlegend=False
        )
    )


    st.plotly_chart(fig, use_container_width=True)
