import streamlit as st

# 1. PAGE SETUP
st.set_page_config(page_title="SYSTEM: ARISE", page_icon="🌌", layout="wide")

# 2. GALAXY & SHADOW HUD CSS 
st.markdown("""
    <style>
    /* Deep Space Galaxy Background with Shadow Overlay */
    .stApp {
        background-image: 
            linear-gradient(to bottom, rgba(5, 5, 10, 0.75), rgba(0, 0, 0, 0.95)),
            url("https://images.unsplash.com/photo-1462331940025-496dfbfc7564?q=80&w=1920&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #00ccff;
    }

    /* Glassmorphism Panels - Now more transparent so you can see the galaxy */
    [data-testid="stSidebar"], .stMetric, .stCheckbox {
        background: rgba(0, 15, 30, 0.4) !important;
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border: 1px solid rgba(0, 204, 255, 0.2) !important;
        border-radius: 15px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.6) !important;
    }

    /* Animated Neon Headers */
    h1 {
        text-transform: uppercase;
        font-weight: 900;
        color: #fff;
        text-shadow: 0 0 5px #fff, 0 0 10px #00ccff, 0 0 20px #00ccff;
        animation: flicker 2s infinite alternate;
    }

    @keyframes flicker {
        0%, 18%, 22%, 25%, 53%, 57%, 100% { text-shadow: 0 0 5px #fff, 0 0 10px #00ccff; }
        20%, 24%, 55% { text-shadow: none; }
    }

    /* Progress Bar Color */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #002244 , #00ccff);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. DATABASE INITIALIZATION
if 'level' not in st.session_state: st.session_state.level = 1
if 'xp' not in st.session_state: st.session_state.xp = 0
if 'stats' not in st.session_state: 
    st.session_state.stats = {"STR": 10, "AGI": 10, "INT": 10, "VIT": 10}

# 4. LEVEL & RANK CALCULATOR
def get_rank():
    lvl = st.session_state.level
    if lvl < 5: return "E-Rank Hunter", "#808080"
    if lvl < 10: return "D-Rank Awakened", "#00ffcc"
    if lvl < 20: return "S-Rank Monarch", "#ff00ff"
    return "Shadow Sovereign", "#ffffff"

rank_title, rank_color = get_rank()

# 5. SIDEBAR: HUD DISPLAY
with st.sidebar:
    st.title("👤 PLAYER HUD")
    st.markdown(f"### <span style='color:{rank_color}; text-shadow: 0 0 10px {rank_color};'>{rank_title}</span>", unsafe_allow_html=True)
    st.write("---")
    
    st.metric("SYSTEM LEVEL", st.session_state.level)
    st.write(f"EXP Progress: {st.session_state.xp}%")
    st.progress(st.session_state.xp / 100)
    
    st.write("### Attributes")
    for stat, val in st.session_state.stats.items():
        st.write(f"{stat}: {val}")
        st.progress(min(val/100, 1.0))

# 6. MAIN CONTENT
st.title("⚔️ SYSTEM: DAILY QUEST")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 MISSION LOG")
    q1 = st.checkbox("🔥 PUSH-UPS (100 REPS)", key="c1")
    q2 = st.checkbox("⚡ SIT-UPS (100 REPS)", key="c2")
    q3 = st.checkbox("🦵 SQUATS (100 REPS)", key="c3")
    q4 = st.checkbox("🏃 10KM RUN", key="c4")

    if st.button("EXECUTE REWARD PROTOCOL"):
        if q1 and q2 and q3 and q4:
            st.session_state.xp += 50
            if st.session_state.xp >= 100:
                st.session_state.level += 1
                st.session_state.xp = 0
                st.session_state.stats["STR"] += 5
                st.session_state.stats["AGI"] += 3
                st.session_state.stats["VIT"] += 4
                st.balloons()
            st.success("STRENGTH RECORDED. EVOLUTION CONTINUES...")
        else:
            st.error("QUEST INCOMPLETE. PENALTY IMMINENT.")

with col2:
    st.subheader("🤖 SHADOW GUIDE")
    with st.container():
        st.write(f"**Vessel Status:** {rank_title}")
        if st.session_state.level < 5:
            st.info("System: 'The shadows are swirling around you, but your vessel is still too weak. Keep grinding.'")
        else:
            st.warning("System: 'Warning: Detecting mana overflow. The shadows are ready to obey.'")
            
    st.divider()
    feedback = st.text_input("Report Physical Strain Level:")
    if feedback:
        st.write(f"System Logging: '{feedback}'. Adjusting recovery protocol.")
