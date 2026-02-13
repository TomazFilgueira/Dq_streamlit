import streamlit as st # type: ignore
st.title("GlobalJava Roasters ☕")
st.title("Navigation")

def general_faqs():
    bean_source_expander = st.expander('Where do you source your coffee beans?')
    with bean_source_expander:
        st.write('Our coffee beans are ethically sourced from family-owned farms and cooperatives across various coffee-growing regions, ensuring quality and sustainability in every cup.')
        
    roast_expander = st.expander('How do you roast your beans?')
    with roast_expander:
        st.write('We employ a combination of traditional and modern roasting techniques, meticulously adjusting the roast profile for each batch to bring out the unique flavors and aromas of the beans.')

# Define your function here
def recipe_faqs():
    
    with st.expander("What is your recommended recipe for a classic cold brew coffee?"):
        st.write("For a smooth and robust cold brew, mix coarsely ground coffee beans with cold water in a 1:8 ratio, steep for 12-18 hours, and then filter. Serve over ice and customize with milk or sweeteners to taste.")
    
    with st.expander('Do you have a signature coffee-based dessert recipe?'):
        st.write("Yes, our signature dessert is the 'GlobalJava Mocha Brownies.' Blend melted dark chocolate with your favorite GlobalJava espresso shot, add to your brownie mix, and bake. These rich, coffee-infused brownies are a coffee lover's delight and perfect for any occasion.")


    
    

page = st.sidebar.selectbox("Choose a section",['About Us','FAQs','Submit Feedback'])

if page == 'About Us':
    st.header('About Us')
    # Add your columns here
    col1, col2, col3 = st.columns(3)

    with col1:
    
        st.image('https://s3-us-east-2.amazonaws.com/dq-authoring-tmp-data/901-1114/Elizabeth_Bennet.png')
        st.header('Elizabeth Bennet')
        st.write('Founder and CEO, Elizabeth is passionate about bringing customers flavorful and delicious coffee.')

    with col2:
    
        st.image('https://s3-us-east-2.amazonaws.com/dq-authoring-tmp-data/901-1114/Charles_Bingley.png')
        st.header('Charles Bingley')
        st.write('Marketing Director and Social Media Expert, Charles helps the world know about our great new flavors!')

    with col3:
    
        st.image('https://s3-us-east-2.amazonaws.com/dq-authoring-tmp-data/901-1114/Georgiana_Darcy.png')
        st.header('Georgiana Darcy')
        st.write('Georgiana is the creative genius behind the scenes!')

if page == 'FAQs':
    st.header('FAQs')
       
    tab1,tab2 = st.tabs(["General","Recipes"])
    
    with tab1:
        general_faqs()
    
    with tab2:
        recipe_faqs()