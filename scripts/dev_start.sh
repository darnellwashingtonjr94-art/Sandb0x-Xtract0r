#!/bin/bash
# dev_start.sh - Launch SandB0x-Xtract0r full stack locally

echo "[+] Starting Python Backend..."
cd ../src
# Adjust for your specific framework (e.g., uvicorn api.server:app or python main.py)
python3 main.py &
BACKEND_PID=$!

echo "[+] Starting React Frontend..."
cd ../frontend
npm run dev &
FRONTEND_PID=$!

# Trap Ctrl+C to kill both processes
trap "echo 'Shutting down...'; kill $BACKEND_PID $FRONTEND_PID; exit" SIGINT

wait
