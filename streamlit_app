import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("📉 RUL 真实值 vs 预测值 对比图")

# GitHub 原始文件路径前缀
BASE_URL = "https://raw.githubusercontent.com/Micheal-undue/cmaps-data/main/"

# 文件配对：真实值 vs 预测值
file_pairs = [
    ("RUL_FD001.txt", "predicted_rul1.csv"),
    ("RUL_FD002.txt", "predicted_rul2.csv"),
    ("RUL_FD003.txt", "predicted_rul3.csv"),
    ("RUL_FD004.txt", "predicted_rul4.csv"),
]

# 加载文件函数
def load_rul_file(file):
    sep = r"\s+" if file.endswith(".txt") else ","
    df = pd.read_csv(BASE_URL + file, sep=sep, header=None)
    df.columns = ['RUL']
    return df

# 一列四行绘图
for true_file, pred_file in file_pairs:
    df_true = load_rul_file(true_file)
    df_pred = load_rul_file(pred_file)

    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df_true.index, df_true['RUL'], label='True RUL', linestyle='-', color='blue')
    ax.plot(df_pred.index, df_pred['RUL'], label='Predicted RUL', linestyle='--', color='orange')
    ax.set_title(f"{true_file} vs {pred_file}")
    ax.set_xlabel("Index")
    ax.set_ylabel("RUL")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)
