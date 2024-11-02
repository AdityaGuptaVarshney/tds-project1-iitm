import pandas as pd

# Load the users data
users_df = pd.read_csv('users.csv')

# Convert the 'created_at' column to datetime format
users_df['created_at'] = pd.to_datetime(users_df['created_at'])

# Sort by 'created_at' in ascending order
sorted_users = users_df.sort_values(by='created_at').head(5)

# Get the 'login' column in a comma-separated list
earliest_users = ','.join(sorted_users['login'])
print(earliest_users)
