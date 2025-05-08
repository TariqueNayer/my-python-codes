# This finds the top rated movies of any year. 


import pandas as pd


def top_movies(*,year,num):
    db = pd.read_csv("2025 Top rated Movies.csv")
    db.set_index("index",inplace=True)
    db["release_date"] = pd.to_datetime(db["release_date"])
    db['year'] = db['release_date'].dt.year
    # get the top movies.
    top = db.loc[db["year"] == year,["title","vote_average"]].sort_values(by="vote_average",ascending=False).head(num)
    top = top.rename(columns={'vote_average': 'rating'})
    return top

if __name__ == "__main__":
    y = int(input("what year's best movies do you want? (1902 to 2025) "))
    n = int(input("how long should be the list? "))
    print(top_movies(year=y,num=n))

