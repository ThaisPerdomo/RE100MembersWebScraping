---

# RE100 Members Data Extraction

RE100 is a global initiative where companies commit to using 100% renewable energy to combat climate change and reduce their carbon footprint.

This Python script is tailored to scrape data from the RE100 Members webpage and export it to an Excel file. The script utilizes the BeautifulSoup library for web scraping and pandas for data manipulation.

## Python Version
- 3.11.5

## Requirements

- BeautifulSoup (`bs4`) - 4.12.3
- pandas (`pd`) - 2.1.1
- requests - 2.31.0 
- openpyxl - 3.0.10 

## Installation

You can install the required libraries via pip:

```bash
pip install -r requirements.txt
```

## Usage

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/ThaisPerdomo/RE100MembersWebSraping
    ```

2. **Navigate to the Directory:**

    ```bash
    cd re100-web-scraper
    ```

3. **Run the Script:**

    ```bash
    python scraper.py
    ```

    The script will scrape data from [RE100 Members](https://www.there100.org/re100-members?items_per_page=All) webpage and create an Excel file named `re100_data.xlsx` in the current directory.

## Functionality

The script contains several functions:

1. **`response(url: str) -> requests.models.Response`**

    - Takes a URL as input and returns the response object.

2. **`find_tables(response: requests.models.Response) -> bs4.element.ResultSet`**

    - Takes a response object as input and returns the tables from the response object.

3. **`get_data(table: bs4.element.ResultSet) -> list`**

    - Takes a table as input and returns a list with the data.

4. **`get_columns_name(table: bs4.element.Tag) -> list`**

    - Takes a table as input and returns a list with the columns names.

5. **`create_dataframe(data: list, columns_name: list) -> pd.DataFrame`**

    - Takes the data and column names as input and returns a pandas DataFrame. It also selects the odd rows from the DataFrame.

6. **`create_excel(df: pd.DataFrame) -> None`**

    - Takes a pandas DataFrame as input and creates an Excel file with the data.

7. **`main(url: str) -> pd.DataFrame`**

    - Takes the RE100 Members webpage url as input and returns a pandas DataFrame with the data from the URL, creating an Excel file as an output. 



This will scrape data from the RE100 Members webpage and export it to an Excel file.

---

Feel free to adjust the script according to your requirements or customize it further as needed! Let me know if you have any questions or need further assistance. -- Thais Perdomo

---
