# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib.dates as mdates


# I used AI to write this code and learn how it works

# Load file, extract data, and format data as a string
data = np.loadtxt("June-2021-Provo-River-Streamflow-Rates.csv", delimiter=",", skiprows=1, dtype=str)

# Split up data by column and insert into variables
# Turn parts of data into floats and integers
x = data[:, 0]
y_1 = data[:, 1].astype(float)
y_2 = data[:, 2].astype(int)
y_3 = data[:, 3].astype(int)
y_4 = data[:, 4].astype(float)
y_5 = data[:, 5].astype(float)

# I used AI to write this code and learn how it works

# Set plot size
plt.figure(figsize=(8, 6))

# plot and label relevent data
plt.plot(x, y_1, color='purple', label='10163000')
plt.plot(x, y_2, color='teal', label='10155200')
plt.plot(x, y_3, color='green', label='10155500')
plt.plot(x, y_4, color='orange', label='10154200')
plt.plot(x, y_5, color='red', label='10155000')

# Convert dates from file into date format inside the code
dt_dates = [datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S') for d in x]

# Determine dates for x-axis that are 4 days apart
tick_indices = []
previous_day = 0
for idx in range(len(dt_dates)):
    dt = dt_dates[idx]
    day_num = dt.day
    if (day_num - 1) % 4 == 0 and day_num != previous_day:
        tick_indices.append(idx)
        previous_day = day_num

# Format dates in x-axis to have year, month, day
tick_positions = [x[i] for i in tick_indices]
tick_labels = [dt_dates[i].strftime('%Y-%m-%d') for i in tick_indices]

# Place dates in axis at an angle
plt.xticks(tick_positions, tick_labels, rotation=45)

# Insert chart labels
plt.title('Provo River Streamflow Data (2021)')
plt.xlabel('Date')
plt.ylabel('Flowrate (cfs)')
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend(title='site numbers')
plt.tight_layout()

# Show chart
plt.show()
