import streamlit as st

st.title("Password-Based Key Derivation Function 2 Algorithm")
st.image("https://res.cloudinary.com/dngmrdhjx/image/upload/v1701354014/PBKDF1_ogmhaj.jpg")

st.subheader('Proyek Akhir Mata Kuliah Kriptografi - Kelompok 6', divider='green')
st.markdown("Moza Rizki Ilahi           (2210511048)")
st.markdown("Nisaul Husna               (2210511055)") 
st.markdown("Choirunnisa Zalfaa Nabilah (2210511070)")
st.markdown("Mahira Afifa Mulia         (2210511071)") 
st.markdown("Muhammad Rezka Al Maghribi (2210511086)")

st.subheader('How Password-Based Key Derivation Function 2 Works', divider='green', anchor="/google")
with st.expander("Algoritma Password-Based Key Derivation Function 2"):
        st.write("""
        Pada dasarnya, algoritma Password-Based Key Derivation Function 2 (PBKDF2) digunakan untuk meningkatkan keamanan kata sandi dengan memperkenalkan elemen salt (garam) dan proses iteratif. Garam ini adalah nilai acak yang ditambahkan ke dalam kata sandi sebelum diolah oleh fungsi hash. Fungsi hash ini kemudian diiterasikan beberapa kali untuk membuat prosesnya lebih lambat dan memerlukan lebih banyak sumber daya komputasi. Hasil akhir dari PBKDF2 adalah kunci yang lebih aman dan sulit dipecahkan, yang dapat digunakan untuk keperluan kriptografi seperti enkripsi atau autentikasi..
        """)
st.image('https://res.cloudinary.com/dngmrdhjx/image/upload/v1701354013/PBKDF2_fopdal.png')


