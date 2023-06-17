import streamlit as st
import time
import main as mn

bullet_points = []

def display_text(text):
    t = st.empty()
    for i in range(len(text) + 1):
        t.markdown("- ##### %s" % text[0:i])
        time.sleep(0.02)

st.sidebar.title('Retire Smart 2023')

current_age = st.sidebar.number_input("Current Age:", value=36, min_value=0, max_value=100)
retirement_age = st.sidebar.number_input("Retirement Age:", value=42, min_value=0, max_value=100)
st.sidebar.markdown("---")
st.sidebar.markdown("#### Current Income & Assets")
average_income_mon = st.sidebar.number_input("Current Monthly Income (in ₹):", value=80000, min_value=0, max_value=10000000000)
term_ins_cover = st.sidebar.number_input("Current Term Insurance Cover (in ₹):", value=0, min_value=0, max_value=10000000000)
health_ins_cover = st.sidebar.number_input("Current Health Insurance Cover (in ₹):", value=300000, min_value=0, max_value=10000000000)
emergency_fund = st.sidebar.number_input("Emergency Fund Saved (in ₹) for unforeseen circumstances: ", value=1000000, min_value=0, max_value=10000000000)
curr_asset = st.sidebar.number_input("Non-Rental Assets that can be converted to cash during retirement(in ₹)", value= 10000000, min_value=0, max_value=10000000000)
st.sidebar.markdown("---")
st.sidebar.markdown("#### Current Liabilities and Expenses")
monthly_emi = st.sidebar.number_input("Current EMI(in ₹)", value=0, min_value=0, max_value=10000000000)
monthly_expense = st.sidebar.number_input("Current Monthly Expenses (in ₹):", value=70000, min_value=0, max_value=10000000000)
# st.sidebar.markdown("---")
# st.sidebar.markdown("#### Retirement goals & Current Readiness")
exp_monthly_income_ret = st.sidebar.number_input("Expected Monthly Retirement Income (in ₹)", value=round(average_income_mon*0.7), min_value=0, max_value=10000000000)
rental_income_ret = st.sidebar.number_input("Post-Retirement Rental Income (in ₹)", value=9000, min_value=0, max_value=10000000000)
monthly_pension_ret = st.sidebar.number_input("Any Monthly Pension Post-Retirement (in ₹)", value=0, min_value=0, max_value=10000000000)

if st.sidebar.button('Calculate Retirement Readiness'):
    term_suggestion, health_suggestion, emergency_suggestion, surplus_suggestion, \
        other_suggestion, readiness, dilution_suggestion, readiness_suggestion, summary = mn.start_readiness(\
            term_ins_cover, health_ins_cover,  emergency_fund, average_income_mon, monthly_emi, \
                monthly_expense, current_age, retirement_age, rental_income_ret, monthly_pension_ret, \
                    curr_asset,exp_monthly_income_ret)
    
    st.markdown("### RetireSmart Advisor: Investment Insights and Readiness Tracker")
    # progress_bar = st.progress(readiness/100)

    progress = st.progress(0)  # Initialize the progress bar

    for readiness in range(int(readiness)):
        progress.progress(readiness)  # Update the progress bar\
        time.sleep(0.1)  # Add a small delay to visualize the progressive increase

    bullet_points = [term_suggestion, health_suggestion, emergency_suggestion, surplus_suggestion, other_suggestion, dilution_suggestion, summary, readiness_suggestion]
    
    result_text =  st.empty()  # Create an empty space in the main bar
    
    for bullet_point in bullet_points:
        if(bullet_point != ""):
            display_text(bullet_point)  # Display bullet points in the main bar
            result_text.text("\n")  # Add a new line after each bullet point
    

