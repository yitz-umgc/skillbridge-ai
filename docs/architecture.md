# SkillBridge AI Alpha Architecture

## Overview

SkillBridge AI uses a client-server architecture. The React frontend collects employee and project information and communicates with a FastAPI backend over JSON REST endpoints. The backend separates employee/project data handling from the skill-matching service.

## Component Diagram

```text
User
  |
  v
React Frontend
  |
  | REST / JSON
  v
FastAPI Backend
  |----------------------|-----------------------|
  v                      v                       v
/employees/           /projects/              /match
Employee API          Project API             Matching Route
  |                      |                       |
  v                      v                       v
Employee schema       Project schema      Matching Service
                                                  |
                                      -------------------------
                                      |           |           |
                                      v           v           v
                                  Match score  Missing     Training
                                               skills    recommendations
```

## Frontend Responsibilities

- Collect employee name, email, and skills.
- Collect project name, description, and required skills.
- Create employee and project records through the backend API.
- Send employee skills and project requirements to `/match`.
- Display match score, matched skills, missing skills, and training recommendations.
- Present loading and API error states to the user.

## Backend Responsibilities

- Validate employee and project request data.
- Provide employee and project REST endpoints.
- Route match requests to the matching service.
- Calculate deterministic skill overlap for the Alpha release.
- Generate introductory training recommendations for missing skills.

## Primary Data Flow

1. A user enters an employee profile and project requirements in the React frontend.
2. The frontend sends the employee to `POST /employees/`.
3. The frontend sends the project to `POST /projects/`.
4. The frontend sends `employee_skills` and `required_skills` to `POST /match`.
5. FastAPI delegates the matching request to the matching service.
6. The service returns the match score, matched skills, missing skills, and training recommendations.
7. The frontend renders the results.

## Alpha Constraints

The Alpha intentionally uses simplified in-memory data handling and deterministic skill overlap. Production persistence, authentication/authorization, semantic skill matching, and broader system-level testing remain future enhancements.
