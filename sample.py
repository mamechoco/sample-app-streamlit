from pandas.core import series
import streamlit as streamlit
import numpy as np
import pandas as pd
from PIL import Image


streamlit.title("streamlit 入門")

streamlit.write("DataFrame")

dataFrame = pd.DataFrame({
    "1列目": [1, 2, 3, 4],
    "2列目": [10, 20, 30, 40]
})

# streamlit.write(dataFrame)でも良いが、streamlit.dataframeだとオプション設定できる 
streamlit.dataframe(dataFrame.style.highlight_max(axis=0))



# staticなテーブル作成の場合
streamlit.table(dataFrame.style.highlight_min(axis=1))

# マークダウン形式マジックコマンド
"""
# 章
## 節
### 項
```python
import streamlit as streamlit
import numpy as np
import pandas as pd
```
"""

dataFrame2 = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)

# グラフ
streamlit.area_chart(dataFrame2)

dataFrame3 = pd.DataFrame(
    np.random.randn(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

# map ＊列名がlat, lon(もしくはフルネーム)の必要がある
streamlit.map(dataFrame3)

streamlit.write("Display Image")

img = Image.open('01-6.jpg')

#画像の表示
streamlit.image(img, caption='foraminifera', use_column_width=True)