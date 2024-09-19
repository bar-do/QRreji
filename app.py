import cv2 
import numpy as np
import streamlit as st


from camera_input_live import camera_input_live

st.title("レジアプリ")


image = camera_input_live()

if image is not None:
    st.image(image)
    bytes_data = image.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    detector = cv2.QRCodeDetector()

    data = detector.detectAndDecode(cv2_img)

    if data:
        st.write("# Found QR code")
        st.write(data)
        tax_pey=(int(data)*0.1)+int(data)
        st.subheader("お支払い金額は")
        st.subheader(tax_pey)

        maney=st.number_input("お預かり金額は",value=0,format="%0u",placeholder="何円？")

        if tax_pey-maney==0:
         st.subheader("お買い上げありがとうございます。")
        elif tax_pey>=maney:
          st.subheader("金額が足りません")
        elif tax_pey<=maney:
          st.subheader("おつりは")
          st.subheader(maney-tax_pey)
        


