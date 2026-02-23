##  Live Demo
https://retailfoodwasteanalytics-8wu4f25uxml9lqggvca8h.streamlit.app

---
# Retail Food Waste & Demand Analytics System

A multi-restaurant analytics and decision-support dashboard designed to identify production-demand mismatch, reduce food waste, and improve profitability in retail food businesses.

---

## Project Overview

Retail food businesses often face overproduction, leading to food wastage and revenue loss.  
This system analyzes historical production and sales data to:

- Detect high-waste items
- Quantify financial impact
- Suggest optimized production levels
- Monitor expiry-related risks
- Simulate potential savings from waste reduction

The dashboard provides both operational monitoring and strategic insights.

---

## Key Features

### 1. Multi-Restaurant Support

- Supports multiple restaurants in a single dataset
- Restaurant-specific filtering
- Dynamic CSV upload functionality

### 2. KPI Metrics

- Waste Percentage
- Waste-to-Revenue Percentage
- Revenue Contribution Percentage
- Overstock Risk Score
- Performance Score

### 3. Production Recommendation Engine

- Suggests production reduction or maintenance
- Calculates:
  - Average Production
  - Suggested Production
  - Reduction Units

### 4. Real-Time Risk Alerts

- Flags items with:
  - Waste > 20%
  - High expiry risk
- Acts as monitoring system

### 5. Waste Heatmap

- Visual representation of:
  - Item vs Day-of-Week waste patterns
- Helps identify recurring inefficiencies

### 6. Expiry Risk Analysis

- Operational View (Daily monitoring)
- Strategic View (Item-level summary)

### 7. Scenario Simulation

- Adjustable waste reduction percentage
- Calculates potential financial savings

### 8. Executive Summary & PDF Report

- Generates business-ready report
- Includes key KPIs and risk overview

---

## Tech Stack

- Python
- Pandas
- Streamlit
- Seaborn
- Matplotlib
- Scikit-learn (MinMaxScaler)
- ReportLab (PDF generation)

---

## Dataset Structure

The system expects structured data with the following columns:

| Column Name     | Description                  |
| --------------- | ---------------------------- |
| Restaurant_Name | Name of restaurant           |
| Date            | Transaction date             |
| Item            | Food item                    |
| Category        | Item category                |
| Produced_Qty    | Quantity produced            |
| Sold_Qty        | Quantity sold                |
| Waste_Qty       | Quantity wasted              |
| Revenue         | Revenue generated            |
| Waste_Loss      | Financial loss due to waste  |
| Expiry_Days     | Days remaining before expiry |
| Day_of_Week     | Weekday name                 |

---

## How to Run the Project

### Step 1: Clone Repository

```bash
git clone https://github.com/akaskatiyar/Retail_Food_Waste_Project.git
cd Retail_Food_Waste_Project
```
