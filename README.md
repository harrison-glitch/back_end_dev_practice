# Chess Game - Full Stack Application

A full-stack chess game with Python backend API and JavaScript frontend. Play chess in your browser with full rule validation, check/checkmate detection, and move history tracking.

![Chess Game](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.0.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## Features

### Backend (Python + Flask)
- ✅ Complete chess rule implementation for all pieces
- ✅ Move validation with check/checkmate detection
- ✅ Stalemate detection
- ✅ RESTful API with CORS support
- ✅ Move history tracking
- ✅ Multiple concurrent games support

### Frontend (HTML + CSS + JavaScript)
- ✅ Interactive chess board with drag-and-click
- ✅ Visual feedback for valid moves
- ✅ Real-time game status display
- ✅ Move history with algebraic notation
- ✅ Keyboard shortcuts (ESC, N)
- ✅ Responsive design
- ✅ Smooth animations and transitions

## Project Structure

```
back_end_dev_practice/
├── backend/
│   ├── app.py              # Flask REST API
│   ├── board.py            # Chess board and game logic
│   ├── pieces.py           # Chess piece classes
│   ├── test_chess.py       # Unit tests
│   ├── requirements.txt    # Python dependencies
│   ├── API.md             # API documentation
│   └── venv/              # Virtual environment
├── frontend/
│   ├── index.html         # Main HTML page
│   ├── style.css          # Styling and animations
│   └── app.js             # Game logic and API integration
└── README.md
```

## Quick Start

### Prerequisites
- Python 3.9 or higher
- Modern web browser (Chrome, Firefox, Safari, Edge)

### Backend Setup

1. **Navigate to backend directory:**
```bash
cd backend
```

2. **Create and activate virtual environment:**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Start the API server:**
```bash
python app.py
```

Backend will be available at `http://localhost:5001`

### Frontend Setup

1. **Navigate to frontend directory:**
```bash
cd frontend
```

2. **Start a local web server:**
```bash
python3 -m http.server 8080
```

3. **Open in browser:**
```
http://localhost:8080
```

## How to Play

1. **Start a new game** - Click "New Game" button or press `N`
2. **Select a piece** - Click on any piece of your color (white starts)
3. **See valid moves** - Green dots show where you can move
4. **Make a move** - Click on a highlighted square
5. **Clear selection** - Press `ESC` to deselect
6. **View history** - See all moves in the sidebar

## Keyboard Shortcuts

- `ESC` - Clear current selection
- `N` - Start new game (with confirmation)

## API Endpoints

### Health Check
```
GET /api/health
```

### Create New Game
```
POST /api/game/new
```

### Get Game State
```
GET /api/game/<game_id>/state
```

### Make Move
```
POST /api/game/<game_id>/move
Content-Type: application/json

{
  "from": [6, 4],
  "to": [4, 4]
}
```

### Get Move History
```
GET /api/game/<game_id>/history
```

See [API.md](backend/API.md) for detailed documentation.

## Testing

### Run Backend Tests
```bash
cd backend
source venv/bin/activate
python test_chess.py
```

### Manual Testing Checklist
- [ ] Create new game
- [ ] Move white pawn
- [ ] Move black pawn
- [ ] Test invalid moves (wrong turn, illegal move)
- [ ] Test check detection
- [ ] Test checkmate scenario
- [ ] Test keyboard shortcuts
- [ ] Test move history display

## Architecture

### Backend
- **Flask** - REST API framework
- **Flask-CORS** - Cross-origin resource sharing
- **Python Classes** - Object-oriented chess logic

### Frontend
- **Vanilla JavaScript** - No frameworks, pure JS
- **CSS Grid** - Chess board layout
- **Fetch API** - Backend communication

## Development

### Adding New Features

1. **Backend changes:**
   - Modify `pieces.py` for piece logic
   - Update `board.py` for game rules
   - Add endpoints in `app.py`

2. **Frontend changes:**
   - Update `app.js` for game logic
   - Modify `style.css` for styling
   - Edit `index.html` for structure

### Code Style
- Python: PEP 8
- JavaScript: ES6+
- CSS: BEM-like naming

## Known Limitations

- No en passant capture
- No castling
- No pawn promotion
- Games stored in memory (lost on server restart)
- Single-player only (no AI opponent)

## Future Enhancements

- [ ] Add castling support
- [ ] Add en passant capture
- [ ] Add pawn promotion
- [ ] Implement AI opponent
- [ ] Add game persistence (database)
- [ ] Add multiplayer support
- [ ] Add game timer
- [ ] Add move undo/redo

## Troubleshooting

**Port already in use:**
```bash
# Change port in app.py (backend) or use different port for frontend
python3 -m http.server 8081
```

**CORS errors:**
- Ensure backend is running on port 5001
- Check API_URL in frontend/app.js

**Moves not working:**
- Check browser console for errors
- Verify backend is running
- Test API with curl

## License

MIT License - feel free to use for learning and projects!

## Contributing

This is a learning project. Feel free to fork and experiment!

## Author

Built as a full-stack development practice project.

---

**Enjoy playing chess!** ♟️
