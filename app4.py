import streamlit as st
import time

# 1. Page Configuration for a Premium Native App Feel
st.set_page_config(
    page_title="Kanpur Pitch Pro",
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
            font-family: -apple-system, BlinkMacSystemFont, "Helvetica Neue", sans-serif;
        }
        
        .cred-logo-text {
            font-size: 36px;
            font-weight: 200;
            letter-spacing: 8px;
            color: #FFFFFF;
            text-transform: uppercase;
            opacity: 0;
            animation: fadeInOut 2.8s cubic-bezier(0.25, 1, 0.5, 1) forwards;
        }
        
        .cred-sub-text {
            font-size: 11px;
            font-weight: 500;
            letter-spacing: 5px;
            color: #8E8E93;
            text-transform: uppercase;
            margin-top: 15px;
            opacity: 0;
            animation: subFadeInOut 2.8s cubic-bezier(0.25, 1, 0.5, 1) forwards;
        }

        @keyframes fadeInOut {
            0% { opacity: 0; transform: scale(0.96); filter: blur(6px); }
            30% { opacity: 1; transform: scale(1); filter: blur(0px); }
            70% { opacity: 1; transform: scale(1); filter: blur(0px); }
            100% { opacity: 0; transform: scale(1.03); filter: blur(4px); }
        }
        
        @keyframes subFadeInOut {
            0% { opacity: 0; }
            40% { opacity: 0.8; }
            70% { opacity: 0.8; }
            100% { opacity: 0; }
        }
        </style>
        
        <div class="splash-container">
            <div class="cred-logo-text">Kanpur Pitch Pro</div>
            <div class="cred-sub-text">PhonePe Elite Intelligence</div>
        </div>
    """, unsafe_allow_html=True)
    
    time.sleep(2.8)
    st.session_state.animation_played = True
    st.rerun()


# ==========================================
# MAIN APPLICATION INTERFACE (CRED STYLING)
# ==========================================
st.markdown("""
    <style>
    /* Global Clean Typography and Dark Mode Overrides */
    .stApp {
        background-color: #0A0A0A !important;
        color: #F5F5F7 !important;
    }
    
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    h1, h2, h3, h4, p, label, div {
        font-family: -apple-system, BlinkMacSystemFont, "SF Pro Display", "Helvetica Neue", sans-serif !important;
    }
    
    /* CRED Minimalist Nav Tickers */
    .cred-nav-container {
        display: flex;
        justify-content: space-between;
        background-color: #0F0F0F;
        padding: 5px;
        border-radius: 0px;
        border-bottom: 1px solid #1C1C1E;
        margin-bottom: 30px;
        animation: fadeInUI 0.5s ease-out forwards;
    }
    .cred-nav-item {
        flex: 1;
        text-align: center;
        padding: 10px 0;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 1.5px;
        color: #444444;
    }
    .cred-nav-active {
        color: #FFFFFF !important;
        border-bottom: 2px solid #FFFFFF;
    }
    
    /* Flat Ultra-Sophisticated Containers */
    .cred-card {
        background: #111111;
        border: 1px solid #1C1C1E;
        padding: 24px;
        border-radius: 0px;
        margin-bottom: 20px;
        animation: fadeInUI 0.6s ease-out forwards;
    }
    
    .pitch-box {
        background-color: #16161A;
        border: 1px solid #2C2C2E;
        padding: 24px;
        border-radius: 0px;
        color: #E5E5EA;
        font-size: 15px;
        line-height: 1.7;
        margin-top: 20px;
        letter-spacing: 0.3px;
        animation: fadeInUI 0.5s ease-out forwards;
    }
    
    /* High Contrast Text Markers */
    .highlight-amber {
        color: #FFD60A !important;
        font-weight: 700 !important;
    }
    .highlight-neon {
        color: #30D158 !important;
        font-weight: 700 !important;
    }
    .highlight-cyan {
        color: #0A84FF !important;
        font-weight: 700 !important;
    }
    
    /* Fixed Dynamic Bottom Dashboard Metrics */
    .market-share-ticker {
        background-color: #0A0A0A;
        border-top: 1px solid #1C1C1E;
        padding: 16px 20px;
        position: fixed;
        bottom: 0; left: 0; right: 0; width: 100%;
        display: flex;
        justify-content: space-around;
        align-items: center;
        z-index: 999;
    }
    .ticker-item {
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 1px;
        color: #8E8E93;
        text-transform: uppercase;
    }
    .ticker-value {
        font-weight: 700;
        margin-left: 6px;
    }
    
    /* Heavy Modded CRED System Buttons */
    div.stButton > button {
        background-color: #1C1C1E !important;
        color: #FFFFFF !important;
        border: 1px solid #2C2C2E !important;
        padding: 16px 20px !important;
        border-radius: 0px !important;
        width: 100% !important;
        font-size: 13px !important;
        font-weight: 500 !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        transition: all 0.2s ease-in-out !important;
    }
    div.stButton > button:hover {
        border-color: #FFFFFF !important;
        background-color: #FFFFFF !important;
        color: #0A0A0A !important;
    }
    
    /* Premium Call To Action Button Styling */
    .action-btn button {
        background-color: #FFFFFF !important;
        color: #0A0A0A !important;
        border: 1px solid #FFFFFF !important;
        font-weight: 700 !important;
    }
    .action-btn button:hover {
        background-color: #0A0A0A !important;
        color: #FFFFFF !important;
        border-color: #FFFFFF !important;
    }

    @keyframes fadeInUI {
        from { opacity: 0; transform: translateY(4px); }
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

# 3. Master Intelligence Matrix
data = {
    "ECB Smart Speaker": {
        "Paytm": {
            "points": [
                "Expose the hidden monthly device rentals via the Paytm Business App filter history.",
                "Highlight the current PhonePe special retention discount (₹99/₹199 setup fee).",
                "Contrast Paytm's frustrating online ticket/chatbot support with PhonePe's dedicated Area Sector Incharge.",
                "Zero online customer care dependency; direct call to the local executive for instant resolution."
            ],
            "pitch": "Bhaiya, ek minute dijiye, main aapko aapke Paytm Business app mein ek cheez dikhata hoon. Aap bol rahe ho na ki sirf ₹1 kat ta hai? Yeh dekho, app ke 'Soundbox History' aur 'Filters' mein jaakar—yeh <span class='highlight-amber'>har mahine ka hidden rental kat raha hai aapka</span>. PhonePe par humare purane merchants ke liye abhi ek special offer chal raha hai jismein setup fee par bhari discount hai (<span class='highlight-neon'>sirf ₹99/₹199 live stock ke hisab se</span>). Aur sabse badi baat—Paytm mein agar speaker kharab ho jaye, toh unke customer care par robot se chat karte-karte thak jaoge, koi sunne wala nahi hota. PhonePe par humara system bilkul alag hai. Humne aapke Kanpur ke isi market area mein ek <span class='highlight-cyan'>dedicated Sector Incharge</span> bitha rakha hai. Koi online ticket-vicket raising ka jhamela nahi hai. Ek call ghumao, humara ladka turant aapki dukaan par hazir hoga. Agar daily target hit kar lete ho, toh rental bhi zero aur service bhi top class!"
        },
        "BharatPe": {
            "points": [
                "Leverage the fact that 70% to 80% of local consumers natively use PhonePe.",
                "Explain how routing PhonePe users through a third-party QR delays settlements.",
                "Pitch the reliable on-ground network: Local Sector Incharges stationed in every specific market zone.",
                "Emphasize fast, direct human support over automated, slow online complaint portals."
            ],
            "pitch": "Bhaiya, aap khud dekho, aapke dukaan par jitne bhi log aate hain, unmein se <span class='highlight-neon'>70% se 80% log PhonePe use karte hain</span>. Jab consumer hi PhonePe ka hai, toh aap BharatPe ke QR par ghumakar settlement kyun delay kar rahe ho? Seedha PhonePe ka Smart Speaker lagao. Customers ke liye bhi frictionless payment hoga aur isi transaction volume ke basis par aapka loan offer bhi raat-o-raat active ho jayega. Rahi baat service ki—toh BharatPe ka na toh koi on-ground aadmi milta hai aur na hi unka support system local hai. Humara <span class='highlight-cyan'>Sector Incharge har waqt isi market mein rehta hai</span>. Kal ko network ka ya payment ka koi bhi issue aaye, aapko kisi app par jaakar shikayat nahi darj karni. Aapke paas humare local team ka number hoga, direct phone milao aur on-the-spot tension saaf!"
        },
        "Google Pay": {
            "points": [
                "Position the speaker as a gateway to the merchant ecosystem, not just an audio box.",
                "Explain how device deployment positions the merchant into top-priority early approval lending brackets.",
                "Frame GPay as a distant tech platform with zero local human service architecture.",
                "Highlight PhonePe's hyper-local team backup ensuring 100% counter uptime."
            ],
            "pitch": "Bhaiya, Google Pay ka speaker sirf ek audio box hai, usse aapke business ko koi fayda nahi mil raha. PhonePe ka Smart Speaker lagane ka matlab hai ki aapka business humare system mein top priority par aa jata hai. Iske lagte hi aapka business loan <span class='highlight-neon'>early approval brackets mein active ho jata hai</span>, aur aane wale time mein jo shop insurance aur retail health benefits hum de rahe hain, uski facilities bhi sabse pehle aapko milengi. Aur sabse matted baat bataun? Google Pay ka koi local office ya on-ground team nahi hai Kanpur mein. Kuch dikkat aayi toh mail likhte reh jaoge. PhonePe ka hamara <span class='highlight-cyan'>local Sector Incharge hamesha aapke area mein round par rehta hai</span>. Humara maqsad hai ki aapka counter kabhi band na ho. Bina kisi online ticketing ke, hand-to-hand aur reliable service sirf PhonePe par milti hai."
        },
        "Banks": {
            "points": [
                "Expose that bank QRs clutter the main bank ledger with individual micro-transactions, making it tedious to track and verify daily business in the ledger.",
                "Highlight PhonePe’s unified end-of-day (EOD) single settlement that makes daily tracking effortless.",
                "Contrast slow, institutional bank compliance with PhonePe's 1-2 hour physical device replacement guarantee.",
                "Eliminate bank manager visits with direct Sector Incharge direct-line access."
            ],
            "pitch": "Bhaiya, bank wale QR mein sabse bada jhamela yeh hai ki unke yahan har ek chota-mota transaction seedha aapke bank account mein jaakar girta hai. Ab din bhar mein 100 transaction huye toh aapki passbook aur bank ledger mein 100 entries bhar jayengi, jisse har ek transaction ko verify karna aur track rakhna bohot tedious aur mushkil ho jata hai. <span class='highlight-amber'>PhonePe par aisa kachra nahi hota!</span> Hum din bhar ka poora collection ek sath, <span class='highlight-neon'>single settlement mein aapke bank mein bhejte hain</span>, jisse har din ka dhandha track karna bilkul aasan ho jata hai. Aur agar aapko kisi ek transaction ki in-depth detail chahiye, toh aap PhonePe Business app mein dekh sakte hain. Sabse badi baat—bank ka speaker kharab hua toh aap apni chalti dukaan chhod kar manager ke samne application lekar khade hoge kya? Bank ka support system bohot dheema hai. Humare yahan har area ke liye alag Sector Incharge assigned hai. Machine mein 1% dikkat aayi, direct call karo, ladka <span class='highlight-cyan'>1 se 2 ghante ke andar dukaan par aakar physically speaker badal kar dega</span>. Hum dhandha rukne nahi dete!"
        }
    },
    "Merchant Lending": {
        "Paytm": {
            "points": [
                "Expose Paytm’s true Annual Percentage Rate (APR) of 36%–37% hidden under processing fees and GST.",
                "Pitch PhonePe’s clear, low monthly entry-level interest rates of 1.25%–1.5%.",
                "Highlight the security of having an active on-ground Sector Incharge to assist with any payment queries during the loan tenure.",
                "Avoid cold automated fintech systems with localized human relationship managers."
            ],
            "pitch": "Bhaiya, agar aapne Paytm se loan lene ka socha hai ya liya hai, toh unka ek baar interest certificate nikal kar dekhiye. Woh upar se bolte hain 2% mahina, par hidden charges, processing fees aur GST milakar <span class='highlight-amber'>saal ka 36% se 37% tak baithta hai</span>. Aap loot rahe ho wahan! Ek baar PhonePe ka loan banner check kariye, hum aapko pehli dafa mein hi <span class='highlight-neon'>1.25% se 1.5% ke clear interest rate par loan de rahe hain</span>. Koi hidden jhamela nahi hai. Aur sabse badhiya baat, Paytm par loan lene ke baad agar collection ya deduction ka koi confusion ho, toh aap chatbot se sarr marte reh jaoge. PhonePe par aapka bhai, humara <span class='highlight-cyan'>local Sector Incharge hamesha aapke sath khada hai</span>. Kuch bhi baat ho, direct usko phone lagao, woh aakar table par baith kar aapka hisab clear karega. Jan local support ka bharosa ho, toh dhandha fikar-mukt chalta hai."
        },
        "BharatPe": {
            "points": [
                "Pitch PhonePe's 'Continuous Eligibility' model allowing active Top-Ups without full closure.",
                "Guarantee new repeat loan banners within 1 week of closing a current loan block.",
                "Position the local Sector Incharge as an advocate who monitors your QR health to unlock bigger limits.",
                "Emphasize that reliable, human ground-support is unmatched by corporate apps."
            ],
            "pitch": "Bhaiya, BharatPe loan deta hai, thik hai. Par PhonePe aapko <span class='highlight-neon'>'Continuous Eligibility'</span> deta hai. Iska matlab yeh hai ki agar aapka loan chal raha hai aur aapko beech mein paise ki zaroorat padi, toh aapko live Top-Up ka option mil jata hai. Aur jaise hi aap purana loan close karte ho, within 1 week aapko naya repeat loan ka banner mil jata hai. Itna hi nahi, jag aap humare sath 3-4 loan cycle poori kar lete ho, toh aapki processing fee bhi bilkul zero ho jaati hai. Sabse bada fayda pata hai kya hai? BharatPe mein sab kuch digital machine par chalta hai, unka koi local chehra nahi hai aapse baat karne ke liye. PhonePe par humara <span class='highlight-cyan'>Sector Incharge aapke touch mein rehta hai</span>. Woh aapke QR ka health aur volume track karke system se aapki limit badhwane mein khud madad karta hai. Yeh machine ka nahi, bharose aur asli insani service ka rishta hai."
        },
        "Google Pay": {
            "points": [
                "Highlight 100% collateral-free, paperless lending backed purely by QR volume.",
                "Explain the streamlined architecture engineered for lightning fast early approval processing pipelines.",
                "Contrast GPay's complicated third-party NBFC approvals with PhonePe's direct account capital routing.",
                "Emphasize that the local Sector Incharge can expedite and verify any glitch on the spot."
            ],
            "pitch": "Bhaiya, market mein kahin bhi loan lene jaoge toh itne documents maangenge ki aap pareshan ho jaoge. PhonePe par agar aapka loan offer aaya hai, toh aapko koi collateral ya paperwork nahi chahiye. Sirf basic Aadhaar aur PAN card verify karna hai screen par, aur backend system setup ki wajah se <span class='highlight-neon'>early approval milte hi paisa seedha aapke linked bank account mein credit!</span> Google Pay par teesri party ka jhamela rehta hai, unka customer care kabhi phone nahi uthata. Humare yahan agar aapka loan process hote waqt koi technical glitch aa bhi gaya, toh aapko pareshan nahi hona hai. Aap seedha humare <span class='highlight-cyan'>area ke Sector Incharge ko batayiye</span>, woh piche system par baat karke aapka temporary block turant clear karwayega. Fast capital ke sath fast aur reliable ground service sirf humare paas hai."
        },
        "Banks": {
            "points": [
                "Detail how bank QRs clutter the main bank ledger with individual micro-transactions, creating thousands of entries that ruin credit assessments.",
                "Explain PhonePe's single daily settlement architecture that keeps bank statements clean and premium for future big loans.",
                "Highlight that local financiers attack a merchant's local reputation if collections dip.",
                "Position the PhonePe automated EOD tracking and local Sector Incharge backing as a total peace-of-mind shield."
            ],
            "pitch": "Bhaiya, bank se loan lene par ya bank ka QR chalane par sabse badi dikkat yeh hai ki har ek transaction seedha aapke bank account mein credit hota hai. Isse mahine mein hazaron entries ho jaati hain aur bank ledger itna tedious jata hai ki ek-ek entry ko verify karna aur hisab rakhna sir-dard ban jata hai. Jab bank ka bada manager aapki passbook mein yeh kachra dekhega na, toh badi loan file reject kar dega. PhonePe par kya hota hai—din bhar ka jitna bhi collection hai, woh raat ko <span class='highlight-neon'>sirf ek single unified settlement entry ke roop mein bank mein jata hai</span>. Mahine mein sirf 30 entries! Aapka bank statement bilkul premium aur clean rahega. Aur doosra bada khatra—market ke local financiers se james aap paisa uthate ho, toh mandi aane par woh dukaan par aakar khade ho jaate hain. <span class='highlight-amber'>Kanpur market mein dhandhe se badi apni izzat hoti hai—baat seedhe izzat par aa jaati hai!</span> PhonePe par aapka loan chalega toh digital automatic settlement se chalega. Koi aapke counter par aakar tamasha nahi karega. Aur kisi bhi tarah ke manual verification ya madad ke liye humara <span class='highlight-cyan'>area Sector Incharge hamesha available hai</span>. Na manager ke chakkar katna, na online ticket raise karna, bilkul izzat aur shanti se apna dhandha bada karo!"
        }
    }
}

# 4. Tracker Navigation Display
p1_class = "cred-nav-active" if st.session_state.page == 1 else ""
p2_class = "cred-nav-active" if st.session_state.page == 2 else ""
p3_class = "cred-nav-active" if st.session_state.page == 3 else ""

st.markdown(f"""
    <div class='cred-nav-container'>
        <div class='cred-nav-item {p1_class}'>01 // OBJECTIVE</div>
        <div class='cred-nav-item {p2_class}'>02 // COMPETITION</div>
        <div class='cred-nav-item {p3_class}'>03 // INTELLIGENCE</div>
    </div>
""", unsafe_allow_html=True)


# ==========================================
# PAGE 1: OBJECTIVE CONFIGURATION
# ==========================================
if st.session_state.page == 1:
    st.markdown("<h2 style='font-size:22px; font-weight:200; letter-spacing:1px; color:#FFF; margin-bottom:30px; text-transform:uppercase;'>Select Objective Matrix</h2>", unsafe_allow_html=True)
    
    st.markdown("<div class='cred-card'>", unsafe_allow_html=True)
    if st.button("🔊 Smart Speaker Deployment", key="btn_speaker"):
        st.session_state.task_type = "ECB Smart Speaker"
        go_to_page(2)
    st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='cred-card'>", unsafe_allow_html=True)
    if st.button("💼 Merchant Lending Scale-Up", key="btn_lending"):
        st.session_state.task_type = "Merchant Lending"
        go_to_page(2)
    st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# PAGE 2: TARGET OUTLET IDENTIFICATION
# ==========================================
elif st.session_state.page == 2:
    st.markdown(f"<p style='color:#8E8E93; font-size:11px; letter-spacing:1px; text-transform:uppercase;'>Objective // {st.session_state.task_type}</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size:22px; font-weight:200; letter-spacing:1px; color:#FFF; margin-bottom:30px; text-transform:uppercase;'>Identify Counter Competition</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='cred-card'>", unsafe_allow_html=True)
        if st.button("Paytm Counter", key="comp_paytm"):
            st.session_state.competitor = "Paytm"
            go_to_page(3)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='cred-card'>", unsafe_allow_html=True)
        if st.button("Google Pay Counter", key="comp_gpay"):
            st.session_state.competitor = "Google Pay"
            go_to_page(3)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div class='cred-card'>", unsafe_allow_html=True)
        if st.button("BharatPe Counter", key="comp_bharatpe"):
            st.session_state.competitor = "BharatPe"
            go_to_page(3)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='cred-card'>", unsafe_allow_html=True)
        if st.button("Traditional Bank QR", key="comp_banks"):
            st.session_state.competitor = "Banks"
            go_to_page(3)
        st.markdown("</div>", unsafe_allow_html=True)
        
    st.write("<br>", unsafe_allow_html=True)
    if st.button("← Return to Objectives", key="back_p2"):
        go_to_page(1)


# ==========================================
# PAGE 3: HIGH INTENSITY INTELLIGENCE REPORT
# ==========================================
elif st.session_state.page == 3:
    st.markdown(f"<p style='color:#8E8E93; font-size:11px; letter-spacing:1px; text-transform:uppercase;'>{st.session_state.task_type} // {st.session_state.competitor.upper()}</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size:22px; font-weight:200; letter-spacing:1px; color:#FFF; margin-bottom:20px; text-transform:uppercase;'>Field Deployment Strategy</h2>", unsafe_allow_html=True)
    
    selected_node = data[st.session_state.task_type][st.session_state.competitor]
    
    st.markdown("<p style='color:#8E8E93; font-weight:600; font-size:11px; letter-spacing:1px; text-transform:uppercase; margin-bottom:10px;'>Strategic Counter Points</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='cred-card'>", unsafe_allow_html=True)
    for bullet in selected_node['points']:
        st.markdown(f"<div style='padding: 6px 0; font-size:14px; color:#E5E5EA;'>• {bullet}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
        
    st.write("<br>", unsafe_allow_html=True)
    
    if not st.session_state.pitch_generated:
        st.markdown("<div class='action-btn'>", unsafe_allow_html=True)
        if st.button("Generate Customised Pitch", key="gen_pitch_btn"):
            st.session_state.pitch_generated = True
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:#8E8E93; font-weight:600; font-size:11px; letter-spacing:1px; text-transform:uppercase; margin-bottom:0;'>Spoken Hinglish Script</p>", unsafe_allow_html=True)
        st.markdown(f"<div class='pitch-box'>{selected_node['pitch']}</div>", unsafe_allow_html=True)
        
        st.write("<br>", unsafe_allow_html=True)
        st.markdown("<p style='color:#8E8E93; font-size:11px; font-weight:600; letter-spacing:1px; text-transform:uppercase;'>Select Coaching Audio Track</p>", unsafe_allow_html=True)
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

    st.write("<br><br>", unsafe_allow_html=True)
    if st.button("← Initialize New Audit", key="restart_btn"):
        go_to_page(1)


# ==========================================
# FIXED MINIMALIST METRIC TICKER (CRED STYLE)
# ==========================================
st.markdown("""
    <div class='market-share-ticker'>
        <span class='ticker-item'>Kanpur Share Matrix</span>
        <span class='ticker-item'>PhonePe <span class='ticker-value' style='color:#30D158;'>38.2%</span></span>
        <span class='ticker-item'>Paytm <span class='ticker-value' style='color:#FF453A;'>37.1%</span></span>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)
