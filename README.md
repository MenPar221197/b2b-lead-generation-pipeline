# B2B Lead Generation Pipeline

An automated workflow for collecting, organizing, and preparing B2B leads for commercial prospecting.

This project started as a real-world pilot for identifying potential customers in the lumber industry in Querétaro, Mexico.

## Project Status

**MVP in development**

The current version connects Apify, n8n, and Google Sheets. It can collect business information, organize the results, and prepare them for manual commercial follow-up.

Python-based data cleaning, validation, and lead scoring are planned for upcoming versions.

## Problem

Raw business data frequently contains:

- Duplicate companies
- Missing or invalid contact information
- Inconsistent phone-number formats
- Irrelevant businesses
- Incomplete records
- Data that is difficult for a salesperson to use

The objective is not only to collect leads, but to transform them into a clean and useful prospecting list.

## Current Workflow

1. Apify collects publicly available business information.
2. n8n receives and transforms the extracted records.
3. Basic filters organize the information.
4. Google Sheets stores the results.
5. A salesperson reviews each lead and records its commercial status.

## Technologies

- Apify
- n8n
- Google Sheets
- Python — planned for advanced cleaning and validation
- SQL — planned for data storage and analysis
- Git and GitHub

## Collected Fields

Depending on public availability, the workflow can collect:

- Business name
- Category
- Phone number
- Website
- Address
- Location
- Google Maps URL
- Rating and review count
- Commercial follow-up status
- Sales notes

## Roadmap

- [x] Build the initial Apify extraction process
- [x] Connect Apify with n8n
- [x] Send organized results to Google Sheets
- [ ] Improve lead relevance filters
- [ ] Add Python data-cleaning scripts
- [ ] Normalize and validate phone numbers
- [ ] Detect and remove duplicates
- [ ] Add lead-quality scoring
- [ ] Store historical data in SQL
- [ ] Create performance dashboards
- [ ] Adapt the workflow for multiple industries

## Privacy and Security

This public repository does not contain API keys, credentials, private customer information, or real prospect datasets. Any future sample data will be anonymized.

## Author

**Edgar Mendez**  
Junior Automation Developer based in Querétaro, Mexico.

Currently building practical automation and data projects with Python, SQL, Git, n8n, APIs, and Google Sheets.

## License

This project is available under the MIT License.
