from fastapi import FastAPI,HTTPException
from dtos import SGPARequest,GRADE_POINTS
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins= os.getenv("origin"),
    allow_credentials= True,
    allow_methods= ["POST"],
    allow_headers= ["*"],
)

@app.get("/")
def home():
    return {
        "message": "SGPA API is running"
    }


@app.post("/calculate-sgpa")

def calculate_sgpa(data: SGPARequest):

    total_credit = 0
    total_credit_points = 0

    result = []

    for subject in data.subjects:

        grade = subject.grade.upper()

        if grade not in GRADE_POINTS:
            raise HTTPException(
                status_code=400,
                detail=f"Invalid grade: {subject.grade}"
            )

        grade_point = GRADE_POINTS[grade]

        credit_points = subject.credit * grade_point

        total_credit += subject.credit
        total_credit_points += credit_points

        result.append({
    
            "grade": grade,
            "credit": subject.credit,
            "grade_point": grade_point,
            "credit_points": credit_points
        })

    if total_credit == 0:
        raise HTTPException(
            status_code=400,
            detail="Total credit cannot be zero"
        )

    sgpa = total_credit_points / total_credit

    return {
        "subjects": result,
        "total_credit": total_credit,
        "total_credit_points": total_credit_points,
        "sgpa": round(sgpa, 2)
    }