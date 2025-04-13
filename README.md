# Streamlit-dashboard-app
# 📊 Real-Time Scheduler Dashboard

This Streamlit app allows you to visualize and compare scheduling results for three real-time schedulers: **EDF**, **Greedy**, and **PSO**, using real task execution data. It supports visual summaries, Gantt charts, and CPU utilization insights across multiple modes.

## 🚀 Features

- 📈 **CPU Utilization** comparison per scheduler and mode
- 📅 **Gantt Charts** showing task execution per core
- 📌 **Summary Cards** with energy, deadlines, slack, and fairness
- ⚙️ Supports four scheduling modes:
  - Normal
  - Multi-Core
  - DVFS
  - Task Migration

## 🗂️ Included Files

| File Name | Description |
|-----------|-------------|
| `app.py` | Main Streamlit dashboard app |
| `scheduler_results.xlsx` | Pre-generated results from simulator (used by app) |
| `requirements.txt` | Python dependencies for Streamlit Cloud |

## 🧪 Sample Visuals

| CPU Utilization | Gantt Chart |
|-----------------|--------------|
| ![CPU](assets/cpu_utilization.png) | ![Gantt](assets/gantt_chart.png) |

## ⚙️ Setup Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## ☁️ Deploy to Streamlit Cloud
1. Fork or clone this repo
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **New App**, select this repo, set `app.py` as entry point

## 📬 Contact

For research collaboration or support:
- 📧 alamin.ite.su@gmail.com
- 🧑‍💻 GitHub: [yourusername](https://github.com/Alamin-Advance)

---

© 2025 Real-Time Scheduling Research · All rights reserved

