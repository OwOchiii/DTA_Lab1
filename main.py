import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import io
import sys

# Capture output for the report
output_capture = io.StringIO()
sys.stdout = output_capture

print("Task: Import data in .csv file to requests data frame in Python")
requests = pd.read_csv('yearly_request.csv')
print("Successfully loaded data. Shape:", requests.shape)

print("\nTask: Export the histogram of number of requests to jpeg file")
plt.figure()
requests['no_of_requests'].plot.hist(bins=20)
plt.title('Histogram of Number of Requests')
plt.xlabel('Number of Requests')
plt.ylabel('Frequency')
plt.savefig('requests_histogram.jpg', format='jpeg')
print("Saved histogram to requests_histogram.jpg")

print("\nTask: Add a column per_request to dataset and exports the modified dataset to “requests_modified.txt” file")
requests['per_request'] = requests['req_total'] / requests['no_of_requests']
requests.to_csv('requests_modified.txt', sep='\t', index=False)
print("Added per_request and saved to requests_modified.txt")

print("\nTask: Extract the second, third, and fourth column of the requests data frame")
extracted_cols = requests.iloc[:, 1:4]
print(extracted_cols.head())

print("\nTask: build an empty character vector of the same length as requests and group the customers according to the request amount")
# Convert to character (string) vector equivalent using numpy and pandas
group_vector = np.empty(len(requests), dtype=object)
group_vector[requests['req_total'] < 200] = 'Low'
group_vector[(requests['req_total'] >= 200) & (requests['req_total'] < 500)] = 'Medium'
group_vector[requests['req_total'] >= 500] = 'High'
requests['request_amount_group'] = group_vector
print(requests[['req_total', 'request_amount_group']].head())

print("\nTask: Summary of requests")
print(requests.describe(include='all'))

print("\nTask: Calculate and show total of request value")
total_req_value = requests['req_total'].sum()
print("Total request value: ", total_req_value)

# Restore stdout
sys.stdout = sys.__stdout__

# Write report to markdown
report_content = f"""# Result Report

## 1. Import Data
```python
requests = pd.read_csv('yearly_request.csv')
```

## 2. Export Histogram
```python
plt.figure()
requests['no_of_requests'].plot.hist(bins=20)
plt.savefig('requests_histogram.jpg', format='jpeg')
```

## 3. Add column and export to txt
```python
requests['per_request'] = requests['req_total'] / requests['no_of_requests']
requests.to_csv('requests_modified.txt', sep='\\t', index=False)
```

## 4. Extract columns
```python
extracted_cols = requests.iloc[:, 1:4]
```

## 5. Group customers
```python
group_vector = np.empty(len(requests), dtype=object)
group_vector[requests['req_total'] < 200] = 'Low'
group_vector[(requests['req_total'] >= 200) & (requests['req_total'] < 500)] = 'Medium'
group_vector[requests['req_total'] >= 500] = 'High'
requests['request_amount_group'] = group_vector
```

## 6. Summary
```python
requests.describe(include='all')
```

## 7. Total Request Value
```python
total_req_value = requests['req_total'].sum()
```

## Complete Script Output
```
{output_capture.getvalue()}
```
"""

with open('result_report.md', 'w') as f:
    f.write(report_content)
    
print("Report generated at result_report.md")

