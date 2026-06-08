# Last Mile Logistics Audit: Delivery Performance Analysis for Veridi Logistics

## A. Executive Summary

This project analyzes delivery performance across the Brazilian E-Commerce Public Dataset by Olist to identify whether delivery issues are concentrated in specific regions or represent a broader nationwide challenge. A delivery audit was conducted by integrating logistics, customer sentiment, geographic, and product-level data into a unified analytical framework.

The analysis found that while the majority of deliveries were completed on time, delayed deliveries were strongly associated with lower customer review scores, confirming that logistics performance directly impacts customer satisfaction. Geographic analysis revealed that some states experience significantly higher late-delivery rates than others, indicating that delivery performance is not evenly distributed across the country.

A distance-based logistics investigation showed that longer shipping distances increase the probability of late deliveries and are associated with declining customer review scores. Product category analysis further identified operational risk areas, with categories such as Office Furniture, Audio, Home Comfort, and Furniture-related products exhibiting elevated delivery risk and lower customer satisfaction metrics.

These findings provide Veridi Logistics with a data-driven foundation for improving delivery forecasting, prioritizing operational improvements, and reducing the customer impact of logistics delays.

---

## B. Project Links

### Notebook

**Jupyter Notebook:**
https://github.com/Derrickamponsah/logistics-audit/blob/main/notebooks/delivery_audit.ipynb

### Dashboard

**Streamlit Dashboard:**
https://logistics-audit.streamlit.app/

### Presentation

**Presentation Slides (PDF/PPT):**



---

## C. Technical Explanation

### Data Cleaning and Preparation

The project utilized multiple relational tables from the Olist Brazilian E-Commerce Dataset, including Orders, Reviews, Customers, Products, Sellers, Order Items, and Geolocation data.

Key data preparation steps included:

#### 1. Data Quality Assessment

* Loaded all required datasets into a reproducible Jupyter Notebook environment.
* Audited dataset dimensions, missing values, and duplicate records.
* Verified data consistency across tables prior to merging.

#### 2. Date and Timestamp Processing

Converted all delivery-related timestamps into datetime format, including:

* Order Purchase Timestamp
* Order Approval Date
* Carrier Pickup Date
* Customer Delivery Date
* Estimated Delivery Date

This enabled accurate delivery duration and delay calculations.

#### 3. Delivery Performance Engineering

Created new business-focused metrics:

* **Actual Delivery Days**

  * Time between purchase and customer delivery.

* **Estimated Delivery Days**

  * Time between purchase and estimated delivery date.

* **Delay Days**

  * Difference between actual and estimated delivery dates.

* **Delivery Status**

  * On Time
  * Late
  * Super Late (>5 days late)

Orders that were cancelled, unavailable, or never delivered were excluded from delivery-performance calculations.

#### 4. Master Dataset Construction

A unified master dataset was created by joining:

* Orders
* Reviews
* Customers

Special attention was given to review records because some orders contained multiple review entries. Duplicate review records were removed by retaining the earliest review record per order before joining.

Validation checks confirmed:

* One row per order
* No duplicate orders
* Preserved delivery and review integrity

#### 5. Geographic Integration

Customer location information was merged into the master dataset using customer identifiers and state-level information.

State-level metrics were calculated, including:

* Total Orders
* Late Orders
* Late Delivery Percentage
* Average Delay
* Average Review Score

This enabled regional performance comparisons and geographic auditing.

---

### Candidate's Choice: Distance Impact Audit

To provide additional business value beyond the project requirements, a distance-based logistics audit was developed.

The objective was to determine whether shipping distance contributes to delivery delays and customer dissatisfaction.

#### Methodology

Additional datasets used:

* Sellers Dataset
* Order Items Dataset
* Geolocation Dataset

Steps performed:

1. Linked each order to its primary seller.
2. Estimated customer and seller geographic coordinates using ZIP code geolocation data.
3. Calculated approximate shipping distance (kilometers) between seller and customer locations using geographic coordinates.
4. Created distance bands to group shipments by travel range.
5. Compared distance against:

   * Late Delivery Percentage
   * Delivery Delays
   * Average Customer Review Score

#### Key Findings

The analysis showed that:

* Longer-distance deliveries experience significantly higher late-delivery rates.
* Orders traveling more than 2,000 km were nearly three times more likely to be delivered late than local deliveries.
* Customer review scores decline as shipping distance increases.
* Distance contributes to delivery risk but does not fully explain all delays, suggesting additional operational factors such as category complexity, carrier performance, and regional logistics constraints.

#### Business Value

This analysis provides Veridi Logistics with actionable insights for:

* Improving delivery-date forecasting
* Prioritizing long-distance shipment monitoring
* Optimizing carrier allocation
* Reducing customer dissatisfaction caused by unrealistic delivery expectations

---

## Project Structure

```text
last-mile-logistics-audit/

├── dashboard/
│   └── app.py

├── notebooks/
│   └── delivery_audit.ipynb

├── outputs/
│   ├── master_dataset.csv
│   ├── state_metrics.csv
│   ├── category_metrics.csv
│   ├── distance_metrics.csv
│   ├── delivery_status_summary.csv
│   ├── review_by_status.csv
│   ├── bad_review_status.csv
│   ├── bad_review_rate.csv
│   └── sentiment_summary.csv

├── README.md
├── requirements.txt
└── .gitignore
```

## Technologies Used

* Python
* Pandas
* NumPy
* Plotly
* Streamlit
* Jupyter Notebook
* GitHub

## Deliverables

* Data Cleaning and Analysis Notebook
* Streamlit Dashboard
* Insight Presentation
* Technical Documentation
* Public GitHub Repository
