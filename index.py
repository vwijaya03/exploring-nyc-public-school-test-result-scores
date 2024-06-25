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