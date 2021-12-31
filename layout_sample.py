from pandas.core import series
import streamlit as streamlit
import numpy as np
import pandas as pd
from PIL import Image
import time


streamlit.title("streamlit 入門")

streamlit.write("DataFrame")



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

# テキスト入力(サイドバー)
streamlit.sidebar.write('Interactive Widgets')
option2 = streamlit.sidebar.text_input('あなたの趣味を教えてください')
'あなたの趣味：', option2, 'です'

# スライダー(min, max, default)(サイドバー)
option3 = streamlit.sidebar.slider('あなたの調子は？', 0, 100, 50)
'コンディション：' , option3

#2カラム
left_colmun, right_colmun = streamlit.columns(2)

displayButton = left_colmun.button('右カラムにボタン表示')

if displayButton :
    right_colmun.write('ここは右カラム')


# プログレスバー(完了するまでこの下のコードも実行されない)
'Start !!'
latest_iteration = streamlit.empty()
bar = streamlit.progress(0)

for i in range(100):
    # 設置済みのエレメントの表示を更新
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

# 折り畳み
expander = streamlit.expander('問い合わせ')
expander.write('問い合わせ内容')



