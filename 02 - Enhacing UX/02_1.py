import st

st.title("GlobalJava Roasters ☕")
st.title("Navigation")

page = st.sidebar.selectbox("Choose a section",['About Us','FAQs','Submit Feedback'])

if page == "About Us":
    st.header("About Us")
elif page == "FAQs":
    st.header("FAQs")
elif page == "Submit Feedback":
    st.header("Submit Feedback")
    