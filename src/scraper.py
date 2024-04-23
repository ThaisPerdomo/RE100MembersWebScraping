import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests

def response(url: str) -> requests.models.Response:

    """
    
    This function takes a url as input and returns the response object. 

    Parameters:
    url (str): The url to extract data from.

    Returns:
    response (requests.models.Response): The response object.

    """

    response = requests.get(url)
    return response


def find_tables(response: requests.models.Response) -> bs4.element.ResultSet:

    """
    
    This function takes a response object as input and returns the tables from the response object. 

    Parameters:
    response (requests.models.Response): The response object.

    Returns:
    tables (bs4.element.ResultSet): The tables from the response object.

    """

    soup = BeautifulSoup(response.text, 'html.parser')

    tables = soup.find('table')

    return tables

def get_data(table: bs4.element.ResultSet) -> list:

    """

    This function takes the table as input and returns a list with the data.

    Parameters:
    table (bs4.element.ResultSet): The table to extract data from.

    Returns:
    data (list): The list with the data.

    """

    data = []
    # Itera sobre todas as linhas da tabela
    for row in table.find_all('tr'):
        
        # Encontra todas as células (td) na linha
        cells = row.find_all('td')
        
        # Verifica se a linha não está vazia
        if cells:
            # Inicializa uma lista vazia para armazenar os dados da linha
            row_data = []
            
            # Itera sobre todas as células na linha
            for cell in cells:
                
                if cell.get('headers') == ['view-field-increased-ambition-table-column']:

                    # aqui, se ela tiver um elemento svg, vamos adicionar 'V' na lista de dados da linha: 
                    if cell.find('svg'):
                        row_data.append('V')
                    # se não, vamos deixar vazio: 
                    else:
                        row_data.append('')                
                else:
                # Extrai o texto de cada célula e remove espaços em branco, adicionando à lista de dados da linha
                    row_data.append(cell.text.strip())
            
            # Adiciona os dados da linha à lista de dados
            data.append(row_data)

    return data


def get_columns_name(table: bs4.element.Tag) -> list:

    """

    This function takes the table as input and returns a list with the columns names.

    Parameters:
    table (bs4.element.Tag): The table to extract data from.

    Returns:
    columns_name (list): The list with the columns names.

    """

    first_row = table.find('tr')

    columns_name = []

    header_elements = first_row.find_all('th')

    for header in header_elements:
        # Extrair o texto do elemento e remover espaços em branco extras
        header_text = header.text.strip()
    
        # Adicionar o nome da coluna à lista de cabeçalhos
        columns_name.append(header_text)

    return columns_name


def create_dataframe(data: list, columns_name: list) -> pd.DataFrame:

    """

    This function takes the data and columns names as input and returns a pandas DataFrame. 
    Also selects the odd rows from the DataFrame.

    Parameters:
    data (list): The data to extract.
    columns_name (list): The columns names.

    Returns:
    df (pd.DataFrame): The DataFrame with the data.

    """

    df = pd.DataFrame(data, columns=columns_name)

    odd_rows = df.iloc[::2]

    odd_rows.reset_index(drop=True, inplace=True)

    return odd_rows

def create_excel(df: pd.DataFrame) -> None:
    
    """

    This function takes a pandas DataFrame as input and creates an Excel file with the data.

    Parameters:
    df (pd.DataFrame): The DataFrame with the data.

    """

    df.to_excel('re100_data.xlsx', index=False)

    return None

def main(url: str) -> pd.DataFrame:
    
    """

    This function takes a url as input and returns a pandas DataFrame with the data from the url.

    Parameters:
    url (str): The url to extract data from.

    Returns:
    df (pd.DataFrame): The DataFrame with the data.

    """

    response_object = response(url)

    tables = find_tables(response_object)

    data = get_data(tables)

    columns_name = get_columns_name(tables)

    df = create_dataframe(data, columns_name)

    create_excel(df)

    return df

if __name__ == '__main__':

    url = 'https://www.there100.org/re100-members?items_per_page=All'

    main(url)