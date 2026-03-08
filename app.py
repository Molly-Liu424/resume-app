import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Zimo (Molly) Liu", page_icon="📊", layout="wide")

# Header
st.title("Zimo (Molly) Liu 👩‍💻")
st.markdown("**Data Analyst** | MMA Candidate @ Rotman | CFA & FRM Candidate")
st.markdown("📧 zimo.liu@rotman.utoronto.ca | 📞 (226) 789-8632 | 🔗 [LinkedIn](https://www.linkedin.com/in/zimo-molly-liu-09a409262)")
st.divider()

# ── Sidebar widgets ──────────────────────────────────────────────
with st.sidebar:
    st.header("🔍 Navigation")

    # Widget 1: multiselect
    skill_filter = st.multiselect(
        "Filter Skills by Category",
        ["Programming", "Software", "Analytics"],
        default=["Programming", "Software", "Analytics"]
    )

    # Widget 2: toggle
    compact_view = st.toggle("Hide Charts (Compact View)", value=False)

    # Widget 3: radio
    chart_type = st.radio(
        "Skills Chart Orientation",
        ["Vertical", "Horizontal"]
    )

    # Widget 4: selectbox
    project_select = st.selectbox("Quick Jump to Project", [
        "StockTrak Investment (2025)",
        "Statistical Modeling (2024)",
        "E-commerce Analysis (2023)"
    ])

# ── Tabs ─────────────────────────────────────────────────────────
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 About", "🛠️ Skills", "🎓 Education", "💼 Experience", "📁 Projects", "🏆 Achievements"
])

# ── Tab 1: About ─────────────────────────────────────────────────
with tab1:
    st.header("About Me")
    col1, col2, col3 = st.columns(3)
    col1.metric("Years of Experience", "2+", "Internship + Projects")
    col2.metric("Portfolio Return", "8%", "Outperformed S&P by 12%")
    col3.metric("Dance Crew Followers", "3,000+", "+40% engagement")
    st.info("""
    Data Analyst with a passion for uncovering insights that drive smarter financial and business decisions.
    Recognized for transforming raw data into meaningful analysis using **Python, R, SQL, and Excel VBA**.
    Experienced in financial statement analysis and stock research, with a strong foundation in risk management
    as a **CFA Level I** and **FRM candidate**.
    """)

# ── Tab 2: Skills ────────────────────────────────────────────────
with tab2:
    st.header("Technical Skills")
    skills_data = {
        "Skill": ["Python", "R", "SQL", "Excel VBA", "MS PowerPoint", "Statistical Analysis", "Financial Modeling", "Data Visualization"],
        "Category": ["Programming", "Programming", "Programming", "Software", "Software", "Analytics", "Analytics", "Analytics"],
        "Proficiency": [90, 85, 80, 85, 75, 88, 82, 80]
    }
    df_skills = pd.DataFrame(skills_data)
    df_filtered = df_skills[df_skills["Category"].isin(skill_filter)]

    if not compact_view:
        if chart_type == "Vertical":
            fig = px.bar(df_filtered, x="Skill", y="Proficiency", color="Category",
                         title="Skills Proficiency (%)", range_y=[0, 100],
                         color_discrete_sequence=px.colors.qualitative.Pastel)
        else:
            fig = px.bar(df_filtered, x="Proficiency", y="Skill", color="Category",
                         orientation='h', title="Skills Proficiency (%)", range_x=[0, 100],
                         color_discrete_sequence=px.colors.qualitative.Pastel)
        st.plotly_chart(fig, use_container_width=True)

    st.dataframe(df_filtered, use_container_width=True, hide_index=True)

# ── Tab 3: Education ─────────────────────────────────────────────
with tab3:
    st.header("Education")
    edu_data = {
        "Degree": ["Master of Management Analytics", "Bachelor of Mathematics"],
        "Institution": ["Rotman, University of Toronto", "University of Waterloo"],
        "Specialization": ["Management Analytics", "Financial Analysis & Risk Management, Minor in Statistics"],
        "Year": ["2026 (Expected)", "2025"],
        "Award": ["—", "🏅 President's Scholarship 2022"]
    }
    st.table(pd.DataFrame(edu_data))
    st.divider()
    st.subheader("Certifications In Progress")
    col1, col2 = st.columns(2)
    col1.success("📜 CFA Level I Candidate")
    col2.success("📜 FRM Candidate")

# ── Tab 4: Experience ────────────────────────────────────────────
with tab4:
    st.header("Professional Experience")
    with st.expander("📌 PICC Property and Casualty Co. Ltd. — Data Analyst Intern", expanded=True):
        st.caption("Henan, China | May 2023 – August 2023")
        st.markdown("""
        - Utilized Excel (pivot tables, VLOOKUP) across **300+ insurance products**, improving data accuracy by **20%**
        - Wrote and optimized SQL queries and Python scripts to analyze complex datasets for revenue performance
        - Conducted comparative studies on client profiles and policyholder trends, boosting sales performance by **16%**
        """)

# ── Tab 5: Projects ──────────────────────────────────────────────
with tab5:
    st.header("Technical Projects")
    proj = project_select  # uses sidebar selectbox

    if proj == "StockTrak Investment (2025)":
        st.subheader("📈 StockTrak Investment Project")
        col1, col2, col3 = st.columns(3)
        col1.metric("Portfolio Size", "$1M")
        col2.metric("Annual Return", "8%")
        col3.metric("vs S&P 500", "+12%")
        st.markdown("""
        - Maintained <15% cash allocation across stocks, ETFs, and bonds
        - Executed 3+ short sales and options trades, enhancing portfolio value by **5%**
        - Improved risk resilience using S&P 500 Index and oil futures hedging
        """)
    elif proj == "Statistical Modeling (2024)":
        st.subheader("🔬 Advanced Statistical Modeling")
        col1, col2 = st.columns(2)
        col1.metric("Sample Size", "8,000 obs")
        col2.metric("Mortality Reduction", "30%")
        st.markdown("""
        - Estimated parameters using MLE with 95% confidence intervals in R
        - Logistic regression revealed **30% reduction in mortality** for high-risk patients
        - Employed Poisson & negative binomial regression for cystic fibrosis data
        """)
    elif proj == "E-commerce Analysis (2023)":
        st.subheader("🛒 E-commerce Data Analysis")
        col1, col2, col3 = st.columns(3)
        col1.metric("Processing Time Reduction", "96%")
        col2.metric("Outlier Influence Reduction", "20%")
        col3.metric("Order Total Increase", "12%")
        st.markdown("""
        - Applied advanced Excel techniques to ASOS user dataset
        - A/B test on "free shipping" banner resulted in **12% increase in order totals**
        - Used robust regression with Huber loss and IRLS in R
        """)

# ── Tab 6: Achievements ──────────────────────────────────────────
with tab6:
    st.header("Achievements & Interests")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("💃 Director — Haebeat Dance Crew (2023–2025)")
        st.metric("Followers", "3,000+")
        st.metric("Engagement Increase", "40%")
        st.metric("Audition Candidates Managed", "50+")
    with col2:
        st.subheader("🌐 Languages")
        st.success("✅ English — Fluent")
        st.success("✅ Chinese (Mandarin) — Fluent")
        st.subheader("🏅 Academic Award")
        st.info("President's Scholarship — University of Waterloo, 2022")

st.divider()
st.caption("Built with Streamlit ❤️ | Zimo (Molly) Liu © 2025")
