import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/My photo.jpg")
with col2:
    st.title("Nandagopal Pammi chiranjeevi")
    content = "So, here I am, embarking on a new adventure – not with sword and shield, but with pen and imagination. My mission? To bring the grandeur of Indian mythology to life, weaving tales that captivate readers and reignite the awe these stories evoke. Join me on this journey as I delve into the hearts and battles of these timeless heroes!"
    st.info(content)

content2 = "Below you can find some of the apps i have built with Python, feel free to reach out to me. Thanks"
st.write(content2)