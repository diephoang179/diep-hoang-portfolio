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
st.sidebar.markdown("! [Github](https://github.com/diephoang179?tab=repositories)")

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
        I specialize in automating repetitive data tasks and building smart reporting systems in Google Sheets. With 4 years of experience in logistics and operations data management, I’ve helped teams reduce manual work and improve accuracy through custom Apps Script automations and data integrations.
        ##### Key skills:
        ✔️ Google Apps Script\\
        ✔️ Google Sheets formulas\\
        ✔️ Looker Dashboard Visulization\\
        ✔️ Report generation and scheduling

        ##### List of some typical achievements:
        - Automated daily reports using G-Sheets formulas and GAS, scheduling data consolidation from multiple source sheets into a single master report.
        - Developed an automated email alert system to notify relevant departments upon dispute form submissions.
        - Developed an simple automated chatbot notification in Google Chat Workspace on an hourly basis.
        - Developed a Google Sheet to track rider's attendance based on GPS and order log data, and to calculate the weekly income of over 120 riders, including fixed salary and performance-based incentives.

        Besides that, I’ve completed a mini delivery analysis project, which you can explore on page **Delivery Analysis Project**. Hope you enjoy exploring it!
        And if you did, I always welcome new insights and feedback. You can reach out to me via email or LinkedIn.
        """)

if choice == 'Delivery Analysis Project':
    st.subheader("Mini Delivery Analysis Project")
    st.write("""
        ##### I. Project Overview
        **1. Data source:**
        The dataset contains delivery data from a supermarket distribution network, covering the period from June 2024 to November 2024. It records all booking details and delivery shipments from distribution centers (DCs) to retail marts across multiple provinces.\\
        \\
        **2. Project objectives:**
        - Build an interactive dashboard to visualize delivery performance by carrier.
        - Identify key factors affecting delivery performance (carrier capacity, delivery time and truck utilization).
        - Provide some actionable insights and recommendations.
        \
        """)
    st.markdown("**Link [data](https://docs.google.com/spreadsheets/d/1c4KkkLPWjM-L-XP_prtbmjIBusoMJs-MsIJP4LKYvCM/edit?gid=1389441584#gid=1389441584)**")
    st.markdown("**Link [dashboard](https://lookerstudio.google.com/reporting/9e4647d9-85e7-4f9c-84da-7adefc4d9663)**")
    st.write("""
        \
        ##### II. Data Selection And Processing
        After carefully reviewing the dataset, I identified opportunities to leverage the data to evaluate delivery performance for each carrier based on three key aspects:
        - Carrier fleet capacity
        - Time performance
        - Truck utilization rate

        I then selected the relevant fields and performed calculations to generate the booking_data_summary sheet, containing 19 columns and 1,049 rows, where each record represents information for one booking ID (one trip).

        ##### III. Data Analysis
        ###### 1. Carrier fleet capacity overview
        """)
    st.image("carrier_fleet_capacity.jpg", caption="Carrier fleet capacity", use_container_width=True)
    st.write("""
        From the chart, we can observe that:
        - Carrier A is rarely used and mainly provides light trucks (≤ 2 tons).
        - Carrier B is used more frequently than Carrier A and only supplies extra heavy trucks (> 10 tons).
        - Carriers C and D appear to have a similar number of bookings.
        - Carrier C offers a wide variety of truck types, which may be one of the reasons it is often selected.
        - Carrier E is the most frequently used carrier, accounting for approximately 40% of all bookings, and mainly provides medium-sized trucks (> 2 and ≤ 5 tons).
        - Overall, the supermarket most commonly uses medium-sized trucks for deliveries and rarely uses light truck.
        
        ###### 2. Time performance
        """)
    st.image("time_performance.jpg", caption="Time performance", use_container_width=True)

    # Đọc dữ liệu để tạo bảng thống kê mô tả cho 2 chỉ số time performance
    clean_data = pd.read_csv("data_cleaning.csv")
    time_data = clean_data[["pickup_time (days)","delivery_time (days)"]]
    # Xem thống kê mô tả
    # Hiển thị tiêu đề
    st.markdown("**Thống kê mô tả về 2 chỉ số thời gian**")
    # Hiển thị bảng thống kê mô tả
    st.dataframe(time_data.describe())
    st.write("""
        Overall, pickup times are quite similar among carriers operating on the same route.
        However, Carrier B shows abnormal pickup durations on routes CB and AC.
        When I analyzed the data further, I found that pickup times have a large standard deviation and a noticeable gap between the median and mean values.
        This suggests the presence of outlier trips, mainly associated with Carrier B on the two routes mentioned earlier — possibly due to unexpected handling issues during those trips.

        In addition, pickup trips managed by Carrier B tend to take longer, while those handled by Carrier A are generally quicker.
        Since the dataset does not account for waiting time while the warehouse arranges loading staff, we can assume that larger truck sizes (with more parcels) may increase the loading arrangement time, leading to longer pickup durations.
        
        Furthermore, the delivery time chart shows that light trucks (Carrier A) appear to be faster than heavier trucks (Carrier C) on the same routes.
        However, since most carriers operate on unique routes and the available data is limited, we cannot further explore deeper insights about delivery time at this stage.
        ###### 2. Truck utiliztion rate
        """)
    st.image("truck_utilization.jpg", caption="Truck utilization rate", use_container_width=True)
    st.write("""
        The table and indicators show that the truck utilization rate is at a good level (over 99%)..

        We can also see more details about the amount of goods that need to be distributed from distribution centers to marts in the table below.
        """)
    st.image("load_proportion.jpg", caption="Load proportion by distribution center", use_container_width=True)
    st.write("""
        ##### IV. Conclusion
        The Delivery Analysis Report provides an overview of each carrier’s delivery performance and serves as an important step toward improving overall performance indices.
        
        And this project gave me a better understanding of how to apply data analysis tools in practice.
        """)



