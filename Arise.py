import streamlit as st

# This makes the website look like the Solo Leveling Blue Screen
st.set_page_config(page_title="The System", page_icon="⚔️")

# FIX: Changed 'value' to 'html' below
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #00ccff; }
    stMarkdown { color: #00ccff; }
    </style>
    """, unsafe_allow_html=True)

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
    st.balloons()
else:
    st.info("Penalty Quest will begin in 00:00:10 if not completed.")

# 3. AI Feedback (The "Bot")
st.divider()
st.subheader("🤖 System Feedback")
feedback_input = st.text_input("How does your body feel?")

if feedback_input:
    st.write(f"System Analysis: '{feedback_input}' detected. Adjusting difficulty for tomorrow.")
    import streamlit as st
import random

# System configuration for the Solo Leveling Blue Screen
st.set_page_config(page_title="THE SYSTEM", page_icon="⚔️", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #00ccff; font-family: 'Courier New', Courier, monospace; }
    .stMarkdown { color: #00ccff; }
    div.stButton > button { background-color: #004466; color: white; border: 1px solid #00ccff; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR: PLAYER STATUS ---
st.sidebar.title("👤 PLAYER STATUS")
player_name = st.sidebar.text_input("Player Name", "Sung Jin-Woo")
rank = st.sidebar.selectbox("Current Rank", ["E-Rank (Weakest)", "D-Rank", "C-Rank", "B-Rank", "A-Rank", "S-Rank"])

# Level and Stats
if 'level' not in st.session_state: st.session_state.level = 1
if 'xp' not in st.session_state: st.session_state.xp = 0

st.sidebar.metric("Level", st.session_state.level)
st.sidebar.progress(st.session_state.xp / 100)
st.sidebar.write(f"XP: {st.session_state.xp}/100")

st.sidebar.divider()
st.sidebar.write("**Attributes:**")
st.sidebar.text(f"Strength: {10 + st.session_state.level}")
st.sidebar.text(f"Agility: {8 + st.session_state.level}")

# --- MAIN SCREEN ---
st.title(f"⚔️ SYSTEM: DAILY QUEST FOR {player_name.upper()}")
st.write("---")
