import os
from urllib.request import urlretrieve
import pandas as pd

Fremont_URL = 'https://data.seattle.gov/api/views/65db-xm6k/rows.csv?accessType=DOWNLOAD'


def get_fremont_data(filename='Fremont.csv', url=Fremont_URL, force_download=False):
    """Download and cache the fremont data
    Parameters:
    --------
    filename: string (optional)
        location to safe the data
    url: string (optional)
        weblocation of the data
    force_download: bool (optional)
        if True, force redownload of data
    Returns:
    --------
    data: pandas.DataFrame
        The fremont bridge data
    """
    
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('Fremont.csv', index_col='Date')
    try:
        data.index=pd.to_datetime(data.index, format='%m/%d/%Y %I:%M:%S %p')
        "Source: https://strftime.org/"
    except TypeError:
        data.index=pd.to_datetime(data.index)
    data.columns = ['Total', 'West', 'East']
    return data