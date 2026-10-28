# Phishing URL Awareness Checker - Test Results

Python version used: Fill in after running the program  
Operating system: Fill in your operating system  
Date: Fill in the date you ran the tests

| # | Input | Expected result | Actual result | Pass/Fail |
|---|---|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs; this is not a safety guarantee. | Fill in after running | Fill in |
| 2 | `http://192.0.2.10/account` | IP address + HTTP | Fill in after running | Fill in |
| 3 | `http://example.com@sample.invalid/login` | @ symbol + HTTP | Fill in after running | Fill in |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname segments | Fill in after running | Fill in |
| 5 | `https://xn--example.invalid/` | Punycode-style hostname | Fill in after running | Fill in |

## Notes

Write 2 or 3 sentences about what you learned and what surprised you after running the tests.

## Important

Record the actual output you observe. Mark each test PASS or FAIL based on whether the output matches the expected result. Do not mark tests as passed before running them.
