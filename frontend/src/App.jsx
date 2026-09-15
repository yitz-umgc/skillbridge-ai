import { useState } from "react";
import { createEmployee, createProject, matchSkills } from "./api.js";

const initialEmployee = {
  name: "",
  email: "",
  skills: "",
};

const initialProject = {
  name: "",
  description: "",
  requiredSkills: "",
};

function parseSkills(value) {
  return [...new Set(
    value
      .split(",")
      .map((skill) => skill.trim())
      .filter(Boolean),
  )];
}

function SkillList({ items, emptyText }) {
  if (!items?.length) {
    return <p className="muted">{emptyText}</p>;
  }

  return (
    <div className="chips">
      {items.map((item) => (
        <span className="chip" key={item}>{item}</span>
      ))}
    </div>
  );
}

export default function App() {
  const [employee, setEmployee] = useState(initialEmployee);
  const [project, setProject] = useState(initialProject);
  const [result, setResult] = useState(null);
  const [savedRecords, setSavedRecords] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  function updateEmployee(event) {
    const { name, value } = event.target;
    setEmployee((current) => ({ ...current, [name]: value }));
  }

  function updateProject(event) {
    const { name, value } = event.target;
    setProject((current) => ({ ...current, [name]: value }));
  }

  async function handleSubmit(event) {
    event.preventDefault();
    setError("");
    setResult(null);
    setSavedRecords(null);

    const employeeSkills = parseSkills(employee.skills);
    const requiredSkills = parseSkills(project.requiredSkills);

    if (!employee.name.trim() || !employee.email.trim()) {
      setError("Employee name and email are required.");
      return;
    }

    if (!project.name.trim() || !project.description.trim()) {
      setError("Project name and description are required.");
      return;
    }

    if (requiredSkills.length === 0) {
      setError("Enter at least one required project skill.");
      return;
    }

    setLoading(true);

    try {
      const [createdEmployee, createdProject, matchResult] = await Promise.all([
        createEmployee({
          name: employee.name.trim(),
          email: employee.email.trim(),
          skills: employeeSkills,
        }),
        createProject({
          name: project.name.trim(),
          description: project.description.trim(),
          required_skills: requiredSkills,
        }),
        matchSkills(employeeSkills, requiredSkills),
      ]);

      setSavedRecords({ employee: createdEmployee, project: createdProject });
      setResult(matchResult);
    } catch (requestError) {
      setError(requestError.message || "Unable to analyze this match.");
    } finally {
      setLoading(false);
    }
  }

  function loadDemo() {
    setEmployee({
      name: "Alex Morgan",
      email: "alex.morgan@example.com",
      skills: "Python, SQL, Git",
    });
    setProject({
      name: "Internal Skills Dashboard",
      description: "Build and support an internal employee skills dashboard.",
      requiredSkills: "Python, SQL, Git, React",
    });
    setResult(null);
    setSavedRecords(null);
    setError("");
  }

  return (
    <main className="page-shell">
      <section className="hero">
        <div>
          <p className="eyebrow">Alpha Release</p>
          <h1>SkillBridge AI</h1>
          <p className="subtitle">
            Compare employee skills with project requirements and identify training needs.
          </p>
        </div>
        <button className="secondary-button" type="button" onClick={loadDemo}>
          Load Demo Data
        </button>
      </section>

      <form className="workspace" onSubmit={handleSubmit}>
        <section className="card">
          <div className="section-heading">
            <span className="step">1</span>
            <div>
              <h2>Employee</h2>
              <p>Enter the employee profile to evaluate.</p>
            </div>
          </div>

          <label>
            Name
            <input
              name="name"
              value={employee.name}
              onChange={updateEmployee}
              placeholder="Alex Morgan"
            />
          </label>

          <label>
            Email
            <input
              name="email"
              type="email"
              value={employee.email}
              onChange={updateEmployee}
              placeholder="alex.morgan@example.com"
            />
          </label>

          <label>
            Skills
            <input
              name="skills"
              value={employee.skills}
              onChange={updateEmployee}
              placeholder="Python, SQL, Git"
            />
            <span className="field-help">Separate skills with commas.</span>
          </label>
        </section>

        <section className="card">
          <div className="section-heading">
            <span className="step">2</span>
            <div>
              <h2>Project</h2>
              <p>Define the project and the skills it requires.</p>
            </div>
          </div>

          <label>
            Project name
            <input
              name="name"
              value={project.name}
              onChange={updateProject}
              placeholder="Internal Skills Dashboard"
            />
          </label>

          <label>
            Description
            <textarea
              name="description"
              rows="3"
              value={project.description}
              onChange={updateProject}
              placeholder="Describe the project."
            />
          </label>

          <label>
            Required skills
            <input
              name="requiredSkills"
              value={project.requiredSkills}
              onChange={updateProject}
              placeholder="Python, SQL, Git, React"
            />
            <span className="field-help">At least one required skill is needed.</span>
          </label>
        </section>

        <section className="submit-panel">
          {error && <div className="error-message" role="alert">{error}</div>}
          <button className="primary-button" type="submit" disabled={loading}>
            {loading ? "Analyzing…" : "Analyze Match"}
          </button>
        </section>
      </form>

      {result && (
        <section className="results card" aria-live="polite">
          <div className="section-heading">
            <span className="step">3</span>
            <div>
              <h2>Match Results</h2>
              <p>
                Employee #{savedRecords?.employee.id} compared with project #{savedRecords?.project.id}.
              </p>
            </div>
          </div>

          <div className="score-row">
            <div className="score-block">
              <span className="score-value">{result.match_score}%</span>
              <span className="score-label">Match score</span>
            </div>

            <div className="score-summary">
              <strong>{savedRecords?.employee.name}</strong>
              <span>→</span>
              <strong>{savedRecords?.project.name}</strong>
            </div>
          </div>

          <div className="result-grid">
            <div>
              <h3>Matched Skills</h3>
              <SkillList items={result.matched_skills} emptyText="No matching skills." />
            </div>

            <div>
              <h3>Missing Skills</h3>
              <SkillList items={result.missing_skills} emptyText="No missing skills." />
            </div>
          </div>

          <div className="recommendations">
            <h3>Training Recommendations</h3>
            {result.training_recommendations?.length ? (
              <ul>
                {result.training_recommendations.map((recommendation) => (
                  <li key={recommendation}>{recommendation}</li>
                ))}
              </ul>
            ) : (
              <p className="muted">No additional training recommended.</p>
            )}
          </div>
        </section>
      )}
    </main>
  );
}
