import streamlit as st
import pandas as pd
import numpy as np

# Ma'lumotlar jadvali
data = {
    'Athlete age category': ['MU23', 'M35', 'M23', 'M40', 'M45', 'W35', 'M50', 'W23', 'M55', 'W40', 'W45', 'M60', 'W50', 'M65'],
    'mean': [8.329217, 8.122638, 8.115355, 7.935726, 7.881049, 7.707617, 7.654792, 7.628854, 7.450510, 7.446708, 7.405470, 7.340222, 7.257289, 7.154957],
    'count': [23, 531, 685, 577, 530, 60, 308, 82, 153, 72, 66, 54, 45, 23]
}

df = pd.DataFrame(data)

# Orqa fon rangini sozlash
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, lightblue, lightgreen);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Dastur sarlavhasi
st.title("Yosh toifasini aniqlash")

# Foydalanuvchi kiritmalari
user_mean = st.number_input("Sportchining o'rtacha tezligi (mean) ni kiriting:", min_value=0.0, step=0.01)
user_count = st.number_input("Sportchining musobaqa soni (count) ni kiriting:", min_value=1, step=1)

# Eng yaqin yosh toifasini topish tugmasi
if st.button("Eng yaqin yosh toifasini aniqlash"):
    if user_mean and user_count:
        # Masofa hisoblash (Euclidean distance)
        df['distance'] = np.sqrt((df['mean'] - user_mean)**2 + (df['count'] - user_count)**2)
        nearest_category = df.loc[df['distance'].idxmin(), 'Athlete age category']
        st.write(f"Eng yaqin yosh toifasi= **{nearest_category}**")
    else:
        st.warning("Iltimos, barcha maydonlarni to'ldiring!")
