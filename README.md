# enterprise-ci-cd
![Build Status](https://github.com/LakshayJakhar/enterprise-ci-cd/actions/workflows/ci.yml/badge.svg)

# Enterprise CI/CD Python Project

![Python](https://img.shields.io/badge/Python-3.10-blue)
![GitHub Actions](https://img.shields.io/github/actions/workflow/status/LakshayJakhar/enterprise-ci-cd/ci.yml?branch=main)
![Docker](https://img.shields.io/badge/Docker-Ready-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**One-liner:**  
Professional Python Flask project demonstrating CI/CD pipelines, automated testing, code quality checks, security scanning, and Docker deployment.

---

## Table of Contents
1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Technologies Used](#technologies-used)  
4. [Setup & Installation](#setup--installation)  
5. [CI/CD Pipeline](#cicd-pipeline)  
6. [Usage](#usage)  
7. [Folder Structure](#folder-structure)  
8. [Contributing](#contributing)  
9. [License](#license)  

---

## Project Overview
This project is a Python Flask application designed to showcase **modern DevOps practices**.  
It includes:  
- Automated **CI pipeline** (linting, testing, code formatting, security scans)  
- **Dockerized** application for consistent deployments  
- **CD pipeline** to Railway with workflow notifications via Discord  

It’s a perfect portfolio piece to demonstrate real-world Python development and DevOps skills.

---

## Features
- Python Flask web application  
- CI pipeline using GitHub Actions:  
  - Linting (`flake8`)  
  - Code formatting check (`black`)  
  - Security scanning (`Bandit`)  
  - Dependency vulnerability scanning (`Safety`)  
  - Unit tests & coverage (`pytest` + `pytest-cov`)  
- Dockerized for consistent deployments  
- CD pipeline to Railway (deploys only if CI passes)  
- Discord notifications for CI/CD workflow status  

---

## Technologies Used
- **Python 3.10 / 3.11**  
- **Flask**  
- **GitHub Actions** (CI/CD)  
- **Docker**  
- **Railway**  
- **flake8, black, Bandit, Safety, pytest, pytest-cov**  

---

## Setup & Installation

# 1. Clone the repository
git clone https://github.com/LakshayJakhar/enterprise-ci-cd.git
cd enterprise-ci-cd

# 2. Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the Flask app
python src/main.py

# 5. Open in browser
