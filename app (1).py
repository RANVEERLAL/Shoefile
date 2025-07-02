import streamlit as st

st.set_page_config(page_title="Custom Shoe App", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", [
    "Data Visualisation",
    "Classification",
    "Clustering",
    "Association Rules",
    "Regression Insights"
])

if page == "Data Visualisation":
    from pages.Data_Visualization import show
    show()
elif page == "Classification":
    from pages.Classification import show
    show()
elif page == "Clustering":
    from pages.Clustering import show
    show()
elif page == "Association Rules":
    from pages.Association_Rules import show
    show()
elif page == "Regression Insights":
    from pages.Regression_Insights import show
    show()