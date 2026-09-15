const API_BASE = import.meta.env.VITE_API_BASE_URL ?? "";

async function postJson(path, payload) {
  const response = await fetch(`${API_BASE}${path}`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    let detail = `Request failed with status ${response.status}`;

    try {
      const body = await response.json();
      if (body.detail) {
        detail = typeof body.detail === "string" ? body.detail : JSON.stringify(body.detail);
      }
    } catch {
      // Keep the default status-based message if no JSON body is returned.
    }

    throw new Error(detail);
  }

  return response.json();
}

export function createEmployee(employee) {
  return postJson("/employees/", employee);
}

export function createProject(project) {
  return postJson("/projects/", project);
}

export function matchSkills(employeeSkills, requiredSkills) {
  return postJson("/match", {
    employee_skills: employeeSkills,
    required_skills: requiredSkills,
  });
}
