@echo off
uvicorn bookapi.books:app --reload --reload-dir=./bookapi
