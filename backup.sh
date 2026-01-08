#!/bin/bash
# Lihtne varundamise skript

BACKUP_DIR="backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "Alustan varundamist..."

mkdir -p "$BACKUP_DIR"
tar -czf "$BACKUP_DIR/backup_$TIMESTAMP.tar.gz" notes.txt README.md

echo "Varundus valmis: $BACKUP_DIR/backup_$TIMESTAMP.tar.gz"
