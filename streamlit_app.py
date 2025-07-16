import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("Evaluation of Predicted RUL Against True RUL")

# GitHub 文件前缀
BASE_URL = "https://raw.githubusercontent.com/Micheal-undue/cmaps-data/main/"

# 文件配对
file_pairs = [
    ("RUL_FD001.txt", "predicted_rul1.csv"),
    ("RUL_FD002.txt", "predicted_rul2.csv"),
    ("RUL_FD003.txt", "predicted_rul3.csv"),
    ("RUL_FD004.txt", "predicted_rul4.csv"),
]

# 修复：读取 txt / csv
def load_rul_file(file):
    if file.endswith(".txt"):
        df = pd.read_csv(BASE_URL + file, sep=r"\s+", header=None)
    else:
        df = pd.read_csv(BASE_URL + file, header=None)
    df.columns = ['RUL']
    return df

# 开始绘图
for true_file, pred_file in file_pairs:
    df_true = load_rul_file(true_file)
    df_pred = load_rul_file(pred_file)

    # 绘图
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(df_true.index, df_true['RUL'], label='True RUL', linestyle='-', color='blue')
    ax.plot(df_pred.index, df_pred['RUL'], label='Predicted RUL', linestyle='--', color='orange')

    ax.set_title(f"{true_file} ")
    ax.set_xlabel("Engine ID")
    ax.set_ylabel("RUL")

    # 设置固定刻度
    ax.set_yticks([20, 40, 60, 80, 100, 120, 140])
    ax.set_ylim(0, 150)

    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
