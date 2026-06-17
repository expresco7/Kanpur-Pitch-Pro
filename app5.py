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
# PHONEPE PREMIUM GRADIENT SPLASH TRANSITION
# ==========================================
if not st.session_state.animation_played:
    st.markdown("""
        <style>
        .stApp { background: linear-gradient(135deg, #5f259f 0%, #4d1c84 100%) !important; }
        header {visibility: hidden;}
        footer {visibility: hidden;}
        
        .splash-container {
            position: fixed;
            top: 0; left: 0; width: 100vw; height: 100vh;
            background: linear-gradient(135deg, #5f259f 0%, #4d1c84 100%);
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 99999;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        }
        
        .pp-logo-circle {
            width: 80px;
            height: 80px;
            background: #FFFFFF;
            border-radius: 24px;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 42px;
            margin-bottom: 20px;
            box-shadow: 0 20px 40px rgba(0,0,0,0.3);
            opacity: 0;
            animation: popIn 0.8s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
        }
        
        .cred-logo-text {
            font-size: 28px;
            font-weight: 800;
            letter-spacing: 1px;
            color: #FFFFFF;
            opacity: 0;
            animation: fadeInUp 1s cubic-bezier(0.25, 1, 0.5, 1) 0.4s forwards;
        }
        
        .cred-sub-text {
            font-size: 12px;
            font-weight: 500;
            letter-spacing: 3px;
            color: #d1bbf2;
            text-transform: uppercase;
            margin-top: 10px;
            opacity: 0;
            animation: fadeIn 1s ease 0.8s forwards;
        }

        @keyframes popIn {
            0% { opacity: 0; transform: scale(0.6) rotate(-15deg); }
            100% { opacity: 1; transform: scale(1) rotate(0deg); }
        }
        @keyframes fadeInUp {
            0% { opacity: 0; transform: translateY(20px); filter: blur(5px); }
            100% { opacity: 1; transform: translateY(0); filter: blur(0px); }
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 0.8; }
        }
        </style>
        
        <div class="splash-container">
            <div class="pp-logo-circle">🔮</div>
            <div class="cred-logo-text">Kanpur Pitch Pro</div>
            <div class="cred-sub-text">PhonePe Elite Intelligence</div>
        </div>
    """, unsafe_allow_html=True)
    
    time.sleep(2.5)
    st.session_state.animation_played = True
    st.rerun()


