import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="Torrent Power Analytics Progress Tracker",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Data Analyst Roadmap Tracker")
st.caption("Tailored 12-Week Fast-Track Program for Electrical Engineers | Torrent Power MIS & Dashboards")

# Roadmap Data Construction
roadmap = [
    {
        "Week": 1,
        "Phase": "Phase 1: Advanced Excel & Power Query",
        "Topic": "Excel Fundamentals & Discom Data Basics",
        "Subtopics": "Absolute cell references ($A$1), formatting, SUMIFS, COUNTIFS, AVERAGEIFS, Text to Columns",
        "Discom Project": "Daily Substation Feeder Tripping Summary Report",
        "Resource Channel": "Chandoo",
        "Resource URL": "https://www.youtube.com/@chandoo_"
    },
    {
        "Week": 2,
        "Phase": "Phase 1: Advanced Excel & Power Query",
        "Topic": "Advanced Lookup Functions & Validation",
        "Subtopics": "XLOOKUP, INDEX-MATCH, Nested IFS, IFERROR, Data Validation Dropdowns",
        "Discom Project": "Mapping Consumer Account IDs to Distribution Transformers (DTRs)",
        "Resource Channel": "Leila Gharani",
        "Resource URL": "https://www.youtube.com/@LeilaGharani"
    },
    {
        "Week": 3,
        "Phase": "Phase 1: Advanced Excel & Power Query",
        "Topic": "Power Query Data Automation",
        "Subtopics": "Get & Transform, Unpivoting Columns, Merging/Appending queries, handling nulls",
        "Discom Project": "Automating Monthly Metering CSV Ingestion & Cleanup",
        "Resource Channel": "TrumpExcel",
        "Resource URL": "https://www.youtube.com/@trumpexcel"
    },
    {
        "Week": 4,
        "Phase": "Phase 2: Discom KPIs & Dynamic Dashboards",
        "Topic": "MIS Principles & Key Metrics",
        "Subtopics": "AT&C Loss %, Billing Efficiency, Collection Efficiency, SAIDI & SAIFI Reliability",
        "Discom Project": "Daily Executive MIS Operations Summary Sheet",
        "Resource Channel": "Chandoo",
        "Resource URL": "https://www.youtube.com/@chandoo_"
    },
    {
        "Week": 5,
        "Phase": "Phase 2: Discom KPIs & Dynamic Dashboards",
        "Topic": "Interactive Excel Dashboards",
        "Subtopics": "Pivot Tables, Pivot Charts, Interactive Slicers, Timelines, Dynamic Headers",
        "Discom Project": "Interactive Feeder Interruption & Outage Tracker",
        "Resource Channel": "Leila Gharani",
        "Resource URL": "https://www.youtube.com/@LeilaGharani"
    },
    {
        "Week": 6,
        "Phase": "Phase 2: Discom KPIs & Dynamic Dashboards",
        "Topic": "Data Storytelling & Variance Analysis",
        "Subtopics": "Actual vs Target charts, conditional formatting heatmaps, executive summary design",
        "Discom Project": "Subdivision Reliability & Energy Loss Variance Report",
        "Resource Channel": "Chandoo",
        "Resource URL": "https://www.youtube.com/watch?v=QePrHo92ogM"
    },
    {
        "Week": 7,
        "Phase": "Phase 3: Grid Analytics & Statistics",
        "Topic": "Statistical Concepts for Power Grids",
        "Subtopics": "Mean, Median, Variance, Standard Deviation, Z-Score Outlier Detection",
        "Discom Project": "Detecting Metering Anomalies & Abnormally High Distribution Losses",
        "Resource Channel": "Khan Academy / StatQuest",
        "Resource URL": "https://www.youtube.com/@chandoo_"
    },
    {
        "Week": 8,
        "Phase": "Phase 3: Grid Analytics & Statistics",
        "Topic": "Exploratory Data Analysis (EDA)",
        "Subtopics": "Load Profile Curves, Peak Load Identification, Temperature vs Consumption Correlation",
        "Discom Project": "Distribution Transformer Overloading & Phase Unbalance Diagnostic",
        "Resource Channel": "StatQuest with Josh Starmer",
        "Resource URL": "https://www.youtube.com/@chandoo_"
    },
    {
        "Week": 9,
        "Phase": "Phase 3: Grid Analytics & Statistics",
        "Topic": "Trend Analysis & Load Forecasting",
        "Subtopics": "Moving Averages, Exponential Smoothing, Excel Forecast Sheets",
        "Discom Project": "Short-Term Peak Power Demand Estimation for Scheduling",
        "Resource Channel": "Simplilearn",
        "Resource URL": "https://www.youtube.com/@chandoo_"
    },
    {
        "Week": 10,
        "Phase": "Phase 4: Power BI & Dashboard Publishing",
        "Topic": "Power BI Desktop Fundamentals",
        "Subtopics": "Connecting Data Sources, Power Query in BI, Star Schema Data Modeling, Relationships",
        "Discom Project": "Building Torrent Power Distribution Data Model",
        "Resource Channel": "Guy in a Cube",
        "Resource URL": "https://www.youtube.com/channel/UCFp1vaKzpfvoGai0vE5VJ0w"
    },
    {
        "Week": 11,
        "Phase": "Phase 4: Power BI & Dashboard Publishing",
        "Topic": "DAX Calculations & Visual Analytics",
        "Subtopics": "CALCULATE, SUMX, Time Intelligence (SAMEPERIODLASTYEAR), Custom Visuals",
        "Discom Project": "Power BI Executive Dashboard for Division-level AT&C Losses",
        "Resource Channel": "Guy in a Cube",
        "Resource URL": "https://www.youtube.com/channel/UCFp1vaKzpfvoGai0vE5VJ0w"
    },
    {
        "Week": 12,
        "Phase": "Phase 4: Power BI & Dashboard Publishing",
        "Topic": "Automated Publishing & Daily Workflows",
        "Subtopics": "Power BI Service, Scheduled Data Refresh, Row-Level Security, Exporting Workbooks",
        "Discom Project": "Automated Daily MIS Portal for Torrent Power Leadership",
        "Resource Channel": "Guy in a Cube",
        "Resource URL": "https://www.youtube.com/channel/UCFp1vaKzpfvoGai0vE5VJ0w"
    }
]

