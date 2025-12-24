import streamlit as st
import pandas as pd

from utils.preprocessing import (
    preprocess_text_steps
)

st.set_page_config(
    page_title="Data Preparation",
    page_icon="🧹",
    layout="wide"
)

st.title("🧹 Data Preparation (Pre-processing Data)")

st.write(
    """
    Tahap **Data Preparation** bertujuan untuk membersihkan dan menyiapkan
    data teks agar siap digunakan pada proses pemodelan sistem rekomendasi
    wisata berbasis **Content-Based Filtering (CBF)**.
    """
)

st.divider()

# Path File
INPUT_PATH = "data/destinasi-wisata-indonesia.csv"
OUTPUT_PATH = "data/destinasi-wisata-preprocessed.csv"
TEXT_COLUMNS = ["Place_Name", "Description", "Category", "City"]

df = pd.read_csv(OUTPUT_PATH)

# Ambil 1 contoh data
sample_text = df["combined_text"].iloc[0]
result = preprocess_text_steps(sample_text)

# Penggabungan Fitur
with st.container(border=True):
    st.subheader("1. Penggabungan Fitur Teks")

    st.write(
        """
        Beberapa atribut teks, yaitu **Place_name**, **Description**, **Category**,
        dan **City**, digabungkan menjadi satu kolom teks untuk membentuk
        representasi konten destinasi wisata secara menyeluruh.
        """
    )

    st.dataframe(
        df[TEXT_COLUMNS + ["combined_text"]].head(3),
        use_container_width=True
    )

# Case Folding
with st.container(border=True):
    st.subheader("2. Case Folding")

    st.write(
        "Proses case folding mengubah seluruh huruf pada teks menjadi huruf kecil."
    )

    st.dataframe(
        pd.DataFrame({
            "Tahap": ["Sebelum", "Sesudah"],
            "Teks": [sample_text, result["case_folding"]]
        }),
        use_container_width=True
    )

# Tokenizing
with st.container(border=True):
    st.subheader("3. Tokenizing")

    st.write(
        "Tokenizing memecah teks menjadi kata-kata (token)."
    )

    st.dataframe(
        pd.DataFrame({
            "Tahap": ["Sebelum", "Sesudah"],
            "Output": [
                result["case_folding"],
                ", ".join(result["tokenizing"])
            ]
        }),
        use_container_width=True
    )
# Stopword Removal
with st.container(border=True):
    st.subheader("4. Stopword Removal (Sastrawi)")

    st.write(
        "Stopword removal menghilangkan kata-kata umum yang tidak memiliki "
        "makna penting dalam analisis teks."
    )

    st.dataframe(
        pd.DataFrame({
            "Tahap": ["Sebelum", "Sesudah"],
            "Output": [
                ", ".join(result["tokenizing"]),
                ", ".join(result["stopword_removal"])
            ]
        }),
        use_container_width=True
    )

# Stemming
with st.container(border=True):
    st.subheader("5. Stemming (Sastrawi)")

    st.write(
        "Stemming mengubah kata menjadi bentuk dasar untuk meningkatkan "
        "konsistensi fitur teks."
    )

    st.dataframe(
        pd.DataFrame({
            "Tahap": ["Sebelum", "Sesudah"],
            "Output": [
                ", ".join(result["stopword_removal"]),
                ", ".join(result["stemming"])
            ]
        }),
        use_container_width=True
    )

st.info(
    "Hasil preprocessing telah disimpan dan data siap digunakan "
    "pada tahap pemodelan sistem rekomendasi."
)
