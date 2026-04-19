import streamlit as st

# This makes the website look like the Solo Leveling Blue Screen
st.set_page_config(page_title="The System", page_icon="⚔️")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #00ccff; }
    </style>
    """, unsafe_allow_value=True)

st.title("⚔️ SYSTEM: DAILY QUEST")
st.write("---")

# 1. Tracker Section
st.header("Status Window")
job = st.selectbox("Current Class", ["F-Rank Human", "Shadow Monarch", "Mage", "Assassin"])
exp = st.slider("Daily Progress", 0, 100, 0)

# 2. The Exercise Goal
st.subheader("Today's Tasks")
q1 = st.checkbox("Pushups (0/100)")
q2 = st.checkbox("Squats (0/100)")
q3 = st.checkbox("Running (10km)")

if q1 and q2 and q3:
    st.success("QUEST COMPLETED! YOU HAVE SURVIVED.")
else:
    st.info("Penalty Quest will begin in 00:00:10 if not completed.")

# 3. AI Feedback (The "Bot")
st.divider()
st.subheader("🤖 System Feedback")
feedback_input = st.text_input("How does your body feel?")

if feedback_input:
    # This is a simple logic 'bot' - we can make it smarter later!
    st.write(f"System Analysis: '{feedback_input}' detected. Adjusting difficulty for tomorrow.")
