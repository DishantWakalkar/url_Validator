# URL Validator

A Python utility that scans a MySQL-backed table of URLs, checks each one's reachability over HTTP, and writes the result (valid, invalid, or unreachable) back to the database.

## What it does

- Connects to a MySQL database via SQLAlchemy and pulls the list of URLs to check.
- Sends a request to each URL and classifies it as valid, invalid, or unreachable, with error handling for timeouts and connection failures.
- Writes the result back to the same table, so downstream systems can filter out dead links without manual review.


## Background

Built while cleaning and validating a large URL dataset during my internship at Jio Platforms, where automating this check replaced manual review and helped scan a database of over a million records for broken links.

## Stack

Python, SQLAlchemy, Requests, MySQL
