# HSN Code Validation Agent

An intelligent FastAPI-based validation agent to verify the correctness of HSN (Harmonized System Nomenclature) codes using a master dataset.

---

## Project Summary

This agent:
- Accepts one or more HSN codes as input (via API)
- Validates each code for:
  -  Format (2–8 digits, numeric)
  -  Existence in the master Excel file
  -  Hierarchical validity of parent levels (optional)
- Returns structured JSON response with validation results

---

## Tech Stack

- **Language:** Python 3.12
- **Framework:** FastAPI
- **Data Handling:** Pandas
- **File Input:** `HSN_Master_Data.xlsx`
- **Validation Logic:** Format → Existence → Hierarchy

---

## How to Run

### Setup

```bash
git clone https://github.com/yourusername/hsn-code-validator-agent.git
cd hsn-code-validator-agent
pip install -r requirements.txt
uvicorn app:app --reload
# hsn-code-validator-agent
