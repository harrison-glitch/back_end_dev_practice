# Building Full-Stack Projects with Kiro CLI

A comprehensive guide for creating full-stack web applications using Kiro CLI, based on the chess game project.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Project Planning](#project-planning)
3. [Repository Setup](#repository-setup)
4. [Backend Development](#backend-development)
5. [Frontend Development](#frontend-development)
6. [Testing & Documentation](#testing--documentation)
7. [Best Practices](#best-practices)
8. [Common Patterns](#common-patterns)

---

## Prerequisites

### Required Tools
- **Kiro CLI** - AI-powered development assistant
- **Python 3.9+** - Backend development
- **Git** - Version control
- **GitHub Account** - Code hosting
- **Modern Browser** - Testing

### Recommended Knowledge
- Basic Python programming
- HTML/CSS/JavaScript fundamentals
- REST API concepts
- Git basics

---

## Project Planning

### Step 1: Define Your Project

Ask Kiro to help you plan:
```
"I want to build a [project type] with [features]. 
Please help me create a plan with both frontend and backend."
```

**Example:**
```
"I want to build a task manager with user authentication, 
task CRUD operations, and a web interface."
```

### Step 2: Review the Plan

Kiro will create a structured plan with phases:
- Phase 1: Repository Setup
- Phase 2: Backend Core Logic
- Phase 3: Backend API Layer
- Phase 4: Frontend UI Structure
- Phase 5: Frontend Integration
- Phase 6: Testing & Documentation

**Always approve the plan before proceeding!**

---

## Repository Setup

### Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Name your repository (e.g., `my-project`)
3. Choose public or private
4. **Don't** initialize with README
5. Copy the repository URL

### Step 2: Tell Kiro to Set Up Project

```
"Set up the project at ~/Projects/my-project with this GitHub URL:
https://github.com/username/my-project.git"
```

Kiro will:
- Create project directory
- Initialize Git
- Set up monorepo structure (backend/ and frontend/)
- Create virtual environment
- Make initial commit

### Step 3: Authenticate with GitHub

If needed:
```bash
gh auth login
```
Follow prompts to authenticate.

---

## Backend Development

### Phase 1: Core Logic

#### Step 1: Define Your Data Models

Ask Kiro:
```
"Create Python classes for [your domain objects]"
```

**Example:**
```
"Create Python classes for Task with title, description, 
status, and due_date"
```

#### Step 2: Implement Business Logic

```
"Add methods to create, update, delete, and list tasks"
```

Kiro will:
- Create class files
- Implement methods
- Add validation logic

#### Step 3: Test Core Logic

```
"Create a test file to verify the task operations work"
```

Run tests:
```bash
cd backend
python test_tasks.py
```

### Phase 2: API Layer

#### Step 1: Set Up Flask

```
"Create a Flask API with endpoints for task operations"
```

Kiro will:
- Create `requirements.txt`
- Install Flask and Flask-CORS
- Set up `app.py` with routes

#### Step 2: Define Endpoints

Standard REST endpoints:
- `POST /api/resource/new` - Create
- `GET /api/resource/<id>` - Read
- `PUT /api/resource/<id>` - Update
- `DELETE /api/resource/<id>` - Delete
- `GET /api/resource/list` - List all

#### Step 3: Test API

```
"Test the API endpoints with curl commands"
```

Kiro will run tests and show results.

---

## Frontend Development

### Phase 1: UI Structure

#### Step 1: Create HTML Layout

```
"Create an HTML page with [describe your UI layout]"
```

**Example:**
```
"Create an HTML page with a header, task list, 
and form to add new tasks"
```

#### Step 2: Style with CSS

```
"Add CSS styling with [describe your design preferences]"
```

**Example:**
```
"Add CSS styling with a modern gradient background, 
card-based layout, and smooth animations"
```

### Phase 2: JavaScript Integration

#### Step 1: Connect to API

```
"Create JavaScript to fetch tasks from the API and display them"
```

#### Step 2: Add Interactivity

```
"Add click handlers to create, update, and delete tasks"
```

#### Step 3: Add Polish

```
"Add keyboard shortcuts, loading states, and error messages"
```

---

## Testing & Documentation

### Step 1: Create Tests

```
"Create integration tests for the API"
```

Run tests:
```bash
cd backend
python test_integration.py
```

### Step 2: Write Documentation

```
"Create a comprehensive README with setup instructions"
```

### Step 3: Create Testing Guide

```
"Create a testing checklist for manual testing"
```

---

## Best Practices

### 1. Always Use Virtual Environments

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # Always activate before installing
```

### 2. Commit Frequently

After each phase:
```bash
git add .
git commit -m "Descriptive message about what was added"
git push
```

### 3. Test as You Build

Don't wait until the end:
- Test core logic before building API
- Test API before building frontend
- Test frontend features as you add them

### 4. Use Descriptive Names

- **Variables:** `camelCase` (e.g., `currentUser`)
- **Classes:** `PascalCase` (e.g., `TaskManager`)
- **Files:** `snake_case` (e.g., `task_manager.py`)
- **CSS classes:** `kebab-case` (e.g., `task-card`)

### 5. Handle Errors Gracefully

Always include:
- Try-catch blocks in JavaScript
- Error responses in API
- User-friendly error messages

---

## Common Patterns

### Pattern 1: CRUD Application

**Use for:** Task managers, note apps, inventory systems

**Structure:**
```
backend/
  ├── models.py      # Data classes
  ├── storage.py     # Data persistence
  ├── app.py         # API endpoints
frontend/
  ├── index.html     # UI layout
  ├── style.css      # Styling
  ├── app.js         # API integration
```

**Key Features:**
- Create, Read, Update, Delete operations
- List view with filtering
- Form validation
- Confirmation dialogs

### Pattern 2: Game Application

**Use for:** Board games, puzzles, interactive games

**Structure:**
```
backend/
  ├── pieces.py      # Game pieces/entities
  ├── board.py       # Game state and rules
  ├── app.py         # API for game actions
frontend/
  ├── index.html     # Game board UI
  ├── style.css      # Visual styling
  ├── app.js         # Game interaction
```

**Key Features:**
- Turn-based logic
- Move validation
- Game state management
- Visual feedback

### Pattern 3: Dashboard Application

**Use for:** Analytics, monitoring, data visualization

**Structure:**
```
backend/
  ├── data_source.py # Data fetching
  ├── analytics.py   # Data processing
  ├── app.py         # API endpoints
frontend/
  ├── index.html     # Dashboard layout
  ├── style.css      # Chart styling
  ├── app.js         # Data visualization
```

**Key Features:**
- Real-time updates
- Charts and graphs
- Filtering and sorting
- Export functionality

---

## Kiro-Specific Tips

### 1. Be Specific in Requests

❌ **Vague:** "Add some features"
✅ **Specific:** "Add a delete button for each task with confirmation dialog"

### 2. Request One Phase at a Time

❌ **Too much:** "Build the entire backend and frontend"
✅ **Incremental:** "Create the Task class with CRUD methods"

### 3. Ask for Explanations

```
"Explain how the move validation works in the chess logic"
```

### 4. Request Improvements

```
"Add animations when tasks are added or removed"
```

### 5. Debug with Kiro

```
"The API is returning 404 errors. Help me debug this."
```

---

## Example Project Ideas

### Beginner Level
1. **Todo List** - Tasks with priorities and due dates
2. **Note Taking App** - Create, edit, and organize notes
3. **Contact Manager** - Store and search contacts
4. **Recipe Book** - Save and categorize recipes

### Intermediate Level
1. **Expense Tracker** - Track spending with categories
2. **Habit Tracker** - Daily habit logging with streaks
3. **Quiz App** - Multiple choice questions with scoring
4. **Weather Dashboard** - Display weather data from API

### Advanced Level
1. **Chat Application** - Real-time messaging
2. **E-commerce Store** - Products, cart, checkout
3. **Project Management** - Tasks, teams, timelines
4. **Social Media Feed** - Posts, likes, comments

---

## Troubleshooting

### Port Already in Use

**Problem:** `Address already in use`

**Solution:**
```bash
# Find process using port
lsof -i :5001

# Kill the process
kill <PID>

# Or use different port in app.py
app.run(port=5002)
```

### CORS Errors

**Problem:** Frontend can't access backend

**Solution:**
- Ensure Flask-CORS is installed
- Check API_URL in frontend matches backend port
- Verify backend is running

### Virtual Environment Issues

**Problem:** Packages not found

**Solution:**
```bash
# Always activate venv first
cd backend
source venv/bin/activate

# Then install
pip install -r requirements.txt
```

### Git Authentication

**Problem:** Push fails with authentication error

**Solution:**
```bash
# Use GitHub CLI
gh auth login

# Or use token in URL
git push https://$(gh auth token)@github.com/user/repo.git main
```

---

## Quick Reference Commands

### Start Backend
```bash
cd backend
source venv/bin/activate
python app.py
```

### Start Frontend
```bash
cd frontend
python3 -m http.server 8080
```

### Run Tests
```bash
cd backend
source venv/bin/activate
python test_integration.py
```

### Commit Changes
```bash
git add .
git commit -m "Description of changes"
git push
```

### Create New Branch
```bash
git checkout -b feature-name
```

---

## Next Steps

After completing your first project:

1. **Add More Features** - Expand functionality
2. **Improve UI/UX** - Better design and interactions
3. **Add Database** - Replace in-memory storage
4. **Deploy Online** - Host on Heroku, AWS, or Vercel
5. **Add Authentication** - User login and sessions
6. **Build Another Project** - Practice makes perfect!

---

## Resources

### Documentation
- Flask: https://flask.palletsprojects.com/
- JavaScript MDN: https://developer.mozilla.org/en-US/docs/Web/JavaScript
- CSS Tricks: https://css-tricks.com/

### Learning
- Python Tutorial: https://docs.python.org/3/tutorial/
- Web Development: https://www.freecodecamp.org/
- Git Guide: https://git-scm.com/book/en/v2

### Tools
- GitHub CLI: https://cli.github.com/
- Postman: https://www.postman.com/ (API testing)
- VS Code: https://code.visualstudio.com/

---

## Conclusion

Building full-stack projects with Kiro CLI:
1. ✅ Start with a clear plan
2. ✅ Build incrementally (backend → API → frontend)
3. ✅ Test at each phase
4. ✅ Document as you go
5. ✅ Commit frequently
6. ✅ Ask Kiro for help when stuck

**Remember:** Kiro is your AI pair programmer. Be specific, ask questions, and iterate on your ideas!

Happy coding! 🚀
