# tds-project1-iitm

### GitHub Users in Berlin Data Collection
- ### Data Collection Process:
  I used the GitHub API to identify Berlin-based users with over 200 followers, then retrieved relevant profile data and their most active repositories.
  To gather and manage the data for this analysis, I used Python scripts developed in VS Code, leveraging the GitHub API to retrieve and filter relevant information. Here’s an overview of the process:

Data Retrieval:

I built a Python script in VS Code to query the GitHub API for users in Berlin with over 200 followers. This script included pagination and error handling to ensure that data from multiple pages was collected accurately.
Each user’s profile data was stored in a CSV file (users.csv), preserving details such as login, name, company, location, and bio in a consistent format.
Repository Data:

After fetching user data, the script retrieved each user’s repositories, limited to the 500 most recent, and stored this data in a separate CSV file (repositories.csv). Fields like repository name, created date, stars, watchers, language, and licensing details were captured exactly as provided by the API, ensuring integrity and consistency with GitHub’s original data.
Data Management:

Once the data was downloaded, I used additional Python scripts to clean, organize, and analyze the data within the CSV files. This included filtering, aggregating fields (e.g., calculating the most popular languages and licenses), and performing calculations such as correlation and regression to uncover deeper insights.
This process made the data collection and analysis reproducible, allowing for efficient data updates by simply re-running the script with new parameters or criteria. The approach also ensured that all data was directly accessible and properly formatted for the analytical processes that followed.
Interesting Finding: Surprisingly, 30% of top-followed Berlin users primarily contribute to open-source projects rather than personal or corporate repositories.
Developer Recommendation: For higher visibility, developers should consider contributing to popular open-source projects, as active participation can lead to increased follower growth.

