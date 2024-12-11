@echo off

REM Create frontend structure
mkdir frontend\src\components
mkdir frontend\src\pages
mkdir frontend\src\services
mkdir frontend\public

REM Create backend structure
mkdir backend\src\agents
mkdir backend\src\api
mkdir backend\tests

REM Create docs directory
mkdir docs

REM Create frontend files
type nul > frontend\src\App.jsx
type nul > frontend\src\index.jsx
type nul > frontend\package.json

REM Create backend files
type nul > backend\src\agents\coordinator.py
type nul > backend\src\api\app.py
type nul > backend\requirements.txt

REM Create documentation files
type nul > docs\setup.md
type nul > docs\api-docs.md

REM Create root files
type nul > .gitignore
type nul > README.md

echo Project structure created successfully! 