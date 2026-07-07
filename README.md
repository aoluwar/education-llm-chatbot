# 📚 Education LLM Chatbot

> An intelligent educational assistant powered by Large Language Models, enabling interactive learning experiences with advanced RAG (Retrieval-Augmented Generation) capabilities.

## Overview

Education LLM Chatbot is a sophisticated conversational AI platform designed for educational institutions and learners. It combines modern LLM technology with document processing and retrieval capabilities to provide intelligent tutoring, instant answer generation, and personalized learning support.

### Key Features

- 🤖 **Multi-Provider LLM Support** - OpenAI, Anthropic, Ollama, and more
- 📄 **Document Processing** - PDF, DOCX, PPTX, TXT, and Markdown support
- 🔍 **RAG Integration** - Pinecone vector database for semantic search
- 🔐 **Enterprise Security** - JWT authentication, role-based access control, encryption
- 📊 **Production-Ready** - Logging, monitoring, error tracking with Sentry
- 🚀 **Async-First** - Built with FastAPI for high performance
- 🐳 **Containerized** - Docker and Docker Compose support
- ⚡ **Caching & Queuing** - Redis integration with Celery task processing
- 📈 **Observable** - Prometheus metrics and structured logging

## Tech Stack

### Backend Framework
- **FastAPI** - Modern async web framework for building APIs
- **Uvicorn** - Lightning-fast ASGI server for running the FastAPI application
- **Pydantic** - Data validation and settings management with type hints

### AI & LLM
- **LangChain** - LLM orchestration and RAG pipeline construction
- **OpenAI API** - Primary LLM provider for conversations
- **Anthropic SDK** - Alternative provider support (Claude models)
- **FAISS & Pinecone** - Vector database and semantic search capabilities

### Database & Storage
- **PostgreSQL** - Primary relational database via SQLAlchemy ORM
- **Redis** - In-memory caching and session management
- **Alembic** - Database migration management

### Document Processing
- **pdf2image** - Extract images from PDF documents
- **python-docx** - Process Microsoft Word (.docx) files
- **python-pptx** - Process PowerPoint presentations
- **Pillow** - Advanced image processing

### Security
- **PyJWT** - JWT token generation and verification
- **Passlib + bcrypt** - Secure password hashing
- **Cryptography** - Encryption utilities for sensitive data

### Monitoring & Observability
- **Loguru** - Advanced logging with rotation and formatting
- **Sentry** - Real-time error tracking and reporting
- **Prometheus** - Metrics collection and exposure
- **Celery** - Distributed task processing for async operations

### Development & Testing
- **Pytest** - Testing framework with async support
- **Black** - Code formatting for consistency
- **Flake8** - Linting for code quality
- **MyPy** - Static type checking
- **isort** - Automatic import sorting

## Project Architecture

### Application Structure

```
education-llm-chatbot/
├── app/
│   ├── __init__.py              # Package initialization
│   ├── main.py                  # FastAPI application entry point and route setup
│   ├── config.py                # Configuration management and environment variables
│   ├── database.py              # Database connection and session setup
│   ├── cache.py                 # Redis caching utilities and decorators
│   │
│   ├── models/                  # SQLAlchemy database models
│   │   ├── __init__.py
│   │   ├── user.py              # User model with authentication fields
│   │   ├── chat.py              # Chat message and conversation models
│   │   └── document.py          # Document storage and metadata models
│   │
│   ├── schemas/                 # Pydantic request/response schemas
│   │   ├── __init__.py
│   │   ├── auth_schema.py       # Registration, login, token schemas
│   │   ├── chat_schema.py       # Message and conversation schemas
│   │   └── document_schema.py   # Document upload and retrieval schemas
│   │
│   ├── api/                     # API route handlers (routers)
│   │   ├── __init__.py
│   │   ├── auth.py              # Authentication endpoints (register, login, refresh)
│   │   ├── chat.py              # Chat endpoints (message, history, context)
│   │   └── documents.py         # Document management endpoints (upload, list, delete)
│   │
│   ├── services/                # Business logic layer
│   │   ├── __init__.py
│   │   ├── llm_service.py       # LLM integration and model management
│   │   ├── rag_service.py       # RAG pipeline and vector search
│   │   ├── document_service.py  # Document processing and chunking
│   │   └── auth_service.py      # User authentication and token management
│   │
│   ├── utils/                   # Utility functions and helpers
│   │   ├── __init__.py
│   │   ├── security.py          # JWT, password hashing, encryption
│   │   ├── logging.py           # Loguru configuration
│   │   └── exceptions.py        # Custom exception classes
│   │
│   └── tasks/                   # Celery async tasks
│       ├── __init__.py
│       └── document_tasks.py    # Long-running document processing tasks
│
├── migrations/                  # Alembic database migrations
│   ├── env.py
│   ├── script.py.mako
│   └── versions/                # Individual migration files
│
├── tests/                       # Pytest test suite
│   ├── test_auth.py            # Authentication tests
│   ├── test_chat.py            # Chat functionality tests
│   ├── test_documents.py       # Document processing tests
│   └── conftest.py             # Pytest fixtures and configuration
│
├── Dockerfile                   # Container image definition
├── docker-compose.yml           # Multi-container orchestration
├── requirements.txt             # Python dependencies
├── .env.example                 # Environment variable template
└── README.md                    # This file
```