# ==========================================
# VIBRANT PHONEPE CLASSY LIGHT UI STYLING
# ==========================================
st.markdown("""
    <style>
    /* Premium PhonePe Colorway Overrides */
    .stApp {
        background-color: #F5F7FB !important;
        color: #2D2D3A !important;
    }
    
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    h1, h2, h3, h4, p, label, div {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", sans-serif !important;
    }
    
    /* Segment Tracker Header (PhonePe Style Navigation) */
    .cred-nav-container {
        display: flex;
        justify-content: space-between;
        background-color: #FFFFFF;
        padding: 4px;
        border-radius: 16px;
        border: 1px solid #E2E8F0;
        box-shadow: 0 4px 12px rgba(95, 37, 159, 0.03);
        margin-bottom: 25px;
    }
    .cred-nav-item {
        flex: 1;
        text-align: center;
        padding: 12px 0;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1px;
        color: #A0AEC0;
        text-transform: uppercase;
        transition: all 0.3s ease;
    }
    .cred-nav-active {
        color: #5f259f !important;
        background-color: #F1EDFA;
        border-radius: 12px;
    }
    
    /* Vibrant Colorful Container Blocks */
    .cred-card {
        background: #FFFFFF;
        border: 1px solid #E6EFFC;
        padding: 24px;
        border-radius: 18px;
        margin-bottom: 20px;
        box-shadow: 0 6px 16px rgba(95, 37, 159, 0.04);
        transition: transform 0.2s cubic-bezier(0.2, 0, 0, 1);
    }
    
    .pitch-box {
        background-color: #F8F5FE;
        border-left: 5px solid #5f259f;
        padding: 24px;
        border-radius: 0 16px 16px 0;
        color: #3B3B4F;
        font-size: 15.5px;
        line-height: 1.7;
        margin-top: 20px;
        box-shadow: inset 0 2px 4px rgba(95, 37, 159, 0.02);
    }
    
    /* Dynamic Metric Highlighters */
    .highlight-amber {
        color: #D97706 !important;
        background-color: #FEF3C7;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: 700 !important;
    }
    .highlight-neon {
        color: #15803D !important;
        background-color: #DCFCE7;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: 700 !important;
    }
    .highlight-cyan {
        color: #1D4ED8 !important;
        background-color: #DBEAFE;
        padding: 2px 6px;
        border-radius: 4px;
        font-weight: 700 !important;
    }
    
    /* Fixed Dynamic Bottom Dashboard Ticker */
    .market-share-ticker {
        background-color: #FFFFFF;
        border-top: 1px solid #E2E8F0;
        padding: 16px 20px;
        position: fixed;
        bottom: 0; left: 0; right: 0; width: 100%;
        display: flex;
        justify-content: space-around;
        align-items: center;
        z-index: 999;
        box-shadow: 0 -10px 25px rgba(0,0,0,0.03);
    }
    .ticker-item {
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 0.8px;
        color: #718096;
        text-transform: uppercase;
    }
    .ticker-value {
        font-weight: 800;
        margin-left: 6px;
    }
    
    /* Tactile Premium Button Layouts */
    div.stButton > button {
        background: linear-gradient(135deg, #FFFFFF 0%, #F9FAFB 100%) !important;
        color: #4A5568 !important;
        border: 1px solid #E2E8F0 !important;
        padding: 16px 20px !important;
        border-radius: 14px !important;
        width: 100% !important;
        font-size: 14px !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
        box-shadow: 0 4px 6px rgba(0,0,0,0.02) !important;
        transition: all 0.25s ease !important;
    }
    div.stButton > button:hover {
        border-color: #5f259f !important;
        color: #5f259f !important;
        background: #F1EDFA !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px rgba(95, 37, 159, 0.1) !important;
    }
    
    /* Colorful Primary Action Trigger Styling */
    .action-btn button {
        background: linear-gradient(135deg, #5f259f 0%, #7b3fd3 100%) !important;
        color: #FFFFFF !important;
        border: none !important;
        box-shadow: 0 8px 16px rgba(95, 37, 159, 0.2) !important;
    }
    .action-btn button:hover {
        background: linear-gradient(135deg, #4d1c84 0%, #5f259f 100%) !important;
        color: #FFFFFF !important;
        transform: translateY(-2px);
        box-shadow: 0 12px 20px rgba(95, 37, 159, 0.3) !important;
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
                "Detail how bank QRs clutter the main bank ledger with individual micro-transactions, creating thousands of entries that ruin credit assessments.",
                "Explain PhonePe's single daily settlement architecture that keeps bank statements clean and premium for future big loans.",
                "Highlight that local financiers attack a merchant's local reputation if collections dip.",
                "Position the PhonePe automated EOD tracking and local Sector Incharge backing as a total peace-of-mind shield."
            ],
            "pitch": "Bhaiya, bank wale QR mein sabse bada jhamela yeh hai ki unke yahan har ek chota-mota transaction seedha aapke bank account mein jaakar girta hai. Ab din bhar mein 100 transaction huye toh aapki passbook aur bank ledger mein 100 entries bhar jayengi, jisse har ek transaction ko verify karna aur track rakhna bohot tedious aur mushkil ho jata hai. <span class='highlight-amber'>PhonePe par aisa kachra nahi hota!</span> Hum din bhar ka poora collection ek sath, <span class='highlight-neon'>single settlement mein aapke bank mein bhejte hain</span>, jisse har din ka dhandha track karna bilkul aasan ho jata hai. Aur agar aapko kisi ek transaction ki in-depth detail chahiye, toh aap PhonePe Business app mein dekh sakte hain. Sabse badi baat—bank ka speaker kharab hua toh aap apni chalti dukaan chhod kar manager ke samne application lekar khade hoge kya? Bank ka support support system bohot dheema hai. Humare yahan har area ke liye alag Sector Incharge assigned hai. Machine mein 1% dikkat aayi, direct call karo, ladka <span class='highlight-cyan'>1 se 2 ghante ke andar dukaan par aakar physically speaker badal kar dega</span>. Hum dhandha rukne nahi dete!"
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
            "pitch": "Bhaiya, bank se loan lene par ya bank ka QR chalane par sabse badi dikkat yeh hai ki har ek transaction seedha aapke bank account mein credit hota hai. Isse mahine mein hazaron entries ho jaati hain aur bank ledger itna tedious jata hai ki ek-ek entry ko verify karna aur hisab rakhna sir-dard ban jata hai. Jab bank ka bada manager aapki passbook mein yeh kachra dekhega na, toh badi loan file reject kar dega. PhonePe par kya hota hai—din bhar ka jitna bhi collection hai, woh raat ko <span class='highlight-neon'>sirf ek single unified settlement entry ke roop mein bank mein jata hai</span>. Mahine mein sirf 30 entries! Aapka bank statement bilkul premium aur clean rahega. Aur doosra bada khatra—market ke local financiers se james aap paisa uthate ho, toh mandi aane par woh dukaan par aakar khade ho jaate hain. <span class='highlight-amber'>Kanpur market mein dhandhe se badi apni izzat hoti hai—baat seedhe izzat par aa jaati hai!</span> PhonePe par aapka loan chalega toh digital automatic settlement se chalega. Koi aapke counter par aakar tamasha nahi korea. Aur kisi bhi tarah ke manual verification ya madad ke liye humara <span class='highlight-cyan'>area Sector Incharge hamesha available hai</span>. Na manager ke chakkar katna, na online ticket raise karna, bilkul izzat aur shanti se apna dhandha bada karo!"
        }
    },
    "Objection Handling": {
        "Paytm": {
            "points": [
                "Merchant Claim: 'Paytm updates their machine features instantly without physical swaps.'",
                "PhonePe Counter Strategy: Point out hidden system latency issues and emphasize PhonePe's rapid local execution grid.",
                "Highlight that feature updates mean nothing if the speaker hardware itself glitches on the counter."
            ],
            "pitch": "Bhaiya, cloud update toh sab companies karti hain, par jab device physically speaker parde se jam jaye ya battery switch fail ho jaye, toh unka software update kaam nahi aayega. PhonePe ka hamara local Sector Incharge aapke market line mein har alternate din hota hai. Kuch bhi physical technicality ho, we resolve it within <span class='highlight-neon'>1 to 2 hours flat</span> on-site."
        },
        "BharatPe": {
            "points": [
                "Merchant Claim: 'BharatPe provides high limits instantly on screen.'",
                "PhonePe Counter Strategy: Challenge the post-disbursal hidden platform management processing parameters.",
                "Expose that on-screen vanity numbers include heavy backend document scrubbing."
            ],
            "pitch": "Bhaiya, screen par bada number dikhana bohot aasan hai, par actual balance bank account mein credit hote waqt BharatPe extra hidden platform fees aur processing charges debit kar leta hai. PhonePe jo banner dikhata hai, <span class='highlight-neon'>wahi net clean amount bina kisi extra service deduction ke transfer karta hai</span>."
        },
        "Google Pay": {
            "points": [
                "Merchant Claim: 'Google is a global platform, trusted system infrastructure.'",
                "PhonePe Counter Strategy: Attack the total missing layer of dedicated human verification frameworks.",
                "Position corporate detachment as a massive liability during billing anomalies."
            ],
            "pitch": "Google ka trust platform scale par sahi hai bhaiya, par Kanpur ke retail wholesale bazaar mein jab transaction fast tick par fans jata hai, toh California se koi executive verification ke liye nahi aayega. <span class='highlight-cyan'>Dhandhe mein local insani support zaroori hai</span>, jo sirf PhonePe ka Kanpur 1 squad maintain karta hai."
        },
        "Banks": {
            "points": [
                "Merchant Claim: 'I have a strong 10-year relation with my banking institution.'",
                "PhonePe Counter Strategy: Remind the client about rigorous security clearance margins.",
                "Explain that banks prioritize institutional collateral lines over localized micro-merchant assets."
            ],
            "pitch": "Relation apni jagah bilkul sahi hai bhaiya, par emergency mein jab capital requirement hoti hai, tab bank wahi purana documentation clearance aur passbook evaluation check karega. PhonePe humare active partner margins par <span class='highlight-neon'>purely automated fast evaluation system</span> se capital disburse karta hai."
        }
    },
    "Loan Errors": {
        "Paytm": {
            "points": [
                "Error Signature: High CIBIL Score drop alerts due to multi-NBFC hard inquiries.",
                "Root Diagnostics: Paytm distributes lead matrices across multiple backing financiers, hitting credit metrics hard.",
                "Resolution Framework: Guide the user to freeze unutilized fintech lines and shift cleanly to PhonePe's single ledger routing."
            ],
            "pitch": "Bhaiya, Paytm par click karne se unke multiple structural landing partners aapki profile check karte hain, jisse score drop ho jata hai. Iska clean solution hai ki aap unutilized application links clear kariye aur PhonePe par structured unified ledger pipeline execute kijiye, <span class='highlight-cyan'>jisse internal optimization scale boost hoga</span>."
        },
        "BharatPe": {
            "points": [
                "Error Signature: Auto-debit settlement locks and settlement adjustment traps.",
                "Root Diagnostics: Mismatched EOD transaction mapping parameters with internal ledger hooks.",
                "Resolution Framework: Initiate a fresh dynamic balance synchronization directly via the local Sector Incharge portal link."
            ],
            "pitch": "Bhaiya, settlement lock hone ka bada karan yeh hota hai ki collection matrix settle nahi ho pata backend par. Iska primary resolution humara assigned team mate link verification check bypass karke, <span class='highlight-neon'>within 24 hours platform data swap execution se force-clear karwa dega</span>."
        },
        "Google Pay": {
            "points": [
                "Error Signature: Application stuck on processing verification status loops.",
                "Root Diagnostics: Third-party NBFC integration data sync freeze during high volume trading.",
                "Resolution Framework: Wipe application cached data blocks, verify tracking hooks via identity data, and trigger dynamic early approval."
            ],
            "pitch": "Bhaiya, agar loop processing fast nahi chal raha, toh iska matlab link synchronization down ho gaya hai core level par. Google network automation par fail hota hai toh tick generate karna padta hai. Humare yahan <span class='highlight-cyan'>direct terminal validation system overrides run karke manual override processing activate kar sakte hain</span>."
        },
        "Banks": {
            "points": [
                "Error Signature: Ledger mismatch anomalies on banking passbook updates.",
                "Root Diagnostics: Thousands of micro-entries cluttering parsing loops during credit score evaluation cycles.",
                "Resolution Framework: Move immediately to PhonePe single end-of-day (EOD) routing matrices to preserve banking premium visibility status."
            ],
            "pitch": "Bhaiya, bank passbook mein processing errors ka main problem micro-entries ka data overflow hota hai. Iska direct solution humara <span class='highlight-neon'>unified single settlement matrix deployment hai</span>, jisse accounting entries clean rahengi aur auditing metrics standard benchmark scale match kar sakenge."
        }
    }
}

# 4. PhonePe Unified Segment Tracker Bar
p1_class = "cred-nav-active" if st.session_state.page == 1 else ""
p2_class = "cred-nav-active" if st.session_state.page == 2 else ""
p3_class = "cred-nav-active" if st.session_state.page == 3 else ""

st.markdown(f"""
    <div class='cred-nav-container'>
        <div class='cred-nav-item {p1_class}'>🔮 01 // OBJECTIVE</div>
        <div class='cred-nav-item {p2_class}'>⚔️ 02 // COMPETITION</div>
        <div class='cred-nav-item {p3_class}'>⚡ 03 // INTELLIGENCE</div>
    </div>
""", unsafe_allow_html=True)


# ==========================================
# PAGE 1: OBJECTIVE CONFIGURATION
# ==========================================
if st.session_state.page == 1:
    st.markdown("<h2 style='font-size:20px; font-weight:800; color:#5f259f; margin-bottom:25px; text-transform:uppercase;'>🎯 Select Target Operation</h2>", unsafe_allow_html=True)
    
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

    # NEW SPECIFIED MATRIX HEADERS
    st.markdown("<div class='cred-card'>", unsafe_allow_html=True)
    if st.button("🛡️ Objection Handling Matrix", key="btn_objection"):
        st.session_state.task_type = "Objection Handling"
        go_to_page(2)
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div class='cred-card'>", unsafe_allow_html=True)
    if st.button("🛠️ Loan Errors & Diagnostics", key="btn_errors"):
        st.session_state.task_type = "Loan Errors"
        go_to_page(2)
    st.markdown("</div>", unsafe_allow_html=True)


# ==========================================
# PAGE 2: TARGET OUTLET IDENTIFICATION
# ==========================================
elif st.session_state.page == 2:
    st.markdown(f"<p style='color:#5f259f; font-size:12px; font-weight:700; letter-spacing:1px; text-transform:uppercase;'>Active Target Matrix // {st.session_state.task_type}</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size:20px; font-weight:800; color:#2D2D3A; margin-bottom:25px; text-transform:uppercase;'>⚔️ Choose Competitor Counter</h2>", unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<div class='cred-card'>", unsafe_allow_html=True)
        if st.button("🔵 Paytm Counter", key="comp_paytm"):
            st.session_state.competitor = "Paytm"
            go_to_page(3)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='cred-card'>", unsafe_allow_html=True)
        if st.button("🟢 Google Pay", key="comp_gpay"):
            st.session_state.competitor = "Google Pay"
            go_to_page(3)
        st.markdown("</div>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div class='cred-card'>", unsafe_allow_html=True)
        if st.button("🟠 BharatPe Counter", key="comp_bharatpe"):
            st.session_state.competitor = "BharatPe"
            go_to_page(3)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='cred-card'>", unsafe_allow_html=True)
        if st.button("🏛️ Traditional Bank", key="comp_banks"):
            st.session_state.competitor = "Banks"
            go_to_page(3)
        st.markdown("</div>", unsafe_allow_html=True)
        
    st.write("<br>", unsafe_allow_html=True)
    if st.button("← Return to Master Hub", key="back_p2"):
        go_to_page(1)


# ==========================================
# PAGE 3: FIELD SQUAD INTELLIGENCE OUTPUT
# ==========================================
elif st.session_state.page == 3:
    st.markdown(f"<p style='color:#718096; font-size:12px; font-weight:700; letter-spacing:1px; text-transform:uppercase;'>{st.session_state.task_type} // {st.session_state.competitor.upper()}</p>", unsafe_allow_html=True)
    st.markdown("<h2 style='font-size:20px; font-weight:800; color:#5f259f; margin-bottom:20px; text-transform:uppercase;'>⚡ Strategic Execution Data</h2>", unsafe_allow_html=True)
    
    selected_node = data[st.session_state.task_type][st.session_state.competitor]
    
    st.markdown("<p style='color:#4A5568; font-weight:700; font-size:12px; letter-spacing:0.8px; text-transform:uppercase; margin-bottom:10px;'>📋 Operational Checklist / Diagnostic Points</p>", unsafe_allow_html=True)
    
    st.markdown("<div class='cred-card'>", unsafe_allow_html=True)
    for bullet in selected_node['points']:
        st.markdown(f"<div style='padding: 6px 0; font-size:14.5px; color:#2D2D3A; font-weight:500;'>• {bullet}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
        
    st.write("<br>", unsafe_allow_html=True)
    
    if not st.session_state.pitch_generated:
        st.markdown("<div class='action-btn'>", unsafe_allow_html=True)
        if st.button("⚡ Generate Customised Pitch", key="gen_pitch_btn"):
            st.session_state.pitch_generated = True
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.markdown("<p style='color:#4A5568; font-weight:700; font-size:12px; letter-spacing:0.8px; text-transform:uppercase; margin-bottom:0;'>🗣️ Active Spoken Hinglish Script</p>", unsafe_allow_html=True)
        st.markdown(f"<div class='pitch-box'>{selected_node['pitch']}</div>", unsafe_allow_html=True)
        
        st.write("<br>", unsafe_allow_html=True)
        st.markdown("<p style='color:#718096; font-size:12px; font-weight:700; letter-spacing:0.8px; text-transform:uppercase; margin-bottom:10px;'>🎵 Play Audio Briefing</p>", unsafe_allow_html=True)
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

    st.write("<br><br>", unsafe_allow_html=True)
    if st.button("← Initialize New Field Session", key="restart_btn"):
        go_to_page(1)


# ==========================================
# FIXED PREMIUM DYNAMIC BOTTOM MATRIX TICKER
# ==========================================
st.markdown("""
    <div class='market-share-ticker'>
        <span class='ticker-item'>📍 KANPUR METRICS</span>
        <span class='ticker-item'>🔮 PhonePe: <span class='ticker-value' style='color:#5f259f;'>38.2%</span></span>
        <span class='ticker-item'>🔵 Paytm: <span class='ticker-value' style='color:#00BAF2;'>37.1%</span></span>
    </div>
""", unsafe_allow_html=True)

st.markdown("<br><br><br>", unsafe_allow_html=True)
