import streamlit as st
import random

# ゲームの開始
st.title("数字当てゲーム")

# ランダムな数字を生成
number = random.randint(1, 100)

# ユーザーに数字を入力させる
guess = st.number_input("数字を入力してください", min_value=1, max_value=100)

# ユーザーの入力とランダムな数字を比較する
if guess == number:
    st.write("正解です！")
else:
    st.write("不正解です。正解は{}でした。".format(number))