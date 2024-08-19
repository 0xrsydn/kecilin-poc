import streamlit as st
from ai_itinerary import generate_itinerary

st.title("AI Vacation Planner")

# User preferences
destination = st.text_input("Preferred Destination")
budget = st.number_input("Budget", min_value=0)
dates = st.date_input("Travel Dates", [])
activities = st.text_area("Preferred Activities")

# Payment Information (placeholder for secure handling)
payment_info = st.text_input("Payment Information", type="password")

# Confirm Permissions
confirm_booking = st.checkbox("I allow the planner to make bookings on my behalf")

# Submit
if st.button("Plan My Vacation"):
    # Trigger backend planning
    itinerary = generate_itinerary(destination, budget, dates, activities)
    st.write("Planning your vacation...")
    st.write("Here's your itinerary:")
    st.write(itinerary)