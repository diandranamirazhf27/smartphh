# smartpH.app.py
import streamlit as st
import math
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Kalkulator pH", page_icon=":1234:", layout="wide")

# ========== Fungsi Perhitungan (Dengan Validasi) ==========
def perhitungan_pH_asam_kuat(konsentrasi, a):
    try:
        if konsentrasi <= 0 or a <= 0:
            raise ValueError("Nilai harus positif")
        H_plus = konsentrasi * a
        pH = -math.log10(H_plus)
        return round(H_plus, 10), round(pH, 2)
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return 0, 0

def perhitungan_pH_basa_kuat(konsentrasi, a):
    try:
        if konsentrasi <= 0 or a <= 0:
            raise ValueError("Nilai harus positif")
        OH_minus = konsentrasi * a
        pOH = -math.log10(OH_minus)
        pH = 14 - pOH
        return round(OH_minus, 10), round(pOH, 2), round(pH, 2)
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return 0, 0, 7

def perhitungan_pH_asam_lemah(Ka, konsentrasi):
    try:
        if Ka <= 0 or konsentrasi <= 0:
            raise ValueError("Nilai harus positif")
        H_plus = math.sqrt(Ka * konsentrasi)
        pH = -math.log10(H_plus)
        return round(H_plus, 10), round(pH, 2)
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return 0, 0

def perhitungan_pH_basa_lemah(Kb, konsentrasi):
    try:
        if Kb <= 0 or konsentrasi <= 0:
            raise ValueError("Nilai harus positif")
        OH_minus = math.sqrt(Kb * konsentrasi)
        pOH = -math.log10(OH_minus)
        pH = 14 - pOH
        return round(OH_minus, 10), round(pOH, 2), round(pH, 2)
    except Exception as e:
        st.error(f"Error: {str(e)}")
        return 0, 0, 7

# ========== Tampilan UI ==========
with st.sidebar:
    selected = option_menu(
        menu_title="Menu Utama",
        options=["Beranda", "Asam Kuat", "Asam Lemah", "Basa Kuat", "Basa Lemah"],
        icons=["house", "droplet", "droplet-half", "capsule", "capsule-pill"],
        default_index=0
    )

if selected == "Beranda":
    st.title("Kalkulator pH Larutan")
    st.image("https://via.placeholder.com/800x200?text=Kalkulator+pH", use_column_width=True)
    st.write("""
    Aplikasi ini membantu menghitung:
    - pH Asam Kuat (HCl, H2SO4, dll)
    - pH Asam Lemah (CH3COOH, HF, dll)
    - pH Basa Kuat (NaOH, KOH, dll)
    - pH Basa Lemah (NH4OH, dll)
    """)

elif selected == "Asam Kuat":
    st.header("Kalkulator pH Asam Kuat")
    
    contoh = {
        "HCl 0.1 M (a=1)": {"konsentrasi": 0.1, "a": 1},
        "H2SO4 0.01 M (a=2)": {"konsentrasi": 0.01, "a": 2}
    }
    
    pilihan = st.selectbox("Pilih contoh cepat:", list(contoh.keys()))
    konsentrasi = st.number_input("Konsentrasi (M)", min_value=0.0, value=contoh[pilihan]["konsentrasi"], step=1e-4, format="%.4f")
    a = st.number_input("Valensi (a)", min_value=1, value=contoh[pilihan]["a"], step=1)
    
    if st.button("Hitung pH"):
        H_plus, pH = perhitungan_pH_asam_kuat(konsentrasi, a)
        st.success(f"""
        Hasil Perhitungan:
        - [H⁺] = {H_plus:.2e} M
        - pH = {pH:.2f}
        """)

elif selected == "Asam Lemah":
    st.header("Kalkulator pH Asam Lemah")
    
    contoh = {
        "CH3COOH (Ka=1.8e-5) 0.1 M": {"Ka": 1.8e-5, "konsentrasi": 0.1},
        "HF (Ka=6.6e-4) 0.01 M": {"Ka": 6.6e-4, "konsentrasi": 0.01}
    }
    
    pilihan = st.selectbox("Pilih contoh cepat:", list(contoh.keys()))
    Ka = st.number_input("Ka", min_value=0.0, value=contoh[pilihan]["Ka"], step=1e-5, format="%.1e")
    konsentrasi = st.number_input("Konsentrasi (M)", min_value=0.0, value=contoh[pilihan]["konsentrasi"], step=1e-4, format="%.4f")
    
    if st.button("Hitung pH"):
        H_plus, pH = perhitungan_pH_asam_lemah(Ka, konsentrasi)
        st.success(f"""
        Hasil Perhitungan:
        - [H⁺] = {H_plus:.2e} M
        - pH = {pH:.2f}
        """)

elif selected == "Basa Kuat":
    st.header("Kalkulator pH Basa Kuat")
    
    contoh = {
        "NaOH 0.1 M (a=1)": {"konsentrasi": 0.1, "a": 1},
        "Ca(OH)2 0.01 M (a=2)": {"konsentrasi": 0.01, "a": 2}
    }
    
    pilihan = st.selectbox("Pilih contoh cepat:", list(contoh.keys()))
    konsentrasi = st.number_input("Konsentrasi (M)", min_value=0.0, value=contoh[pilihan]["konsentrasi"], step=1e-4, format="%.4f")
    a = st.number_input("Valensi (a)", min_value=1, value=contoh[pilihan]["a"], step=1)
    
    if st.button("Hitung pH"):
        OH_minus, pOH, pH = perhitungan_pH_basa_kuat(konsentrasi, a)
        st.success(f"""
        Hasil Perhitungan:
        - [OH⁻] = {OH_minus:.2e} M
        - pOH = {pOH:.2f}
        - pH = {pH:.2f}
        """)

elif selected == "Basa Lemah":
    st.header("Kalkulator pH Basa Lemah")
    
    contoh = {
        "NH4OH (Kb=1.8e-5) 0.1 M": {"Kb": 1.8e-5, "konsentrasi": 0.1},
        "Al(OH)3 (Kb=1.3e-9) 0.01 M": {"Kb": 1.3e-9, "konsentrasi": 0.01}
    }
    
    pilihan = st.selectbox("Pilih contoh cepat:", list(contoh.keys()))
    Kb = st.number_input("Kb", min_value=0.0, value=contoh[pilihan]["Kb"], step=1e-5, format="%.1e")
    konsentrasi = st.number_input("Konsentrasi (M)", min_value=0.0, value=contoh[pilihan]["konsentrasi"], step=1e-4, format="%.4f")
    
    if st.button("Hitung pH"):
        OH_minus, pOH, pH = perhitungan_pH_basa_lemah(Kb, konsentrasi)
        st.success(f"""
        Hasil Perhitungan:
        - [OH⁻] = {OH_minus:.2e} M
        - pOH = {pOH:.2f}
        - pH = {pH:.2f}
        """)
