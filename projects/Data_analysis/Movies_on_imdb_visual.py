import matplotlib.pyplot as plt
import pandas as pd
import seaborn as  sns
import sqlite3 as sq
import matplotlib.ticker as ticker

# Connect to the movies SQLite Database.
conn = sq.connect("movies.sqlite")

# Getting the full information and storing it on a Excel sheet to review later.
full_df = pd.read_sql("SELECT  movies.title, movies.release_date, movies.budget, movies.vote_count, movies.vote_average, movies.revenue, directors.name AS director_name FROM movies JOIN directors ON movies.director_id = directors.id;",conn)
full_df["release_date"] = pd.to_datetime(full_df["release_date"])

full_df.to_excel("Movies_from_1920s_to_2016.xlsx",index=False, engine="openpyxl")




# Bar chart for the most successful director.
def director_bar(d_id : int):
    """Get a bar chart of the revenues of movies directed by a specific director."""
    # get the data.
    d_id = str(d_id)
    qrr = f"SELECT d.name AS director_name, m.title, m.revenue FROM movies m JOIN directors d ON m.director_id = d.id WHERE d.id = {d_id};"
    movies = pd.read_sql(qrr,conn)
    name_query = f"SELECT name FROM directors WHERE id = {d_id};"
    d_name = pd.read_sql(name_query, conn).loc[0, 'name']

    # Plot the figure and style the figure.
    sns.set_theme(style="whitegrid")
    fig, ax = plt.subplots(figsize=(12, 5))
    
    # the plot
    sns.barplot(data=movies, x='title', y='revenue', ax=ax, palette='Blues_d', edgecolor='black')
    ax.tick_params(axis='both', labelsize=8)

    # Using matplotlib.ticker to format the axis to show the complete value.
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))

    # Making apropriate labels.
    ax.set_xlabel("Revenue")
    ax.set_ylabel("titles")
    ax.set_title(f"The directed movies and their revenue by {d_name}")

     
    # optionally can rotate the x-axis ticks. (just uncomment the line below)
    #plt.xticks(rotation=25, ha='right')

    # save the figure.
    plt.savefig(f"figure_{d_name}.png")
    plt.show()

    # Compare plot to compare a films budget and revenue.
def movie_prf(name):
    """Get a line chart of a movie's budget and revenue to find out how much profit/loss its made."""
    if data.empty:
        print(f"Movie '{name}' not found.")
        return
    # Getting data.
    name = name.capitalize()
    data = full_df.loc[full_df['title'] == name, ['revenue', 'budget']]
    revenue = data.at[0, 'revenue']
    budget = data.at[0, 'budget']
    result = revenue - budget
    if result > budget: outcome = 'Profit' 
    else: outcome = 'Loss'


    # Plotting Time!
    sns.set_theme(style="darkgrid")
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.bar(['Budget','Revenue'], [budget,revenue])
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: f'{int(x):,}'))
    plt.show()

# Gotta close the connection to the Databae.
conn.close()
if __name__ == "__main__":
    director_bar(4762)
    movie_prf('Avatar')
