st.markdown("""
<style>

/* 🌌 Background */
.stApp {
    background: radial-gradient(circle at center, #020412 0%, #000000 100%);
    color: #00eaff;
    font-family: 'Orbitron', sans-serif;
}

/* 🧊 Holographic Panel */
.holo-box {
    background: rgba(0, 20, 40, 0.35);
    border: 1px solid rgba(0, 234, 255, 0.4);
    border-radius: 12px;
    padding: 20px;
    box-shadow: 
        0 0 15px rgba(0, 234, 255, 0.3),
        inset 0 0 10px rgba(0, 234, 255, 0.2);
    backdrop-filter: blur(10px);
}

/* ⚡ Glowing Title */
.system-title {
    font-size: 40px;
    font-weight: 900;
    text-align: center;
    color: #00eaff;
    text-shadow: 
        0 0 10px #00eaff,
        0 0 20px #0088ff,
        0 0 40px #0055ff;
    animation: pulse 2s infinite;
}

/* ✨ Pulse Animation */
@keyframes pulse {
    0% { text-shadow: 0 0 5px #00eaff; }
    50% { text-shadow: 0 0 25px #00eaff; }
    100% { text-shadow: 0 0 5px #00eaff; }
}

/* 📺 Scanline Effect */
.stApp::after {
    content: "";
    position: fixed;
    top:0; left:0;
    width:100%; height:100%;
    background: repeating-linear-gradient(
        to bottom,
        rgba(0,255,255,0.03) 0px,
        rgba(0,255,255,0.03) 1px,
        transparent 2px,
        transparent 4px
    );
    pointer-events: none;
}

/* ⚠️ System Alert Box */
.system-alert {
    background: rgba(0,0,0,0.6);
    border-left: 4px solid #00eaff;
    padding: 15px;
    font-weight: bold;
    animation: flicker 1.5s infinite;
}

/* 🔥 Flicker animation */
@keyframes flicker {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.6; }
}

</style>
""", unsafe_allow_html=True
