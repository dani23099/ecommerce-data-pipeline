# Global E-commerce Data Pipeline: Market Intelligence

## About This Project
This project is an End-to-End Data Pipeline designed to collect and analyze real e-commerce data using a RESTful API (Fake Store API). By performing rigorous data cleansing and wrangling on the extracted data, this pipeline transforms raw JSON responses into actionable business insights, enabling true market intelligence and trend analysis.

**Note:** The architecture is designed to be highly adaptable, allowing quick pivots between different data sources if API security policies change.

### Technologies Used

  * **Python:** For scripting and API requests.
  * **Pandas:** For data cleaning, structuring, and transformation.
  * **REST API:** As the primary data source (handling JSON responses and status codes).
  * **Git & GitHub:** For version control and portfolio showcase.

### 📈 Business Intelligence & Actionable Insights

Going beyond basic data extraction, this pipeline features an automated **Risk and Investment Matrix** designed to drive strategic business decisions. By analyzing multiple variables simultaneously (Price, Customer Rating, and Review Volume against market medians), the script segments products into actionable categories:

* **💎 Hidden Gems:** High-satisfaction, affordable products with above-average review counts. *(Strategy: Highlight these products and allocate marketing budget to drive volume).*
* **⚠️ High-Risk Inventory:** Expensive items with poor customer ratings. *(Strategy: Flag for quality review with suppliers or consider delisting to protect brand reputation).*

This feature demonstrates the ability to translate raw JSON data into tangible, profit-oriented recommendations.

### Future Enhancements
Currently, this project uses Pandas for data transformation, which is the perfect tool for the current volume of data extracted from the API. However, to demonstrate scalability and modern data engineering practices, I plan to migrate the pipeline to the following technologies in the future:

  * **Polars:** To replace Pandas and achieve much faster, multi-           threaded data processing.

  * **DuckDB:** To execute rapid analytical SQL queries locally without heavy server installations.

  * **dbt (Data Build Tool):** To manage data transformations directly in SQL, applying software engineering best practices.
