import streamlit as st

def calculate_profit(n, T, P, C):
  earnings=0
  time_used=0

  for i in range(T):
    time_used += 5
    if time_used <= n: 
      earnings += (n-time_used)*1500

  for i in range(P):
    time_used += 4
    if time_used <= n: 
      earnings += (n-time_used)*1000

  for i in range(C):
    time_used += 10
    if time_used <= n: 
      earnings += (n-time_used)*2000

  return earnings

def max_profit(n):
  best_profit=0  
  best_solutions=[]

  max_T=n//5
  max_P=n//4
  max_C=n//10

  for T in range(max_T+1):
    for P in range(max_P+1):
      for C in range(max_C+1):
        total_time=5*T+4*P+10*C
        if total_time>n:
          continue
        profit=calculate_profit(n, T, P, C)

        if profit>best_profit:
          best_profit=profit
          best_solutions=[(T, P, C)]
        elif profit==best_profit: 
          best_solutions.append((T, P, C))

  return best_profit, best_solutions

st.set_page_config(page_title="Build Mars Smart: Max Profit Planner", page_icon="🛠️", layout="wide")

st.markdown("""
<style>
body, .main {
    background-color: #000000 !important;
    color: #FFD700 !important;
    font-family: 'Arial', sans-serif;
    padding: 20px;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #111111 !important;
    border-right: 1px solid #333;
    padding: 22px;
}
section[data-testid="stSidebar"] p {
    color: #FFFFFF !important;
    font-size: 15px;
}
section[data-testid="stSidebar"] h2 {
    color: #FFD700 !important;
    font-weight: 700;
}

/* HEADERS */
.main-title {
    text-align: center;
    color: #FFD700;
    font-size: 50px;
    font-weight: 900;
    margin-top: -5px;
    text-shadow: 0 0 15px #DAA520;
}
.sub-title {
    text-align: center;
    color: #FFD700;
    font-size: 22px;
    font-weight: 500;
    margin-top: -15px;
}

/* CARDS */
.gold-card, .strategy-box, .instruction-box {
    background-color: rgba(0,0,0,0.7);
    border: 1px solid #FFD700;
    border-radius: 15px;
    box-shadow: 0 0 20px #FFD700;
    padding: 20px;
    margin-bottom: 20px;
}
.strategy-box p, .instruction-box p {
    color: #FFFFFF;
    font-size: 18px;
}

/* BUTTONS */
div.stButton > button {
    background-color: #111 !important;
    border: 1px solid #FFD700 !important;
    color: #FFD700 !important;
    font-weight: 700 !important;
    font-size: 18px !important;
    border-radius: 12px !important;
    padding: 10px 22px;
    transition: 0.3s;
}
div.stButton > button:hover {
    background-color: #FFD700 !important;
    color: #000000 !important;
    box-shadow: 0 0 20px #FFD700;
}

/* FEEDBACK BOX */
div.stTextArea>div>textarea {
    background-color: #FFD700 !important;
    color: #000000 !important;
    border: 2px solid #333333 !important;
    border-radius: 10px !important;
    padding: 10px !important;
    font-size: 15px !important;
    font-weight: 500;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.markdown("## 🏗️ Build Profiles")

st.sidebar.markdown("""
<div style="color:#FFD700; font-weight:700;">🎭 Theatre</div>
<div style="color:#FFFFFF; margin-left:10px;">
• Time Cost: 5 units<br>
• Earnings: $1500 / time unit
</div>

<div style="color:#FFD700; font-weight:700; margin-top:10px;">🍺 Pub</div>
<div style="color:#FFFFFF; margin-left:10px;">
• Time Cost: 4 units<br>
• Earnings: $1000 / time unit
</div>

<div style="color:#FFD700; font-weight:700; margin-top:10px;">🏢 Commercial Park</div>
<div style="color:#FFFFFF; margin-left:10px;">
• Time Cost: 10 units<br>
• Earnings: $2000 / time unit
</div>
""", unsafe_allow_html=True)


st.sidebar.markdown("## 💬 Feedback")
feedback = st.sidebar.text_area("Share your thoughts or suggestions:", placeholder="Your input helps make this app better ✨")

if st.sidebar.button("Submit Feedback"):
    st.sidebar.success("Thank you! Your feedback is appreciated 💛")


st.markdown("<h1 class='main-title'>🚧 Build Mars Smart: Max Profit Planner</h1>", unsafe_allow_html=True)

st.markdown("<p class='sub-title'>Design Mars’ most profitable city layout using smart property optimization.</p>",unsafe_allow_html=True)

st.markdown("""
<div class="instruction-box" style="text-align:center;">
<h2 style="color:#FFD700; font-weight:700;">🚀 Quick Start Guide</h2>
<p>• Enter your available construction time to calculate the best property mix.</p>
<p>• Click <b>✨ Generate Optimal Strategies</b> to see top-earning builds.</p>
<p>• Check the suggested combinations for Theatres, Pubs, and Commercial Parks.</p>
<p>• View maximum potential earnings to plan efficiently.</p>
<p>• Adjust time units to explore profit variations.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### 🪙 Specify Your Total Available Construction Time (units)")
n = st.number_input("Enter your total available build time:", min_value=0, step=1)


if st.button("✨ Generate Optimal Strategies"):
    profit, solutions = max_profit(int(n))

    st.markdown(f"""
    <div class="gold-card">
        <h2 style='color:#FFD700;'>💰 Maximum Potential Earnings: ${profit:,}</h2>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🏗️ Optimal Construction Plan")

    for i, (T, P, C) in enumerate(solutions, start=1):
        st.markdown(f"""
        <div class="strategy-box">
            <h3 style='color:#FFD700;'>Strategy {i} 💡</h3>
            <p>
                🎭 <b>Theatres:</b> {T} &nbsp;&nbsp;
                🍺 <b>Pubs:</b> {P} &nbsp;&nbsp;
                🏢 <b>Commercial Parks:</b> {C}
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="gold-card">
        <p style='color:#FFFFFF;'>
        "These configurations deliver the highest possible earnings within the given time."
        </p>
    </div>
    """, unsafe_allow_html=True)
