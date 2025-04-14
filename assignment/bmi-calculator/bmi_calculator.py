import streamlit as st

# Page title
st.title("💪 BMI Calculator")

# User input for height and weight
height = st.number_input("Enter your height (in cm):", min_value=50.0, max_value=300.0, step=0.1)
weight = st.number_input("Enter your weight (in kg):", min_value=10.0, max_value=500.0, step=0.1)

# Calculate button
if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        height_m = height / 100
        bmi = weight / (height_m ** 2)
        st.subheader(f"Your BMI is: {bmi:.2f}")
        
        # Classification
        if bmi < 18.5:
            st.warning("You're underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You're overweight.")
        else:
            st.error("You're in the obese range.")
    else:
        st.error("Please enter valid height and weight.")
