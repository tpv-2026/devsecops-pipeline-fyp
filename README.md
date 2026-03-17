# DevSecOps CI/CD Pipeline (Final Year Project)

- This project rpesents the design and implementation of a **secure DevSecOps CI/CD pipeline**, integrating automated security testing
- The objective is to ensure that applications are continuously build, tested, and scanned for vulnerabilities before deployment

---

## Overview: 

- Traditional CI/CD pipelines focus on speed and automation, often overlooking security.
- This project enhances the pipeline by embedding **security checks at every stage**, following DevSecOps principles.

The pipeline automates: 
- Code integration
- Build processes
- Security scanning
- Deployment readiness

---

## Key Features: 

- Automated CI/CD pipelines using Kenkins
- Integrated security scanning tools:
    - Trivy (container vulnerability scanning)
    - OWASP Dependency Check (dependency vulnerabilities)
- Docker-based containerisation
- Continuous vulnerability detection
- Early identification of security risks

---

## Tech Stack: 
| Category         | Tools Used |
|--------------------------|
| CI/CD            | Jenkins |
| Security         | Trivy, OWASP Dependency Check |
| Containers       | Docker |
| Version Control  | GitHub |
| Languages        | Python, Bash, JavaScript |

---

## Pipeline Architecture:

The pipeline follows a secure DevSecOps workflows: 

1. Developer pushes code to GitHub
2. Jenkins pipeline is triggered automatically
3. Application is built
4. Security scans are executed:
  - Dependency scanning
  - Container image scanning
5. Vulnerability reports are generated
6. Application proceeds to deployment only if security checks pass

---

## Pipeline Flow: 

```text
Developer -> Github -> Jenkins -> Build -> Security Scans -> Report -> Deploy
