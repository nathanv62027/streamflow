# -*- coding: utf-8 -*-
# I used AI to write this code and learn how it works

import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as mdates

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

# Main program
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)

plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")

plt.show()
