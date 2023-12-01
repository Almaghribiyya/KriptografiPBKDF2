import streamlit as st
import base64
import hashlib
import os

def generate_key(password, salt):
    """
    Menghasilkan kunci menggunakan algoritma PBKDF2 dengan hash SHA-256.

    Parameters:
    - password (str): Kata sandi yang diberikan oleh pengguna.
    - salt (bytes): Salt yang dihasilkan secara acak.

    Returns:
    - bytes: Kunci yang dihasilkan.
    """
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=32)
    return key

def encrypt(text, password):
    """
    Melakukan enkripsi teks yang diberikan menggunakan kunci yang dihasilkan dari PBKDF2.

    Parameters:
    - text (bytes): Teks yang akan dienkripsi.
    - password (str): Kata sandi yang diberikan oleh pengguna.

    Returns:
    - bytes: Teks yang terenkripsi.
    """
    salt = os.urandom(16)
    key = generate_key(password, salt)
    iv = os.urandom(16)

    ciphertext = bytearray()

    for i in range(len(text)):
        ciphertext.append(text[i] ^ key[i % 32])

    return base64.urlsafe_b64encode(salt + iv + bytes(ciphertext))

def decrypt(ciphertext, password):
    """
    Melakukan dekripsi teks yang telah dienkripsi menggunakan algoritma yang serupa dengan enkripsi.

    Parameters:
    - ciphertext (str): Teks terenkripsi.
    - password (str): Kata sandi yang diberikan oleh pengguna.

    Returns:
    - bytes: Teks yang terdekripsi.
    """
    data = base64.urlsafe_b64decode(ciphertext)
    salt, iv, ciphertext = data[:16], data[16:32], data[32:]

    key = generate_key(password, salt)

    plaintext = bytearray()

    for i in range(len(ciphertext)):
        plaintext.append(ciphertext[i] ^ key[i % 32])

    return bytes(plaintext)

def main():
    """
    Fungsi utama untuk menjalankan program kriptografi menggunakan algoritma PBKDF2.
    """
    st.set_page_config(
        page_title="PBKDF2",
        page_icon="🔐",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title("Kriptografi Menggunakan Algoritma Password-Based Key Derivation Function 2 (PBKDF2)")

    choice = st.sidebar.radio("Pilih Operasi:", ("Enkripsi", "Dekripsi"))

    if choice == "Enkripsi":
        text_enkripsi = st.text_area("Masukkan Pesan Asli:", height=200, key="text_enkripsi")
        password_enkripsi = st.text_input("Masukkan kunci (Enkripsi):", type="password", key="password_enkripsi")
        confirm_password_enkripsi = st.text_input("Konfirmasi kunci (Enkripsi):", type="password", key="confirm_password_enkripsi")

        # Validasi Input
        if not text_enkripsi or not password_enkripsi or password_enkripsi != confirm_password_enkripsi:
            st.warning("Masukkan teks dan kunci.")
            return

        # Bersihkan Tampilan Tombol
        st.image("https://res.cloudinary.com/dngmrdhjx/image/upload/v1701261816/lockclose_vjzcwb.png", width=50)
        encrypt_button = st.button("Enkripsi", key="encrypt_button")
        if encrypt_button:
            encrypted_text = encrypt(text_enkripsi.encode(), password_enkripsi)
            st.success("Ciphertext:")
            st.code(encrypted_text.decode(), language='plaintext')

    elif choice == "Dekripsi":
        text_dekripsi = st.text_area("Masukkan Ciphertext:", height=200, key="text_dekripsi")
        password_dekripsi = st.text_input("Masukkan kunci (Dekripsi):", type="password", key="password_dekripsi")
        confirm_password_dekripsi = st.text_input("Konfirmasi kunci (Dekripsi):", type="password", key="confirm_password_dekripsi")

        # Validasi Input
        if not text_dekripsi or not password_dekripsi or password_dekripsi != confirm_password_dekripsi:
            st.warning("Masukkan teks dan kunci.")
            return

        # Bersihkan Tampilan Tombol
        st.image("https://res.cloudinary.com/dngmrdhjx/image/upload/v1701261817/lockopen_i7solj.png", width=50)
        decrypt_button = st.button("Dekripsi", key="decrypt_button")
        if decrypt_button:
            # Menggunakan decrypt_password sebagai kata sandi
            decrypted_text = decrypt(text_dekripsi.encode(), password_dekripsi)
            st.success("Plaintext:")
            st.code(decrypted_text.decode(), language='plaintext')

if __name__ == "__main__":
    main()
