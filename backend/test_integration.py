"""Integration tests for chess API."""

import requests
import json

API_URL = "http://localhost:5001/api"

def test_health_check():
    """Test API health endpoint."""
    response = requests.get(f"{API_URL}/health")
    assert response.status_code == 200
    data = response.json()
    assert data['status'] == 'healthy'
    print("✓ Health check passed")

def test_create_game():
    """Test game creation."""
    response = requests.post(f"{API_URL}/game/new")
    assert response.status_code == 201
    data = response.json()
    assert data['success'] == True
    assert 'game_id' in data
    print(f"✓ Game created: {data['game_id']}")
    return data['game_id']

def test_make_moves(game_id):
    """Test making valid moves."""
    # White pawn e2 to e4
    response = requests.post(
        f"{API_URL}/game/{game_id}/move",
        json={"from": [6, 4], "to": [4, 4]}
    )
    assert response.status_code == 200
    data = response.json()
    assert data['success'] == True
    assert data['state']['current_turn'] == 'black'
    print("✓ White pawn moved")
    
    # Black pawn e7 to e5
    response = requests.post(
        f"{API_URL}/game/{game_id}/move",
        json={"from": [1, 4], "to": [3, 4]}
    )
    assert response.status_code == 200
    data = response.json()
    assert data['success'] == True
    assert data['state']['current_turn'] == 'white'
    print("✓ Black pawn moved")

def test_invalid_move(game_id):
    """Test invalid move rejection."""
    # Try to move black piece on white's turn
    response = requests.post(
        f"{API_URL}/game/{game_id}/move",
        json={"from": [1, 0], "to": [3, 0]}
    )
    assert response.status_code == 400
    data = response.json()
    assert data['success'] == False
    print("✓ Invalid move rejected")

def test_move_history(game_id):
    """Test move history retrieval."""
    response = requests.get(f"{API_URL}/game/{game_id}/history")
    assert response.status_code == 200
    data = response.json()
    assert data['success'] == True
    assert len(data['history']) == 2
    print(f"✓ Move history retrieved: {len(data['history'])} moves")

def test_game_state(game_id):
    """Test game state retrieval."""
    response = requests.get(f"{API_URL}/game/{game_id}/state")
    assert response.status_code == 200
    data = response.json()
    assert data['success'] == True
    assert 'board' in data['state']
    assert data['state']['move_count'] == 2
    print("✓ Game state retrieved")

def run_all_tests():
    """Run all integration tests."""
    print("\n=== Running Integration Tests ===\n")
    
    try:
        test_health_check()
        game_id = test_create_game()
        test_make_moves(game_id)
        test_invalid_move(game_id)
        test_move_history(game_id)
        test_game_state(game_id)
        
        print("\n=== All Tests Passed! ===\n")
        return True
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        return False
    except requests.exceptions.ConnectionError:
        print("\n✗ Cannot connect to API. Is the server running?")
        return False
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    exit(0 if success else 1)
