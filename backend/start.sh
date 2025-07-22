
#!/bin/sh

python -m main

# Use Railway's PORT or default to 5000
PORT=${PORT:-5000}

echo "Starting server on port $PORT..."

# Start the backend server
uvicorn app.main:app --host 0.0.0.0 --port $PORT

