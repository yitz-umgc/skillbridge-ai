# SkillBridge AI Frontend

React/Vite frontend for the SkillBridge AI Alpha release.

## Run locally

Start the FastAPI backend on port 8000 first. Then, from this `frontend` directory:

```bash
npm install
npm run dev
```

Open the URL printed by Vite (normally `http://localhost:5173`).

The Vite development server proxies `/employees`, `/projects`, and `/match` requests to `http://localhost:8000`.

## Alpha workflow

1. Enter an employee name, email, and comma-separated skills.
2. Enter a project name, description, and comma-separated required skills.
3. Select **Analyze Match**.
4. The frontend creates the employee and project records, calls the matching endpoint, and displays the match score, matched skills, missing skills, and training recommendations.

## Optional API URL

For an environment where the API is hosted separately, set `VITE_API_BASE_URL` before building or running the frontend.
