# SkillBridge AI - Alpha Technical Debt

The Alpha release intentionally prioritizes a stable, demonstrable end-to-end workflow over production-level complexity. The following technical debt has been identified for future development.

## 1. Simplified Skill-Matching Algorithm

The current matching service uses deterministic skill overlap to calculate match scores rather than a trained NLP or machine-learning model.

**Impact:** The Alpha can accurately demonstrate the matching workflow, but it does not yet recognize related skills, synonyms, experience levels, or semantic similarity.

**Mitigation:** Future versions can incorporate NLP embeddings or an established machine-learning library while preserving the current matching service interface.

## 2. Simplified Training Recommendations

Training recommendations are currently generated directly from missing skills.

**Impact:** Recommendations demonstrate the required workflow but are not yet personalized based on employee experience, training history, or available courses.

**Mitigation:** Future releases can connect missing skills to a structured training catalog and rank recommendations based on employee needs.

## 3. Limited Persistence and Production Data

The Alpha uses a simplified data environment rather than production workforce data.

**Impact:** This limits testing against large, diverse real-world datasets.

**Mitigation:** PostgreSQL persistence and larger synthetic datasets can be expanded before production deployment.

## 4. Limited Security and Authentication

The current Alpha matching endpoint does not yet implement production-level authentication and authorization.

**Impact:** The endpoint should not be exposed to sensitive employee data in a production environment.

**Mitigation:** Future development will add authenticated manager access, role-based authorization, secure configuration, and appropriate data protections.

## 5. Limited Automated Test Coverage

The current automated test suite covers core matching behavior, edge cases, and the matching API endpoint but does not yet provide comprehensive system-level testing.

**Impact:** Future modules and frontend/backend interactions may introduce integration issues not covered by the current tests.

**Mitigation:** Test coverage will expand as employee, project, database, and frontend modules are integrated.
