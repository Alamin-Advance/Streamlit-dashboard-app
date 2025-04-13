# Streamlit Deployment - app.py (Same functionality as Gradio)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image

# Load Excel file
def load_data():
    file_path = "scheduler_results.xlsx"  # This file will be pushed to GitHub
    data = pd.read_excel(file_path, sheet_name=None)
    metrics = data['Best_Metrics'].set_index(data['Best_Metrics'].columns[0])
    task_data = {k: v for k, v in data.items() if k != 'Best_Metrics'}
    return metrics, task_data

def generate_charts(metrics, task_data, scheduler, mode):
    selected_key = f"{scheduler}-{mode}"
    metric_row = metrics.loc[selected_key]
    summary = f"""
    ### Summary - {scheduler} in {mode} mode
    - Total Energy (J): {metric_row['Total Energy (J)']:.2f}
    - Missed Deadlines: {int(metric_row['Missed Deadlines'])}
    - CPU Utilization: {metric_row['CPU Utilization (%)']:.1f}%
    """

    # CPU Utilization Chart
    filtered = metrics.filter(like=f'-{mode}', axis=0)
    filtered.index = filtered.index.str.replace(f'-{mode}', '')
    fig1, ax1 = plt.subplots()
    ax1.bar(filtered.index, filtered['CPU Utilization (%)'], color=['blue', 'green', 'orange'])
    ax1.set_title(f"CPU Utilization - {mode.title()} Mode")
    ax1.set_ylabel("Utilization (%)")
    buf1 = BytesIO()
    fig1.savefig(buf1, format="png")
    plt.close(fig1)
    cpu_chart = Image.open(BytesIO(buf1.getvalue()))

    # Gantt Chart
    df_tasks = task_data[selected_key]
    fig2, ax2 = plt.subplots(figsize=(10, 2.5))
    for _, row in df_tasks.iterrows():
        ax2.barh(row['core'], row['end'] - row['start'], left=row['start'], edgecolor='black')
        ax2.text(row['start'] + 0.2, row['core'] + 0.1, row['id'], fontsize=8)
    ax2.set_xlabel("Time")
    ax2.set_ylabel("Core")
    ax2.set_title(f"Gantt Chart: {scheduler} - {mode}")
    plt.tight_layout()
    buf2 = BytesIO()
    fig2.savefig(buf2, format="png")
    plt.close(fig2)
    gantt_chart = Image.open(BytesIO(buf2.getvalue()))

    return summary, cpu_chart, gantt_chart

# UI
def main():
    st.set_page_config(page_title="Real-Time Scheduler Dashboard", layout="wide")
    st.title("📊 Real-Time Scheduling Dashboard")

    metrics, task_data = load_data()
    schedulers = ["EDF", "Greedy", "PSO"]
    modes = ["normal", "multi", "dvfs", "mig"]

    scheduler = st.selectbox("Select Scheduler", schedulers, index=0)
    mode = st.selectbox("Select Mode", modes, index=0)

    summary, cpu_chart, gantt_chart = generate_charts(metrics, task_data, scheduler, mode)

    st.markdown(summary)

    col1, col2 = st.columns(2)
    with col1:
        st.image(cpu_chart, caption="CPU Utilization Chart")
    with col2:
        st.image(gantt_chart, caption="Gantt Chart")

if __name__ == '__main__':
    main()
