# 📄 PyPDF Report Generator — Enterprise XML-to-PDF Reporting Engine

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg?logo=python&logoColor=white)](https://www.python.org/)
[![ReportLab](https://img.shields.io/badge/Engine-ReportLab-3776AB)](https://www.reportlab.com/)
[![Format](https://img.shields.io/badge/Format-XML%20%7C%20DTD%20%7C%20PDF-brightgreen)](#)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

An automated **Enterprise XML-to-PDF Reporting Engine** built with Python and ReportLab. It ingests structured, hierarchical organizational XML data (validated against a Document Type Definition / DTD schema) and dynamically generates formatted, multi-page corporate PDF reports with dynamic coordinate calculations, division breakdowns, project budgets, and employee hour tracking.

---

## ✨ Key Capabilities

* **📑 Automated Data-Driven PDF Generation:**
  * Eliminates manual reporting by compiling raw XML data feeds directly into publication-ready PDF documents.
  * Headless and fast — executes instantaneously without browser dependencies or heavy WebKit drivers.

* **📐 Dynamic Canvas & Layout Calculation:**
  * Uses ReportLab's low-level `canvas.Canvas` for pixel-perfect typography, custom line spacing, and precise component alignments.
  * Automatically calculates offsets per employee record (`y_offset`) to prevent overlapping text elements.

* **🏢 Multi-tier Organizational Hierarchy:**
  * Renders nested data structures cleanly: **Division** $\rightarrow$ **Projects** $\rightarrow$ **Allocated Budgets** $\rightarrow$ **Assigned Employees** $\rightarrow$ **Project Task Hours**.
  * Displays granular attributes including Employee IDs, Office locations, Birthdates, and Salaries.

* **📄 Smart Multi-Page Flow:**
  * Automatically generates clean page breaks (`showPage()`) after each division project, ensuring distinct departmental reporting.

* **🛡️ Strict Schema Validation:**
  * Accompanied by formal DTD validation (`company.dtd`) and structured metadata configuration (`format.json`).

---

## 📁 Repository Structure

| File | Description |
| :--- | :--- |
| `report.py` | Core Python automation script that parses the XML and renders the PDF canvas. |
| `company.xml` | Source hierarchical corporate dataset (Divisions, Projects, Budgets, Employees). |
| `company.dtd` | Document Type Definition specifying the validation rules and grammar for `company.xml`. |
| `format.json` | JSON schema specification for data fields and structural hierarchy. |
| `Assignment2.pdf` | Sample compiled output PDF demonstrating layout and typography. |

---

## 🚀 Getting Started

### Prerequisites
* Python 3.8 or higher installed on your system.

### Quick Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Moeez-03/py.pdf.git
   cd py.pdf
   ```

2. **Install ReportLab:**
   ```bash
   pip install reportlab
   ```

3. **Run the report generator:**
   ```bash
   python report.py
   ```

4. The script will parse `company.xml` and generate `Assignment2.pdf` in the root directory.

---

## 🛠️ Tech Stack
* **Language:** Python
* **PDF Rendering Engine:** [ReportLab](https://pypi.org/project/reportlab/)
* **XML Parser:** Python standard library (`xml.etree.ElementTree`)
* **Validation:** XML DTD (Document Type Definition)

---

## 👨‍💻 Author
**Abdul Moeez Nadeem**  
* GitHub: [@Moeez-03](https://github.com/Moeez-03)
