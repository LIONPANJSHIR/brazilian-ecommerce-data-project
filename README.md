# Brazilian E-Commerce Analytics

## Overview

This project analyzes the Brazilian Olist e-commerce dataset in order to understand business performance, customer behavior, product performance, payments, logistics and customer satisfaction.

The project follows a layered data approach:

- **Raw**: original source data
- **Silver**: cleaned, standardized and validated tables
- **Gold**: analytical tables enriched with business metrics and engineered features

The final objective is to build a complete analytical workflow that can support exploratory analysis, customer segmentation and BI reporting.

---

## Project Objectives

The main objectives of this project are to:

- analyze overall business performance;
- understand customer purchasing behavior;
- measure customer retention and repeat purchases;
- identify high-performing products and categories;
- analyze payment behavior;
- evaluate delivery performance;
- measure customer satisfaction;
- prepare analytical datasets for Power BI and customer segmentation.

---

## Project Structure

```text
Brazilien_ecommerce/
│
├── data/
│   ├── raw/
│   ├── silver/
│   └── gold/
│
├── notebooks/
│   ├── 01_data_quality.ipynb
│   ├── 02_silver_validation.ipynb
│   ├── 03_gold_tables.ipynb
│   ├── 01_business_overview.ipynb
│   ├── 02_customer_analysis.ipynb
│   ├── 03_product_analysis.ipynb
│   └── ...
│
├── src/
│   └── brazilien_ecommerce/
│       ├── cleaning.py
│       ├── validation.py
│       └── ...
│
└── README.md