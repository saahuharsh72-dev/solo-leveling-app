import streamlit as st

# Setup
st.set_page_config(page_title="THE SYSTEM", page_icon="⚔️", layout="wide")

# Dark Theme CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #00ccff; }
    .stMetric { background-color: #1a1c24; padding: 10px; border-radius: 10px; border: 1px solid #00ccff; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. THE DATA ENGINE (Session State) ---
# This keeps your stats from resetting every time you click a button
if 'level' not in st.session_state:
    st.session_state.level = 1
    st.session_state.xp = 0
    st.session_state.strength = 10
    st.session_state.agility = 10

# --- 2. SIDEBAR (Locked Stats) ---
st.sidebar.title("👤 PLAYER STATUS")
st.sidebar.subheader("Rank: E-Rank")

# These are metrics, NOT inputs (so they aren't editable)
st.sidebar.metric("Current Level", st.session_state.level)
st.sidebar.write(f"XP to Level Up: {st.session_state.xp}/100")
st.sidebar.progress(st.session_state.xp / 100)

st.sidebar.divider()
st.sidebar.write("### Attributes")
st.sidebar.text(f"Strength: {st.session_state.strength}")
st.sidebar.text(f"Agility: {st.session_state.agility}")

# --- 3. MAIN QUEST AREA ---
st.title("⚔️ DAILY QUEST: GETTING STRONGER")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### Active Tasks")
    p1 = st.checkbox("100 Push-ups")
    p2 = st.checkbox("100 Sit-ups")
    p3 = st.checkbox("100 Squats")
    p4 = st.checkbox("10km Run")

    # The Button that triggers the change
    if st.button("COLLECT REWARD"):
        if p1 and p2 and p3 and p4:
            # Increase XP
            st.session_state.xp += 50
            st.success("Quest Cleared! +50 XP")
            # Level Up Logic
            if st.session_state.xp >= 100:
                st.session_state.level += 1
                st.session_state.xp = 0
                # Auto-calculate new stats
                st.session_state.strength += 2
                st.session_state.agility += 1
                st.balloons()
                st.toast("LEVEL UP! Your body feels lighter.")
        else:
            st.error("Quest incomplete. The System does not reward laziness.")

with col2:
    st.markdown("### 🤖 Shadow Guide")
    st.info("System is analyzing your growth...")
    
    # Quick AI Feedback based on Level
    if st.session_state.level < 2:
        st.write("Current Status: 'Weak.' Continue training to unlock the Job Change quest.")
    else:
        st.write("Current Status: 'Evolving.' You are no longer the weakest.")
