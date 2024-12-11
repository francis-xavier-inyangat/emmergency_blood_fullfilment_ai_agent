#!/bin/bash

# Create frontend structure
mkdir -p frontend/src/{components,pages,services}
mkdir -p frontend/public

# Create backend structure
mkdir -p backend/src/{agents,api}
mkdir -p backend/tests

# Create docs directory
mkdir -p docs

# Create frontend files
touch frontend/src/App.jsx
touch frontend/src/index.jsx
touch frontend/package.json

# Create backend files
touch backend/src/agents/coordinator.py
touch backend/src/api/app.py
touch backend/requirements.txt

# Create documentation files
touch docs/setup.md
touch docs/api-docs.md

# Create root files
touch .gitignore
touch README.md

echo "Project structure created successfully!" 