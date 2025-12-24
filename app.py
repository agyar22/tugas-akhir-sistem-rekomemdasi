import streamlit as st

st.set_page_config(
    page_title="Sistem Rekomendasi Wisata di Indonesia",
    page_icon="🌍",
    layout="wide"
)

st.title(
    "🌍 Sistem Rekomendasi Wisata di Indonesia Menggunakan Metode Content-Based Filtering (CBF)"
)

st.subheader("Project Overview")

st.markdown(
    """
    Aplikasi ini merupakan sistem rekomendasi wisata yang bertujuan untuk
    membantu pengguna menemukan destinasi wisata di Indonesia yang relevan
    berdasarkan **kemiripan konten destinasi**.

    Metode **Content-Based Filtering (CBF)** digunakan dengan menganalisis
    informasi deskriptif destinasi wisata dan menghitung tingkat kesamaan
    antar destinasi untuk menghasilkan rekomendasi.
    """
)

st.divider()