# Re-run this cell 
import pandas as pd

# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Start coding here...
# Add as many cells as you like...

filter_best_math_80_percent = schools[schools['average_math'] >= (800 * (80 / 100))]
best_math_schools = filter_best_math_80_percent[['school_name', 'average_math']].sort_values('average_math', ascending=False)

schools['total_SAT'] = schools['average_math'] + schools['average_reading'] + schools['average_writing']
top_10_schools = schools[['school_name', 'total_SAT']].sort_values('total_SAT', ascending=False).head(10)

# Preview the data
# schools.head()

# borough_max_std_dev = schools.groupby(['borough'])['total_SAT'].std().idxmax()
# num_schools_in_borough = schools.groupby('borough')['school_name'].nunique()
# average_SAT = schools['total_SAT'].mean()
# std_SAT = schools['total_SAT'].std()

# largest_std_dev = pd.DataFrame({
#     'borough': [borough_max_std_dev],
#     'num_schools': [num_schools_in_borough],
#     'average_SAT': [average_SAT],
#     'std_SAT': [std_SAT]
# })

boroughs = schools.groupby("borough")["total_SAT"].agg(["count", "mean", "std"]).round(2)

largest_std_dev = boroughs[boroughs["std"] == boroughs["std"].max()]

# Rename the columns for clarity
largest_std_dev = largest_std_dev.rename(columns={"count": "num_schools", "mean": "average_SAT", "std": "std_SAT"})

# Optional: Move borough from index to column
largest_std_dev.reset_index(inplace=True)
                            
print(
    largest_std_dev
)