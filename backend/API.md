# Chess API Documentation

Base URL: `http://localhost:5001`

## Endpoints

### Health Check
```
GET /api/health
```
Returns API status and number of active games.

**Response:**
```json
{
  "status": "healthy",
  "active_games": 0
}
```

### Create New Game
```
POST /api/game/new
```
Creates a new chess game.

**Response:**
```json
{
  "success": true,
  "game_id": "game_1",
  "message": "New game created",
  "state": {
    "board": [...],
    "current_turn": "white",
    "game_status": "active",
    "move_count": 0
  }
}
```

### Get Game State
```
GET /api/game/<game_id>/state
```
Returns current state of the game.

**Response:**
```json
{
  "success": true,
  "game_id": "game_1",
  "state": {
    "board": [...],
    "current_turn": "white",
    "game_status": "active",
    "move_count": 0
  }
}
```

### Make Move
```
POST /api/game/<game_id>/move
Content-Type: application/json
```

**Request Body:**
```json
{
  "from": [6, 4],
  "to": [4, 4]
}
```

**Response:**
```json
{
  "success": true,
  "message": "Move successful",
  "state": {...}
}
```

### Get Move History
```
GET /api/game/<game_id>/history
```
Returns all moves made in the game.

**Response:**
```json
{
  "success": true,
  "game_id": "game_1",
  "history": [
    {
      "from": [6, 4],
      "to": [4, 4],
      "piece": "Pawn",
      "captured": null
    }
  ]
}
```

## Board Coordinates

Board uses array indices [row, col]:
- Row 0 = Black's back rank
- Row 7 = White's back rank
- Col 0-7 = a-h files

## Game Status Values

- `active` - Game in progress
- `check` - Current player is in check
- `checkmate` - Game over, current player is checkmated
- `stalemate` - Game over, stalemate
