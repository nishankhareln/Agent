from pydantic import BaseModel
from typing  import List
    
class Experience(BaseModel):
    company: str
    position: str
    start_date: str
    end_date: str
    description: str

class Skill(BaseModel):
    name:str
    level:str

class Project(BaseModel):
    title: str
    description: str
    technologies: List[str]
    link: str

class Education(BaseModel):
    institution: str
    degree: str
    start_date: str
    end_date: str

class StructuredResume(BaseModel):
    name: str
    email: str
    phone: str
    summary: str
    experiences: List[Experience]
    skills: List[Skill]
    projects: List[Project]
    education: List[Education]
    