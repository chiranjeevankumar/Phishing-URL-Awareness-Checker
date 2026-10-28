# EWB Phishing URL Awareness Checker

## Project Overview

The Phishing URL Awareness Checker is a beginner-friendly Python
command-line project. It examines the text of a URL for common
warning signs that may appear in suspicious links.

The program does not open websites, scan for malware, or send data
to external services.

## Features

The program checks six warning signs:

1. An @ symbol in the URL.
2. A URL longer than 100 characters.
3. An IP address used as the hostname.
4. Five or more hostname segments.
5. A punycode marker (`xn--`) in the hostname.
6. The HTTP scheme.

It also includes these improvements:

- A loop that allows multiple URLs to be checked without restarting.
- A quit option.
- A warning summary that counts the warning signs found.
- Error handling for empty or malformed URL input.
- A reminder that the result is not a guarantee of safety.

## Requirements

- Python 3.10 or later.
- No third-party Python packages are required.

## How to Run

Open a terminal in the project folder.

On Windows:

    python phishing_checker.py

On macOS or Linux:

    python3 phishing_checker.py

Enter a sample URL when prompted. Type `q` to quit.

## How to Run Automated Tests

Run this command from the main project folder:

    python -m unittest discover -s tests -v

On macOS or Linux, use `python3` if that is the command for your
Python installation.

## Sample Testing

The five required sample URLs and expected observations are listed
in `tests/test_samples.md`.

Run the program with each sample, record the actual output, and
mark each test PASS or FAIL based on the observed result.

## Screenshots

Add genuine screenshots of your own program run to the `screenshots`
folder using these exact filenames:

- `sample_run.png`
- `test_results.png`

The first screenshot should show the program running with a sample
URL. The second should show your completed test results.

## Improvements Made

1. Repeat checking: the program uses a loop so multiple URLs can
   be checked in one session.
2. Warning summary: the program lists the warning signs found and
   counts them.
3. Input error handling: empty or malformed input produces a
   readable error message rather than an unhandled exception.

## Limitations

This is an educational awareness tool, not a complete security
scanner. It checks only the text of a URL. It does not visit websites,
check online reputation, or detect every phishing attempt.

"No warning signs found" does NOT mean a URL is safe. HTTPS alone
also does not prove that a website is trustworthy.

## Ethical Use

Use the sample strings provided for this learning project. Do not
collect credentials, send phishing messages, or test websites
without permission.

## Author

Chiranjeevan Kumar Raavi
