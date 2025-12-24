import streamlit as st
from models.model import load_model, recommend, get_places_by_category

st.set_page_config(
    page_title="Rekomendasi Wisata",
    layout="wide"
)

@st.cache_resource
def get_model():
    return load_model()

model = get_model()

# Header
st.title("🎯 Sistem Rekomendasi Wisata Indonesia")
st.write("Masukkan kata kunci (nama, kota, atau kategori), lalu pilih tempat untuk melihat rekomendasi.")

# Layout kolom untuk input keyword dan jumlah rekomendasi
col_search, col_n = st.columns([3, 1])

with col_search:
    keyword = st.text_input(
        "Cari Wisata (Nama Tempat / Kota / Kategori)",
        placeholder="Ketik kata kunci, misal: 'Pantai', 'Jogja', atau 'Candi'..."
    )

with col_n:
    num_recs = st.slider("Jumlah Rekomendasi", min_value=3, max_value=10, value=5)

# Initialize session state for search results
if 'search_results' not in st.session_state:
    st.session_state.search_results = []
if 'search_performed' not in st.session_state:
    st.session_state.search_performed = False

# Tombol cari
if st.button("🔍 Cari Rekomendasi"):
    if not keyword:
        st.warning("Mohon masukkan kata kunci terlebih dahulu.")
    else:
        # Cari tempat yang cocok
        found_places = get_places_by_category(model, keyword)
        st.session_state.search_results = found_places
        st.session_state.search_performed = True

# Tampilkan hasil jika pencarian sudah dilakukan (persistent)
if st.session_state.search_performed:
    found_places = st.session_state.search_results

    if not found_places:
        st.error(f"Maaf, tidak ditemukan tempat wisata dengan kata kunci '{keyword}'.")
        st.info("Coba gunakan kata kunci lain yang lebih umum, seperti 'Pantai', 'Taman', atau nama kota.")
    else:
        # Jika ditemukan lebih dari satu, biarkan user memilih
        if len(found_places) > 1:
            st.info(f"Ditemukan {len(found_places)} tempat yang cocok.")
            selected_place = st.selectbox("Pilih tempat yang dimaksud:", found_places)
        else:
            selected_place = found_places[0]
        
        st.success(f"Menampilkan rekomendasi berdasarkan: **{selected_place}**")

        with st.spinner("Mengunyah data..."):
            results = recommend(selected_place, model, n=num_recs)

        if not results:
            st.error("Tidak ditemukan rekomendasi tambahan.")
        else:
            st.subheader("✨ Rekomendasi Tempat Wisata Serupa")
            
            # Gunakan container agar tampilan lebih rapi
            for i, r in enumerate(results, start=1):
                with st.container():
                    st.markdown(f"### {i}. {r['name']}")
                    col1, col2 = st.columns([1, 2])
                    with col1:
                        st.write(f"**Kategori:** {r['category']}")
                        st.write(f"**Kota:** {r['city']}")
                    with col2:
                         st.metric("Tingkat Kemiripan", f"{r['score']}")
                    st.divider()
