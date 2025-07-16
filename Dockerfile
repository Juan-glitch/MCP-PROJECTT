# Basic Python runtime
FROM python:3.11-slim

# Install runtime dependencies
RUN pip install --no-cache-dir fastapi uvicorn[standard] requests arxiv

WORKDIR /app
COPY . /app

# Install the project in editable mode so changes take effect
RUN pip install --no-cache-dir -e .

CMD ["uvicorn", "mcp_server.main:app", "--host", "0.0.0.0", "--port", "8000"]
