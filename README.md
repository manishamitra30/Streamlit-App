# 🛡 Persona Cloak – Command Center Dashboard  
Streamlit Web App for Generating & Visualizing Bait Profiles

This is the frontend dashboard for the *Persona Cloak* project.  
It lets the team generate bait profiles, view personality scores, and visualize traits using a radar chart.

This dashboard is built by *Manisha (Frontend)*.

---

## 🚀 Features

### ✔ Generate Bait Profile
Clicking *"Generate Bait Profile"* displays:
- A generated *bio*
- *Big Five personality scores*
- A *radar chart* (Plotly)

### ✔ Clean & Simple UI  
Runs on Streamlit with mock data or real backend API.

### ✔ Backend-Ready  
The backend (Poonam’s ML function) is expected to return:

```json
{
  "bio": "Generated biography text...",
  "personality": {
    "openness": 0.73,
    "conscientiousness": 0.41,
    "extraversion": 0.55,
    "agreeableness": 0.62,
    "neuroticism": 0.19
  }
}
