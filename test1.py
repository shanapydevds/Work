# Input dictionary
employees = [
    {"Name": "Alice", "Employee Code": "E001", "Designation": "Manager", "Company": "TechCorp"},
    {"Name": "Bob", "Employee Code": "E002", "Designation": "Analyst", "Company": ""},
    {"Name": "Charlie", "Employee Code": "E003", "Designation": "Engineer", "Company": "BuildIt"}
]

# Add Status column based on Company name
for employee in employees:
    if employee["Company"].strip():  # Check if Company is not blank
        employee["Status"] = "Yes"
    else:
        employee["Status"] = "No"

# Output the updated dictionary
print(employees)
