import streamlit as st
import time

# 1. Page Configuration for a Premium Native App Feel
st.set_page_config(
    page_title="Kanpur 1 - Elite Pitch Intelligence",
    page_icon="🔮",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 2. State Management Configuration
if 'animation_played' not in st.session_state:
    st.session_state.animation_played = False
if 'page' not in st.session_state:
    st.session_state.page = 1
if 'task_type' not in st.session_state:
    st.session_state.task_type = None
if 'competitor' not in st.session_state:
    st.session_state.competitor = None
if 'pitch_generated' not in st.session_state:
    st.session_state.pitch_generated = False

# ==========================================
# CRED SIGNATURE TRANSITION SCREEN
# ==========================================
if not st.session_state.animation_played:
    # Embedded cinematic CSS injection for the intro splash screen
    st.markdown("""
        <style>
        .stApp { background-color: #0A0A0A !important; }
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        .splash-container {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background-color: #0A0A0A;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 99999;
            font-family: -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        .cred-logo-text {
            font-size: 32px;
            font-weight: 200;
            letter-spacing: 6px;
            color: #FFFFFF;
            text-transform: uppercase;
            opacity: 0;
            animation: fadeInOut 2.8s cubic-bezier(0.25, 1, 0.5, 1) forwards;
        }
        
        .cred-sub-text {
            font-size: 10px;
            font-weight: 600;
            letter-spacing: 4px;
            color: #00E5FF;
            text-transform: uppercase;
            margin-top: 15px;
            opacity: 0;
            animation: subFadeInOut 2.8s cubic-bezier(0.25, 1, 0.5, 1) forwards;
        }

        @keyframes fadeInOut {
            0% { opacity: 0; transform: scale(0.95); filter: blur(4px); }
            30% { opacity: 1; transform: scale(1); filter: blur(0px); }
            70% { opacity: 1; transform: scale(1); filter: blur(0px); }
            100% { opacity: 0; transform: scale(1.02); filter: blur(2px); }
        }
        
        @keyframes subFadeInOut {
            0% { opacity: 0; }
            40% { opacity: 0.7; }
            70% { opacity: 0.7; }
            100% { opacity: 0; }
        }
        </style>
        
        <div class="splash-container">
            <div class="cred-logo-text">Kanpur Pitch Pro</div>
            <div class="cred-sub-text">PhonePe Elite Intelligence</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Wait for the cinematic CSS keyframe timeline to complete, then flip state
    time.sleep(2.8)
    st.session_state.animation_played = True
    st.rerun()


# ==========================================
# MAIN APPLICATION INTERFACE (CRED STYLING)
# ==========================================
st.markdown("""
    <style>
    /* Global Background Override */
    .stApp {
        background-color: #0A0A0A !important;
        color: #F5F5F7 !important;
    }
    
    /* Hide Default Header Elements */
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Text Typography styling */
    h1, h2, h3, p, label {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
    }
    
    /* Custom Navigation Pills mimicking CRED tabs */
    .cred-nav-container {
        display: flex;
        justify-content: space-between;
        background-color: #121212;
        padding: 6px;
        border-radius: 30px;
        border: 1px solid #222222;
        margin-bottom: 25px;
        animation: fadeInUI 0.8s ease-out forwards;
    }
    .cred-nav-item {
        flex: 1;
        text-align: center;
        padding: 8px 0;
        font-size: 13px;
        font-weight: 600;
        letter-spacing: 0.5px;
        color: #666666;
    }
    .cred-nav-active {
        color: #00E5FF !important;
        background-color: #1A1A1A;
        border-radius: 25px;
        border: 1px solid #333333;
    }
    
    /* Sophisticated Container Cards */
    .cred-card {
        background: linear-gradient(145deg, #141414, #0D0D0D);
        border: 1px solid #1C1C1E;
        padding: 24px;
        border-radius: 18px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        margin-bottom: 20px;
        animation: fadeInUI 0.8s ease-out forwards;
    }
    
    .pitch-box {
        background-color: #0F1A1C;
        border: 1px solid #1A3A3E;
        padding: 20px;
        border-radius: 14px;
        color: #E0F7FA;
        font-size: 15px;
        line-height: 1.6;
        margin-top: 15px;
    }
    
    /* Market Share Floating Ticker */
    .market-share-ticker {
        background-color: #111111;
        border-top: 1px solid #222222;
        padding: 12px 20px;
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        width: 100%;
        display: flex;
        justify-content: space-around;
        align-items: center;
        z-index: 999;
    }
    .ticker-item {
        font-size: 12px;
        font-weight: 500;
        letter-spacing: 0.5px;
        color: #8E8E93;
    }
    .ticker-value {
        font-weight: bold;
        margin-left: 5px;
    }
    
    /* Streamlit widget override adjustments */
    div.stButton > button {
        background-color: #1C1C1E !important;
        color: #FFFFFF !important;
        border: 1px solid #2C2C2E !important;
        padding: 14px 24px !important;
        border-radius: 12px !important;
        width: 100% !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
    }
    div.stButton > button:hover {
        border-color: #00E5FF !important;
        color: #00E5FF !important;
        background-color: #121212 !important;
        box-shadow: 0 0 15px rgba(0, 229, 255, 0.2) !important;
    }
    
    /* Highlight Action Button Override */
    .action-btn button {
        background: linear-gradient(90deg, #5F259F, #00E5FF) !important;
        color: #FFFFFF !important;
        border: none !important;
    }

    @keyframes fadeInUI {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    </style>
""", unsafe_allow_html=True)

# Navigation Helper Functions
def go_to_page(page_num):
    st.session_state.page = page_num
    if page_num < 3:
        st.session_state.pitch_generated = False
    st.rerun()

# Global Core Intelligence Database
data = {
    "ECB Smart Speaker": {
        "Paytm": {
            "hook": "Hidden Rental Audit & Direct Service",
            "points": [
                "Expose the hidden monthly device rentals via the Paytm Business App filter history.",
                "Highlight the current PhonePe special retention discount (₹318/₹349 setup fee).",
                "Contrast Paytm's frustrating online ticket/chatbot support with PhonePe's dedicated Area Sector Incharge.",
                "Zero online customer care dependency; direct call to the local executive for instant resolution."
            ],
            "pitch": "Bhaiya, ek minute dijiye, main aapko aapke Paytm Business app mein ek cheez dikhata hoon. Aap bol rahe ho na ki sirf ₹1 kat ta hai? Yeh dekho, app ke 'Soundbox History' aur 'Filters' mein jaakar—yeh har mahine ka hidden rental kat raha hai aapka. PhonePe par humare purane merchants ke liye abhi ek special offer chal raha hai jismein setup fee par bhari discount hai (sirf ₹318/₹349 live stock ke hisab se). Aur sabse badi baat—Paytm mein agar speaker kharab ho jaye, toh unke customer care par robot se chat karte-karte thak jaoge, koi sunne wala nahi hota. PhonePe par humara system bilkul alag hai. Humne aapke Kanpur ke isi market area mein ek dedicated Sector Incharge bitha rakha hai. Koi online ticket-vicket raising ka jhamela nahi hai. Ek call ghumao, humara ladka turant aapki dukaan par hazir hoga. Agar daily target hit kar lete ho, toh rental bhi zero aur service bhi top class!"
        },
        "BharatPe": {
            "hook": "Market Volume & Hyper-Local Support",
            "points": [
                "Leverage the fact that 70% to 80% of local consumers natively use PhonePe.",
                "Explain how routing PhonePe users through a third-party QR delays settlements.",
                "Pitch the reliable on-ground network: Local Sector Incharges stationed in every specific market zone.",
                "Emphasize fast, direct human support over automated, slow online complaint portals."
            ],
            "pitch": "Bhaiya, aap khud dekho, aapke dukaan par jitne bhi log aate hain, unmein se 70% se 80% log PhonePe use karte hain. Jab consumer hi PhonePe ka hai, toh aap BharatPe ke QR par ghumakar settlement kyun delay kar rahe ho? Seedha PhonePe ka Smart Speaker lagao. Customers ke liye bhi frictionless payment hoga aur isi transaction volume ke basis par aapka loan offer bhi raat-o-raat active ho jayega. Rahi baat service ki—toh BharatPe ka na toh koi on-ground aadmi milta hai aur na hi unka support system local hai. Humara Sector Incharge har waqt isi market mein rehta hai. Kal ko network ka ya payment ka koi bhi issue aaye, aapko kisi app par jaakar shikayat nahi darj karni. Aapke paas humare local team ka number hoga, direct phone milao aur on-the-spot tension saaf!"
        },
        "Google Pay": {
            "hook": "Ecosystem Priority & Speed",
            "points": [
                "Position the speaker as a gateway to the merchant ecosystem, not just an audio box.",
                "Explain how device deployment pushes the merchant into top-priority lending brackets.",
                "Frame GPay as a distant tech platform with zero local human service architecture.",
                "Highlight PhonePe's hyper-local team backup ensuring 100% counter uptime."
            ],
            "pitch": "Bhaiya, Google Pay ka speaker sirf ek audio box hai, usse aapke business ko koi fayda nahi mil raha. PhonePe ka Smart Speaker lagane ka matlab hai ki aapka business humare system mein top priority par aa jata hai. Iske lagte hi aapka business loan pre-approve ho jata hai, aur aane wale time mein jo shop insurance aur retail health benefits hum de rahe hain, uski facilities bhi sabse pehle aapko milengi. Aur sabse matted baat bataun? Google Pay ka koi local office ya on-ground team nahi hai Kanpur mein. Kuch dikkat aayi toh mail likhte reh jaoge. PhonePe ka hamara local Sector Incharge hamesha aapke area mein round par rehta hai. Humara maqsad hai ki aapka counter kabhi band na ho. Bina kisi online ticketing ke, hand-to-hand aur reliable service sirf PhonePe par milti hai."
        },
        "Banks": {
            "hook": "Single Settlement & 2-Hour Swap",
            "points": [
                "Expose that bank QRs dump every single transaction directly into the bank account, making it tedious to track and verify daily business in the ledger.",
                "Highlight PhonePe’s unified end-of-day (EOD) single settlement that makes daily tracking effortless.",
                "Contrast slow, institutional bank compliance with PhonePe's 1-2 hour physical device replacement guarantee.",
                "Eliminate bank manager visits with direct Sector Incharge direct-line access."
            ],
            "pitch": "Bhaiya, bank wale QR mein sabse bada jhamela yeh hai ki unke yahan har ek chota-mota transaction seedha aapke bank account mein jaakar girta hai. Ab din bhar mein 100 transaction huye toh aapki passbook aur bank ledger mein 100 entries bhar jayengi, jisse har ek transaction ko verify karna aur track rakhna bohot tedious aur mushkil ho jata hai. PhonePe par aisa kachra nahi hota! Hum din bhar ka poora collection ek sath, single settlement mein aapke bank mein bhejte hain, jisse har din ka dhandha track karna bilkul aasan ho jata hai. Aur agar aapko kisi ek transaction ki in-depth detail chahiye, toh aap PhonePe Business app mein dekh sakte hain. Sabse badi baat—bank ka speaker kharab hua toh aap apni chalti dukaan chhod kar manager ke samne application lekar khade hoge kya? Bank ka support system bohot dheema hai. Humare yahan har area ke liye alag Sector Incharge assigned hai. Machine mein 1% dikkat aayi, direct call karo, ladka 1 se 2 ghante ke andar dukaan par aakar physically speaker badal kar dega. Hum dhandha rukne nahi dete!"
        }
    },
    "Merchant Lending": {
        "Paytm": {
            "hook": "APR Exposure & Professional Advisory",
            "points": [
                "Expose Paytm’s true Annual Percentage Rate (APR) of 36%–37% hidden under processing fees and GST.",
                "Pitch PhonePe’s clear, low monthly entry-level interest rates of 1.25%–1.5%.",
                "Highlight the security of having an active on-ground Sector Incharge to assist with any payment queries during the loan tenure.",
                "Avoid cold automated fintech systems with localized human relationship managers."
            ],
            "pitch": "Bhaiya, agar aapne Paytm se loan lene ka socha hai ya liya hai, toh unka ek baar interest certificate nikal kar dekhiye. Woh upar se bolte hain 2% mahina, par hidden charges, processing fees aur GST milakar saal ka 36% se 37% tak baithta hai. Aap loot rahe ho wahan! Ek baar PhonePe ka loan banner check kariye, hum aapko pehli dafa mein hi 1.25% se 1.5% ke clear interest rate par loan de rahe hain. Koi hidden jhamela nahi hai. Aur sabse badhiya baat, Paytm par loan lene ke baad agar collection ya deduction ka koi confusion ho, toh aap chatbot se sarr marte reh jaoge. PhonePe par aapka bhai, humara local Sector Incharge hamesha aapke sath khada hai. Kuch bhi baat ho, direct usko phone lagao, woh aakar table par baith kar aapka hisab clear karega. Jan local support ka bharosa ho, toh dhandha fikar-mukt chalta hai."
        },
        "BharatPe": {
            "hook": "Continuity, Top-Up & Relationship Trust",
            "points": [
                "Pitch PhonePe's 'Continuous Eligibility' model allowing active Top-Ups without full closure.",
                "Guarantee new repeat loan banners within 1 week of closing a current loan block.",
                "Position the local Sector Incharge as an advocate who monitors your QR health to unlock bigger limits.",
                "Emphasize that reliable, human ground-support is unmatched by corporate apps."
            ],
            "pitch": "Bhaiya, BharatPe loan deta hai, thik hai. Par PhonePe aapko 'Continuous Eligibility' deta hai. Iska matlab yeh hai ki agar aapka loan chal raha hai aur aapko beech mein paise ki zaroorat padi, toh aapko live Top-Up ka option mil jata hai. Aur jaise hi aap purana loan close karte ho, within 1 week aapko naya repeat loan ka banner mil jata hai. Itna hi nahi, jag aap humare sath 3-4 loan cycle poori kar lete ho, toh aapki processing fee bhi bilkul zero ho jaati hai. Sabse bada fayda pata hai kya hai? BharatPe mein sab kuch digital machine par chalta hai, unka koi local chehra nahi hai aapse baat karne ke liye. PhonePe par humara Sector Incharge aapke touch mein rehta hai. Woh aapke QR ka health aur volume track karke system se aapki limit badhwane mein khud madad karta hai. Yeh machine ka nahi, bharose aur asli insani service ka rishta hai."
        },
        "Google Pay": {
            "hook": "Document-Free Capital & Speed Verification",
            "points": [
                "Highlight 100% collateral-free, paperless lending backed purely by QR volume.",
                "Explain the lightning-fast 24 to 48-hour direct bank account capital disbursal.",
                "Contrast GPay's complicated third-party NBFC approvals with PhonePe's streamlined processing.",
                "Emphasize that the local Sector Incharge can expedite and verify any glitch on the spot."
            ],
            "pitch": "Bhaiya, market mein kahin bhi loan lene jaoge toh itne documents maangenge ki aap pareshan ho jaoge. PhonePe par agar aapka loan offer aaya hai, toh aapko koi collateral ya paperwork nahi chahiye. Sirf basic Aadhaar aur PAN card verify karna hai screen par, aur 24 se 48 ghante ke andar paisa seedha aapke linked bank account mein credit! Google Pay par teesri party ka jhamela rehta hai, unka customer care kabhi phone nahi uthata. Humare yahan agar aapka loan process hote waqt koi technical glitch aa bhi gaya, toh aapko pareshan nahi hona hai. Aap seedha humare area ke Sector Incharge ko batayiye, woh piche system par baat karke aapka temporary block turant clear karwayega. Fast capital ke sath fast aur reliable ground service sirf humare paas hai."
        },
        "Banks": {
            "hook": "Passbook Cleaning & The 'Izzat' Factor",
            "points": [
                "Detail how bank QRs clutter the main bank ledger with individual micro-transactions, creating thousands of tedious entries that ruin credit assessments.",
                "Explain PhonePe's single daily settlement architecture that keeps bank statements clean and premium for future big loans.",
                "Highlight that local financiers attack a merchant's local reputation if collections dip.",
                "Position the PhonePe automated EOD tracking and local Sector Incharge backing as a total peace-of-mind shield."
            ],
            "pitch": "Bhaiya, bank se loan lene par ya bank ka QR chalane par sabse badi dikkat yeh hai ki har ek transaction seedha aapke bank account mein credit hota hai. Isse mahine mein hazaron entries ho jaati hain aur bank ledger itna tedious jata hai ki ek-ek entry ko verify karna aur hisab rakhna sir-dard ban jata hai. Jab bank ka bada manager aapki passbook mein yeh kachra dekhega na, toh badi loan file reject kar dega. PhonePe par kya hota hai—din bhar ka jitna bhi collection hai, woh raat ko sirf ek single unified settlement entry ke roop mein bank mein jata hai. Mahine mein sirf 30 entries! Aapka bank statement bilkul premium aur clean rahega. Aur doosra bada khatra—market ke local financiers se james aap paisa uthate ho, toh mandi aane par woh dukaan par aakar khade ho jaate hain. Kanpur market mein dhandhe se badi apni izzat hoti hai—baat seedhe izzat par aa jaati hai! PhonePe par aapka loan chalega toh digital automatic settlement se chalega. Koi aapke counter par aakar tamasha nahi karega. Aur kisi bhi tarah ke manual verification ya madad ke liye humara area Sector Incharge hamesha available hai. Na manager ke chakkar katna, na online ticket raise karna, bilkul izzat aur shanti se apna dhandha bada karo!"
        }
    }
}

# 3. Native Visual Navigation Bar (CRED Tracker)
p1_class = "cred-nav-active" if st.session_state.page == 1 else ""
p2_class = "cred-nav-active" if st.session_state.page == 2 else ""
p3_class = "cred-nav-active" if st.session_state.page == 3 else ""

st.markdown(f"""
    <div class='cred-nav-container'>
        <div class='cred-nav-item {p1_class}'>01. TARGET</div>
        <div class='cred-nav-item {p2_class}'>02. COMPETITION</div>
        <div class='cred-nav-item {p3_class}'>03. INTELLIGENCE</div>
    </div>
""", unsafe_allow_html=True)


# ==========================================
# PAGE 1: CHOOSE TARGET OPERATION TASK
# ==========================================
if st.session_state.page == 1:
    st.markdown("<h3 style='font-size:16px; color:#8E8E93; text-transform:uppercase; letter-spacing:1px; margin-bottom:5px;'>Step 01</h3>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size:26px; font-weight:700; color:#FFF; margin-bottom:25px;'>Select Market Objective</h2>", unsafe_allow_html=True)
    
    st.markdown("<div class='cred-card'>", unsafe_allow_html=True)
    if st.button("🔊 ECB Smart Speaker Deployment", key="btn_speaker"):
        st.session_state.task_type = "ECB Smart Speaker"
        go_to_page(2)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='cred-card'>", unsafe_allow_html=True)
    if st.button("💼 Merchant Lending Scale-Up", key="btn_lending"):
        st.session_state.task_type = "Merchant Lending"
        go_to_page(2)
    st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# PAGE 2: CHOOSE COUNTER COMPETITOR
# ==========================================
elif st.session_state.page == 2:
    st.markdown(f"<p style='color:#00E5FF; font-size:13px; font-weight:600;'>🎯 TARGET: {st.session_state.task_type}</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size:26px; font-weight:700; color:#FFF; margin-bottom:25px;'>Identify Competitor on Counter</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='cred-card' style='text-align:center;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='color:#00E5FF; margin-bottom:10px;'>🔵 PAYTM</h4>", unsafe_allow_html=True)
        if st.button("Select Paytm", key="comp_paytm"):
            st.session_state.competitor = "Paytm"
            go_to_page(3)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='cred-card' style='text-align:center;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='color:#4285F4; margin-bottom:10px;'>🟢 GOOGLE PAY</h4>", unsafe_allow_html=True)
        if st.button("Select GPay", key="comp_gpay"):
            st.session_state.competitor = "Google Pay"
            go_to_page(3)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div class='cred-card' style='text-align:center;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='color:#FF9100; margin-bottom:10px;'>🟠 BHARATPE</h4>", unsafe_allow_html=True)
        if st.button("Select BharatPe", key="comp_bharatpe"):
            st.session_state.competitor = "BharatPe"
            go_to_page(3)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='cred-card' style='text-align:center;'>", unsafe_allow_html=True)
        st.markdown("<h4 style='color:#A4A4A4; margin-bottom:10px;'>🏛️ TRADITIONAL BANKS</h4>", unsafe_allow_html=True)
        if st.button("Select Bank", key="comp_banks"):
            st.session_state.competitor = "Banks"
            go_to_page(3)
        st.markdown("</div>", unsafe_allow_html=True)
        
    if st.button("← Back to Objectives", key="back_p2"):
        go_to_page(1)


# ==========================================
# PAGE 3: PITCH STRATEGY & DIALOGUE GENERATOR
# ==========================================
elif st.session_state.page == 3:
    st.markdown(f"<p style='color:#8E8E93; font-size:12px; letter-spacing:0.5px;'>{st.session_state.task_type}  //  {st.session_state.competitor.upper()}</p>", unsafe_allow_html=True)
    
    selected_node = data[st.session_state.task_type][st.session_state.competitor]
    
    st.markdown(f"<h2 style='font-size:24px; font-weight:700; color:#FFF; margin-bottom:5px;'>{selected_node['hook']}</h2>", unsafe_allow_html=True)
    st.write("---")
    
    st.markdown("<p style='color:#FFB300; font-weight:600; font-size:14px; text-transform:uppercase;'>📋 Strategic Counter Points</p>", unsafe_allow_html=True)
    for bullet in selected_node['points']:
        st.markdown(f"<div style='padding: 6px 0; font-size:14px; color:#E5E5EA;'>• {bullet}</div>", unsafe_allow_html=True)
        
    st.write("")
    
    if not st.session_state.pitch_generated:
        st.markdown("<div class='action-btn'>", unsafe_allow_html=True)
        if st.button("⚡ Generate Custom Field Pitch", key="gen_pitch_btn"):
            st.session_state.pitch_generated = True
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:#00E5FF; font-weight:600; font-size:14px; text-transform:uppercase; margin-bottom:0;'>🗣️ Spoken Hinglish Script (Izhar Flow)</p>", unsafe_allow_html=True)
        st.markdown(f"<div class='pitch-box'>{selected_node['pitch']}</div>", unsafe_allow_html=True)
        
        st.write("")
        st.markdown("<p style='color:#8E8E93; font-size:12px; font-weight:600;'>🎵 PLAY AUDIO COACHING TRACK</p>", unsafe_allow_html=True)
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

    st.write("---")
    if st.button("← Start New Audit", key="restart_btn"):
        go_to_page(1)


# ==========================================
# FIXED PREMIUM BOTTOM TAB: KANPUR REGION MARKET SHARE
# ==========================================
st.markdown("""
    <div class='market-share-ticker'>
        <span class='ticker-item'>📍 KANPUR REGION DATA MATRIX</span>
        <span class='ticker-item'>🔮 PhonePe Share: <span class='ticker-value' style='color:#00E5FF;'>38.2%</span></span>
        <span class='ticker-item'>📉 Paytm Share: <span class='ticker-value' style='color:#FF3B30;'>37.1%</span></span>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)
