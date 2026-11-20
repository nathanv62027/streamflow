# -*- coding: utf-8 -*-
# I used AI, throughout this entire assignment, to write all the code and learn how it works


# Import required libraries
import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as mdates
import pandas as pd

# Used AI to write this code.
# Create function to load streamflow data into code
def load_streamflow(filename):
    data = np.loadtxt(filename, delimiter=",", skiprows=1, dtype=str)
    dates = data[:, 0]
    flows = data[:, 1:].astype(float)
    return dates, flows

# Used AI to write this code.
# Create a function to create and format data into plot
def plot_streamflow(dates, flows, sites):
    plt.figure(figsize=(8, 6))

    # Assign colors for plotted information
    colors = ['purple', 'teal', 'green', 'orange', 'red']
    for idx, site in enumerate(sites):
        plt.plot(dates, flows[:, idx], color=colors[idx], label=site)

    # Format dates so that they can be used in the code
    dt_dates = [datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in dates]

    # Format tick marks on x axis to show desired dates
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

    # Finish formatting plot axis, labels, and titles
    plt.title('Provo River Streamflow Data (2021)')
    plt.xlabel('Date')
    plt.ylabel('Flowrate (cfs)')
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend(title='site numbers')
    plt.tight_layout()

# I used AI to write this code.
# I ran the numbers in excel for gauge 10163000. Max was 131 and Average was 56.95236
# Create function to summarize data into table format. Do this for each gauge.
def summarize(dates, flows, sites):
    summary_rows = []
    for idx, site in enumerate(sites):
        site_flows = flows[:, idx]
        max_flow = np.max(site_flows)
        max_date = dates[np.argmax(site_flows)]
        min_flow = np.min(site_flows)
        average_flow = np.mean(site_flows)
       
        # Format summary
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

# I used AI to write this code.
# Define function to print summary in terminal
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

# I used AI to write this code.
# Create function to save summary to a file
def save_summary_csv(summary):
    summary.to_csv("streamflow_summary.csv", index=False, float_format="%.2f")
    print("Saved summary to streamflow_summary.csv")

# I used AI to write this code.
# Ask for user to input threshold. Calls predetermined functions. Checks data and prints how many hrs each gauge was above the requested threshold.
# Main program
threshold = float(input("Enter a flow threshold in CFS: "))
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
summary = summarize(dates, flows, sites)
print_flow_statistics(summary)
save_summary_csv(summary)
print(f"\nHours above {threshold:.2f} CFS:")
print(f"{'Gauge':<12} {'Hours':>10}")
print("-" * 22)
hours_per_reading = 15 / 60
for idx, site in enumerate(sites):
    hours_above = np.count_nonzero(flows[:, idx] > threshold) * hours_per_reading
    print(f"{site:<12} {hours_above:>10.2f}")

# Creates plot with relevant info
plot_streamflow(dates, flows, sites)

# I used AI to write this code.
# Saves plot to specified file
plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")

# Displays plot
plt.show()
