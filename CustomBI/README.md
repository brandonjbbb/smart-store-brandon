# 📊 M7 Custom BI Project – Maximizing Sales by Region and Segment

## 1. The Business Goal  
To identify which regions and customer segments generate the most sales and how performance trends over time.

## 2. Data Source  
Prepared datasets from the OLAP folder:  
- `sales_data_prepared_updated.csv`  
- `customers_data_prepared_updated.csv`

## 3. Tools Used  
- Python 3, Jupyter Notebook  
- Pandas, Matplotlib, Seaborn  

## 4. Workflow & Logic  
- Merged sales and customer data using `CustomerID`  
- Extracted `Month` from sale date for trend analysis  
- Grouped by `Region`, `CustomerSegment`, and `Month`  
- Performed slicing, dicing, and drilldown aggregations  

## 5. Results  
- **East region** had the highest sales overall  
- **Enterprise customers** dominated in the South  
- **Q2 months** saw noticeable sales spikes across regions

## 6. Suggested Business Action  
- Focus marketing efforts on high-performing regions  
- Target Enterprise customers in regions where they lead  
- Prepare for seasonal surges in Q2 with inventory and campaigns

## 7. Challenges  
- Ensuring the data merge was accurate  
- Keeping visualizations clean and informative  
- Managing multiple dimensions (region, month, segment) at once

## 8. Ethical Considerations  
- Avoiding bias in analysis (e.g., favoring larger regions)  
- Maintaining data privacy and responsible insights use  
- Ensuring human oversight in interpreting automated outputs
