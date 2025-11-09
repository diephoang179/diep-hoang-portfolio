import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("PORTFOLIO")

menu = ["About Me", "Delivery Analysis Project"]
choice = st.sidebar.radio('📋 Menu', menu)

st.sidebar.markdown("---")  # Đường kẻ phân cách
st.sidebar.markdown("""**Contact me**""")
st.sidebar.markdown("📧 hdiep0508@gmail.com")
st.sidebar.markdown("🔗 [Linkedin](www.linkedin.com/in/diep-hoang-393779a9)")
st.sidebar.markdown("💻 [Github](https://github.com/diephoang179)")

if choice == 'About Me':
    st.subheader("About Me")
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image("me.jpg", width=190)
    with col2:
        st.markdown("""
        **👋 Hi, My name is Diep Hoang.**\\
        I'm passionate about logistics, data analysis, and process automation using Google Apps Script. I aim to leverage my experience and skills to contribute effectively, improve service quality, and enhance company value.\\
        Currently, I'm learning to develop my technical and analytical skills, and this portfolio showcases my selected projects and insights.\
        """)
    st.subheader("Achievements")
    st.write("""
        I specialize in automating repetitive data tasks and building smart reporting systems in Google Sheets. With 4 years of experience in logistics and operations data management, I’ve helped teams reduce manual work and improve accuracy through custom Apps Script automations and data integrations. Throughout my career, I've discovered my passion working with data and am continously learning to become an expert in data analyst.
        ##### Key skills:
        ✔️ Google Apps Script\\
        ✔️ Google Sheets formulas\\
        ✔️ Looker Dashboard Visulization\\
        ✔️ Report generation and scheduling\\
        ✔️ Python

        ##### List of some typical projects:
        **Here are some of my projects — I hope you enjoy exploring them!**\\
        If you have any insights or feedback, feel free to reach out to me via email or LinkedIn.
        
        1️⃣ **Delivery Analysis**\\
        **Tools:** Google Sheets, Looker Dashboard\\
        **Goal:** Evaluate delivery performance based on analyzing and visualizing data.\\
        **What I did:**\\
        ●   Build an interactive dashboard to visualize delivery performance by carrier.\\
        ●   Identify key factors affecting delivery performance.\\
        ●   Provide some relevant insights.\\
        **Key features:**\\
        ✔️  Data processing and visualizing.\\
        ✔️  Data analyzing.\\
        **Details:** Please learn more at **Data Analysis Project** page.

        2️⃣ **Customer Segmentation**\\
        **Tools:** Python\\
        **Goal:** Worked with my team to built an simple application to automate customer segmentation using RFM analysis, enabling marketing teams to identify high-value customers and personalize promotional strategies efficiently.\\
        **What we did:**\\
        ●   Applied the K-Means clustering model to perform RFM analysis and segment customers.\\
        ●   Developed an simple application that allows users to search for customer segments and input new customer data to automatically identify the customer type.\\
        **Key features:**\\
        ✔️  Applied machine learning in a case study.\\
        **Details:** [Customer Segmentation Project](https://customer-segmentation-project-ek2ji3stlguqwsjjqdsi5y.streamlit.app/).
        """)

if choice == 'Delivery Analysis Project':
    st.subheader("Mini Delivery Analysis Project")
    st.write("""
        ##### I. Project Overview
        **1. About data source:**
        The dataset contains delivery data from a supermarket distribution network, covering the period from June 2024 to November 2024. It records all booking details and delivery shipments from distribution centers (DCs) to retail marts across multiple provinces.\\
        \\
        **2. Project objectives:**
        - Build an interactive dashboard to visualize delivery performance by carrier.
        - Identify key factors affecting delivery performance (carrier capacity, delivery time and truck utilization).
        - Provide some relevant insights.
        
        **3. Data analysis process steps:**
        """)
    st.image("process_steps.jpg", caption="Process steps", use_container_width=True)
    st.write("""
        **4. Result:**
        You can check the project results here:
    """)
    st.markdown("**Link [data](https://docs.google.com/spreadsheets/d/1yLLasMDPSpGWDgLYwJQxUi5f2DTypsJgGdGc8iNd3ac/edit?gid=1389441584#gid=1389441584)**")
    st.markdown("**Link [dashboard](https://lookerstudio.google.com/reporting/f9760e61-0bdc-43f6-9989-2942b6fa4f96)**")
    st.write("""
        ##### III. Data Analysis
        ###### 1. Overview
        Overall, the delivery performance remained stable with promising indicators.
        Firstly, although the number of bookings increased significantly in August and November — roughly one-third higher than in other months — the lead time showed a slightly decreasing trend from August onward and remained relatively stable in the following months.
        At the same time, truck utilization stayed consistently high at around 99%.
        """)
    st.image("time_trend.jpg", caption="Bookings trend", use_container_width=True)
    st.write("""
        Additionally, in spite of slight changes in the number of bookings by truck type in November, the distribution of carrier usage remained stable, with Carrier E and medium-sized trucks being the most frequently used, while Carrier A and light-sized trucks were the least utilized.
    """)
    st.image("booking_trend.jpg", caption="Truck bookings distribution", use_container_width=True)
    st.image("truck_type_by_carrier.jpg", caption="Truck type usage by carrier", use_container_width=True)
    st.write("""
        As the dataset only covers six months, it is difficult to confirm whether these fluctuations indicate a seasonal trend. However, the peaks in August and November may reflect higher demand during these months or suggest that August’s stock planning was intended to support 2 months upcoming demand. Further analysis of demand patterns would help in developing an efficient transportation plan.
        
        ###### 2. Detail by Carrier
        In general, each carrier shows distinct operational characteristics in terms of truck types and delivery coverage:
        -	Carrier A mainly provides light trucks for Mart F, with time performance improving from August and remaining stable afterward.
        -	Carrier C operates various truck types for Mart F, showing a similar improvement and stable trend after August.
        -	Carrier B uses only extra-heavy trucks for Mart D, with consistently stable delivery performance.
        -	Carrier D provides medium and light trucks from DC B to Mart E, with a sharp performance drop in August followed by stabilization.
        -	Carrier F serves Mart E using medium and light trucks from DCs A and C, maintaining stable performance over time.

        Truck utilization rates remain high overall, especially for heavy and extra-heavy trucks, where utilization mainly depends on cargo volume (CBM).
        
        Additionally, handling time for waiting and loading tends to be longer for extra-heavy trucks compared to other types.
        """)
    st.image("detail_truck_utilization.jpg", caption="Truck utilization table and handle time by truck type chart", use_container_width=True)
    st.write("""
        ##### IV. Conclusion
        The Delivery Analysis Report offers a comprehensive overview of each carrier’s delivery performance, highlighting neccessary points and will serves as a key step in enhancing overall operational efficiency and performance metrics.
        
        Additionally, this project help me improve valuable hands-on experience in applying data analysis tools to real operational data, reinforcing practical skills in extracting insights and supporting data-driven decisions.
        """)