# Initialize Session State
if "completed_weeks" not in st.session_state:
    st.session_state.completed_weeks = set()

# Overall Progress
total_weeks = len(roadmap)
completed_count = len(st.session_state.completed_weeks)
progress_pct = int((completed_count / total_weeks) * 100)

col1, col2, col3 = st.columns(3)
col1.metric("Total Curriculum Duration", f"{total_weeks} Weeks")
col2.metric("Weeks Completed", f"{completed_count} / {total_weeks}")
col3.metric("Completion Rate", f"{progress_pct}%")

st.progress(completed_count / total_weeks)

# Filters
st.sidebar.header("Filter Roadmap")
phase_filter = st.sidebar.selectbox(
    "Select Phase",
    ["All Phases"] + sorted(list(set(w["Phase"] for w in roadmap)))
)

# Display Interactive Cards
st.subheader("Interactive Weekly Curriculum Tracker")

for item in roadmap:
    if phase_filter != "All Phases" and item["Phase"] != phase_filter:
        continue

    is_checked = item["Week"] in st.session_state.completed_weeks

    with st.expander(f"Week {item['Week']}: {item['Topic']} {'✅' if is_checked else '⏳'}", expanded=not is_checked):
        col_check, col_info = st.columns([1, 5])

        with col_check:
            status = st.checkbox("Complete", key=f"week_{item['Week']}", value=is_checked)
            if status:
                st.session_state.completed_weeks.add(item["Week"])
            else:
                st.session_state.completed_weeks.discard(item["Week"])

        with col_info:
            st.markdown(f"**Phase:** `{item['Phase']}`")
            st.markdown(f"**Key Topics:** {item['Subtopics']}")
            st.markdown(f"**Discom Project:** ⚡ *{item['Discom Project']}*")
            st.markdown(f"**Free YouTube Channel:** [{item['Resource Channel']}]({item['Resource URL']})")
