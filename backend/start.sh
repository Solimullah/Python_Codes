#!/bin/bash

# Exit on any error
set -e

# Start FastAPI server using Uvicorn
exec uvicorn app.main:app --host 0.0.0.0 --port 5000
