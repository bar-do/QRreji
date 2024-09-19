import qrcode
from PIL import Image
import streamlit as st

st.title("QR作成")

maney=st.selectbox("金額を入力してください",
                   (100, 200, 300),
)

if maney==100 or 200 or 300:
  img = qrcode.make(maney)
  img.save('imgs/QR.png')
  st.image('imgs/QR.png')



with open("imgs/QR.png", "rb") as file:
    btn = st.download_button(
        label="Download image",
        data=file,
        file_name="QR.png",
        mime="image/png",
    )
