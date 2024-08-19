import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import streamlit as st

def generate_itinerary(destination, budget, dates, activities):
    # Ensure the GROQ API key is set in the environment
    os.environ["GROQ_API_KEY"]

    # Initialize the model
    model = ChatGroq(
        temperature=0.4,
        model="llama3-8b-8192"
    )

    # Define the prompt template for generating itineraries
    system = "You are an AI travel planner. Please plan a vacation to {destination} with the following preferences:"
    human = """
    Here is the preference input detail to plan a vacation:
    - Destination: {destination}
    - Budget: {budget}
    - Dates: {dates}
    - Activities: {activities}
    - Confirm Booking: {confirm_booking}
    """
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

    # Initialize the parser
    parser = StrOutputParser()

    # Create the chain by combining the prompt, model, and parser
    chain = prompt | model | parser

    # Invoke the chain with the input values
    output = chain.invoke({"destination": destination, "budget": budget, "dates": dates, "activities": activities, "confirm_booking": True})

    # Return the output
    return output

