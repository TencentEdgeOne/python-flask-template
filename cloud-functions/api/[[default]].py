"""
Python Cloud Function - Flask Framework
A serverless function using the Flask web framework.
"""
from flask import Flask, request, jsonify
import time
import datetime

app = Flask(__name__)


@app.route('/')
def index():
    """Root endpoint."""
    return jsonify({
        "message": "Hello from Flask Cloud Function!",
        "framework": "Flask",
        "timestamp": time.time()
    })


@app.route('/health')
def health():
    """Health check endpoint."""
    return jsonify({
        "status": "healthy",
        "timestamp": time.time(),
        "type": "flask_function"
    })


@app.route('/info')
def info():
    """Function information endpoint."""
    return jsonify({
        "name": "Flask Cloud Function",
        "framework": "Flask",
        "description": "A serverless function using the Flask web framework",
        "features": [
            "Flask routing",
            "Request/Response handling",
            "JSON serialization",
            "Middleware support",
            "Blueprint architecture"
        ]
    })


@app.route('/time')
def get_time():
    """Return current server time."""
    now = datetime.datetime.now()
    return jsonify({
        "timestamp": time.time(),
        "iso": now.isoformat(),
        "formatted": now.strftime("%Y-%m-%d %H:%M:%S"),
    })


@app.route('/echo', methods=['GET', 'POST'])
def echo():
    """Echo request information."""
    return jsonify({
        "method": request.method,
        "query": dict(request.args),
        "headers_count": len(dict(request.headers)),
        "body": request.get_data(as_text=True)[:500] if request.data else None,
        "timestamp": time.time()
    })


@app.route('/json', methods=['POST'])
def handle_json():
    """Handle JSON request body."""
    try:
        data = request.get_json() or {}
    except Exception:
        return jsonify({"error": "Invalid JSON body"}), 400
    
    return jsonify({
        "message": "JSON received and parsed",
        "received": data,
        "keys": list(data.keys()) if isinstance(data, dict) else [],
        "size": len(request.get_data(as_text=True))
    })


@app.route('/users/<int:user_id>')
def get_user(user_id):
    """Get user by ID."""
    return jsonify({
        "user_id": user_id,
        "username": f"user_{user_id}",
        "email": f"user{user_id}@example.com",
        "source": "flask_function"
    })


@app.route('/users', methods=['POST'])
def create_user():
    """Create a new user."""
    try:
        data = request.get_json() or {}
    except Exception:
        return jsonify({"error": "Invalid JSON body"}), 400
    
    if 'username' not in data:
        return jsonify({"error": "Username is required"}), 400
    
    return jsonify({
        "message": "User created",
        "user": {
            "id": 12345,
            "username": data['username'],
            "email": data.get('email', ''),
        }
    }), 201


@app.route('/search')
def search():
    """Search functionality with query parameters."""
    q = request.args.get('q', '')
    limit = int(request.args.get('limit', 10))
    offset = int(request.args.get('offset', 0))
    
    if not q:
        return jsonify({"error": "Query parameter 'q' is required"}), 400
    
    results = [
        {"id": i, "name": f"Result {i}", "score": round(0.95 - i * 0.08, 2)}
        for i in range(offset, offset + min(limit, 10))
    ]
    
    return jsonify({
        "query": q,
        "limit": limit,
        "offset": offset,
        "count": len(results),
        "results": results
    })


# Error handlers
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not Found"}), 404


@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Internal Server Error"}), 500


# Export the Flask app for the serverless runtime
def handler(event, context=None):
    """Serverless function handler wrapper."""
    return app
