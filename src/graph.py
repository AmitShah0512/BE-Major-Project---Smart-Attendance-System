import matplotlib.pyplot as plt #Imports matplotlib plotting module.Used to create charts and graphs.
import matplotlib.dates as mdates #Imports date-handling utilities for matplotlib.Used to format date values on x-axis.
import datetime #Used to work with date and time objects.
import random #Used to randomly shuffle colors for visualization.

# Define project tasks and their durations
tasks = [
    ("Project Discussion", "2025-01-08", "2025-01-14"),
    ("Project Structure Setup", "2025-01-15", "2025-01-21"),
    ("Face Recognition Implementation", "2025-01-22", "2025-02-04"),
    ("GUI Development (Tkinter)", "2025-02-05", "2025-02-18"),
    ("Attendance Management System", "2025-02-19", "2025-03-05"),
    ("Testing and Debugging", "2025-03-06", "2025-03-20"),
    ("Final Report Preparation", "2025-03-21", "2025-03-31"),
]

# Convert date strings to datetime objects. Required because matplotlib works with datetime objects for timelines.
task_names, start_dates, end_dates = zip(*tasks) #Separates task data into three tuples: task_names,start_dates,end_dates.
start_dates = [datetime.datetime.strptime(date, "%Y-%m-%d") for date in start_dates] #Converts each start date string into a datetime object. %Y-%m-%d specifies the date format.
end_dates = [datetime.datetime.strptime(date, "%Y-%m-%d") for date in end_dates] #Converts each end date string into a datetime object.

# Subtracts start date from end date.Extracts number of days.Stores duration for each task
durations = [(end - start).days for start, end in zip(start_dates, end_dates)]

# Define a color palette for tasks
colors = [
    "#ff9999", "#66b3ff", "#99ff99", "#ffcc99", "#c2c2f0", "#ffb3e6", "#ff6666"
]
random.shuffle(colors)  # Randomly rearranges colors.Adds visual variety to chart.

# Create fig -> entire figure,ax -> plotting area(axis).Sets figure size to 12 × 6 inches.
fig, ax = plt.subplots(figsize=(12, 6))

# Plot each task as a horizontal bar
for i, (task, start, duration, color) in enumerate(zip(task_names, start_dates, durations, colors)): #Loops through:,Task name,Start date,Duration,Color. enumerate provides index (not used here)
    ax.barh(task, duration, left=start, color=color, edgecolor="black", alpha=0.8)
    '''
    Draws a horizontal bar
    task → y-axis label
    duration → bar length
    left=start → bar starts from start date
    color=color → bar color
    edgecolor="black" → black border
    alpha=0.8 → slight transparency
    📌 This is the core Gantt chart drawing line.
    '''


# Format x-axis with dates
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=2))  # Shows date ticks every 2 weeks on x-axis
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))  # Format dates as "Jan 08"
plt.xticks(rotation=45, fontsize=10) #Rotates date labels by 45°. Sets font size to 10.

# Add labels and title
plt.xlabel("Timeline", fontsize=12, fontweight="bold") #Labels x-axis
plt.ylabel("Tasks", fontsize=12, fontweight="bold") #Labels y-axis
plt.title("Gantt Chart for Smart Attendance System", fontsize=14, fontweight="bold") #Sets chart title

# Enable grid for better readability
plt.grid(axis="x", linestyle="--", alpha=0.7)

# Adjust layout and show chart
plt.tight_layout()
plt.show()
