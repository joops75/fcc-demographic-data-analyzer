import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = df['age'][df['sex'] == 'Male'].mean()

    # What is the percentage of people who have a Bachelor's degree?
    edu_vals = df['education'].value_counts()
    percentage_bachelors = 100 * edu_vals['Bachelors'] / edu_vals.sum()

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    higher_education_query = df.query("education == ['Bachelors', 'Masters', 'Doctorate']")

    higher_education_rich_query = higher_education_query.query("salary == '>50K'")

    higher_education_rich = 100 * len(higher_education_rich_query) / len(higher_education_query)

    # What percentage of people without advanced education make more than 50K?
    lower_education_query = df.query("education != ['Bachelors', 'Masters', 'Doctorate']")

    lower_education_rich_query = lower_education_query.query("salary == '>50K'")

    lower_education_rich = 100 * len(lower_education_rich_query) / len(lower_education_query)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers_query = df.loc[df['hours-per-week'] == min_work_hours]

    min_workers_rich_query = min_workers_query.loc[df['salary'] == '>50K']
    
    rich_percentage = 100 * len(min_workers_rich_query) / len(min_workers_query)

    # What country has the highest percentage of people that earn >50K?
    countries = df['native-country'].unique()
    
    country_earnings_data = df[['native-country', 'salary']].value_counts()
    
    highest_earning_country = ''
    highest_earning_country_percentage = 0
    
    for country in countries:
      try:
        low_earnings_count = country_earnings_data[country]['<=50K']
      except:
        low_earnings_count = 0

      try:
        high_earnings_count = country_earnings_data[country]['>50K']
      except:
        high_earnings_count = 0

      high_earnings_percentage = 100 * high_earnings_count / (low_earnings_count + high_earnings_count)

      if high_earnings_percentage > highest_earning_country_percentage:
        highest_earning_country_percentage = (high_earnings_percentage)
        highest_earning_country = country

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df.query("`native-country` == 'India' & salary == '>50K'")['occupation'].value_counts().idxmax()
    
    # also works:
    # top_IN_occupation = df[['native-country', 'salary', 'occupation']].value_counts()['India']['>50K'].idxmax()

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
