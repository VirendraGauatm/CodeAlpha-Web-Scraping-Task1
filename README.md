# CodeAlpha Data Analytics Internship

## Project: Books Data Analysis

This project was completed as part of the CodeAlpha Data Analytics Internship. It involves web scraping, exploratory data analysis (EDA), and data visualization using Python.

## Project Objectives

- Collect book information from a website using web scraping.
- Clean and explore the collected dataset.
- Analyze book prices, ratings, and availability.
- Create visualizations to communicate findings.

## Technologies Used

- Python
- Pandas
- Requests
- BeautifulSoup
- Matplotlib

## Dataset Information

**Website:** https://books.toscrape.com/

- Pages scraped: 5
- Total books collected: 100
- Total columns: 4

### Data Collected

| Column | Description |
|---|---|
| Title | Book title |
| Price | Book price in GBP |
| Rating | Book rating |
| Availability | Stock availability |

## Task 1: Web Scraping

Used Python Requests and BeautifulSoup to scrape book information from the Books to Scrape website.

**Results:**
- Successfully scraped 100 books.
- Collected four attributes for each book.
- Exported the dataset to `books_data.csv`.
- No missing values were found.

## Task 2: Exploratory Data Analysis (EDA)

Used Pandas to explore the dataset and identify important patterns.

**Key Findings:**
- Total records: 100
- Missing values: 0
- Duplicate rows: 0
- Average book price: £34.56
- Highest book price: £58.11
- Lowest book price: £10.16
- Detected outliers using the IQR method: 0

**Additional Analysis:**
- Book rating distribution
- Average price by rating
- Book availability
- Price statistics

## Task 3: Data Visualization

Used Matplotlib to create five visualizations:

1. Book Rating Distribution
2. Book Price Distribution
3. Average Book Price by Rating
4. Book Price Distribution by Rating (Box Plot)
5. Top 10 Most Expensive Books

The visualizations help compare book ratings, prices, and price distributions.

## Project Limitations

- The analysis covers only the first five pages of the website.
- The dataset contains 100 books and may not represent the entire website.
- All 100 books were marked as in stock.
- The relationship between book ratings and prices does not establish causation.

## How to Run the Project

### 1. Install required libraries

```bash
pip install requests beautifulsoup4 pandas matplotlib
```

### 2. Run the scripts

```bash
python scraper.py
python eda.py
python visualization.py
```

Run `scraper.py` first to generate the dataset. The other two scripts use `books_data.csv`.

## Project Files

- `scraper.py` – Web scraping script
- `eda.py` – Exploratory data analysis script
- `visualization.py` – Data visualization script
- `books_data.csv` – Scraped dataset
- `eda_findings.txt` – EDA findings
- `visualization_findings.txt` – Visualization findings
- `chart1_rating_distribution.png` – Rating distribution chart
- `chart2_price_distribution.png` – Price distribution chart
- `chart3_average_price_by_rating.png` – Average price chart
- `chart4_boxplot_rating_vs_price.png` – Box plot
- `chart5_top_10_expensive_books.png` – Top 10 expensive books chart

## Internship

**Organization:** CodeAlpha  
**Program:** Data Analytics Internship

## Author

Virendra Kumar Gautam
