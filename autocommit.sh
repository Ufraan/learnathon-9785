#!/bin/bash

while true; do
  git add .
  git commit -m "Automatic commit at $(date)"
  git push origin main
  sleep 15s
done
