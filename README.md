Task 24 – Data Quality Audit

Project Overview

This project performs a basic data quality audit on the Superstore dataset using Python and Pandas.

The objective is to identify common data quality issues such as missing values, duplicate records, invalid ranges, and date consistency issues.

Tools Used

- Python
- Pandas
- Excel/Superstore Dataset
- GitHub

Dataset

The project uses the Superstore dataset containing sales and order-related information.

Quality Checks Performed

The following validation rules were applied:

1. Missing Values
   
   - Checked all columns for missing values.

2. Duplicate Records
   
   - Checked for completely duplicated rows.

3. Sales Validation
   
   - Sales should not be negative.

4. Quantity Validation
   
   - Quantity should be greater than zero.

5. Discount Validation
   
   - Discount should be between 0 and 1.

6. Date Consistency
   
   - Order Date should not be later than Ship Date.

7. Profit Validation
   
   - Negative profit records were identified for review.

Process

The audit was performed using Pandas.

The process included:

- Loading the dataset
- Checking missing values
- Checking duplicate rows
- Validating numeric ranges
- Checking date consistency
- Quantifying identified issues
- Creating an issue log
- Creating a cleaned sample
- Creating an audit report

Deliverables

1. Issue Log

"issue_log.csv"

Contains the identified data quality issues and their counts.

2. Cleaned Sample

"cleaned_sample.csv"

Contains a cleaned sample after removing duplicate records.

3. Audit Report

"audit_report.csv"

Contains the overall data quality audit results.

4. Python Script

"data_quality_audit.py"

Contains the Python/Pandas code used to perform the audit.

Outcome

The audit provides a repeatable checklist for identifying common data quality issues before using the dataset for analysis or reporting.

The identified issues were quantified so that they can be reviewed and addressed systematically.

Rollback Evidence

The original dataset was kept unchanged.

All data-quality processing was performed using Python and the results were saved separately as output files.

This allows the original dataset to be retained as the source version while the cleaned sample can be reviewed independently.

Interview Questions

What makes a quality rule useful?

A quality rule should be clear, measurable, and relevant to the business or dataset. It should clearly define what is valid and invalid data.

How do you prioritize issues?

I would prioritize issues based on their impact, frequency, and importance to the final analysis. Issues that can significantly affect reports or business decisions should be addressed first.

Conclusion

The project demonstrates a basic and repeatable approach to data quality auditing using Python and Pandas.
