import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("loan_model.pkl", "rb"))

st.set_page_config(page_title="Loan Prediction App")
st.title("🏦 Loan Approval Prediction App")

st.write("Enter customer details to check loan approval status")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", [0, 1, 2, 3])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])

income = st.number_input("Applicant Income", min_value=0)
co_income = st.number_input("Coapplicant Income", min_value=0)

loan_amount = st.number_input("Loan Amount", min_value=0)
loan_term = st.number_input("Loan Amount Term", min_value=0)

credit_history = st.selectbox("Credit History", [0, 1])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])


def encode_data():
    g = 1 if gender == "Male" else 0
    m = 1 if married == "Yes" else 0
    e = 1 if education == "Graduate" else 0
    se = 1 if self_employed == "Yes" else 0

    if property_area == "Urban":
        pa = 2
    elif property_area == "Semiurban":
        pa = 1
    else:
        pa = 0


    return np.array([[g, m, dependents, e, se,
                      income, co_income,
                      loan_amount, loan_term,
                      credit_history, pa]])

if st.button("Predict Loan Status"):

    input_data = encode_data()
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")
        st.markdown("---")
        st.markdown("👨‍💻 Built by Mahesh 🚀")