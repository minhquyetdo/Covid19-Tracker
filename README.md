# COVID-19 Case Tracker

## Overview
The COVID-19 Case Tracker is a **data tracker** tool designed to extract and monitor new COVID-19 cases from the national CDC website. \
It provides valuable insights into the total number of new cases reported each day and the new cases in specific cities. \
The tracker utilizes the **Scrapy framework** to scrape and process the data, ensuring accurate and up-to-date information for analysis and tracking.

**Technical features** in this Data Tracker:
|Features| Description |
|:------|-----------:|
|**Web scraping**|Scrapy|
|**Data cleaning and transformation**|XPath|
||CSS Selector|
||Regex|
|**Data Storage**|JSON|

#### Explode the repository 
|Files| Description |
|:------|-----------:|
|what-how-why.txt|Data scrapy document|
|covidcase.py|Source code for data crawler|
|requirements.txt|Requirements Python libraries for virtual environment to run Scrapy|
|sample-results.json|Result for tracking covid case in 2021 May|

## Clone the data warehouse
To create and run the COVID-19 Case Tracker, follow these steps:
#### Requirements and Setting Python Environment

1. Python 3.7 or higher is required.

2. Create a virtual environment (optional but recommended) using your preferred method.

#### Scrapy Installation

1. Change to the project environment (your path to the folder):
```cli
[your venv] activate
```
2. Install Scrapy using pip:
```cli
pip install scrapy
```

3. Install project dependencies:
```cli
pip install -r requirements.txt
```


#### Running the Tracker
Creating the Scrapy Spider:

**Change working directory to the project directory**
```cli
cd covid_tracker
```

**Create a new Scrapy project**
```cli
scrapy startproject covid_tracker
```
**Create a new Spider**
```cli
scrapy genspider covidcase
```
Open the spider file covidcase.py in a text editor.

Configuring the Spider (Optional) (The website may change by time)

Set the allowed domains: allowed_domains = ['covid19.gov.vn']

Specify the start URL: start_urls = ['https://covid19.gov.vn/big-story/cap-nhat-dien-bien-dich-covid-19-moi-nhat-hom-nay-171210901111435028.htm']

**Extracting and Cleaning Data**

In the Spider's parse method, use XPath or CSS selectors to extract the relevant data from the response.

Apply filters and cleaning operations as necessary, such as removing unwanted characters, converting data types, or handling missing values.

Create a dictionary or data structure to store the extracted and cleaned data.

Storing Data in JSON Format:

In the Spider's parse method, after processing the data, convert the data structure into JSON format.

Write the JSON data to a file using Python's json module or any other preferred JSON library.

**Running the Spider**

Open a terminal and navigate to the project directory.
Run the Spider
```cli
scrapy crawl covidcase -o [your_path]/newcases.json
```

**Handling Pagination**

If the CDC website has multiple pages for tracking new cases, implement pagination logic in the Spider to follow the next page links and continue extracting data until there are no more pages.

**Scheduling and Automation**

Use tools like cron (Unix) or Task Scheduler (Windows) to schedule the Spider's execution at specific intervals automatically.

**Error Handling and Logging**

Implement error handling mechanisms to handle any exceptions or errors that may occur during the data extraction process.

Utilize Scrapy's logging capabilities to log important events, errors, or warnings for better troubleshooting.

## Contributions
Contributions to the COVID-19 Case Tracker project are welcome. If you encounter any issues, feel free to open an issue in the repository. You can also submit pull requests with improvements, bug fixes, or additional features.

Please ensure you adhere to the license terms when using or modifying this project.
