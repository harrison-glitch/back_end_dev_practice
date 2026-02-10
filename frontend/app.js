// Chess piece Unicode symbols
const PIECE_SYMBOLS = {
    'white': {
        'King': '♔',
        'Queen': '♕',
        'Rook': '♖',
        'Bishop': '♗',
        'Knight': '♘',
        'Pawn': '♙'
    },
    'black': {
        'King': '♚',
        'Queen': '♛',
        'Rook': '♜',
        'Bishop': '♝',
        'Knight': '♞',
        'Pawn': '♟'
    }
};

const API_URL = 'http://localhost:5001/api';
let currentGameId = null;
let selectedSquare = null;
let gameState = null;

// Initialize game on page load
document.addEventListener('DOMContentLoaded', () => {
    document.getElementById('new-game-btn').addEventListener('click', createNewGame);
    createNewGame();
});

// Create new game
async function createNewGame() {
    try {
        const response = await fetch(`${API_URL}/game/new`, {
            method: 'POST'
        });
        const data = await response.json();
        
        if (data.success) {
            currentGameId = data.game_id;
            gameState = data.state;
            renderBoard(gameState.board);
            updateGameInfo(gameState);
            showMessage('New game started!', 'success');
        } else {
            showMessage('Failed to create game: ' + data.error, 'error');
        }
    } catch (error) {
        showMessage('Error connecting to server: ' + error.message, 'error');
    }
}

// Render chess board
function renderBoard(board) {
    const boardElement = document.getElementById('chess-board');
    boardElement.innerHTML = '';
    
    for (let row = 0; row < 8; row++) {
        for (let col = 0; col < 8; col++) {
            const square = document.createElement('div');
            square.className = 'square';
            square.className += (row + col) % 2 === 0 ? ' light' : ' dark';
            square.dataset.row = row;
            square.dataset.col = col;
            
            const piece = board[row][col];
            if (piece) {
                square.textContent = PIECE_SYMBOLS[piece.color][piece.type];
            }
            
            square.addEventListener('click', () => handleSquareClick(row, col));
            boardElement.appendChild(square);
        }
    }
}

// Handle square click
function handleSquareClick(row, col) {
    if (!currentGameId) return;
    
    const clickedSquare = document.querySelector(`[data-row="${row}"][data-col="${col}"]`);
    
    // If no square selected, select this one
    if (!selectedSquare) {
        const piece = gameState.board[row][col];
        if (piece && piece.color === gameState.current_turn) {
            selectedSquare = { row, col };
            clickedSquare.classList.add('selected');
            showMessage(`Selected ${piece.type}. Click a square to move.`, 'info');
        }
    } else {
        // Try to move to clicked square
        makeMove(selectedSquare.row, selectedSquare.col, row, col);
        clearSelection();
    }
}

// Make a move
async function makeMove(fromRow, fromCol, toRow, toCol) {
    try {
        const response = await fetch(`${API_URL}/game/${currentGameId}/move`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                from: [fromRow, fromCol],
                to: [toRow, toCol]
            })
        });
        
        const data = await response.json();
        
        if (data.success) {
            gameState = data.state;
            renderBoard(gameState.board);
            updateGameInfo(gameState);
            showMessage(data.message, 'success');
            
            if (gameState.game_status === 'checkmate') {
                const winner = gameState.current_turn === 'white' ? 'Black' : 'White';
                showMessage(`Checkmate! ${winner} wins!`, 'success');
            } else if (gameState.game_status === 'check') {
                showMessage(`${gameState.current_turn} is in check!`, 'info');
            } else if (gameState.game_status === 'stalemate') {
                showMessage('Stalemate! Game is a draw.', 'info');
            }
        } else {
            showMessage(data.error, 'error');
        }
    } catch (error) {
        showMessage('Error making move: ' + error.message, 'error');
    }
}

// Clear square selection
function clearSelection() {
    if (selectedSquare) {
        const square = document.querySelector(`[data-row="${selectedSquare.row}"][data-col="${selectedSquare.col}"]`);
        if (square) {
            square.classList.remove('selected');
        }
        selectedSquare = null;
    }
    
    document.querySelectorAll('.valid-move').forEach(sq => {
        sq.classList.remove('valid-move');
    });
}

// Update game info display
function updateGameInfo(state) {
    document.getElementById('current-turn').textContent = 
        state.current_turn.charAt(0).toUpperCase() + state.current_turn.slice(1);
    document.getElementById('game-status').textContent = 
        state.game_status.charAt(0).toUpperCase() + state.game_status.slice(1);
    document.getElementById('move-count').textContent = state.move_count;
    
    updateMoveHistory();
}

// Update move history
async function updateMoveHistory() {
    if (!currentGameId) return;
    
    try {
        const response = await fetch(`${API_URL}/game/${currentGameId}/history`);
        const data = await response.json();
        
        if (data.success) {
            const historyElement = document.getElementById('move-history');
            historyElement.innerHTML = '';
            
            data.history.forEach((move, index) => {
                const moveDiv = document.createElement('div');
                const fromPos = `${String.fromCharCode(97 + move.from[1])}${8 - move.from[0]}`;
                const toPos = `${String.fromCharCode(97 + move.to[1])}${8 - move.to[0]}`;
                moveDiv.textContent = `${index + 1}. ${move.piece} ${fromPos} → ${toPos}`;
                if (move.captured) {
                    moveDiv.textContent += ` (captured ${move.captured})`;
                }
                historyElement.appendChild(moveDiv);
            });
        }
    } catch (error) {
        console.error('Error fetching move history:', error);
    }
}

// Show message
function showMessage(text, type = 'info') {
    const messageElement = document.getElementById('message');
    messageElement.textContent = text;
    messageElement.className = `message ${type}`;
}
