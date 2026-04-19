# 1. PAGE SETUP
st.set_page_config(page_title="SYSTEM: ARISE", page_icon="🌌", layout="wide")

# 2. CLEAN HIGH-END CSS (NO FLICKER)
st.markdown("""
    <style>
    /* Deep Space Galaxy Background */
    .stApp {
        background-image: 
            linear-gradient(to bottom, rgba(5, 5, 10, 0.85), rgba(0, 0, 0, 0.98)),
            url("https://images.unsplash.com/photo-1462331940025-496dfbfc7564?q=80&w=1920&auto=format&fit=crop");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: #00ccff;
    }

    /* Glassmorphism Panels */
    [data-testid="stSidebar"], .stMetric, .stCheckbox {
        background: rgba(0, 15, 30, 0.4) !important;
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        border: 1px solid rgba(0, 204, 255, 0.2) !important;
        border-radius: 15px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.6) !important;
    }

    /* Clean Static Neon Headers (No more roadside pub) */
    h1, h2, h3 {
        text-transform: uppercase;
        font-weight: 900;
        color: #ffffff !important;
        text-shadow: 0 0 10px #00ccff, 0 0 20px #0055ff !important;
        letter-spacing: 2px;
    }

    /* Progress Bar */
    .stProgress > div > div > div > div {
        background-image: linear-gradient(to right, #002244 , #00ccff);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. SAVE SYSTEM (Persistent Data)
SAVE_FILE = "player_data.json"

def load_data():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    # Default fresh start
    return {
        "level": 1, 
        "xp": 0, 
        "stats": {"STR": 10, "AGI": 10, "INT": 10, "VIT": 10}, 
        "last_clear_time": None
    }

def save_data(data):
    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

# Load data into session if not already there
if 'db' not in st.session_state:
    st.session_state.db = load_data()

db = st.session_state.db

# 4. RANK LOGIC
def get_rank():
    if db["level"] < 5: return "E-Rank Hunter", "#808080"
    if db["level"] < 10: return "D-Rank Awakened", "#00ffcc"
    if db["level"] < 20: return "S-Rank Monarch", "#ff00ff"
    return "Shadow Sovereign", "#ffffff"

rank_title, rank_color = get_rank()

# 5. TIMER LOGIC
can_quest = True
time_left_str = ""

if db["last_clear_time"]:
    last_clear = datetime.fromisoformat(db["last_clear_time"])
    time_passed = datetime.now() - last_clear
    
    if time_passed < timedelta(hours=24):
        can_quest = False
        time_remaining = timedelta(hours=24) - time_passed
        # Calculate hours, minutes, seconds for display
        total_seconds = int(time_remaining.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        time_left_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

# 6. SIDEBAR: HUD DISPLAY
with st.sidebar:
    st.title("👤 PLAYER HUD")
    st.markdown(f"### <span style='color:{rank_color};'>{rank_title}</span>", unsafe_allow_html=True)
    st.write("---")
    
    st.metric("SYSTEM LEVEL", db["level"])
    st.write(f"EXP Progress: {db['xp']}%")
    st.progress(db["xp"] / 100)
    
    st.write("### Attributes")
    for stat, val in db["stats"].items():
        st.write(f"{stat}: {val}")
        st.progress(min(val/100, 1.0))

# 7. MAIN CONTENT
st.title("⚔️ SYSTEM: DAILY QUEST")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📝 MISSION LOG")
    
    if can_quest:
        q1 = st.checkbox("🔥 PUSH-UPS (100 REPS)")
        q2 = st.checkbox("⚡ SIT-UPS (100 REPS)")
        q3 = st.checkbox("🦵 SQUATS (100 REPS)")
        q4 = st.checkbox("🏃 10KM RUN")

        if st.button("EXECUTE REWARD PROTOCOL"):
            if q1 and q2 and q3 and q4:
                # Add XP and Stats
                db["xp"] += 50
                if db["xp"] >= 100:
                    db["level"] += 1
                    db["xp"] = 0
                    db["stats"]["STR"] += 5
                    db["stats"]["AGI"] += 3
                    db["stats"]["VIT"] += 4
                    st.balloons()
                
                # Lock out for 24 hours by saving the exact current time
                db["last_clear_time"] = datetime.now().isoformat()
                save_data(db) # Permanently save to hard drive!
                st.rerun() # Refresh app to trigger the timer screen
            else:
                st.error("QUEST INCOMPLETE. PENALTY IMMINENT.")
    else:
        # THE 24-HOUR LOCKOUT SCREEN
        st.info("STATUS: RECOVERING")
        st.success("✅ DAILY QUEST CLEARED")
        st.markdown(f"### ⏳ NEXT QUEST UNLOCKS IN:")
        st.markdown(f"## {time_left_str}")
        
        # A tiny dev button so you don't have to wait 24h while coding
        if st.button("Dev Tool: Reset Timer"):
            db["last_clear_time"] = None
            save_data(db)
            st.rerun()

with col2:
    st.subheader("🤖 SHADOW GUIDE")
    with st.container():
        if not can_quest:
            st.info("System: 'Your physical vessel requires rest to integrate the new strength. The shadows will wait.'")
        elif db["level"] < 5:
            st.warning("System: 'Your body is weak. Complete the daily tasks without fail.'")
        else:
            st.success("System: 'The mana flows smoothly. Arise and conquer.'")