## Code Components Explained

### Core Modules

#### `config.py` - Configuration Management
Handles all environment variables and application settings using Pydantic Settings. Provides type-safe access to configuration like API keys, database URLs, LLM settings, and security credentials.

```python
# Example usage in other modules
from app.config import settings
api_key = settings.openai_api_key
max_file_size = settings.max_upload_size
```

#### `database.py` - Database Setup
Manages SQLAlchemy engine creation and session handling. Provides dependency injection for database sessions in FastAPI endpoints.

```python
# Used in FastAPI dependencies
async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

#### `cache.py` - Redis Caching
Provides decorators and utilities for caching frequently accessed data to Redis, improving performance for repeated queries.

```python
# Decorator usage for automatic caching
@cache_result(ttl=3600)
async def get_expensive_data(key: str):
    return await fetch_from_database(key)
```

### API Layer (`app/api/`)

Defines all HTTP endpoints using FastAPI routers. Each module corresponds to a resource:

- **`auth.py`**: User registration, login, token refresh, password reset
- **`chat.py`**: Send messages, retrieve chat history, manage conversation context
- **`documents.py`**: Upload documents for RAG, list user documents, delete documents

### Services Layer (`app/services/`)

Contains business logic separated from HTTP handling. This layer handles:

- **`llm_service.py`**: Communicates with LLM providers, manages model selection and parameters
- **`rag_service.py`**: Orchestrates RAG pipeline - document retrieval, ranking, prompt construction
- **`document_service.py`**: Handles file format parsing, text extraction, document chunking
- **`auth_service.py`**: Password hashing, JWT token generation, user authentication

### Models Layer (`app/models/`)

SQLAlchemy ORM models representing database tables:

- **User**: Stores user credentials, profile info, roles
- **ChatMessage**: Individual messages in conversations
- **Document**: Document metadata, file paths, upload timestamps

### Schemas Layer (`app/schemas/`)

Pydantic models for request/response validation and serialization:

- Validates incoming request data
- Serializes database models to JSON responses
- Provides auto-generated API documentation

## Quick Start

### Prerequisites

- Python 3.11+
- PostgreSQL 13+
- Redis 6+
- Docker & Docker Compose (optional)

### Installation

#### Option 1: Local Installation

1. **Clone the repository**
```bash
git clone https://github.com/aoluwar/education-llm-chatbot.git
cd education-llm-chatbot
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Setup environment variables**
```bash
cp .env.example .env
```

Edit `.env` and configure:
```env
# LLM Configuration
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-your-api-key
OPENAI_MODEL=gpt-4-turbo-preview

# Database
DATABASE_URL=postgresql://edubot:password@localhost:5432/education_chatbot

# Vector Store (RAG)
VECTOR_STORE=pinecone
PINCONE_API_KEY=your-api-key
PINCONE_INDEX=education-chatbot

# Security
SECRET_KEY=your-super-secret-key-change-in-production
JWT_SECRET_KEY=your-jwt-secret-key
```

5. **Run migrations**
```bash
alembic upgrade head
```

6. **Start the application**
```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Access the API at `http://localhost:8000` and Swagger UI at `http://localhost:8000/docs`

#### Option 2: Docker Installation

1. **Ensure `.env` is configured** (see above)

2. **Start with Docker Compose**
```bash
docker-compose up -d
```

This will start:
- PostgreSQL database
- Redis cache
- Education LLM Chatbot API on port 8000

3. **View logs**
```bash
docker-compose logs -f app
```

## API Documentation

### Interactive API Docs
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

### Core Endpoints

#### Authentication
```bash
# Register new user
POST /api/auth/register
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepassword",
  "full_name": "User Name"
}

# Login
POST /api/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "securepassword"
}

Response:
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "email": "user@example.com",
    "full_name": "User Name"
  }
}
```

#### Chat
```bash
# Send message
POST /api/chat/message
Authorization: Bearer <access_token>
Content-Type: application/json

{
  "message": "What is photosynthesis?",
  "context_id": "optional-context-id"
}

Response:
{
  "message_id": "msg_123",
  "response": "Photosynthesis is the process by which plants...",
  "context": {
    "sources": ["document_1.pdf", "document_2.docx"],
    "confidence": 0.95
  }
}

# Get chat history
GET /api/chat/history?limit=50
Authorization: Bearer <access_token>

Response:
{
  "messages": [
    {
      "id": "msg_123",
      "user_message": "What is photosynthesis?",
      "bot_response": "Photosynthesis is...",
      "timestamp": "2024-01-15T10:30:00Z"
    }
  ]
}
```

