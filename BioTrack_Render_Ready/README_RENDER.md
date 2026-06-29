# Deploy to Render
1. Create GitHub repo and upload files
2. Create Render Web Service
3. Connect repo
4. Build: pip install -r requirements-render.txt
5. Start: uvicorn backend.main:app --host 0.0.0.0 --port $PORT
SQLite is stored locally and may reset on redeploy.
