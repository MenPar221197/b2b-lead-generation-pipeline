# B2B Lead Generation Pipeline

An automated pipeline for collecting, cleaning, and organizing B2B leads for commercial prospecting.

This project began as a real-world pilot for identifying potential customers in the lumber industry in Querétaro, Mexico.

## Project Status

**Functional MVP under active development**

The current version integrates Apify, n8n, Python, and Google Sheets. It collects public business information, transforms the records, identifies incomplete leads, and prepares the results for manual sales follow-up.

A GitHub Actions workflow automatically verifies that the Python cleaning script runs successfully.

## Problem

Raw business data frequently contains:

- Duplicate companies
- Missing contact information
- Inconsistent phone-number formats
- Irrelevant businesses
- Incomplete records
- Data that is difficult for a salesperson to use

The objective is not only to collect leads, but to transform them into an organized and useful prospecting list.

## Architecture

```text
Apify → n8n → Python cleaning → Google Sheets → Sales follow-up
