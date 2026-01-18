# AI Code Review Assignment (Python)

## Candidate
- Name:Rhonajoy Koome
- Approximate time spent:60 minutes

---

# Task 1 — Average Order Value

## 1) Code Review Findings
### Critical bugs
- if the order array is zero, leading to a count of zero. the program would throw a   Zero division error.
- logic error: the function is counting all orders (both cancelled and non-cancelled) but dividing by only the non-cancelled orders.This will not accurately reflect the correct figure. 

### Edge cases & risks
- Empty orders array causes Zero division error
- if order["status"] and order["amount"] keys miss . A Key Error will be thrown
- Non-numeric amounts
- Negative Amounts

### Code quality / design issues
- simple, readable, easy to understand


## 2) Proposed Fixes / Improvements
### Summary of changes
- catch errors when count of orders is zero
- when there's a missing key
- counts the total of non-cancelled orders and is divided  by the amount of those orders.

### Corrected code
See `correct_task1.py`

> Note: The original AI-generated code is preserved in `task1.py`.

 ### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
Extensively validating the order input. that the data there is valid. Wrong inputs will result to incorrect output or the program crashing.


## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of orders. It correctly excludes cancelled orders from the calculation.

### Issues in original explanation
- The explanation of what the current program is doing  correct however the program itself does not make logical sense.

### Rewritten explanation
-This function calculates average order value by summing the amounts of all non-cancelled orders and dividing by the number of non-cancelled orders. It correctly excludes cancelled orders from the calculation.

## 4) Final Judgment
- Decision:  Reject
- Justification: Program does not make logic sense. 
- Confidence & unknowns:if negatives or zeros should be allowed 

---

# Task 2 — Count Valid Emails

## 1) Code Review Findings
### Critical bugs
- No syntax errors therefore the code will run.(Assuming a Iterable of String emails is passed)
- Function's business logic of checking a valid email is incorrect.

### Edge cases & risks
- Business Logic is Incorrect.As long as there is an @ present , it is counted . In the scenario where an email has more than one @ it will be still be presented as a valid email which is wrong.

### Code quality / design issues
- Simple, easy to understand , readable

## 2) Proposed Fixes / Improvements
### Summary of changes
- using regex expressions to check the viability of an email
- breaking down logic to have a function that only checks the validity of an email and the other that counts No of valid emails.
- ensuring the emails Passed are an iterable

### Corrected code
See `correct_task2.py`

> Note: The original AI-generated code is preserved in `task2.py`. 


### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
 the correctness and validity of an email by:
 checking the placement of the @ symbol in the email.
 checking domain placement in the email
 checking for invalid symbols
 checking for whitespaces
 all these things are important  to determine email validity

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function counts the number of valid email addresses in the input list. It safely ignores invalid entries and handles empty input correctly.

### Issues in original explanation
- Not all cases of Invalid entries are ignored
- Empty Inputs are not handled correctly

### Rewritten explanation
- This function counts the number of the @ symbols in an email.

## 4) Final Judgment
- Decision:  Reject
- Justification: the program  runs but it will not be helpful and is wrong in a real world scenario.
- Confidence & unknowns: Should the emails be lowercased before validation

---

# Task 3 — Aggregate Valid Measurements

## 1) Code Review Findings
### Critical bugs
- Program counts the instance of a None value. so ends up being divided with the total.
- 

### Edge cases & risks
- When all values are None will throw a Zero division error
- if input has both string and numeric values, function will crash
- Booleans will be counted as 1.0 0r 0.0
- 

### Code quality / design issues
- simple, easy to understand, readable

## 2) Proposed Fixes / Improvements
### Summary of changes
- Througly validated all the data types to ensure correct handling.

### Corrected code
See `correct_task3.py`

> Note: The original AI-generated code is preserved in `task3.py`.

### Testing Considerations
If you were to test this function, what areas or scenarios would you focus on, and why?
Throughly validate data types of the input they determine the correct average.

## 3) Explanation Review & Rewrite
### AI-generated explanation (original)
> This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

### Issues in original explanation
- The function includes the None count in the averaging
- The function does not correctly handle mixed types .

### Rewritten explanation
- This function calculates the average of valid measurements by ignoring missing values (None) and averaging the remaining values. It safely handles mixed input types and ensures an accurate average

## 4) Final Judgment
- Decision:  Reject
- Justification: The function has runtime errors and does not make logical sense
- Confidence & unknowns:
Whether or not Negative values should be allowed
Should zeros be treated as  a valid count or ignored