# SkillBridge AI User Manual

## Overview

SkillBridge AI helps managers compare an employee's skills with the skills required for a project. The system calculates a match score, identifies matched and missing skills, and recommends training based on identified skill gaps.

## Starting the Application

Before using SkillBridge AI, the backend and frontend must be running.

### Backend

From the `backend` directory:

    python -m pip install -r requirements.txt
    python -m uvicorn app.main:app --reload

The backend runs at:

    http://127.0.0.1:8000

### Frontend

From the `frontend` directory:

    npm install
    npm run dev

Open the local address displayed by Vite, typically:

    http://localhost:5173

## Using SkillBridge AI

### 1. Enter Employee Information

Enter the employee's name and skills. Skills should be entered as a comma-separated list.

Example:

    Python, SQL, Git

### 2. Enter Project Information

Enter the project name and the skills required for the project.

Example:

    Python, SQL, Git, React

### 3. Analyze the Match

Select **Analyze Match**.

SkillBridge AI compares the employee's skills with the project's required skills.

### 4. Review the Results

The system displays:

- **Match Score** - Percentage of required project skills matched by the employee
- **Matched Skills** - Required skills the employee already has
- **Missing Skills** - Required skills not found in the employee's profile
- **Training Recommendations** - Suggested introductory training based on missing skills

For example, an employee with Python, SQL, and Git skills compared with a project requiring Python, SQL, Git, and React receives a 75% match score and a recommendation for introductory React training.

## Important Limitations

The current system is a project prototype. Skill matching is deterministic and based on normalized skill names rather than semantic similarity or a trained machine-learning model.

Training recommendations are generated directly from identified skill gaps and are not personalized learning plans.

The current version should support human decision-making rather than make employment decisions automatically.

## API Documentation

When the backend is running, interactive FastAPI documentation is available at:

    http://127.0.0.1:8000/docs

## Troubleshooting

If the frontend cannot return matching results:

1. Confirm that the FastAPI backend is running.
2. Confirm that the React frontend is running.
3. Verify that employee and project skills were entered.
4. Review the backend terminal for errors.
5. Run `python -m pytest` from the `backend` directory to verify the automated tests.
