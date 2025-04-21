#Hello World with Streamlit
import streamlit as st
st.write('Hello World')
#----------------------------------------
#text input with Streamlit
import streamlit as st
st.text_input('Favorite Movie?')
#----------------------------------------
#text input with Streamlit and default value

import streamlit as st
x = st.text_input('Favorite Movie?')
st.write(f"Your favorite movie is: {x}")
#----------------------------------------
#button with Streamlit
import streamlit as st
x = st.text_input('Favorite Movie?')
st.write(f"Your favorite movie is: {x}")
is_clicked = st.button("Click Me")
#--------------------------------------------
# text decoration with streamlit
import streamlit as st

st.write("## This is a H2 Title!")

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
#    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
#    :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
st.markdown("Here's a bouquet &mdash;\
#            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,
#a soft return is used for the next line.

#Two (or more) newline characters in a row will result in a hard return.
#'''
st.markdown(multi)
#------------------------------------------
#datalist with streamlit
import pandas as pd
import streamlit as st

st.title("CineScope: Dive into Movie Data")

data = pd.read_csv("movies.csv")

st.write("🎞️ Explore your movie dataset below:")
st.write(data)
#-------------------------------------------
#graph with streamlit
import numpy as np
import pandas as pd
import streamlit as st
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)
#----------------------------------------
#Loan Repayments Calculator with streamlit
import streamlit as st
import pandas as pd
import math

st.title("Mortgage Repayments Calculator")

st.write("### Input Data")
col1, col2 = st.columns(2)  
home_value = col1.number_input("Home Value", min_value=0, value=500000)
deposit = col1.number_input("Deposit", min_value=0, value=100000)
interest_rate = col2.number_input("Interest Rate (in %)", min_value=0.0, value=5.5)
loan_term = col2.number_input("Loan Term (in years)", min_value=1, value=30)

loan_amount = home_value - deposit
monthly_interest_rate = (interest_rate / 100) / 12
number_of_payments = loan_term * 12
monthly_payment = (
    loan_amount
    * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
    / ((1 + monthly_interest_rate) ** number_of_payments - 1)
)

total_payments = monthly_payment * number_of_payments
total_interest = total_payments - loan_amount

st.write("### Repayments")
col1, col2, col3 = st.columns(3)  
col1.metric(label="Monthly Repayments", value=f"${monthly_payment:,.2f}")
col2.metric(label="Total Repayments", value=f"${total_payments:,.0f}")
col3.metric(label="Total Interest", value=f"${total_interest:,.0f}")

schedule = []
remaining_balance = loan_amount

for i in range(1, number_of_payments + 1):
    interest_payment = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment
    remaining_balance -= principal_payment
    year = math.ceil(i / 12) 
    schedule.append(
        [
            i,
            monthly_payment,
            principal_payment,
            interest_payment,
            remaining_balance,
            year,
        ]
    )

df = pd.DataFrame(
    schedule,
    columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance", "Year"],
)

st.write("### Payment Schedule")
payments_df = df[["Year", "Remaining Balance"]].groupby("Year").min()
st.line_chart(payments_df["Remaining Balance"])  
