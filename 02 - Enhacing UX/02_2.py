import streamlit as st # type: ignore
st.title("GlobalJava Roasters ☕")
st.title("Navigation")

page = st.sidebar.selectbox("Choose a section",['About Us','FAQs','Submit Feedback'])

if page == 'About Us':
    st.header('About Us')
    # Add your columns here
    col1, col2, col3 = st.columns(3)

    col1.image("https://s3.amazonaws.com/dq-content/901/Elizabeth_Bennet.png")
    col1.header("Elizabeth Bennet")
    col1.write("Founder and CEO, Elizabeth is passionate about bringing customers flavorful and delicious coffee.")

    col2.image("https://s3.amazonaws.com/dq-content/901/Charles_Bingley.png")
    col2.header("Charles Bingley")
    col2.write("Marketing Director and Social Media Expert, Charles helps the world know about our great new flavors!")

    col3.image("https://s3.amazonaws.com/dq-content/901/Georgiana_Darcy.png")
    col3.header("Georgiana Darcy")
    col3.write("Georgiana is the creative genius behind the scenes!")
