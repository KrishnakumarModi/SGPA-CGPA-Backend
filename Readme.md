# SGPA / CGPA Calculator API

A simple and lightweight **FastAPI backend** for calculating **SGPA (Semester Grade Point Average)** based on subject grades and credits.

This API is designed to work with a frontend such as **React + Tailwind CSS** and can be deployed using **Docker**.

---

## 🚀 Features

- Calculate SGPA from grades and credits
- Supports multiple subjects dynamically
- Grade-to-grade-point conversion
- Calculates:
  - Grade Point
  - Credit Points
  - Total Credits
  - Total Credit Points
  - SGPA
- Input validation using Pydantic
- REST API using FastAPI
- Interactive Swagger API documentation
- CORS support for frontend applications


---

## 🛠️ Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- Axios (for frontend API requests)

---

## For Frontend

- Visit 🔗 https://github.com/KrishnakumarModi/Sgpa-Cgpa-calculator

---

## 🧮 SGPA Calculation

The calculator uses the following formula:

```text
SGPA = Σ(Credit × Grade Point) / Σ(Credit)
```

### Example

| Subject                 | Grade | Grade Point | Credit |
| ----------------------- | ----- | ----------: | -----: |
| Compiler Design         | A+    |          10 |      4 |
| Artificial Intelligence | A     |           9 |      3 |
| Web Technology          | B+    |           8 |      3 |

Calculation:

```text
(4 × 10) + (3 × 8) + (3 × 9)
--------------------------------
        4 + 3 + 3

= 91 / 10

= 9.10
```

> **Note:** Grade points may vary depending on your university's grading system.

## 🔌 API

### Request Body

```json
{
  "subjects": [
    {
      "grade": "A+",
      "credit": 4
    },
    {
      "grade": "A",
      "credit": 3
    },
    {
      "grade": "B+",
      "credit": 3
    }
  ]
}
```

### Example Response

```json
{
  "total_credit": 10,
  "total_credit_points": 81,
  "sgpa": 8.1
}
```
---

## 📈 CGPA

The project can calculate CGPA using semester-wise SGPA and credits.

A commonly used weighted formula is:

```text
CGPA = Σ(SGPA × Semester Credit) / Σ(Semester Credit)
```

The exact calculation can be configured according to the grading system of the institution.

## 🔮 Future Improvements

* [ ] Add CGPA calculator API
* [ ] Add semester management
* [ ] Save calculation history
* [ ] Add database support
* [ ] Add multiple grading systems
* [ ] Add result download
* [ ] Add result sharing
* [ ] Deploy the application
* [ ] Add dark mode
* [ ] Improve mobile responsiveness
---

## 👨‍💻 Author

**Krishna Kumar Modi**

Built as a learning project using **React, Tailwind CSS, FastAPI, and Python**.