#### Documents
```bash
# Upload document for RAG
POST /api/documents/upload
Authorization: Bearer <access_token>
Content-Type: multipart/form-data

{
  "file": <binary file data>,
  "title": "Biology Textbook Chapter 5"
}

Response:
{
  "document_id": "doc_456",
  "filename": "biology_chapter5.pdf",
  "size": 2048576,
  "uploaded_at": "2024-01-15T10:30:00Z"
}

# List documents
GET /api/documents
Authorization: Bearer <access_token>

Response:
{
  "documents": [
    {
      "id": "doc_456",
      "title": "Biology Textbook Chapter 5",
      "filename": "biology_chapter5.pdf",
      "uploaded_at": "2024-01-15T10:30:00Z"
    }
  ]
}

# Delete document
DELETE /api/documents/doc_456
Authorization: Bearer <access_token>
```

#### Health Check
```bash
# Service health status
GET /health

Response:
{
  "status": "healthy",
  "database": "connected",
  "redis": "connected",
  "llm": "operational"
}
```

## Configuration

### Environment Variables

#### LLM Configuration
- `LLM_PROVIDER` - Provider: `openai`, `anthropic`, `ollama`
- `OPENAI_API_KEY` - OpenAI API key
- `OPENAI_MODEL` - Model: `gpt-4-turbo-preview`, `gpt-3.5-turbo`
- `TEMPERATURE` - Response creativity (0.0-1.0, default: 0.7)
- `MAX_TOKENS` - Max response length (default: 2000)

#### Database
- `DATABASE_URL` - PostgreSQL connection string
- `DATABASE_POOL_SIZE` - Connection pool size (default: 20)
- `DATABASE_POOL_RECYCLE` - Connection recycle time in seconds (default: 3600)

#### Vector Store (RAG)
- `VECTOR_STORE` - Provider: `pinecone`, `faiss`
- `PINCONE_API_KEY` - Pinecone API key
- `PINCONE_INDEX` - Index name for vector storage
- `EMBEDDING_MODEL` - Embedding model name

#### Security
- `SECRET_KEY` - Application secret key (used for general encryption)
- `JWT_SECRET_KEY` - JWT signing key (used for token signing)
- `ACCESS_TOKEN_EXPIRE_MINUTES` - Token expiration time (default: 30)
- `REFRESH_TOKEN_EXPIRE_DAYS` - Refresh token expiration (default: 7)

#### File Upload
- `MAX_UPLOAD_SIZE` - Max file size in bytes (default: 52428800 = 50MB)
- `ALLOWED_FILE_TYPES` - Comma-separated list (default: pdf,docx,pptx,txt,md)

#### Caching
- `REDIS_URL` - Redis connection string
- `CACHE_TTL` - Default cache time-to-live in seconds (default: 3600)

See `.env.example` for complete configuration options.

## Testing

Run the test suite with pytest:

```bash
# All tests
pytest

# With coverage report
pytest --cov=app

# Specific test file
pytest tests/test_auth.py

# Async tests with verbose output
pytest -v -s

# Run tests matching a pattern
pytest -k "test_chat"
```

## Code Quality

Maintain code standards:

```bash
# Format code with Black
black app tests

# Sort imports automatically
isort app tests

# Lint code with Flake8
flake8 app tests

# Type checking with MyPy
mypy app
```

## Development Workflow

1. Create a feature branch
```bash
git checkout -b feature/your-feature
```

2. Install development dependencies
```bash
pip install -r requirements.txt
```

3. Make changes and ensure tests pass
```bash
pytest --cov=app
```

4. Format and lint your code
```bash
black app && isort app && flake8 app
```

5. Commit and push
```bash
git add .
git commit -m "feat: add your feature"
git push origin feature/your-feature
```

6. Open a pull request on GitHub

## Monitoring & Observability

### Logging
Logs are configured with `loguru` for structured logging with rotation. Logs are sent to `stdout` by default.

For production environments:
- Configure ELK stack (Elasticsearch, Logstash, Kibana) integration
- Use Datadog agent for centralized logging
- Set up CloudWatch for AWS deployments

### Metrics
Prometheus metrics are exposed at `/metrics` endpoint. Common metrics include:
- HTTP request latency and counts
- LLM API response times
- RAG pipeline performance
- Database query duration

Configure Prometheus to scrape:
```yaml
scrape_configs:
  - job_name: 'education-chatbot'
    static_configs:
      - targets: ['localhost:8000']
```

