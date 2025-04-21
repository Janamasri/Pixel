import streamlit as st
import streamlit.components.v1 as components

# ================================
# Pixel Digital - Growth Dashboard (Final Professional Version)
# ================================

# Set page configuration
st.set_page_config(
    page_title="Pixel Digital",
    layout="wide"
)

# === Inject Custom CSS ===
st.markdown("""
    <style>
        body {
            background-color: #ffffff;
            font-family: 'Segoe UI', sans-serif;
        }
        .stApp {
            background-color: #ffffff;
        }
        h1, h2, h3, h4 {
            color: #24486B;
        }
        .big-title {
            font-size: 48px;
            color: #24486B;
            text-align: center;
            font-weight: bold;
        }
        .blue-line {
            border: none;
            height: 2px;
            background-color: #24486B;
            margin: 30px 0;
        }
    </style>
""", unsafe_allow_html=True)

# === Sidebar Navigation ===
page = st.sidebar.radio(
    " ",
    ["Home", "KPI Dashboard", "Forecast Dashboard"]
)

# === HOME PAGE ===
if page == "Home":
    st.image("Pixel.jpg", width=300)
    st.markdown('<div class="big-title">Pixel Digital</div>', unsafe_allow_html=True)
    st.markdown('<hr class="blue-line"/>', unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: justify; font-size: 18px;'>
    <b>Pixel Digital Office Equipment</b> is Lebanon's trusted partner for advanced IT and imaging solutions, powered by decades of excellence, resilience, and innovation. We deliver cutting-edge technologies, strategic client services, and sustainable growth models tailored for a volatile economy.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### Key Highlights")
    st.markdown("""
    - Official distributor of RICOH technologies in Lebanon  
    - Serving NGOs, education, public sector, and corporate clients  
    - Expertise across imaging, document solutions, and IT systems  
    - Proven adaptability across economic crises and sectoral shifts  
    """)

    st.markdown("### Vision & Mission")
    st.markdown("""
    - Empower Lebanese industries with world-class digital solutions  
    - Drive client success through forecasting and strategic planning  
    - Expand operational excellence across Lebanon and regional markets  
    """)

    st.markdown('<hr class="blue-line"/>', unsafe_allow_html=True)

    st.info("This digital dashboard is part of Pixel Digital's transformation toward predictive, insight-driven growth.")

# === KPI DASHBOARD ===
elif page == "KPI Dashboard":
    st.title("Pixel Digital KPI Dashboard")
    st.markdown("Explore interactive Tableau dashboards showcasing sales, client dynamics, sector trends, and internal performance.")

    st.subheader("1 – Sales by Year and Sector")
    components.iframe(
        "https://public.tableau.com/views/Salesbyyearandsector/Dashboard1?:embed=y&:display_count=yes&:showVizHome=no",
        height=827, width=1600
    )

    st.subheader("2 – Client Portfolio Insights")
    components.iframe(
        "https://public.tableau.com/views/ClientAnalysis_17451765178320/Dashboard2?:embed=y&:display_count=yes&:showVizHome=no",
        height=827, width=1600
    )

    st.subheader("3 – Industry and Product Category Trends")
    components.iframe(
        "https://public.tableau.com/views/IndustryandCategory/Dashboard3?:embed=y&:display_count=yes&:showVizHome=no",
        height=827, width=1600
    )

    st.subheader("4 – Sales Team Performance")
    components.iframe(
        "https://public.tableau.com/views/SalesbySalesperson_17451766336230/Dashboard4?:embed=y&:display_count=yes&:showVizHome=no",
        height=827, width=1600
    )

# === FORECAST DASHBOARD ===
elif page == "Forecast Dashboard":
    st.title("Pixel Digital Forecast Dashboard")
    st.markdown("Sales trends forecasted using the **Weighted Ensemble Model (70% Prophet + 30% XGBoost)**, optimized for Lebanon's volatile retail and institutional markets.")

    st.image("PixelForecast.png", caption="Pixel Digital 2025–2026 Forecast (Weighted Ensemble Model)", use_column_width=True)

    st.markdown("""
    ### Key Takeaways:

    - The **Weighted Ensemble Model** was selected after benchmarking multiple statistical and machine learning models. It combines **Prophet's trend-seasonality strengths** and **XGBoost's macroeconomic sensitivity**.

    - This model is ideal for **Lebanon's dynamic environment**, handling grant cycles, academic procurement periods, and currency-driven demand volatility.

    - The model enables:
        - **Sales Planning**: Sector-specific targets (NGOs, Education) aligned with forecast peaks.
        - **Marketing Synchronization**: Campaigns matched to seasonal demand cycles.
        - **Procurement Optimization**: Stocking aligned to forecasted category trends.
        - **Strategic Resilience**: Scenario modeling for crisis response and expansion planning.

    - Forecast governance includes:
        - Regular updates with fresh sales and macroeconomic data.
        - Sensitivity tests for exchange rate shocks and grant funding patterns.
        - Embedded KPI tracking linked to forecast-driven targets.

    > This forecast is not just a prediction — it's **Pixel Digital’s strategic engine** for proactive, insight-driven decision-making.
    """)
