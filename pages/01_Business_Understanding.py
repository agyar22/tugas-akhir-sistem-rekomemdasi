import streamlit as st

st.set_page_config(
    page_title="Business Understanding",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Business Understanding")

st.write(
    "Pada halaman ini menjelaskan pemahaman awal terkait sistem rekomendasi wisata yang dikembangkan menggunakan metode Content-Based Filtering (CBF)."
)

st.divider()

# Pengertian
with st.container(border=True):
    st.subheader("1. Pengertian Sistem Rekomendasi Menggunakan Content-Based Filtering (CBF)")
    st.write(
        """
        Sistem rekomendasi berbasis **Content-Based Filtering (CBF)** merupakan pendekatan
        yang memberikan rekomendasi berdasarkan **kesesuaian karakteristik atau konten**
        suatu item dengan preferensi pengguna. Dalam metode ini sistem akan meminta tempat wisata yang pernah dikunjungi,
        kemudian merekomendasikan item atau tempat wisata lain yang memiliki tingkat kemiripan tertinggi.

        Pada konteks rekomendasi wisata, CBF bekerja dengan membandingkan informasi
        destinasi wisata seperti nama tempat, deskripsi, kategori, dan kota untuk menemukan
        destinasi yang relevan dengan pilihan pengguna sebelumnya.
        """
    )

# Latar Belakang
with st.container(border=True):
    st.subheader("2. Latar Belakang")
    st.write(
        """
        Indonesia memiliki beragam destinasi wisata dengan karakteristik yang berbeda-beda.
        Banyaknya pilihan destinasi sering kali membuat wisatawan mengalami kesulitan
        dalam menentukan tujuan wisata yang sesuai dengan minat dan preferensi mereka.

        Oleh karena itu, diperlukan sebuah sistem rekomendasi yang mampu membantu
        pengguna dalam menemukan destinasi wisata yang relevan secara personal.
        Metode Content-Based Filtering dipilih karena mampu memberikan rekomendasi
        berdasarkan kesamaan konten destinasi tanpa bergantung pada data pengguna lain.
        """
    )

# Permasalahan
with st.container(border=True):
    st.subheader("3. Permasalahan")
    st.write(
        """
        Permasalahan yang dihadapi dalam pemilihan destinasi wisata antara lain:
        - Banyaknya pilihan destinasi wisata dengan informasi yang beragam  
        - Sulitnya menemukan destinasi yang sesuai dengan minat pengguna  
        """
    )

# Tujuan
with st.container(border=True):
    st.subheader("4. Tujuan")
    st.write(
        """
        Tujuan dari pengembangan sistem rekomendasi wisata ini adalah:
        - Membantu pengguna dalam memilih destinasi wisata di tengah banyaknya pilihan destinasi yang tersedia
        - Menyediakan rekomendasi destinasi wisata yang sesuai dengan minat pengguna berdasarkan karakteristik dan informasi destinasi  
        """
    )
