import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import time

# Page configuration
st.set_page_config(
    page_title="Streamlit Function Demo",
    page_icon="😎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling using HTML & CSS
st.markdown("""
    <style>
    body {
        background-color: #f0f8ff;
    }
    .main {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 30px;
    }
    .stButton>button {
        color: white;
        background-color: #007BFF;
        border-radius: 10px;
        font-size: 16px;
        padding: 10px 24px;
    }
    .stTextInput>div>div>input {
        background-color: #e6f0ff;
    }
    .stSlider>div>div>div {
        background: #007BFF;
    }
    </style>
""", unsafe_allow_html=True)

# Title & Intro
st.title("🌟 Streamlit UI Demo with Enhanced Styling")
st.header("1. Text Elements")
st.markdown("""
**Bold Text**, *Italic Text*, `Code Text`  
:computer: Easy formatting for **data science** dashboards.
""")
st.code("print('Hello everyone!')", language="python")
st.latex(r"a^2 + b^2 = c^2")
st.divider()

# Metrics & Messages
st.header("2. Metrics and Messages")
col1, col2, col3, col4, col5, col6 = st.columns(6)
col1.metric("📈 Revenue", "$1234", "+10%")
col2.error("🚫 Error message")
col3.warning("⚠️ Warning message")
col4.info("ℹ️ Info message")
col5.success("✅ Success message")
col6.exception(ValueError("This is an exception"))
st.divider()

# Data Display
st.header("3. Data Display")
df = pd.DataFrame(np.random.randn(10, 2), columns=["A", "B"])
st.dataframe(df)
st.table(df.head(3))
st.json(df.to_dict())
st.divider()

# Charts
st.header("4. Charts")
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)
chart = alt.Chart(df.reset_index()).mark_line().encode(x="index", y="A")
st.altair_chart(chart, use_container_width=True)
fig, ax = plt.subplots()
ax.plot(df.index, df["A"], color="skyblue", linewidth=2)
ax.set_title("Matplotlib Line Chart")
st.pyplot(fig)
st.divider()

# Widgets
st.header("5. Widgets")
with st.form("User Input Form"):
    name = st.text_input("👤 Enter your name")
    age = st.number_input("🎂 Enter your age")
    mood = st.radio("😊 Select your mood", ("Happy", "Sad", "Normal"))
    languages = st.multiselect("🗣️ Languages Known", ("English", "French", "German"))
    submit = st.form_submit_button("🚀 Submit")
    if submit:
        st.success(f"Name: {name}, Age: {int(age)}, Mood: {mood}, Languages: {languages}")

# 3-column layout
col1, col2, col3 = st.columns(3)
with col1:
    st.text_input("Enter your name")
    st.number_input("Enter your age")
with col2:
    st.radio("Select your mood", ("Happy", "Sad", "Normal"))
    st.multiselect("Select your languages", ("English", "French", "German"))
with col3:
    st.markdown("### Output Will Appear Here")

# Two-column layout for slider and color picker
col1, col2 = st.columns(2)
with col1:
    number = st.slider("🎯 Select a number", 0, 100)
with col2:
    color = st.color_picker("🎨 Pick a color", "#8273A4")

st.text_area("📝 Message Box")
st.date_input("📅 Select a date")
st.time_input("⏰ Select a time")
st.file_uploader("📂 Upload a file")
st.divider()

# Media
st.header("6. Media")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfEKuRxMogBxiSMNiN6Fm9Sx4Hn91tMNAskQ&s", caption="Sample Bike Image")
st.video("https://www.w3schools.com/html/mov_bbb.mp4")
st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

# Sidebar
st.sidebar.header("📌 Sidebar Panel")
st.sidebar.write("Use these controls to interact!")
st.sidebar.button("Click Me!")
option = st.sidebar.selectbox("Choose an Option", ("Option 1", "Option 2", "Option 3"))

# Containers and Expanders
with st.container():
    st.write("✅ This is a container block for grouping content")

with st.expander("🔽 Show More"):
    st.write("This section can be collapsed or expanded.")

# Spinner and Toast
with st.spinner("⏳ Loading data..."):
    time.sleep(3)

st.toast("🎉 Operation complete!", icon="✅")
st.page_link("https://streamlit.io", label="🔗 Visit Streamlit Website", icon="🌐")
