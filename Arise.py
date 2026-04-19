import streamlit as st
import time

# 1. PAGE CONFIG
st.set_page_config(page_title="THE SYSTEM", page_icon="⚔️", layout="wide")

# 2. ADVANCED DARK THEME & ANIMATIONS (CSS)
st.markdown("""
    <style>
    /* Dark Gradient Background */
    .stApp {
        background: radial-gradient(circle, #0a0c10 0%, #06080a 100%);
        color: #00ccff;
    }
    
    /* Glowing Stat Cards */
    div[data-testid="stMetric"] {
        background-color: rgba(0, 204, 255, 0.05);
        border: 1px solid #00ccff;
        border-radius: 15px;
        box-shadow: 0 0 10px rgba(0, 204, 255, 0.2);
        transition: transform 0.3s ease;
    }
    div[data-testid="stMetric"]:hover {
        transform: scale(1.05);
        box-shadow: 0 0 20px rgba(0, 204, 255, 0.4);
    }

    /* Custom Titles */
    h1, h2, h3 {
        text-shadow: 2px 2px 4px #000000, 0 0 15px #00ccff;
        letter-spacing: 2px;
    }

    /* Checkbox Strike-through Effect */
    .stCheckbox {
        background: rgba(255, 255, 255, 0.02);
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 5px;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. INITIALIZE STATS
if 'level' not in st.session_state: st.session_state.level = 1
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'strength' not in st.session_state: st.session_state.strength = 10
if 'agility' not in st.session_state: st.session_state.agility = 10

# 4. LEVELING LOGIC (The "Evolution")
def get_rank(lvl):
    if lvl < 5: return "E-Rank (The Weakest)"
    elif lvl < 10: return "D-Rank (Awakened)"
    elif lvl < 20: return "C-Rank (Veteran)"
    else: return "S-Rank (Shadow Monarch)"

current_rank = get_rank(st.session_state.level)

# 5. SIDEBAR
st.sidebar.title("👤 PLAYER INFO")
st.sidebar.markdown(f"**RANK:** <span style='color:#ff00ff'>{current_rank}</span>", unsafe_allow_html=True)
st.sidebar.metric("LEVEL", st.session_state.level)
st.sidebar.progress(st.session_state.xp / 100)

st.sidebar.write("---")
st.sidebar.subheader("Attributes")
st.sidebar.metric("Strength", st.session_state.strength)
st.sidebar.metric("Agility", st.session_state.agility)

# 6. MAIN SYSTEM INTERFACE
st.title("⚔️ SYSTEM: DAILY QUEST")
st.subheader("Current Mission: Overcome Your Limits")

col1, col2 = st.columns([2, 1])

with col1:
    st.write("### Quest Log")
    q1 = st.checkbox("Push-ups: 100")
    q2 = st.checkbox("Sit-ups: 100")
    q3 = st.checkbox("Squats: 100")
    q4 = st.checkbox("Running: 10km")

    if st.button("CLAIM REWARD"):
        if q1 and q2 and q3 and q4:
            st.session_state.xp += 50
            if st.session_state.xp >= 100:
                st.session_state.level += 1
                st.session_state.xp = 0
                st.session_state.strength += 5
                st.session_state.agility += 3
                st.balloons()
                st.toast("LEVEL UP! THE SYSTEM HAS CHOSEN YOU.")
            else:
                st.success("Task Complete. XP Gained.")
        else:
            st.error("Penalty Quest Triggered: You cannot deceive the System.")

with col2:
    st.write("### 🤖 Shadow Guide")
    
    # DYNAMIC AI DIALOGUE
    if st.session_state.level < 5:
        st.info("System: 'Your muscles are screaming. Good. That is the sound of growth.'")
    elif st.session_state.level < 10:
        st.warning("System: 'E-Rank limits exceeded. Preparing for Job Change Quest.'")
    else:
        st.error("System: 'Arise. The shadows await your command.'")

    # Interactive Feedback
    mood = st.select_slider("How is your physical fatigue?", options=["Low", "Medium", "High", "Critical"])
    if mood == "Critical":
        st.write("🛡️ *System Suggestion: Focus on Vitality today. Reduce speed, increase form.*")
