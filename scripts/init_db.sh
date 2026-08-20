#!/bin/bash
# init_db.sh - Initialize the database schema

DB_FILE="../storage/sandbox.db"

echo "[+] Initializing database schema..."
# Example using SQLite; replace with psql commands if using PostgreSQL
sqlite3 "$DB_FILE" <<EOF
CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, hash TEXT);
CREATE TABLE IF NOT EXISTS reports (id INTEGER PRIMARY KEY, hash TEXT, status TEXT);
EOF
echo "Database initialized at $DB_FILE."
