# 📚 Education LLM Chatbot

> An intelligent educational assistant powered by Large Language Models, enabling interactive learning experiences with advanced RAG (Retrieval-Augmented Generation) capabilities.

## Overview

Education LLM Chatbot is a sophisticated conversational AI platform designed for educational institutions and learners. It combines modern LLM technology with document processing and retrieval capabilities to provide personalized, context-aware educational support. Whether you're looking to build a tutoring system, content Q&A platform, or intelligent learning assistant, this project provides a robust foundation.

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
- **FastAPI** - Modern async web framework
- **Uvicorn** - Lightning-fast ASGI server
- **Pydantic** - Data validation and settings management

### AI & LLM
- **LangChain** - LLM orchestration and RAG pipelines
- **OpenAI API** - Primary LLM provider
- **Anthropic SDK** - Alternative provider support
- **FAISS & Pinecone** - Vector database and semantic search

### Database & Storage
- **PostgreSQL** - Primary database (via SQLAlchemy)
- **Redis** - Caching and session management
- **Alembic** - Database migrations

### Document Processing
- **pdf2image** - PDF extraction
- **python-docx** - DOCX processing
- **python-pptx** - PPTX support
- **Pillow** - Image processing

### Security
- **PyJWT** - JWT token management
- **Passlib + bcrypt** - Password hashing
- **Cryptography** - Encryption utilities

### Monitoring & Observability
- **Loguru** - Advanced logging
- **Sentry** - Error tracking
- **Prometheus** - Metrics collection
- **Celery** - Async task processing

### Development & Testing
- **Pytest** - Testing framework with async support
- **Black** - Code formatting
- **Flake8** - Linting
- **MyPy** - Type checking
- **isort** - Import sorting

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

# Vector Store
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
{
  "email": "user@example.com",
  "password": "securepassword",
  "full_name": "User Name"
}

# Login
POST /api/auth/login
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

#### Chat
```bash
# Send message
POST /api/chat/message
{
  "message": "What is photosynthesis?",
  "context_id": "optional-context-id"
}

# Get chat history
GET /api/chat/history?limit=50
```

#### Documents
```bash
# Upload document for RAG
POST /api/documents/upload
# multipart/form-data with file

# List documents
GET /api/documents

# Delete document
DELETE /api/documents/{document_id}
```

#### Health Check
```bash
# Service health
GET /health
```

## Project Structure

```
education-llm-chatbot/
├── app/
│   ├── main.py                 # Application entry point
│   ├── config.py               # Configuration management
│   ├── models/                 # SQLAlchemy models
│   ├── schemas/                # Pydantic schemas
│   ├── api/
│   │   ├── auth.py             # Authentication endpoints
│   │   ├── chat.py             # Chat endpoints
│   │   └── documents.py        # Document management
│   ├── services/
│   │   ├── llm_service.py      # LLM interactions
│   │   ├── rag_service.py      # RAG pipeline
│   │   └── document_service.py # Document processing
│   ├── utils/
│   │   ├── security.py         # Security utilities
│   │   └── logging.py          # Logging configuration
│   └── tasks/                  # Celery async tasks
├── migrations/                 # Alembic migrations
├── tests/                      # Test suite
├── Dockerfile                  # Container image
├── docker-compose.yml          # Local dev environment
├── requirements.txt            # Python dependencies
├── .env.example               # Environment template
└── README.md                  # This file
```

## Configuration

### Environment Variables

#### LLM Configuration
- `LLM_PROVIDER` - Provider: `openai`, `anthropic`, `ollama`
- `OPENAI_API_KEY` - OpenAI API key
- `OPENAI_MODEL` - Model: `gpt-4-turbo-preview`, `gpt-3.5-turbo`
- `TEMPERATURE` - Response creativity (0.0-1.0)
- `MAX_TOKENS` - Max response length

#### Database
- `DATABASE_URL` - PostgreSQL connection string
- `DATABASE_POOL_SIZE` - Connection pool size
- `DATABASE_POOL_RECYCLE` - Connection recycle time

