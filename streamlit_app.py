import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(layout="wide")
st.title("Evaluation of Predicted RUL Against True RUL")

# GitHub 原始文件路径
BASE_URL = "https://raw.githubusercontent.com/Micheal-undue/cmaps-data/main/"

# 文件配对 + 标题 + y轴配置
file_pairs = [
    ("RUL_FD001.txt", "predicted_rul1.csv", "FD001", list(range(0, 141, 20))),
    ("RUL_FD002.txt", "predicted_rul2.csv", "FD002", list(range(0, 201, 25))),
    ("RUL_FD003.txt", "predicted_rul3.csv", "FD003", list(range(0, 141, 20))),
    ("RUL_FD004.txt", "predicted_rul4.csv", "FD004", list(range(0, 201, 25))),
]

# 加载数据
def load_rul_file(file):
    if file.endswith(".txt"):
        df = pd.read_csv(BASE_URL + file, sep=r"\s+", header=None)
    else:
        df = pd.read_csv(BASE_URL + file, header=None)
    df.columns = ['RUL']
    return df

# 开始绘图
for true_file, pred_file, title, y_ticks in file_pairs:
    df_true = load_rul_file(true_file)
    df_pred = load_rul_file(pred_file)

    avg_value = df_pred['RUL'].mean()
    avg_line = [avg_value] * len(df_pred)

    # 控制开关
    col1, col2, col3 = st.columns(3)
    show_true = col1.checkbox(f"True RUL（from text）（{title}）", value=True, key=f"true_{title}")
    show_pred = col2.checkbox(f"Predicted RUL（{title}）", value=True, key=f"pred_{title}")
    show_avg = col3.checkbox(f"Average（{title}）", value=True, key=f"avg_{title}")

    fig = go.Figure()

    if show_true:
        fig.add_trace(go.Scatter(
            y=df_true['RUL'],
            mode="lines",
            name="True RUL（from text）",
            line=dict(color="blue", dash="solid")
        ))

    if show_pred:
        fig.add_trace(go.Scatter(
            y=df_pred['RUL'],
            mode="lines",
            name="Predicted RUL",
            line=dict(color="orange", dash="dash")
        ))

    if show_avg:
        fig.add_trace(go.Scatter(
            y=avg_line,
            mode="lines",
            name="Average",
            line=dict(color="red", dash="dot")
        ))

    fig.update_layout(
        title=title,
        xaxis_title="Engine ID",
        yaxis_title="RUL",
        yaxis=dict(tickmode='array', tickvals=y_ticks, range=[min(y_ticks), max(y_ticks)]),
        legend=dict(x=0, y=1.15, orientation='h'),
        height=400,
        margin=dict(l=40, r=40, t=60, b=40)
    )

    st.plotly_chart(fig, use_container_width=True)
