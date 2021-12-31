from pandas.core import series
import streamlit as streamlit
import numpy as np
import pandas as pd
from PIL import Image


streamlit.title("streamlit 入門")

streamlit.write("DataFrame")


streamlit.write("Display Image")

#チェックボックス
if streamlit.checkbox('Show image'):
    img = Image.open('01-6.jpg')
    #画像の表示
    streamlit.image(img, caption='foraminifera', use_column_width=True)


# セレクトボックス
option = streamlit.selectbox(
    'あなたが好きな数字を教えてください',
    list(range(1, 11))
)

'あなたの好きな数字は', option, 'です'

# テキスト入力
streamlit.write('Interactive Widgets')
option2 = streamlit.text_input('あなたの趣味を教えてください')
'あなたの趣味：', option2, 'です'

# スライダー(min, max, default)
option3 = streamlit.slider('あなたの調子は？', 0, 100, 50)
'コンディション：' , option3