#### Vector Store (RAG)
- `VECTOR_STORE` - Provider: `pinecone`, `faiss`
- `PINCONE_API_KEY` - Pinecone API key
- `PINCONE_INDEX` - Index name
- `EMBEDDING_MODEL` - Embedding model

#### Security
- `SECRET_KEY` - Application secret key
- `JWT_SECRET_KEY` - JWT signing key
- `ACCESS_TOKEN_EXPIRE_MINUTES` - Token expiration
- `REFRESH_TOKEN_EXPIRE_DAYS` - Refresh token expiration

#### File Upload
- `MAX_UPLOAD_SIZE` - Max file size (bytes)
- `ALLOWED_FILE_TYPES` - Allowed formats

See `.env.example` for complete configuration options.

## Testing

Run the test suite with pytest:

```bash
# All tests
pytest

# With coverage
pytest --cov=app

# Specific test file
pytest tests/test_auth.py

# Async tests
pytest -v -s
```

## Code Quality

Maintain code standards:

```bash
# Format code
black app tests

# Sort imports
isort app tests

# Lint
flake8 app tests

# Type check
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

4. Format and lint
```bash
black app && isort app && flake8 app
```

5. Commit and push
```bash
git add .
git commit -m "feat: add your feature"
git push origin feature/your-feature
```

6. Open a pull request

## Monitoring & Observability

### Logging
Logs are configured with `loguru` and sent to `stdout`. For production, configure ELK stack or Datadog integration.

### Metrics
Prometheus metrics are exposed at `/metrics` endpoint. Configure Prometheus to scrape this endpoint.

### Error Tracking
Set `SENTRY_DSN` environment variable to enable error tracking with Sentry.

### Health Checks
```bash
curl http://localhost:8000/health
```

## Deployment

### Production Considerations

1. **Set secure environment variables**
```bash
export SECRET_KEY=$(python -c 'import secrets; print(secrets.token_urlsafe(32))')
export JWT_SECRET_KEY=$(python -c 'import secrets; print(secrets.token_urlsafe(32))')
```

2. **Use managed database** - RDS, Cloud SQL, or DigitalOcean Managed DB

3. **Use managed Redis** - ElastiCache, Redis Cloud, or DigitalOcean

4. **Setup monitoring** - Configure Prometheus, Grafana, and Sentry

5. **Enable HTTPS** - Use reverse proxy (Nginx) with SSL

6. **Scale workers** - Deploy multiple Celery workers

### Docker Deployment

```bash
# Build image
docker build -t education-llm-chatbot:latest .

# Run container
docker run -d \
  --env-file .env \
  -p 8000:8000 \
  --name chatbot \
  education-llm-chatbot:latest
```

## Troubleshooting

### Common Issues

**Database connection error**
- Ensure PostgreSQL is running
- Verify `DATABASE_URL` in `.env`
- Check database credentials

**Redis connection error**
- Ensure Redis is running
- Verify `REDIS_URL` in `.env`
- Check Redis password if configured

**LLM API errors**
- Verify API keys are correct
- Check API quota and rate limits
- Ensure correct model name

**Document upload failing**
- Check file size (default 50MB limit)
- Verify file format is allowed
- Check disk space

## Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Ensure all tests pass
5. Follow code style guidelines
6. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For issues, questions, or suggestions:

- 📧 Email: support@educationbot.com
- 🐛 Report bugs: [GitHub Issues](https://github.com/aoluwar/education-llm-chatbot/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/aoluwar/education-llm-chatbot/discussions)

## Roadmap

- [ ] Multi-language support
- [ ] Advanced analytics dashboard
- [ ] Custom fine-tuning capabilities
- [ ] Mobile app
- [ ] Offline mode support
- [ ] Advanced RBAC
- [ ] Streaming responses
- [ ] Plugin system

## Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- LLM integration via [LangChain](https://langchain.com/)
- Vector search powered by [Pinecone](https://www.pinecone.io/)

---

**Made with ❤️ for education and learning**
