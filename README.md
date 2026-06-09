# 💼 **NaukariScraper – Naukri Job Skill Scraper**

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Requests](https://img.shields.io/badge/Web%20Requests-Requests-green)
![JSON](https://img.shields.io/badge/Data-JSON-yellow)
![Text Mining](https://img.shields.io/badge/Text%20Mining-Skill%20Ranking-purple)
![Status](https://img.shields.io/badge/Status-Prototype-orange)

---

## ✨ Overview

**NaukariScraper** is a Python-based job-skill extraction project that collects job posting data from Naukri search API URLs, extracts skill tags from job listings, stores the raw response as JSON, and ranks skills based on frequency.

The project is useful for identifying common technical skills required across different job roles such as web developer, machine learning, and Python developer roles.

---

## 🎯 Problem Statement

Job seekers often need to understand which skills are most frequently requested in job postings.

Manually checking multiple job listings can be slow and repetitive. **NaukariScraper** helps automate this process by extracting skill tags from job search results and ranking them based on how often they appear.

---

## 💡 Solution: NaukariScraper

| Feature                    | Description                                                  |
| -------------------------- | ------------------------------------------------------------ |
| 🔗 **URL-Based Scraping**  | Reads Naukri job search API URLs from `url.txt`.             |
| 📥 **Job Data Collection** | Sends HTTP requests to collect job listing data.             |
| 🧾 **Skill Extraction**    | Extracts `tagsAndSkills` from each job listing.              |
| 🗃️ **JSON Storage**       | Saves raw job API responses into `skilljson.json`.           |
| 📊 **Skill Ranking**       | Counts each skill occurrence and prints a ranked skill list. |

---

## 🧰 Tech Stack

| Layer              | Technologies                  |
| ------------------ | ----------------------------- |
| **Language**       | Python                        |
| **HTTP Requests**  | Requests                      |
| **Data Format**    | JSON                          |
| **Input Storage**  | Text file URLs                |
| **Output Storage** | Text file, JSON file          |
| **Analysis**       | Frequency-based skill ranking |

---

## 🏗️ Project Workflow

```text
url.txt
   ↓
gettingskill.py
   ↓
Fetch job API responses from Naukri
   ↓
Extract tagsAndSkills
   ↓
Save skills to skill.txt
   ↓
Save raw response to skilljson.json
   ↓
skillfinder.py
   ↓
Clean, count, and rank skills
```

---

## 📁 Project Structure

```text
NaukariScraper/
├── gettingskill.py
├── skillfinder.py
├── skill.txt
├── skilljson.json
└── url.txt
```

---

## 🔑 Core Files

| File              | Purpose                                                                                               |
| ----------------- | ----------------------------------------------------------------------------------------------------- |
| `gettingskill.py` | Reads API URLs, fetches job data, extracts skill tags, and writes output files.                       |
| `skillfinder.py`  | Reads extracted skills, removes basic punctuation, counts skill frequency, and prints ranked results. |
| `url.txt`         | Contains Naukri job search API URLs.                                                                  |
| `skill.txt`       | Stores extracted skills from job listings.                                                            |
| `skilljson.json`  | Stores raw JSON response data from the job API.                                                       |

---

## ⚙️ Setup Guide

### 1️⃣ Clone Repository

```bash
git clone https://github.com/lekshman-babu/NaukariScraper.git
cd NaukariScraper
```

### 2️⃣ Install Dependencies

```bash
pip install requests
```

### 3️⃣ Add or Update Job Search URLs

Edit `url.txt` and add Naukri job search API URLs.

Example job categories can include:

```text
web developer
machine learning
python developer
```

### 4️⃣ Run Skill Extraction

```bash
python gettingskill.py
```

This generates or updates:

```text
skill.txt
skilljson.json
```

### 5️⃣ Run Skill Ranking

```bash
python skillfinder.py
```

---

## 📊 Example Skills Extracted

The project can extract and rank skills such as:

```text
PYTHON
HTML
CSS
JAVASCRIPT
ANGULAR
NODE.JS
MACHINE LEARNING
DEEP LEARNING
SQL
DJANGO
FLASK
PANDAS
NUMPY
```

---

## 📌 Features

* Reads multiple job search URLs
* Fetches job listing data using HTTP requests
* Extracts skill tags from job listings
* Converts skills to uppercase for consistency
* Stores extracted skills in a text file
* Stores raw job response data in JSON format
* Counts duplicate skill occurrences
* Prints a ranked skill-frequency list

---

## 🚀 Use Cases

* Job market skill analysis
* Resume keyword research
* Skill trend identification
* Beginner web scraping practice
* Python file handling practice
* JSON API response processing
* Frequency-based text analysis

---

## 🔮 Future Improvements

* Add proper error handling for failed requests
* Add support for command-line search keywords
* Store output as CSV
* Add pandas-based analysis
* Add charts for top skills
* Remove duplicate spacing and inconsistent skill formatting
* Add support for more job portals
* Add a Streamlit dashboard
* Add a requirements.txt file
* Add README usage examples with sample output

---

## ⚠️ Notes

This project uses job search API URLs and request headers. Website APIs and response formats may change over time, so the scraper may require updates if Naukri changes its API structure.

Use this project responsibly and follow the website’s terms of service.

---

## 🧑‍💻 Author

**Lekshman Babu**

---

## 🪪 License

No license file is currently included. Add a license before using or distributing the project publicly.

---

> 💼 *NaukariScraper helps identify in-demand job skills by extracting and ranking skill tags from Naukri job listings.*

---

## 📚 Source Basis

This README is based on the repository’s public file list and visible source files, including `gettingskill.py`, `skillfinder.py`, `skill.txt`, `url.txt`, and `skilljson.json`. ([GitHub][1])

[1]: https://github.com/lekshman-babu/NaukariScraper "GitHub - lekshman-babu/NaukariScraper · GitHub"
