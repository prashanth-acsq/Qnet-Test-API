start /MAX cmd /c "title API-SERVER && cd python/venv/Scripts && activate && cd .. && cd .. && cls && uvicorn main:app --port 5000 --reload"