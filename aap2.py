import streamlit as st

# Set page configuration for mobile responsiveness
st.set_page_config(
    page_title="Team Kanpur 1 - Pitch Book",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom Styling to give it a premium PhonePe Purple UI vibe
st.markdown("""
    <style>
    .main { background-color: #f5f7fb; }
    .stSelectbox label { font-size: 16px !important; font-weight: bold !important; color: #5f259f !important; }
    .pitch-card {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 12px;
        border-left: 6px solid #5f259f;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    .points-card {
        background-color: #fffbeb;
        padding: 15px;
        border-radius: 10px;
        border-left: 6px solid #d97706;
        margin-bottom: 15px;
    }
    .header-text { color: #5f259f; text-align: center; font-weight: 800; }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown("<h1 class='header-text'>⚡ Team Kanpur 1 Pitch Book</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #666;'>Kyunki baat Izzat ki hai! Instant Field Guides & Audio Tracks</p>", unsafe_allow_html=True)
st.write("---")

# Navigation/Filters
task_type = st.selectbox("🎯 Select Task Type", ["ECB Smart Speaker", "Merchant Lending"])
competitor = st.selectbox("⚔️ Select Competitor on Counter", ["Paytm", "BharatPe", "Google Pay", "Banks"])

# Master Database Matrix
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
            "pitch": "Bhaiya, ek minute dijiye, main aapko aapke Paytm Business app mein ek cheez dikhata hoon. Aap bol rahe ho na ki sirf ₹1 kat ta hai? Yeh dekho, app ke 'Soundbox History' aur 'Filters' mein jaakar—yeh har mahine ka hidden rental kat raha hai aapka. PhonePe par humare purane merchants ke liye abhi ek special offer chal raha hai jismein setup fee par bhari discount hai (sirf ₹318/₹349 live stock ke hisab se). Aur sabse badi baat—Paytm mein agar speaker kharab ho jaye, toh unke customer care par robot se chat karte-karte thak jaoge, koi sunne wala nahi hota. PhonePe par humara system bilkul alag hai. Humne aapke Kanpur ke isi market area mein ek dedicated Sector Incharge bitha rakha hai. Koi online ticket-vicket raising ka jhamela nahi hai. Ek call ghumao, humara ladka turant aapki dukaan par hazir hoga. Agar daily target hit kar lete ho, toh rental bhi zero aur service bhi top class!",
            "audio": ""
        },
        "BharatPe": {
            "hook": "Market Volume & Hyper-Local Support",
            "points": [
                "Leverage the fact that 70% to 80% of local consumers natively use PhonePe.",
                "Explain how routing PhonePe users through a third-party QR delays settlements.",
                "Pitch the reliable on-ground network: Local Sector Incharges stationed in every specific market zone.",
                "Emphasize fast, direct human support over automated, slow online complaint portals."
            ],
            "pitch": "Bhaiya, aap khud dekho, aapke dukaan par jitne bhi log aate hain, unmein se 70% se 80% log PhonePe use karte hain. Jab consumer hi PhonePe ka hai, toh aap BharatPe ke QR par ghumakar settlement kyun delay kar rahe ho? Seedha PhonePe ka Smart Speaker lagao. Customers ke liye bhi frictionless payment hoga aur isi transaction volume ke basis par aapka loan offer bhi raat-o-raat active ho jayega. Rahi baat service ki—toh BharatPe ka na toh koi on-ground aadmi milta hai aur na hi unka support system local hai. Humara Sector Incharge har waqt isi market mein rehta hai. Kal ko network ka ya payment ka koi bhi issue aaye, aapko kisi app par jaakar shikayat nahi darj karni. Aapke paas humare local team ka number hoga, direct phone milao aur on-the-spot tension saaf!",
            "audio": ""
        },
        "Google Pay": {
            "hook": "Ecosystem Priority & Speed",
            "points": [
                "Position the speaker as a gateway to the merchant ecosystem, not just an audio box.",
                "Explain how device deployment pushes the merchant into top-priority lending brackets.",
                "Frame GPay as a distant tech platform with zero local human service architecture.",
                "Highlight PhonePe's hyper-local team backup ensuring 100% counter uptime."
            ],
            "pitch": "Bhaiya, Google Pay ka speaker sirf ek audio box hai, usse aapke business ko koi fayda nahi mil raha. PhonePe ka Smart Speaker lagane ka matlab hai ki aapka business humare system mein top priority par aa jata hai. Iske lagte hi aapka business loan pre-approve ho jata hai, aur aane wale time mein jo shop insurance aur retail health benefits hum de rahe hain, uski facilities bhi sabse pehle aapko milengi. Aur sabse matted baat bataun? Google Pay ka koi local office ya on-ground team nahi hai Kanpur mein. Kuch dikkat aayi toh mail likhte reh jaoge. PhonePe ka hamara local Sector Incharge hamesha aapke area mein round par rehta hai. Humara maqsad hai ki aapka counter kabhi band na ho. Bina kisi online ticketing ke, hand-to-hand aur reliable service sirf PhonePe par milti hai.",
            "audio": ""
        },
        "Banks": {
            "hook": "Single Settlement & 2-Hour Swap",
            "points": [
                "Expose that bank QRs dump every single transaction directly into the bank account, making it tedious to track and verify daily business in the ledger.",
                "Highlight PhonePe’s unified end-of-day (EOD) single settlement that makes daily tracking effortless.",
                "Contrast slow, institutional bank compliance with PhonePe's 1-2 hour physical device replacement guarantee.",
                "Eliminate bank manager visits with direct Sector Incharge direct-line access."
            ],
            "pitch": "Bhaiya, bank wale QR mein sabse bada jhamela yeh hai ki unke yahan har ek chota-mota transaction seedha aapke bank account mein jaakar girta hai. Ab din bhar mein 100 transaction huye toh aapki passbook aur bank ledger mein 100 entries bhar jayengi, jisse har ek transaction ko verify karna aur track rakhna bohot tedious aur mushkil ho jata hai. PhonePe par aisa kachra nahi hota! Hum din bhar ka poora collection ek sath, single settlement mein aapke bank mein bhejte hain, jisse har din ka dhandha track karna bilkul aasan ho jata hai. Aur agar aapko kisi ek transaction ki in-depth detail chahiye, toh aap PhonePe Business app mein dekh sakte hain. Sabse badi baat—bank ka speaker kharab hua toh aap apni chalti dukaan chhod kar manager ke samne application lekar khade hoge kya? Bank ka support system bohot dheema hai. Humare yahan har area ke liye alag Sector Incharge assigned hai. Machine mein 1% dikkat aayi, direct call karo, ladka 1 se 2 ghante ke andar dukaan par aakar physically speaker badal kar dega. Hum dhandha rukne nahi dete!",
            "audio": ""
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
            "pitch": "Bhaiya, agar aapne Paytm se loan lene ka socha hai ya liya hai, toh unka ek baar interest certificate nikal kar dekhiye. Woh upar se bolte hain 2% mahina, par hidden charges, processing fees aur GST milakar saal ka 36% se 37% tak baithta hai. Aap loot rahe ho wahan! Ek baar PhonePe ka loan banner check kariye, hum aapko pehli dafa mein hi 1.25% se 1.5% ke clear interest rate par loan de rahe hain. Koi hidden jhamela nahi hai. Aur sabse badhiya baat, Paytm par loan lene ke baad agar collection ya deduction ka koi confusion ho, toh aap chatbot se sarr marte reh jaoge. PhonePe par aapka bhai, humara local Sector Incharge hamesha aapke sath khada hai. Kuch bhi baat ho, direct usko phone lagao, woh aakar table par baith kar aapka hisab clear karega. Jan local support ka bharosa ho, toh dhandha fikar-mukt chalta hai.",
            "audio": ""
        },
        "BharatPe": {
            "hook": "Continuity, Top-Up & Relationship Trust",
            "points": [
                "Pitch PhonePe's 'Continuous Eligibility' model allowing active Top-Ups without full closure.",
                "Guarantee new repeat loan banners within 1 week of closing a current loan block.",
                "Position the local Sector Incharge as an advocate who monitors your QR health to unlock bigger limits.",
                "Emphasize that reliable, human ground-support is unmatched by corporate apps."
            ],
            "pitch": "Bhaiya, BharatPe loan deta hai, thik hai. Par PhonePe aapko 'Continuous Eligibility' deta hai. Iska matlab yeh hai ki agar aapka loan chal raha hai aur aapko beech mein paise ki zaroorat padi, toh aapko live Top-Up ka option mil jata hai. Aur jaise hi aap purana loan close karte ho, within 1 week aapko naya repeat loan ka banner mil jata hai. Itna hi nahi, jag aap humare sath 3-4 loan cycle poori kar lete ho, toh aapki processing fee bhi bilkul zero ho jaati hai. Sabse bada fayda pata hai kya hai? BharatPe mein sab kuch digital machine par chalta hai, unka koi local chehra nahi hai aapse baat karne ke liye. PhonePe par humara Sector Incharge aapke touch mein rehta hai. Woh aapke QR ka health aur volume track karke system se aapki limit badhwane mein khud madad karta hai. Yeh machine ka nahi, bharose aur asli insani service ka rishta hai.",
            "audio": ""
        },
        "Google Pay": {
            "hook": "Document-Free Capital & Speed Verification",
            "points": [
                "Highlight 100% collateral-free, paperless lending backed purely by QR volume.",
                "Explain the lightning-fast 24 to 48-hour direct bank account capital disbursal.",
                "Contrast GPay's complicated third-party NBFC approvals with PhonePe's streamlined processing.",
                "Emphasize that the local Sector Incharge can expedite and verify any glitch on the spot."
            ],
            "pitch": "Bhaiya, market mein kahin bhi loan lene jaoge toh itne documents maangenge ki aap pareshan ho jaoge. PhonePe par agar aapka loan offer aaya hai, toh aapko koi collateral ya paperwork nahi chahiye. Sirf basic Aadhaar aur PAN card verify karna hai screen par, aur 24 se 48 ghante ke andar paisa seedha aapke linked bank account mein credit! Google Pay par teesri party ka jhamela rehta hai, unka customer care kabhi phone nahi uthata. Humare yahan agar aapka loan process hote waqt koi technical glitch aa bhi gaya, toh aapko pareshan nahi hona hai. Aap seedha humare area ke Sector Incharge ko batayiye, woh piche system par baat karke aapka temporary block turant clear karwayega. Fast capital ke sath fast aur reliable ground service sirf humare paas hai.",
            "audio": ""
        },
        "Banks": {
            "hook": "Passbook Cleaning & The 'Izzat' Factor",
            "points": [
                "Detail how bank QRs clutter the main bank ledger with individual micro-transactions, creating thousands of tedious entries that ruin credit assessments.",
                "Explain PhonePe's single daily settlement architecture that keeps bank statements clean and premium for future big loans.",
                "Highlight that local financiers attack a merchant's local reputation if collections dip.",
                "Position the PhonePe automated EOD tracking and local Sector Incharge backing as a total peace-of-mind shield."
            ],
            "pitch": "Bhaiya, bank se loan lene par ya bank ka QR chalane par sabse badi dikkat yeh hai ki har ek transaction seedha aapke bank account mein credit hota hai. Isse mahine mein hazaron entries ho jaati hain aur bank ledger itna tedious jata hai ki ek-ek entry ko verify karna aur hisab rakhna sir-dard ban jata hai. Jab bank ka bada manager aapki passbook mein yeh kachra dekhega na, toh badi loan file reject kar dega. PhonePe par kya hota hai—din bhar ka jitna bhi collection hai, woh raat ko sirf ek single unified settlement entry ke roop mein bank mein jata hai. Mahine mein sirf 30 entries! Aapka bank statement bilkul premium aur clean rahega. Aur doosra bada khatra—market ke local financiers se james aap paisa uthate ho, toh mandi aane par woh dukaan par aakar khade ho jaate hain. Kanpur market mein dhandhe se badi apni izzat hoti hai—baat seedhe izzat par aa jaati hai! PhonePe par aapka loan chalega toh digital automatic settlement se chalega. Koi aapke counter par aakar tamasha nahi karega. Aur kisi bhi tarah ke manual verification ya madad ke liye humara area Sector Incharge hamesha available hai. Na manager ke chakkar katna, na online ticket raise karna, bilkul izzat aur shanti se apna dhandha bada karo!",
            "audio": ""
        }
    }
}

# Fetch chosen strategy
selected_data = data[task_type][competitor]

# Display Strategy UI Components
st.subheader(f"💡 Key Hook: {selected_data['hook']}")

# 1. Point-wise Strategy Card
st.markdown("<div class='points-card'><b>📋 Actual Points to Discuss:</b></div>", unsafe_allow_html=True)
for pt in selected_data['points']:
    st.markdown(f"• {pt}")

st.write("")

# 2. Verbal Pitch Card
st.markdown("<div class='pitch-card'><b>🗣️ Verbal Pitch (Izhar Style):</b><br><br>" + selected_data['pitch'] + "</div>", unsafe_allow_html=True)

# 3. Audio Player Block
st.markdown("### 🎵 Field Audio Guide")
if selected_data['audio']:
    st.audio(selected_data['audio'], format="audio/mp3")
else:
    st.info("ℹ️ Audio track for this segment will automatically stream here once uploaded by the Admin.")

# Footer Area Sector Incharge Quick Action Button
st.write("---")
st.markdown("<p style='text-align: center; font-size: 12px; color: #aaa;'>PhonePe Kanpur 1 Internal Operational App v1.2</p>", unsafe_allow_html=True)
