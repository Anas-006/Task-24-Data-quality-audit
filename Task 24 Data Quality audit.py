import pandas as pd

print("Python started")

df = pd.read_excel(r"c:\Users\Admin\Desktop\Superstore.xlsx")

print("File loaded successfully")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print(df.head())

missing_values = df.isnull().sum()

print("\nMissing Values by Column:")
print(missing_values)

duplicate_count = df.duplicated().sum()

print("\nDuplicate Rows:")
print("Total duplicate rows:", duplicate_count)

negative_sales = (df["Sales"] < 0).sum()

invalid_quantity = (df["Quantity"] <= 0).sum()

invalid_discount = ((df["Discount"] < 0) | (df["Discount"] > 1)).sum()

print("\nRange Validation:")
print("Negative Sales:", negative_sales)
print("Invalid Quantity:", invalid_quantity)
print("Invalid Discount:", invalid_discount)

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

invalid_dates = (df["Order Date"] > df["Ship Date"]).sum()

print("Invalid Dates:", invalid_dates)


negative_profit = (df["Profit"] < 0).sum()

print("Negative Profit:", negative_profit)


issue_log = pd.DataFrame({
    "Issue": [
        "Missing Values",
        "Duplicates",
        "Negative Sales",
        "Invalid Quantity",
        "Invalid Discount",
        "Invalid Dates",
        "Negative Profit"
    ],
    "Count": [
        missing_values.sum(),
        duplicate_count,
        negative_sales,
        invalid_quantity,
        invalid_discount,
        invalid_dates,
        negative_profit
    ]
})

print("\nIssue Log:")
print(issue_log)


issue_log.to_csv("issue_log.csv", index=False)

df.drop_duplicates().to_csv(
    "cleaned_sample.csv",
    index=False
)

print("\nFiles created successfully!")

audit_report = pd.DataFrame({
    "Metric": [
        "Total Rows",
        "Total Columns",
        "Missing Values",
        "Duplicate Rows",
        "Negative Sales",
        "Invalid Quantity",
        "Invalid Discount",
        "Invalid Dates",
        "Negative Profit"
    ],
    "Count": [
        len(df),
        len(df.columns),
        missing_values.sum(),
        duplicate_count,
        negative_sales,
        invalid_quantity,
        invalid_discount,
        invalid_dates,
        negative_profit
    ]
})

print("\nAudit Report:")
print(audit_report)

audit_report.to_csv("audit_report.csv", index=False)

print("\nAudit report saved successfully!")