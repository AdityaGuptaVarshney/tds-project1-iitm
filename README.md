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

### Interesting Finding

Here are some interesting insights and facts derived from your analysis of GitHub users in Berlin:

Top Influencers by Followers:

The users with the highest follower counts include developers such as tiangolo, schacon, rwieruch, shuding, and android10. This showcases a blend of creators and influential contributors, many of whom maintain popular repositories and frequently engage with the developer community.
Veteran Developers:

The earliest GitHub adopters among Berlin developers—like schacon, adamwiggins, and lstoll—are long-time GitHub users who registered over a decade ago. Their early adoption is reflected in their high engagement and often prominent roles within the community.
Popular Technologies:

JavaScript emerged as the most popular language among Berlin-based GitHub users, likely due to its widespread application in web development. Surprisingly, Shell was the second-most popular language for users who joined after 2020, indicating a growing interest in automation, scripting, and DevOps-related skills among newer developers.
Corporate Affiliation:

Microsoft has become the most common employer among top GitHub users in Berlin, reflecting its significant investment in the open-source community and its active recruitment of developers well-versed in collaborative development.
Repository and Project Preferences:

There is a positive correlation (0.401) between users enabling project and wiki features together, which suggests that many developers use GitHub’s collaborative tools in tandem for documentation and project management.
Hireability and Engagement:

Users who list themselves as "hireable" tend to follow an average of 46.136 more people compared to non-hireable users, indicating a greater degree of networking among those open to new job opportunities. Interestingly, there is no significant difference in the likelihood of hireable users sharing their email addresses.
Impact of Bio Length on Followers:

While the initial assumption might be that longer bios would correlate with more followers, the regression analysis suggests only a modest effect (if any) on follower count with increasing bio length. Developers may instead attract followers through active project contributions and repository quality rather than detailed bios.
Weekend Warriors:

The most prolific weekend coders include users such as janpio, derhuerst, and saschanaz, who tend to push code on weekends. This indicates a high level of dedication or side project involvement, often a characteristic of passionate open-source contributors.
These findings provide a fascinating snapshot of Berlin's GitHub community. From JavaScript dominance to Microsoft’s influence, these insights can guide developers seeking to grow their own influence by focusing on languages like JavaScript, actively contributing to open-source, or networking with like-minded developers.

### Developer Recommendations for Data Formatting and CSV Management

Standardize Boolean Values:

Ensure consistency in CSV files by converting True to true and False to false. In Python, you can achieve this by converting Boolean fields to lowercase strings when writing to the CSV file:
python
Copy code
boolean_field = str(boolean_value).lower()
Automate this within your data-processing functions to ensure consistent results across all entries.
CSV File Format Validation:

Double-check that the CSV format aligns with required specifications: each field should be separated by commas without extra spaces, and missing values should appear as empty strings (""), not null or other placeholders.
Using Python’s csv module with proper settings (quotechar and escapechar where needed) can help avoid formatting issues:
python
Copy code
import csv
with open('filename.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'field': 'value'})
Avoid Data Duplication:

In large datasets, avoid redundant data by carefully filtering what you collect and save. For example, store only essential fields for each user or repository entry. This makes CSV files cleaner, smaller, and easier to manage.
Field Naming Consistency:

Maintain consistent naming conventions for CSV headers (e.g., snake_case). This is critical, as inconsistent naming can complicate data handling and cause issues when importing CSV data for further analysis.
Encoding and Line Endings:

Save CSV files in UTF-8 encoding to prevent errors with special characters, and use universal line endings (\n) to avoid compatibility issues across different operating systems.
Review and Clean CSVs with VS Code:

VS Code provides extensions like Excel Viewer or CSV to Table that make it easy to review and edit CSV files directly, ensuring fields and values are aligned and correctly formatted.
Test Data Quality with Sample Reads:

Test CSV files by reading them back into Python or another tool to confirm the data's integrity. By loading a few entries and verifying types and values, you can confirm that booleans, dates, and numbers are stored as intended:
python
Copy code
import pandas as pd
data = pd.read_csv('filename.csv')
print(data.head())
Following these best practices ensures that your CSV files are consistent, readable, and compatible with other tools, making data analysis and sharing with teammates straightforward and reliable.

