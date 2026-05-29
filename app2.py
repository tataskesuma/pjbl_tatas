import streamlit as st

st.set_page_config(
    page_title = "Matematika Geometri",
    page_icon = "🤖"
)

with st.sidebar:
    col1, col2, col3, = st.columns([1, 2, 1])
    with col2:
        st.image("geo.png")     
    st.title("Bangun Datar")

    pilihan = st.selectbox("pilihan Bangun Datar", ["Persegi", "Persegi Panjang", "Lingkaran", "Segitiga", "Jajar Genjang"])
    st.caption("Dibuat dengan :fire: oleh **Tatas Kesuma Jati**")

match pilihan:
    case "Persegi":
        st.title("Persegi")
        st.markdown("Menghitung `luas` dan `keliling` persegi")
        sisi = st.number_input("Masukkan Sisi")
        if st.button("Hitung", type="primary"):
            luas = sisi * sisi
            keliling = 4 * sisi
            # st.success(f"Luas persegi adalah {luas} dan kelilingnya adalah {keliling}")
            col1, col2 =st.columns([2, 2])
            with col1:
                st.metric("Luas", value= luas, border= True)
            with col2:
                st.metric("Keliling", value= keliling, border= True)
            st.balloons()
    case "Persegi Panjang":
        st.title("Persegi Panjang")
        st.markdown("Menghitung `luas` dan `keliling` persegi panjang")
        panjang = st.number_input("Masukkan Panjang")
        lebar = st.number_input("Masukkan Lebar")
        if st.button("Hitung", type="primary"):
            luas = panjang * lebar
            keliling = 2 * (panjang + lebar)
            # st.success(f"Luas persegi panjang adalah {luas} dan kelilingnya adalah {keliling}")
            col1, col2 =st.columns([2, 2])
            with col1:
                st.metric("Luas", value= luas, border= True)
            with col2:
                st.metric("Keliling", value= keliling, border= True)
            st.balloons()
    case "Lingkaran":
        st.title("Lingkaran")
        st.markdown("Menghitung `luas` dan `keliling` lingkaran")
        jarijari = st.number_input("Masukkan Jari-Jari")
        if st.button("Hitung", type="primary"):
            luas = 3.14 * jarijari * jarijari
            keliling = 2 * 3.14 * jarijari
            # st.success(f"Luas lingkaran adalah {luas} dan kelilingnya adalah {keliling}")
            col1, col2 =st.columns([2, 2])
            with col1:
                st.metric("Luas", value= luas, border= True)
            with col2:
                st.metric("Keliling", value= keliling, border= True)
            st.balloons()
    case "Segitiga":
        st.title("Segitiga")
        st.markdown("Menghitung `luas` dan `keliling` segitiga")
        alas = st.number_input("Masukkan Alas")
        tinggi = st.number_input("Masukkan Tinggi")
        if st.button("Hitung", type="primary"):
            luas = 0.5 * alas * tinggi
            keliling = 3 * alas
            # st.success(f"Luas segitiga adalah {luas} dan kelilingnya adalah {keliling}")
            col1, col2 =st.columns([2, 2])
            with col1:
                st.metric("Luas", value= luas, border= True)
            with col2:
                st.metric("Keliling", value= keliling, border= True)
            st.balloons()
    case "Jajar Genjang":
        st.title("Jajar Genjang")
        st.markdown("Menghitung `luas` dan `keliling` jajar genjang")
        alas = st.number_input("Masukkan Alas")
        tinggi = st.number_input("Masukkan Tinggi")
        sisi_miring = st.number_input("Masukkan Sisi Miring")
        if st.button("Hitung", type="primary"):
            luas = alas * tinggi
            keliling = 2 * (alas + sisi_miring)
            # st.success(f"Luas jajar genjang adalah {luas} dan kelilingnya adalah {keliling}")
            col1, col2 =st.columns([2, 2])
            with col1:
                st.metric("Luas", value= luas, border= True)
            with col2:
                st.metric("Keliling", value= keliling, border= True)
            st.balloons()
    case _ :
        st.error("Terjadi Kesalahan")