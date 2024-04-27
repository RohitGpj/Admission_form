import streamlit as st

st.title(':blue[Admission Form]')
st.header("Suresh Gyan Vihar University")
st.subheader("Jaipur, Rajasthan, 302017")
st.subheader(':rainbow[Fill the Personal Info.]')
code = """
<style>
    p {
        color: crimson;
        font-family: century;

    }
</style>
"""
st.html(code)

with st.form("Done"):
    fname = st.text_input("Enter your First Name : ")
    mname = st.text_input("Enter your Middle Name : ")
    lname = st.text_input("Enter your Last Name : ")
    fathername = st.text_input("Enter your Father's Name : ")
    contnum1 = st.text_input("Enter your 10 digit Contact no. : ")
    contnum2 = st.text_input("Enter your Father's Contact no.")
    email = st.text_input("Enter your primary Email address : ")
    adr = st.text_area("Enter your Address : ")
    classdata = st.selectbox("Choose Your Course :", ("","BCA", "B.Tech", "HMCT", "LLB", "Diploma"))
    classdata1 = st.selectbox("Choose your Id proofs :", ("","Adhar Card", "Pan Card", "Birth-Certificate"))
    nation = st.text_input("Enter your Nationality : ")
    religion = st.text_input("Enter your Religion : ")
    gender = st.selectbox("Sex : ",("","Male", "Femal", "Other"))
    age = st.text_input("Enter your Age : ")
    html = st.html

    import datetime 
    dob = st.date_input("Enter you DOB : ", datetime.date(2000, 7, 15))


    submit = st.form_submit_button('Submit')
if submit:
    st.markdown(f"""
                First Name : {fname}
                Middle Name : {mname}
                Last Name : {lname}
                Father's Name : {fathername}
                Contact no. : {contnum1}
                Father's Contact no : {contnum2}
                Email id : {email}
                Address : {adr}
                Course : {classdata}
                Id proof : {classdata1}
                Nation : {nation}
                Religion : {religion}
                Sex : {gender}
                Age = {age}
                Dob = {dob}""")