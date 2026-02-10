"""Chess board and game logic."""

from pieces import Pawn, Rook, Knight, Bishop, Queen, King


class ChessBoard:
    """Represents a chess board and game state."""
    
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.current_turn = 'white'
        self.move_history = []
        self.game_status = 'active'  # 'active', 'check', 'checkmate', 'stalemate'
        self._setup_board()
    
    def _setup_board(self):
        """Initialize board with pieces in starting positions."""
        # Black pieces (top)
        self.board[0] = [
            Rook('black', (0, 0)), Knight('black', (0, 1)), Bishop('black', (0, 2)), Queen('black', (0, 3)),
            King('black', (0, 4)), Bishop('black', (0, 5)), Knight('black', (0, 6)), Rook('black', (0, 7))
        ]
        self.board[1] = [Pawn('black', (1, i)) for i in range(8)]
        
        # White pieces (bottom)
        self.board[6] = [Pawn('white', (6, i)) for i in range(8)]
        self.board[7] = [
            Rook('white', (7, 0)), Knight('white', (7, 1)), Bishop('white', (7, 2)), Queen('white', (7, 3)),
            King('white', (7, 4)), Bishop('white', (7, 5)), Knight('white', (7, 6)), Rook('white', (7, 7))
        ]
    
    def get_piece(self, position):
        """Get piece at position."""
        row, col = position
        return self.board[row][col]
    
    def move_piece(self, from_pos, to_pos):
        """Move a piece from one position to another."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        
        piece = self.board[from_row][from_col]
        
        # Validate move
        if piece is None:
            return False, "No piece at starting position"
        
        if piece.color != self.current_turn:
            return False, f"It's {self.current_turn}'s turn"
        
        if not (0 <= to_row < 8 and 0 <= to_col < 8):
            return False, "Target position out of bounds"
        
        if not piece.is_valid_move(to_pos, self.board):
            return False, "Invalid move for this piece"
        
        # Check if move puts own king in check
        if self._would_be_in_check(from_pos, to_pos):
            return False, "Move would put king in check"
        
        # Execute move
        captured_piece = self.board[to_row][to_col]
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = None
        piece.position = to_pos
        piece.has_moved = True
        
        # Record move
        self.move_history.append({
            'from': from_pos,
            'to': to_pos,
            'piece': piece.__class__.__name__,
            'captured': captured_piece.__class__.__name__ if captured_piece else None
        })
        
        # Switch turn
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'
        
        # Update game status
        self._update_game_status()
        
        return True, "Move successful"
    
    def _find_king(self, color):
        """Find the king of the specified color."""
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if isinstance(piece, King) and piece.color == color:
                    return (row, col)
        return None
    
    def _is_position_attacked(self, position, by_color):
        """Check if a position is attacked by any piece of the given color."""
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color == by_color:
                    if piece.is_valid_move(position, self.board):
                        return True
        return False
    
    def _is_in_check(self, color):
        """Check if the king of the given color is in check."""
        king_pos = self._find_king(color)
        if not king_pos:
            return False
        opponent_color = 'black' if color == 'white' else 'white'
        return self._is_position_attacked(king_pos, opponent_color)
    
    def _would_be_in_check(self, from_pos, to_pos):
        """Check if a move would put own king in check."""
        from_row, from_col = from_pos
        to_row, to_col = to_pos
        
        # Simulate move
        piece = self.board[from_row][from_col]
        captured = self.board[to_row][to_col]
        original_pos = piece.position
        
        self.board[to_row][to_col] = piece
        self.board[from_row][from_col] = None
        piece.position = to_pos
        
        # Check if in check
        in_check = self._is_in_check(piece.color)
        
        # Undo move
        self.board[from_row][from_col] = piece
        self.board[to_row][to_col] = captured
        piece.position = original_pos
        
        return in_check
    
    def _update_game_status(self):
        """Update game status (check, checkmate, stalemate)."""
        if self._is_in_check(self.current_turn):
            if self._is_checkmate(self.current_turn):
                self.game_status = 'checkmate'
            else:
                self.game_status = 'check'
        elif self._is_stalemate(self.current_turn):
            self.game_status = 'stalemate'
        else:
            self.game_status = 'active'
    
    def _is_checkmate(self, color):
        """Check if the given color is in checkmate."""
        return self._is_in_check(color) and not self._has_legal_moves(color)
    
    def _is_stalemate(self, color):
        """Check if the given color is in stalemate."""
        return not self._is_in_check(color) and not self._has_legal_moves(color)
    
    def _has_legal_moves(self, color):
        """Check if the given color has any legal moves."""
        for row in range(8):
            for col in range(8):
                piece = self.board[row][col]
                if piece and piece.color == color:
                    for target_row in range(8):
                        for target_col in range(8):
                            if piece.is_valid_move((target_row, target_col), self.board):
                                if not self._would_be_in_check((row, col), (target_row, target_col)):
                                    return True
        return False
    
    def get_board_state(self):
        """Get current board state as a dictionary."""
        state = []
        for row in range(8):
            row_state = []
            for col in range(8):
                piece = self.board[row][col]
                if piece:
                    row_state.append({
                        'type': piece.__class__.__name__,
                        'color': piece.color
                    })
                else:
                    row_state.append(None)
            state.append(row_state)
        
        return {
            'board': state,
            'current_turn': self.current_turn,
            'game_status': self.game_status,
            'move_count': len(self.move_history)
        }
