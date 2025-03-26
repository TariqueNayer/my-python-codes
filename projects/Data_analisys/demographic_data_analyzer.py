import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    races = df['race'].unique()
    race_countlst = {}
    for race in races:
        vals = df.loc[df["race"] == race]
        num = len(vals)
        race_countlst.update({race : num})
    race_count = pd.Series(race_countlst.values())
    race_count.index = race_countlst.keys()

    # What is the average age of men?
    age_of_men = df.loc[df["sex"] == "Male","age"]
    average_age_men = round(age_of_men.mean(),1)
    # What is the percentage of people who have a Bachelor's degree?
    edu = df["education"]
    batch = df.loc[df["education"] == "Bachelors","education"]
    percentage_bachelors = round((batch.size / edu.size) * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    advcd = df.loc[(df["education"] == "Bachelors") | (df["education"] == "Masters") | (df["education"] == "Doctorate"),"salary"]
    more_t50k_a = advcd[advcd == ">50K"]
    lowr = df.loc[~(df["education"] == "Bachelors") & ~(df["education"] == "Masters") & ~(df["education"] == "Doctorate"),"salary"]
    more_t50k_l = lowr[(lowr == ">50K")]
    
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # percentage with salary >50K
    higher_education_rich = round((more_t50k_a.size / advcd.size) * 100,1)
    lower_education_rich = round((more_t50k_l.size / lowr.size) * 100,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_worker = df["hours-per-week"]
    min_work_hours = min_worker.min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df["hours-per-week"] == 1,["hours-per-week","salary"]]
    rich_mini = num_min_workers.loc[num_min_workers["salary"] == ">50K"]
    rich_percentage = rich_mini.size / num_min_workers.size * 100

    # What country has the highest percentage of people that earn >50K?
    contries = df["native-country"].unique()
    con_data = dict()
    
    for contry in contries:
        contry_all = df.loc[(df["native-country"] == contry),"salary"]
        data = df.loc[(df["salary"] == ">50K") & (df["native-country"] == contry),"salary"]
        con_data.update({contry : (data.size/contry_all.size) * 100})
    ky = con_data.keys()
    maxk = max(ky, key=con_data.get)
    maxv = con_data[maxk]
    highest_earning_country = maxk
    highest_earning_country_percentage = round(maxv,1)

    # Identify the most popular occupation for those who earn >50K in India.
    indian_occ = df.loc[df["native-country"] == "India", "occupation"]
    top_IN_occupation = indian_occ.value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
if __name__ == "__main__":
    calculate_demographic_data()