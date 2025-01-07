# Uber-Data-Insights-Modern-Data-Engineering-on-GCP

# Introduction

The objective of this project is to leverage Google Cloud Platform (GCP) tools and modern data engineering practices to analyze Uber data and extract actionable insights. By utilizing GCP Storage, Python, Compute Instances, Mage Data Pipeline Tool, BigQuery, and Looker Studio, we can build a scalable and efficient data pipeline that processes and visualizes the Uber trip records dataset. This project demonstrates the implementation of a modern data pipeline architecture with an emphasis on data processing, transformation, and visualization.

# Architecture

The data pipeline utilizes a combination of cloud services and technologies to efficiently collect, process, and visualize data:

- Data Ingestion: Uber trip records are stored in GCP Storage and processed using Compute Instances.
- Data Transformation: Mage Data Pipeline Tool (https://www.mage.ai/) is used for creating the ETL pipeline to clean, transform, and load data into BigQuery.
- Data Storage: Transformed data is loaded into BigQuery for advanced analytics and querying.
- Data Visualization: Looker Studio (formerly Google Data Studio) is used to create interactive dashboards for visualizing key metrics like trip durations, distances, fares, and payment methods.
![image](https://github.com/user-attachments/assets/4c03569b-db0e-4965-9ad8-0eb9b8c3da95)

# Technologies Used

- Programming Language: Python
- Google Cloud Platform:
- Google Storage: Data storage for raw Uber trip records.
- Compute Instance: To run processing and transformation tasks.
- BigQuery: Data warehouse for storing transformed data and performing advanced queries.
- Looker Studio: Visualization and reporting tool to create insights from the data.
- Modern Data Pipeline Tool: Mage Data Pipeline – a tool for orchestrating the ETL processes.

# Dataset Used

The dataset used in this project is the TLC Trip Record Data, which consists of records from yellow and green taxis in New York City. The dataset contains the following fields:

- Pick-up and Drop-off Dates/Times: Date and time when the trip starts and ends.
- Pick-up and Drop-off Locations: Geographic coordinates where passengers are picked up and dropped off.
- Trip Distances: Distance traveled during the trip.
- Itemized Fares: Detailed cost breakdown of the trip.
- Rate Types: Type of fare applied (e.g., standard, surge).
- Payment Types: Method of payment used by the passenger.
- Driver-reported Passenger Counts: Number of passengers in the trip.
- You can access the dataset used for this project through the following GitHub link:

# More Information on the Dataset:

1. TLC Trip Record Data Overview: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
2. Data Dictionary: https://www.nyc.gov/assets/tlc/downloads/pdf/data_dictionary_trip_records_yellow.pdf
   
# Data Model

![image](https://github.com/user-attachments/assets/eaccebaf-e67f-4f2a-b52e-5cdceeefb1c4)

https://lucid.app/lucidchart/b4e3831d-6c0c-4ab9-8848-38fe0661d40b/edit?invitationId=inv_6568bf25-a1ef-4fb5-b1f8-4d19f11e29d8

Based on the TLC Trip Record Data, the data model involves transforming and cleaning raw data into a structured format suitable for analytical queries. The key components of the data model include:

This structured model allows easy access to insights like the most popular routes, average trip distances, or peak times for Uber rides.
