import streamlit as st

# --- SAYFA AYARLARI (ASİL TEMA) ---
st.set_page_config(page_title="Premium Teaser App", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #050505; }
    .stButton>button {
        background-color: #C5A059;
        color: black;
        border-radius: 5px;
        width: 100%;
        font-weight: bold;
    }
    .cover-card {
        border: 1px solid #1a1a1a;
        padding: 15px;
        border-radius: 10px;
        background-color: #0a0a0a;
        text-align: center;
    }
    h1, h2, h3 { color: #C5A059 !important; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR (KATEGORİLER) ---
st.sidebar.title("💎 PREMIUM TEASER")
category = st.sidebar.radio("Kategori Seçin", ["Son Atılanlar", "Galatasaray", "Fenerbahçe", "Beşiktaş", "Global"])
st.sidebar.markdown("---")
st.sidebar.subheader("💰 Abonelik Durumu")
is_premium = st.sidebar.checkbox("Premium Üyeyim (Giriş Yap)")

# --- ANA SAYFA BAŞLIK ---
st.title(f"✨ {category} Dünyası")
st.write("En asil teaser coverları ve comp dosyaları.")

# --- DUMMY DATA (SEN BURAYA FOTOLARI EKLEYECEKSİN) ---
# Gerçek uygulamada bunları bir klasörden veya veritabanından çekebiliriz.
covers = [
    {"title": "Icardi Special", "team": "Galatasaray", "img": "https://via.placeholder.com/400x500/ce1126/ffffff?text=GS+TEASER"},
    {"title": "Tadic Masterclass", "team": "Fenerbahçe", "img": "https://via.placeholder.com/400x500/003366/ffffff?text=FB+TEASER"},
    {"title": "Eagle Vision", "team": "Beşiktaş", "img": "https://via.placeholder.com/400x500/000000/ffffff?text=BJK+TEASER"},
]

# --- FİLTRELEME MANTIĞI ---
filtered_covers = [c for c in covers if c["team"] == category] if category != "Son Atılanlar" else covers

# --- GRID SİSTEMİ ---
cols = st.columns(3)
for idx, cover in enumerate(filtered_covers):
    with cols[idx % 3]:
        st.markdown(f'<div class="cover-card">', unsafe_allow_html=True)
        st.image(cover["img"], use_container_width=True)
        st.subheader(cover["title"])
        
        if is_premium:
            st.success("✅ Erişim Açık")
            st.button(f"Comp Dosyasını İndir ({idx})", key=f"dl_{idx}")
        else:
            st.warning("🔒 İçerik Kilitli")
            if st.button(f"Erişim Satın Al ({idx})", key=f"buy_{idx}"):
                st.info("Ödeme sayfasına yönlendiriliyorsunuz...")
        st.markdown('</div>', unsafe_allow_html=True)

# --- FİYATLANDIRMA BÖLÜMÜ ---
st.markdown("---")
if not is_premium:
    st.header("🏆 Premium Paketler")
    p_col1, p_col2 = st.columns(2)
    with p_col1:
        st.info("**Aylık Pass**\n\n150 TL / Ay")
    with p_col2:
        st.success("**Yıllık Pass (Elite)**\n\n1000 TL / Yıl")
