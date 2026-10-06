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
```

---

## Data Preparation

### Silver Layer

The Silver layer contains cleaned and validated versions of the source tables.

Main transformations include:

- standardization of city names;
- postal code normalization;
- product category translation;
- validation of primary and composite keys;
- missing-value analysis;
- temporal consistency checks;
- identification of invalid delivery sequences;
- validation of product physical measurements;
- payment consistency checks.

Missing values were not systematically imputed. When no reliable business rule was available, the original missing information was preserved.

---

## Gold Layer

Three main analytical tables were created.

### `gold_orders`

Grain: **one row per order**

The table includes:

- order value;
- product value;
- freight value;
- number of items;
- number of sellers;
- payment information;
- installment behavior;
- delivery duration;
- delivery delay;
- late-delivery indicators;
- review score;
- purchase year, month, day and hour;
- purchase period;
- high-value order indicator.

### `gold_customers`

Grain: **one row per unique customer**

Main features include:

- number of orders;
- total spending;
- average order value;
- total number of items;
- first and last purchase dates;
- recency;
- purchase frequency;
- average review score;
- delivery performance;
- repeat-customer indicator;
- high-value customer indicator;
- customer location.

### `gold_products`

Grain: **one row per product**

Main metrics currently include:

- number of orders;
- units sold;
- product revenue;
- freight revenue;
- average selling price;
- average freight cost;
- average review score.

Further product-level feature engineering will be added during the product analysis phase.

---

## Business Overview

The first business overview identified the following key metrics:

| KPI | Value |
|---|---:|
| Total orders | 99,441 |
| Unique customers | 96,096 |
| Product revenue | 13,591,643.70 |
| Gross order value | 15,843,553.24 |
| Average order value | 160.58 |
| Items sold | 112,650 |
| Average items per order | 1.14 |
| Repeat customer rate | ~3% |
| Average review score | 4.09 / 5 |
| Late delivery rate | ~7% |

---

## Initial Business Insights

### Business Growth

Monthly order volume increased strongly throughout 2017.

The number of monthly orders grew from approximately 1,800 orders in February 2017 to more than 7,500 orders in November 2017.

Business activity remained at a relatively high level during 2018, generally between approximately 6,000 and 7,300 monthly orders.

### Revenue Growth

Gross order value followed a similar pattern to order volume.

The strong increase in gross order value appears to be primarily driven by the growth in the number of orders rather than by an increase in average order value.

### Average Order Value

Average order value remained relatively stable over time, generally between approximately 145 and 170.

This indicates that business growth was mainly volume-driven.

### Customer Retention

The repeat customer rate is approximately **3%**, indicating that most customers purchased only once during the observed period.

Customer retention therefore represents an important area for further analysis.

### Customer Satisfaction

The average review score is **4.09 / 5**, indicating a generally high level of customer satisfaction.

### Delivery Performance

Approximately **7%** of analyzable deliveries arrived after the estimated delivery date.

Further analysis will investigate the relationship between delivery performance and customer reviews.

### Purchase Behavior by Time of Day

Orders are concentrated mainly during the afternoon and evening:

| Purchase period | Share of orders |
|---|---:|
| Night | 4.77% |
| Morning | 22.37% |
| Afternoon | 38.58% |
| Evening | 34.29% |

Approximately **72.87% of orders occur during the afternoon or evening**.

---

## Order Value Distribution

The distribution of order value is strongly right-skewed.

Most orders are concentrated at relatively low values, while a small number of orders reach very high amounts. This long tail means that the mean can be influenced by a limited number of high-value orders.

Extreme values are retained in the dataset unless a clear data-quality issue is identified.

---

## Data Coverage

The dataset contains irregular temporal coverage at the beginning and end of the observation period.

For monthly trend analysis, the main analytical period was therefore restricted to:

**February 2017 – August 2018**

This avoids interpreting partially covered months as genuine business declines.

---

## Next Steps

The next analyses will focus on:

- customer behavior and retention;
- RFM segmentation;
- product and category performance;
- logistics performance;
- payment behavior;
- customer satisfaction;
- Power BI dashboard development.
