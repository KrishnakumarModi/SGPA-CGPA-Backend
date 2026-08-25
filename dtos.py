from pydantic import BaseModel


GRADE_POINTS = {
    "A+": 10,
    "A": 9,
    "B+": 8,
    "B": 7,
    "C+": 6,
    "C": 5,
    "F": 0
}



class Subject(BaseModel):
    grade: str
    credit: float



class SGPARequest(BaseModel):
    subjects: list[Subject]
