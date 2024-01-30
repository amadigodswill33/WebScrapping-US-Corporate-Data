# Web Scraping Wikipedia for List of Largest Companies in the United States by Revenue
![PythonWebScraper](https://github.com/amadigodswill33/WebScrapping-US-Corporate-Data/assets/94016023/5c12caea-a83f-4503-a43e-351a815480f9)

This project involves scraping data from the Wikipedia page that lists the largest companies in the United States by revenue. The Python script utilizes the `requests`, `BeautifulSoup`, and `pandas` libraries to fetch, parse, and organize the data into a Pandas DataFrame, which is then saved as a CSV file.

## Table of Contents

- [Overview](#overview)
- [Dependencies](#dependencies)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Output](#output)
- [Notes](#notes)
---
## Overview

```python
import requests
from bs4 import BeautifulSoup

# Define the URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

# Fetch the HTML content of the page
page = requests.get(url)

# Create BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(page.text, 'html.parser')

# Print the parsed HTML content (optional)
print(soup)

# Extract the table containing the relevant information
table = soup.find_all('table')[1]
soup.find_all('table', class_='wikitable sortable')

# Extract the table headers (column titles)
world_title = table.find_all('th')
print(world_title)

# Extract text from the table headers
world_table_title = [title.text.strip() for title in world_title]
print(world_table_title)

# Create an empty DataFrame with column names
df = pd.DataFrame(columns=world_table_title)
print(df)

# Extract data rows from the table
column_data = table.find_all('tr')
print(column_data)

# Iterate through each row and extract cell data
for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    print(individual_row_data)

    # Append the row data to the DataFrame
    length = len(df)
    df.loc[length] = individual_row_data

# Display the final DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv(r'C:\Users\User\Desktop\My_DataSet\ScrapedProject_companies.csv', index=False)
```
---
## Usage
### 1. Clone the repository:

```git clone https://github.com/your-username/your-repository.git
cd your-repository
```
### 2. Open the script (script.py) and make the following adjustments:

Replace the 'url' variable with the target Wikipedia page URL if needed.
Adjust the output CSV file path in the 'df.to_csv()' line.
Run the script:

```python script.py
```
---
## Code Structure
The script's main components include fetching HTML, parsing with BeautifulSoup, extracting relevant data, creating a Pandas DataFrame, and saving the data as a CSV file.
---
## Output
The script will generate a CSV file (ScrapedProject_companies.csv) containing the scraped data.

![Webscrapping_Health_Dataset](https://github.com/amadigodswill33/WebScrapping-US-Corporate-Data/assets/94016023/7ad16c8a-62a7-48e4-ae22-a7eaf6542178)

---
## Notes
Customize the script according to your needs, such as adjusting the output CSV file path.
Be cautious of potential changes in the HTML structure of the Wikipedia page.
Feel free to contribute, report issues, or suggest improvements!
