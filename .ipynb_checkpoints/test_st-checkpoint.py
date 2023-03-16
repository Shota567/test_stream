import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.write('プログレスバー')
'START'

latest_lit = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_lit.text(f'Interation {i+1}')
    bar.progress(i + 1)
    st.progress(i + 1)
    time.sleep(0.1)
    
'GOAL'

st.title('st testtest')

st.write('df')

df = pd.DataFrame({
    '1列目':[1,25,3,4],
    '2列目':[10,20,30,40]
})

st.table(df.style.highlight_max(axis=0))

df1 = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']
)

st.line_chart(df1)
st.area_chart(df1)
st.bar_chart(df1)
st.table(df1)


"""

# 大
## 中
### 小

```python
import streamlit as st
import numpy as np
import pandas as pd

st.title('st testtest')

st.write('df')
```

"""


df2 = pd.DataFrame(
    np.random.rand(100,2)/[50,50] + [35.69,139.70],
    columns=['lat','lon']
)

st.table(df2)
st.map(df2)


st.write('Image')

img = Image.open('aaa.jpg')
if st.checkbox('チェックボックス'):
    st.image(img , caption='testimg1')
    
st.image(img , caption='testimg2' , use_column_width=True)



option = st.sidebar.selectbox(
    '好きな数字',
    list(range(1,11))
)
text = st.sidebar.text_input('あなたの趣味')
cond = st.sidebar.slider('あなたの調子', 0 , 200 , 20)

'好きな数字は', option ,'です'
'あなたの趣味：',text
'コンディション：',cond

left_column,right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

exp1 = st.expander('質問1')
exp1.write('質問1の回答')
exp2 = st.expander('質問2')
exp2.write('質問2の回答')
exp3 = st.expander('質問3')
exp3.write('質問3の回答')

exp4 = st.expander('問い合わせ')
button_a = exp4.button('aに関する問い合わせ')
button_b = exp4.button('bに関する問い合わせ')
button_c = exp4.button('cに関する問い合わせ')

if button_a:
    text_abc = st.text_input('問い合わせ内容a')
elif button_b:
    text_abc = st.text_input('問い合わせ内容b')
elif button_c:
    text_abc = st.text_input('問い合わせ内容c')  

