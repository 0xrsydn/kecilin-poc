import streamlit as st
from ai_itinerary import generate_itinerary
import stripe
import os

stripe.api_key = os.getenv('STRIPE_TEST_API_KEY')

st.title("AI Vacation Planner")

# User preferences
destination = st.text_input("Preferred Destination")
budget = st.number_input("Budget", min_value=0)
dates = st.date_input("Travel Dates", [])
activities = st.text_area("Preferred Activities")

# Payment Information
st.subheader("Payment Information")
card_number = st.text_input("Card Number", value="4242 4242 4242 4242")
expiry_date = st.text_input("Expiry Date (MM/YY)", value="12/34")
cvc = st.text_input("CVC", value="123")

# Confirm Permissions
confirm_booking = st.checkbox("I allow the planner to make bookings on my behalf")

# Submit
if st.button("Plan My Vacation"):
    # Trigger backend planning
    itinerary = generate_itinerary(destination, budget, dates, activities)
    st.write("Planning your vacation...")
    st.write("Here's your itinerary:")
    st.write(itinerary)

    # Create a Stripe Payment Intent
    try:
        payment_intent = stripe.PaymentIntent.create(
            amount=int(budget * 100),  # Amount in cents
            currency='usd',
            payment_method_types=['card'],
        )

        st.write("Please proceed to payment:")
        st.write(f"Payment Intent created with ID: {payment_intent['id']}")

        # Simulate payment success
        st.write("Payment successful! Your booking is confirmed.")
    except Exception as e:
        st.write(f"Booking failed: {e}")