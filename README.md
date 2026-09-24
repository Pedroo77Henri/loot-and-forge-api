Loot & Forge API

A microservice built with FastAPI for managing RPG item inventories and forging legendary items asynchronously.

Technologies
Python
FastAPI
SQLAlchemy
SQLite
Pydantic
How to run

You'll need two terminals open at the same time.

Terminal 1 - API:

bash
cd app
uvicorn main:app --reload

Terminal 2 - Worker:

bash
cd app
python worker.py

Once running, access the interactive docs at http://localhost:8000/docs

How it works

The API lets you create and manage items in your inventory. If you want to forge a legendary item, you send a request to /itens/forjar and the API responds immediately — no waiting. A background worker picks up the job, waits the required time, then updates the item with a random power value between 80 and 100.

The project follows an MVC-style architecture, with routes, services and repository separated into their own files.