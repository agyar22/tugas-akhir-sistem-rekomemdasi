import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Data Understanding",
    page_icon="📁",
    layout="wide"
)

# Load Dataset
DATA_PATH = "data/destinasi-wisata-indonesia.csv"
df = pd.read_csv(DATA_PATH)

# Judul
st.title("📁 Data Understanding")

st.write(
    """
    Tahap **Data Understanding** bertujuan untuk memahami karakteristik dataset
    yang digunakan dalam pengembangan sistem rekomendasi wisata berbasis
    **Content-Based Filtering (CBF)**. Pada tahap ini dilakukan eksplorasi awal
    terhadap struktur, jumlah, dan kualitas data.
    """
)

st.divider()

# Deskripsi
with st.container(border=True):
    st.subheader("1. Deskripsi Dataset")
    st.write(
        """
        Dataset yang digunakan berisi informasi destinasi wisata di Indonesia.
        Setiap baris data merepresentasikan satu destinasi wisata yang dilengkapi
        dengan atribut deskriptif. Atribut-atribut ini menjadi dasar dalam
        proses ekstraksi fitur pada sistem rekomendasi berbasis konten.
        """
    )
    st.write(f"**Jumlah total destinasi wisata:** {len(df)} data")

# Struktur DAta
with st.container(border=True):
    st.subheader("2. Struktur dan Atribut Data")

    st.write(
        """
        Dataset terdiri dari beberapa atribut utama yang digunakan untuk
        menggambarkan karakteristik setiap destinasi wisata. Atribut berbasis
        teks memiliki peran penting dalam metode Content-Based Filtering.
        """
    )

    atribut_df = pd.DataFrame({
        "Atribut": df.columns,
        "Tipe Data": df.dtypes.astype(str)
    })

    st.dataframe(atribut_df, use_container_width=True)

# Contoh 10 Data Pertama
with st.container(border=True):
    st.subheader("3. Contoh Data")
    st.write(
        "Berikut merupakan contoh beberapa data destinasi wisata yang terdapat dalam dataset:"
    )
    st.dataframe(df.head(10), use_container_width=True)

# Distribusi Data
with st.container(border=True):
    st.subheader("4. Jumlah dan Distribusi Data")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Jumlah Destinasi Wisata", len(df))

    with col2:
        st.metric(
            "Jumlah Kategori Wisata",
            df["Category"].nunique()
        )

    category_count = (
        df["Category"]
        .value_counts()
        .reset_index()
        .rename(columns={
           "index": "Kategori",
            "Category": "Jumlah"
        })
    )

    category_count.columns = ["Kategori", "Jumlah"]

    st.write("Distribusi destinasi wisata berdasarkan kategori:")

    st.bar_chart(
        category_count.set_index("Kategori"),
        use_container_width=True
    )

# Cek Missing Values
with st.container(border=True):
    st.subheader("5. Kualitas Data")

    st.write(
        """
        Pada tahap ini dilakukan pemeriksaan kualitas data untuk mengidentifikasi
        keberadaan nilai kosong (*missing value*) dan potensi masalah data lainnya
        yang perlu ditangani pada tahap Data Preparation.
        """
    )

    missing_df = df.isnull().sum().reset_index()
    missing_df.columns = ["Atribut", "Jumlah Nilai Kosong"]

    st.dataframe(missing_df, use_container_width=True)