### Error Tracking
Set `SENTRY_DSN` environment variable to enable error tracking:
```bash
export SENTRY_DSN="https://your-key@sentry.io/your-project"
```

This will automatically capture and report errors to Sentry for monitoring.

### Health Checks
```bash
curl http://localhost:8000/health
```

Returns component status: database, Redis, and LLM provider connectivity.

## Deployment

### Production Considerations

1. **Set secure environment variables**
```bash
export SECRET_KEY=$(python -c 'import secrets; print(secrets.token_urlsafe(32))')
export JWT_SECRET_KEY=$(python -c 'import secrets; print(secrets.token_urlsafe(32))')
```

2. **Use managed database** - RDS, Cloud SQL, or DigitalOcean Managed DB
   - Regular backups
   - Read replicas for scaling
   - SSL connections

3. **Use managed Redis** - ElastiCache, Redis Cloud, or DigitalOcean
   - Automatic failover
   - Persistence configuration

4. **Setup monitoring** - Configure Prometheus, Grafana, and Sentry
   - Create dashboards for key metrics
   - Set up alerts for anomalies

5. **Enable HTTPS** - Use reverse proxy (Nginx) with SSL/TLS
   ```nginx
   server {
       listen 443 ssl;
       ssl_certificate /path/to/cert.pem;
       ssl_certificate_key /path/to/key.pem;
       
       location / {
           proxy_pass http://localhost:8000;
       }
   }
   ```

6. **Scale workers** - Deploy multiple Celery workers for async tasks
   ```bash
   celery -A app.tasks worker --loglevel=info --concurrency=4
   ```

### Docker Deployment

```bash
# Build image with specific tag
docker build -t education-llm-chatbot:v1.0.0 .

# Run container with environment file
docker run -d \
  --env-file .env \
  -p 8000:8000 \
  --name chatbot \
  --restart unless-stopped \
  education-llm-chatbot:v1.0.0

# View logs
docker logs -f chatbot

# Stop container
docker stop chatbot

# Remove container
docker rm chatbot
```

### Kubernetes Deployment

For larger-scale deployments, use Kubernetes with:
- Deployment manifests for the API
- StatefulSet for Redis
- PostgreSQL managed service (AWS RDS, GCP Cloud SQL)
- Horizontal Pod Autoscaler for scaling

## Troubleshooting

### Common Issues

**Database connection error**
- Ensure PostgreSQL is running and accessible
- Verify `DATABASE_URL` in `.env` matches your setup
- Check database user credentials
- Confirm database name exists
```bash
# Test connection
psql postgresql://user:password@localhost:5432/dbname -c "SELECT 1;"
```

**Redis connection error**
- Ensure Redis is running: `redis-cli ping`
- Verify `REDIS_URL` in `.env`
- Check Redis password if configured
- Confirm port 6379 is accessible

**LLM API errors**
- Verify API keys are correct and not expired
- Check API quota and rate limits in provider dashboard
- Ensure correct model name (e.g., `gpt-4-turbo-preview`)
- Monitor API status pages for outages

**Document upload failing**
- Check file size (default 50MB limit)
- Verify file format is allowed (pdf, docx, pptx, txt, md)
- Check available disk space
- Review upload logs for specific errors

**Slow RAG responses**
- Check Pinecone index health and dimensions
- Review database query performance
- Monitor LLM API latency
- Consider increasing vector search results

**Memory issues in Docker**
- Increase Docker memory allocation
- Optimize Redis configuration
- Monitor Celery worker memory usage
- Consider implementing worker limits

## Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Add tests for new functionality
4. Ensure all tests pass: `pytest --cov=app`
5. Follow code style guidelines: `black`, `isort`, `flake8`
6. Commit with clear messages: `git commit -m "feat: description"`
7. Push and open a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions:

- 📧 Email: support@educationbot.com
- 🐛 Report bugs: [GitHub Issues](https://github.com/aoluwar/education-llm-chatbot/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/aoluwar/education-llm-chatbot/discussions)

## Roadmap

- [ ] Multi-language support with translation service
- [ ] Advanced analytics dashboard for educators
- [ ] Custom fine-tuning capabilities for domain-specific models
- [ ] Native mobile app (iOS/Android)
- [ ] Offline mode support with local LLM
- [ ] Advanced RBAC with organization management
- [ ] Streaming responses for real-time chat
- [ ] Plugin system for extensibility
- [ ] Integration with Learning Management Systems (LMS)
- [ ] Advanced assessment and quiz generation

## Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- LLM integration via [LangChain](https://langchain.com/)
- Vector search powered by [Pinecone](https://www.pinecone.io/)
- Async task processing with [Celery](https://docs.celeryproject.io/)
- Type safety with [Pydantic](https://docs.pydantic.dev/)

---

**Made with ❤️ for education and learning**
