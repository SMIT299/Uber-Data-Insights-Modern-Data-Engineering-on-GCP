from mage_ai.data_preparation.repo_manager import get_repo_path
from mage_ai.io.bigquery import BigQuery
from mage_ai.io.config import ConfigFileLoader
from pandas import DataFrame
from os import path

# Ensure that the data_exporter module is only imported once
if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    """
    Export data to Google BigQuery from the Mage AI data pipeline.

    This function retrieves data from the pipeline, loads the configuration from 
    the 'io_config.yaml' file, and exports each data item to a specific BigQuery table.

    Configuration settings such as project, dataset, and table names are managed in 
    the 'io_config.yaml' file, enabling environment-specific configurations. The 
    function assumes the tables to be replaced if they already exist (with the 'replace' 
    policy specified).

    Parameters:
    -----------
    data : dict
        A dictionary where keys represent the data labels and values represent 
        the corresponding data frames that need to be exported to BigQuery.
    
    kwargs : keyword arguments
        Additional parameters to customize the export behavior (e.g., logging, error handling, etc.)

    Returns:
    --------
    None
        This function doesn't return any value; it performs the data export to BigQuery.
    
    Example Usage:
    --------------
    data = {
        'sales_data': df_sales,
        'customer_data': df_customers
    }
    export_data_to_big_query(data)
    
    Documentation:
    --------------
    For more details on BigQuery export options, refer to:
    https://docs.mage.ai/design/data-loading#bigquery
    """
    
    # Get the absolute path to the repository and load the config file
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'  # Use the default profile for configuration loading

    # Loop through each data entry and export it to BigQuery
    for key, value in data.items():
        # Construct the target table name for BigQuery using the key from the data dictionary
        table_id = 'data-with-smit.uber_data_engineering_yt.{}'.format(key)
        
        # Configure BigQuery export using the settings defined in the YAML config file
        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            DataFrame(value),  # Convert the value to a pandas DataFrame before exporting
            table_id,  # Specify the target BigQuery table
            if_exists='replace',  # Replace the table if it already exists
        )

