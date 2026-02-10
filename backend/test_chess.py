"""Test chess board and piece movement."""

from board import ChessBoard


def test_basic_moves():
    """Test basic piece movements."""
    game = ChessBoard()
    
    print("Initial board state:")
    print(f"Current turn: {game.current_turn}")
    print(f"Game status: {game.game_status}")
    
    # Test pawn move
    print("\n1. Moving white pawn from (6,4) to (4,4)...")
    success, message = game.move_piece((6, 4), (4, 4))
    print(f"Result: {message}")
    print(f"Current turn: {game.current_turn}")
    
    # Test black pawn move
    print("\n2. Moving black pawn from (1,4) to (3,4)...")
    success, message = game.move_piece((1, 4), (3, 4))
    print(f"Result: {message}")
    print(f"Current turn: {game.current_turn}")
    
    # Test knight move
    print("\n3. Moving white knight from (7,1) to (5,2)...")
    success, message = game.move_piece((7, 1), (5, 2))
    print(f"Result: {message}")
    print(f"Current turn: {game.current_turn}")
    
    # Test invalid move
    print("\n4. Attempting invalid move - white pawn when it's black's turn...")
    success, message = game.move_piece((6, 0), (5, 0))
    print(f"Result: {message}")
    
    print(f"\nTotal moves made: {len(game.move_history)}")
    print(f"Game status: {game.game_status}")
    
    return game


if __name__ == "__main__":
    print("=== Chess Engine Test ===\n")
    game = test_basic_moves()
    print("\n=== Test Complete ===")
