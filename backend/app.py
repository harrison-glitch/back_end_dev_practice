"""Flask REST API for chess game."""

from flask import Flask, jsonify, request
from flask_cors import CORS
from board import ChessBoard

app = Flask(__name__)
CORS(app)

# Store active games (in production, use a database)
games = {}
game_counter = 0


@app.route('/api/game/new', methods=['POST'])
def new_game():
    """Create a new chess game."""
    global game_counter
    try:
        game_counter += 1
        game_id = f"game_{game_counter}"
        games[game_id] = ChessBoard()
        
        return jsonify({
            'success': True,
            'game_id': game_id,
            'message': 'New game created',
            'state': games[game_id].get_board_state()
        }), 201
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/game/<game_id>/state', methods=['GET'])
def get_game_state(game_id):
    """Get current state of a game."""
    try:
        if game_id not in games:
            return jsonify({
                'success': False,
                'error': 'Game not found'
            }), 404
        
        return jsonify({
            'success': True,
            'game_id': game_id,
            'state': games[game_id].get_board_state()
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/game/<game_id>/move', methods=['POST'])
def make_move(game_id):
    """Make a move in a game."""
    try:
        if game_id not in games:
            return jsonify({
                'success': False,
                'error': 'Game not found'
            }), 404
        
        data = request.get_json()
        if not data or 'from' not in data or 'to' not in data:
            return jsonify({
                'success': False,
                'error': 'Missing from or to position'
            }), 400
        
        from_pos = tuple(data['from'])
        to_pos = tuple(data['to'])
        
        game = games[game_id]
        success, message = game.move_piece(from_pos, to_pos)
        
        if success:
            return jsonify({
                'success': True,
                'message': message,
                'state': game.get_board_state()
            }), 200
        else:
            return jsonify({
                'success': False,
                'error': message
            }), 400
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/game/<game_id>/history', methods=['GET'])
def get_move_history(game_id):
    """Get move history for a game."""
    try:
        if game_id not in games:
            return jsonify({
                'success': False,
                'error': 'Game not found'
            }), 404
        
        return jsonify({
            'success': True,
            'game_id': game_id,
            'history': games[game_id].move_history
        }), 200
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'active_games': len(games)
    }), 200


if __name__ == '__main__':
    print("Starting Chess API server...")
    print("API will be available at http://localhost:5001")
    print("\nEndpoints:")
    print("  POST   /api/game/new")
    print("  GET    /api/game/<game_id>/state")
    print("  POST   /api/game/<game_id>/move")
    print("  GET    /api/game/<game_id>/history")
    print("  GET    /api/health")
    app.run(debug=True, host='0.0.0.0', port=5001)
