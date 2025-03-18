# Otomoto-Scraper

Otomoto-Scraper is a Python-based tool designed to extract data from the Otomoto website, a popular platform for automotive listings. This scraper alows the user to conduct research on the used cars market.

## Features

- **Data Extraction**: Scrapes detailed information about vehicles, including make, model, year, price, mileage, and more.
- **Automation**: Automates the data collection process, saving time and reducing manual effort.
- **Customizable**: Allows users to specify search criteria to tailor the scraping process to their needs.
- **Result Display**: Provides the user with visual displays of the collected data.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/WiktorKarnia/Otomoto-Scraper.git
   cd Otomoto-Scraper
   ```
   

2. **Install Dependencies**:

   Ensure you have Python installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Environment**:

   Run the installation script:

   ```bash
   ./install.sh
   ```
## Usage

1. **Run the Scraper**:

   Execute the main scraping script:

   ```bash
   cd otomoto_scraper
   scrapy crawl otomoto_spider
   ```

   This will initiate the scraping process.

2. **Access the Data**:

   The scraped data will be saved in a specified output file or directory, as defined in the script's settings.

3. **Visualize the Data**

   The scraped thata may be displayed in form of different charts showing important information about the used car market.
   
     ```bash
     cd statistics
     python cars_counter.py
      ```
