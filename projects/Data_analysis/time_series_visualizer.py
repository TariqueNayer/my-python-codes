import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv")
df["date"] = pd.to_datetime(df['date'], format= "%Y-%m-%d")
print(df["date"].head())
df = df.set_index("date")
print(df.head())
# Clean data
lower = df["value"].quantile(0.025)
higher = df["value"].quantile(0.975)

df = df[(df["value"] >= lower) & (df["value"] <= higher)]
print(df.head())

month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun','Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
def draw_line_plot():
    # Draw line plot
    ax = df.plot(kind="line",y="value",color="red",figsize=(14,4),linewidth=1.0)
    ax.set(xlabel="Date",ylabel="Page Views",title="Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    fig = ax.get_figure()



    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy(deep=True)
    df_bar.reset_index(inplace=True)
    df_bar['year'] = [d.year for d in df_bar.date]
    df_bar['month'] = [d.strftime('%b') for d in df_bar.date]
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    df_bar = df_bar[month]
    # Draw bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    df_bar.plot(kind="bar",ax=ax, width=0.8)

    # Editing the plot
    ax.set_xlabel("Years",fontsize=12)
    ax.set_ylabel("Average Page Views",fontsize=12)
    ax.set_ylim(0, 160000)
    ax.legend(title="Months", loc="upper left")
    plt.xticks(rotation=45, ha='right') 
    plt.tight_layout()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, (ax1,ax2) = plt.subplots(1, 2, figsize=(24, 10))
    sns.boxplot(data=df_box,x="year",y="value",ax=ax1, width=0.6, palette="deep")
    ax1.set_title("Year-wise Box Plot (Trend)",fontsize=14, pad=20)
    ax1.set_ylabel("Page Views", fontsize=12)
    ax1.set_xlabel('Year', fontsize=12)
    ax1.set_ylim(0, 200000)
    ax1.tick_params(labelsize=12)

    sns.boxplot(data=df_box,x="month",y="value",order=month, ax=ax2, width=0.6, palette="deep")
    ax2.set_title("Month-wise Box Plot (Seasonality)",fontsize=14, pad=20)
    ax2.set_ylabel("Page Views", fontsize=12)
    ax2.set_xlabel('Month', fontsize=12)
    ax2.set_xticklabels(month, rotation=45, ha='right')

    plt.tight_layout(pad=4)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
draw_bar_plot()
draw_box_plot()