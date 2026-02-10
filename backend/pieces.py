"""Chess piece classes and movement logic."""

class Piece:
    """Base class for all chess pieces."""
    
    def __init__(self, color, position):
        self.color = color  # 'white' or 'black'
        self.position = position  # tuple (row, col)
        self.has_moved = False
    
    def is_valid_move(self, target_position, board):
        """Check if move to target position is valid."""
        raise NotImplementedError("Subclasses must implement is_valid_move")
    
    def __repr__(self):
        return f"{self.color[0].upper()}{self.__class__.__name__[0]}"


class Pawn(Piece):
    """Pawn piece."""
    
    def is_valid_move(self, target_position, board):
        row, col = self.position
        target_row, target_col = target_position
        direction = -1 if self.color == 'white' else 1
        
        # Move forward one square
        if target_col == col and target_row == row + direction:
            return board[target_row][target_col] is None
        
        # Move forward two squares from starting position
        if not self.has_moved and target_col == col and target_row == row + (2 * direction):
            return board[row + direction][col] is None and board[target_row][target_col] is None
        
        # Capture diagonally
        if abs(target_col - col) == 1 and target_row == row + direction:
            return board[target_row][target_col] is not None and board[target_row][target_col].color != self.color
        
        return False


class Rook(Piece):
    """Rook piece."""
    
    def is_valid_move(self, target_position, board):
        row, col = self.position
        target_row, target_col = target_position
        
        # Must move in straight line
        if row != target_row and col != target_col:
            return False
        
        # Check path is clear
        if row == target_row:
            step = 1 if target_col > col else -1
            for c in range(col + step, target_col, step):
                if board[row][c] is not None:
                    return False
        else:
            step = 1 if target_row > row else -1
            for r in range(row + step, target_row, step):
                if board[r][col] is not None:
                    return False
        
        # Check target square
        target_piece = board[target_row][target_col]
        return target_piece is None or target_piece.color != self.color


class Knight(Piece):
    """Knight piece."""
    
    def is_valid_move(self, target_position, board):
        row, col = self.position
        target_row, target_col = target_position
        
        row_diff = abs(target_row - row)
        col_diff = abs(target_col - col)
        
        # L-shaped move
        if not ((row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)):
            return False
        
        target_piece = board[target_row][target_col]
        return target_piece is None or target_piece.color != self.color


class Bishop(Piece):
    """Bishop piece."""
    
    def is_valid_move(self, target_position, board):
        row, col = self.position
        target_row, target_col = target_position
        
        # Must move diagonally
        if abs(target_row - row) != abs(target_col - col):
            return False
        
        # Check path is clear
        row_step = 1 if target_row > row else -1
        col_step = 1 if target_col > col else -1
        
        current_row, current_col = row + row_step, col + col_step
        while (current_row, current_col) != (target_row, target_col):
            if board[current_row][current_col] is not None:
                return False
            current_row += row_step
            current_col += col_step
        
        target_piece = board[target_row][target_col]
        return target_piece is None or target_piece.color != self.color


class Queen(Piece):
    """Queen piece."""
    
    def is_valid_move(self, target_position, board):
        # Queen moves like rook or bishop
        rook = Rook(self.color, self.position)
        bishop = Bishop(self.color, self.position)
        return rook.is_valid_move(target_position, board) or bishop.is_valid_move(target_position, board)


class King(Piece):
    """King piece."""
    
    def is_valid_move(self, target_position, board):
        row, col = self.position
        target_row, target_col = target_position
        
        # Move one square in any direction
        if abs(target_row - row) > 1 or abs(target_col - col) > 1:
            return False
        
        target_piece = board[target_row][target_col]
        return target_piece is None or target_piece.color != self.color
