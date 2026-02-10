# Chess Game - Full Stack Application

A full-stack chess game with Python backend API and JavaScript frontend.

## Project Structure

```
back_end_dev_practice/
├── backend/          # Python Flask API for chess logic
├── frontend/         # HTML/CSS/JS chess interface
└── README.md
```

## Backend (Python)

Chess game logic and REST API built with Flask.

### Features
- Complete chess rule implementation
- Move validation
- Check and checkmate detection
- RESTful API endpoints

### Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Frontend (JavaScript)

Interactive chess board interface.

### Features
- Visual chess board
- Drag-and-drop piece movement
- Game state display
- Move history

### Setup
```bash
cd frontend
# Open index.html in browser or use a local server
python3 -m http.server 8080
```

## API Endpoints

- `POST /api/game/new` - Start new game
- `GET /api/game/state` - Get current board state
- `POST /api/game/move` - Make a move
- `GET /api/game/history` - Get move history

## Development

Built as a learning project for full-stack development.

## License

MIT
