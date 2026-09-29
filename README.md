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

## Testing, Performance, and Continuous Integration

SkillBridge AI uses automated testing and GitHub Actions to validate the integrated system on pushes and pull requests.

Current validation includes:

- 11 automated backend tests
- 11/11 tests passing in the final CI run
- 76% overall backend code coverage
- 100% coverage of the core matching service
- 100% coverage of the matching API route
- Automated React frontend build validation
- Matching-service performance benchmark

The matching-service benchmark executes 1,000 matching operations with a performance requirement of completing in under 1 second. In the recorded GitHub Actions run, 1,000 operations completed in approximately 0.005 seconds.

The benchmark measures the core matching service only and should not be interpreted as end-to-end application response time.

## Documentation

Additional project documentation is available in the `docs/` directory:

- `docs/architecture.md` - System architecture and integration design
- `docs/technical-debt.md` - Known technical debt and planned mitigation
- `docs/user-manual.md` - Installation, usage, limitations, and troubleshooting
- FastAPI interactive API documentation is available at `/docs` while the backend is running

## Current Technical Debt

The Alpha release intentionally contains several limitations that are documented in `docs/technical-debt.md`, including simplified deterministic skill matching, basic training recommendations, limited persistence, limited production authentication, and limited automated test coverage.

These items are documented with proposed mitigation strategies for future releases.

## Team

- Sullivan Begbie - Lead Architect
- Walter Bibbins - Interface Designer
- Yitz Taragin - Integration Lead
