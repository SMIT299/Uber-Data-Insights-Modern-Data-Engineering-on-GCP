import io
import pandas as pd
import requests

# Import necessary decorators if not already imported
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Loads a CSV file from a public API endpoint and returns it as a pandas DataFrame.
    
    Fetches the CSV file stored on Google Cloud Storage and converts it into 
    a DataFrame for downstream processing in the pipeline.
    """
    url = 'https://storage.googleapis.com/uber-data-engineering-project-smit/uber_data.csv'
    
    # Request the CSV data from the API
    response = requests.get(url)

    # Convert the CSV content into a pandas DataFrame
    return pd.read_csv(io.StringIO(response.text), sep=',')


@test
def test_output(output, *args) -> None:
    """
    Validates that the output of the data loader is not None.
    
    Ensures that data was successfully loaded before moving to the next step in the pipeline.
    """
    # Raise an error if no data is returned
    assert output is not None, 'The output is undefined'
