import streamlit as st


# st.title('Streamlit')

# st.write('Streamlit')

# df = pd.DataFrame({
#     '1列目': [1, 2, 3, 4],
#     '2列目': [10, 20, 30, 40]
# })

# #表の表示
# st.write(df)

# #表の幅と高さが指定可能
# st.dataframe(df, width=100, height= 100)

# #MAXの値色変更
# st.dataframe(df.style.highlight_max(axis=0))

# #静的な表 
# st.table(df.style.highlight_max(axis=0))

# #ランダム
# df = pd.DataFrame(
#     np.random.rand(20, 3),
#     columns=['a', 'b', 'c']
# )

# #マークダウン

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """


# #チャートを出力
# st.line_chart(df)
# st.area_chart(df)
# st.bar_chart(df)

# #東京都新宿区 の緯度と経度は それぞれ35.6938 139.7035 付近にランダムの座標を表示させる
# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)

# #10.インタラクティブなウィジェット 

# #チェックボックス　チェックONの時に画像を出力
# if st.checkbox('Show Image'):
#     img = Image.open('灼熱.jpg')
#     st.image(img, caption='shakunetsu', use_column_width=True)

# #セレクトボックス　数字を選択
# option = st.selectbox(
#     'あなたが好きな数字を教えて下さい',
#     list(range(1, 11))
# )
# 'あなたの好きな数字：', option

# #テキストボックス　文字列を表示
# text = st.text_input('あなたの趣味を教えて下さい')
# 'あなたの趣味：', text

# #スライダー
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'あなたの調子は？：', condition

#11.レイアウトを整える
option = st.sidebar.selectbox(
    'あなたが好きな数字を教えて下さい',
    list(range(1, 11))
)

#テキストボックス　文字列を表示
text = st.sidebar.text_input('あなたの趣味を教えて下さい')

#スライダー
condition = st.sidebar.slider('あなたの今の調子は？', 0, 100, 50)

#表示
'あなたの好きな数字：', option
'あなたの趣味：', text
'コンティション：', condition

left_column, right_column = st.columns(2)
button = left_column.button('今日の運勢 - ボタンを押すと右に表示')
if button:
    right_column.write('末吉')

expander = st.expander('押すとプルダウンで表示されます')
expander.write('表示１')
expander.write('表示２')
expander.write('表示３')