# -*- coding: utf-8 -*-
# I used AI, throughout this entire assignment, to write all this code and learn how it works

import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as mdates
import pandas as pd

def load_streamflow(filename):
    data = np.loadtxt(filename, delimiter=",", skiprows=1, dtype=str)
    dates = data[:, 0]
    flows = data[:, 1:].astype(float)
    return dates, flows

def plot_streamflow(dates, flows, sites):
    plt.figure(figsize=(8, 6))

    colors = ['purple', 'teal', 'green', 'orange', 'red']
    for idx, site in enumerate(sites):
        plt.plot(dates, flows[:, idx], color=colors[idx], label=site)

    dt_dates = [datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in dates]

    tick_indices = []
    previous_day = 0
    for idx, dt in enumerate(dt_dates):
        day_num = dt.day
        if (day_num - 1) % 4 == 0 and day_num != previous_day:
            tick_indices.append(idx)
            previous_day = day_num

    tick_positions = [dates[i] for i in tick_indices]
    tick_labels = [dt_dates[i].strftime('%Y-%m-%d') for i in tick_indices]
    plt.xticks(tick_positions, tick_labels, rotation=45)

    plt.title('Provo River Streamflow Data (2021)')
    plt.xlabel('Date')
    plt.ylabel('Flowrate (cfs)')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(title='site numbers')
    plt.tight_layout()

# I ran the numbers in excel for gauge 10163000. Max was 131 and Average was 56.95236
def summarize(dates, flows, sites):
    summary_rows = []
    for idx, site in enumerate(sites):
        site_flows = flows[:, idx]
        max_flow = np.max(site_flows)
        max_date = dates[np.argmax(site_flows)]
        min_flow = np.min(site_flows)
        average_flow = np.mean(site_flows)
        summary_rows.append({
            "Gauge": site,
            "Max (cfs)": float(max_flow),
            "Date of max": max_date,
            "Min (cfs)": float(min_flow),
            "Avg (cfs)": float(average_flow),
        })
    return pd.DataFrame(
        summary_rows,
        columns=["Gauge", "Max (cfs)", "Date of max", "Min (cfs)", "Avg (cfs)"],
    )

def print_flow_statistics(summary):
    print(f"{'Gauge':<12} {'Max (cfs)':>10}   {'Date of max':<19}   {'Min (cfs)':>10}   {'Avg (cfs)':>10}")
    print("-" * 76)
    for _, stats in summary.iterrows():
        print(
            f"{stats['Gauge']:<12} "
            f"{stats['Max (cfs)']:>10.2f}   "
            f"{stats['Date of max']:<19}   "
            f"{stats['Min (cfs)']:>10.2f}   "
            f"{stats['Avg (cfs)']:>10.2f}"
        )

def save_summary_csv(summary):
    summary.to_csv("streamflow_summary.csv", index=False, float_format="%.2f")
    print("Saved summary to streamflow_summary.csv")

# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
summary = summarize(dates, flows, sites)
print_flow_statistics(summary)
save_summary_csv(summary)
plot_streamflow(dates, flows, sites)

plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")

plt.show()
