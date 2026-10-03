# Example - Fitness Tracking in Your Vault

**The point:** fitness data is a time series that pays off when you can look at a long window. Export the raw data from your tracker, drop it in the vault, and let the agent plus a short python script surface the patterns.

---

## The pattern

1. Export your activity CSV from Garmin, Strava, Fitbit, or Apple Health (any export that lands as a CSV).
2. Drop the file in `07-Attachments/fitness/YYYY-MM-DD_activities.csv`.
3. Write a short note in `04-Areas/Health/Fitness_Tracker.md` that references the data.
4. Run a python script to generate charts and summaries. Save the output image back to `07-Attachments/fitness/`.
5. The agent reads the summary note monthly and surfaces trends.

---

## Chart 1 - Weekly steps line chart

What you are looking at: steps per day aggregated by week, with annotations for weeks that stood out. The value is not the chart itself. It is the three-month view that catches a decline you did not notice.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('07-Attachments/fitness/activities.csv', parse_dates=['date'])
weekly = df.set_index('date')['steps'].resample('W').sum()

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(weekly.index, weekly.values, linewidth=2)
ax.set_title('Weekly steps')
ax.set_ylabel('Steps')
ax.grid(True, alpha=0.3)

# Annotate the low weeks
threshold = weekly.quantile(0.2)
for date, value in weekly.items():
    if value < threshold:
        ax.annotate('low week', xy=(date, value), xytext=(0, -15),
                    textcoords='offset points', fontsize=8, ha='center')

plt.tight_layout()
plt.savefig('07-Attachments/fitness/weekly_steps.png', dpi=120)
```

Save that script as `99-System/scripts/weekly_steps.py`. Run it monthly. Review the output.

---

## Chart 2 - Activity type pie chart

What you are looking at: how your time breaks down across activity types over a given window. Catches the "I thought I was doing variety but I was just running" pattern.

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('07-Attachments/fitness/activities.csv')
counts = df['activity_type'].value_counts()

fig, ax = plt.subplots(figsize=(6, 6))
ax.pie(counts.values, labels=counts.index, autopct='%1.0f%%', startangle=90)
ax.set_title('Activity mix - last 90 days')

plt.tight_layout()
plt.savefig('07-Attachments/fitness/activity_mix.png', dpi=120)
```

---

## The retrospective value

Charts you look at once are low value. Charts you look at every month, next to the previous month's chart, are where the pattern work happens. "I keep saying I will add strength work. The pie chart says I have added strength work three times in six months." That is a decision you can act on.

Hand the vault to the agent monthly:

```
Read 04-Areas/Health/Fitness_Tracker.md and look at the last three monthly charts
in 07-Attachments/fitness/. Write a 5-bullet summary:
1. Trend direction (up, down, flat)
2. Variety trend
3. Any week that stood out and why
4. One honest observation about what I said I would do versus what I did
5. One concrete suggestion for next month
```

The agent is not a coach. It is a mirror. Pattern surfacing. You decide what to do with the signal.

<!-- Source: github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain -->
---
_Part of the obsidian-second-brain template. [Fork on GitHub](https://github.com/Emanuel-Walker/cyber-portfolio/tree/main/06-obsidian-second-brain). Credit appreciated, not required._
