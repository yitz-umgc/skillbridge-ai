# SkillBridge AI

SkillBridge AI is an intelligent workforce skill-matching platform that helps managers compare employee skills with project requirements, identify skill gaps, and recommend relevant training.

This repository contains the Unit 5 Alpha Release.

## Alpha Features

- Employee profile management
- Project requirement management
- AI-assisted skill matching
- Match score calculation
- Identification of matched and missing skills
- Training recommendations based on skill gaps
- React frontend integrated with a FastAPI backend
- Automated testing and GitHub Actions CI

## Project Structure

- `frontend/` - React user interface
- `backend/` - FastAPI backend, API routes, matching service, and automated tests
- `docs/` - System architecture and technical debt documentation
- `.github/workflows/` - GitHub Actions CI configuration

## Backend Setup

From the `backend` directory, install the required dependencies:

    python -m pip install -r requirements.txt

Run the automated tests:

    python -m pytest

Start the FastAPI backend:

    python -m uvicorn app.main:app --reload

The backend runs at `http://127.0.0.1:8000`.

FastAPI interactive API documentation is available at `http://127.0.0.1:8000/docs`.

## Frontend Setup

From the `frontend` directory, install the dependencies:

    npm install

Start the React development server:

    npm run dev

Open `http://localhost:5173` in a web browser.

## Using the Alpha

1. Enter employee information and a comma-separated list of employee skills.
2. Enter project information and the project's required skills.
3. Select **Analyze Match**.
4. SkillBridge AI displays the match score, matched skills, missing skills, and training recommendations.

## Testing and Continuous Integration

The project uses automated tests and GitHub Actions to validate the Alpha release. The CI workflow runs backend tests and frontend build validation on supported pushes and pull requests.

## Current Technical Debt

The Alpha release intentionally contains several limitations that are documented in `docs/technical-debt.md`, including simplified deterministic skill matching, basic training recommendations, limited persistence, limited production authentication, and limited automated test coverage.

These items are documented with proposed mitigation strategies for future releases.

## Team

- Sullivan Begbie - Lead Architect
- Walter Bibbins - Interface Designer
- Yitz Taragin - Integration Lead
