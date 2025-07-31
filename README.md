# Medical Invoice Processing System

A comprehensive system for processing medical invoices using OCR, AI analysis, and fraud detection.

## Features

- **OCR Processing**: Extract text from scanned invoices (images, PDFs)
- **Invoice Parsing**: Identify patient info, services, amounts using regex and NLP
- **AI Claims Analysis**: Automated approval/rejection decisions
- **Fraud Detection**: ML-based anomaly detection and rule-based checks
- **Web Dashboard**: Streamlit-based UI for invoice management
- **Authentication**: JWT-based user management with role-based access
- **API Integration**: Webhooks and external system integration

## Project Structure

```
medical_invoice_system/
├── app/
│   ├── __init__.py
│   ├── main.py                 # FastAPI application
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py           # Configuration settings
│   │   ├── security.py         # Authentication and security
│   │   └── database.py         # Database connection
│   ├── models/
│   │   ├── __init__.py
│   │   ├── invoice.py          # Invoice data models
│   │   ├── user.py             # User models
│   │   └── claim.py            # Claim processing models
│   ├── services/
│   │   ├── __init__.py
│   │   ├── ocr_service.py      # OCR processing
│   │   ├── parser_service.py   # Invoice parsing
│   │   ├── ai_service.py       # AI claims analysis
│   │   ├── fraud_service.py    # Fraud detection
│   │   └── notification_service.py # Email/WhatsApp notifications
│   ├── api/
│   │   ├── __init__.py
│   │   ├── v1/
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── invoices.py
│   │   │   │   ├── claims.py
│   │   │   │   ├── users.py
│   │   │   │   └── auth.py
│   │   │   └── api.py
│   │   └── dependencies.py
│   └── utils/
│       ├── __init__.py
│       ├── text_processing.py  # Text analysis utilities
│       └── validators.py       # Data validation
├── tests/
│   ├── __init__.py
│   ├── test_ocr.py
│   ├── test_parser.py
│   ├── test_ai.py
│   └── test_api.py
├── frontend/
│   ├── streamlit_app.py        # Streamlit dashboard
│   └── components/
├── docker/
│   ├── Dockerfile
│   └── docker-compose.yml
├── scripts/
│   ├── setup.py
│   └── deploy.py
├── requirements.txt
├── .env.example
└── README.md
```

## Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

3. **Run the application**:
   ```bash
   # Start the API server
   uvicorn app.main:app --reload
   
   # Start the Streamlit dashboard
   streamlit run frontend/streamlit_app.py
   ```

## API Endpoints

- `POST /api/v1/invoices/upload` - Upload and process invoices
- `GET /api/v1/invoices/` - List all invoices
- `POST /api/v1/claims/analyze` - Analyze claims with AI
- `GET /api/v1/claims/fraud` - Get fraud detection results
- `POST /api/v1/auth/login` - User authentication

## Development Phases

1.**Phase 1**: OCR and Invoice Parsing
2.**Phase 2**: AI Claims Analysis
3.**Phase 3**: Fraud Detection
4.**Phase 4**: Frontend UI
5.**Phase 5**: Authentication & Security
6.**Phase 6**: Integrations
7.**Phase 7**: Testing & QA
8.**Phase 8**: Deployment

## License

MIT License 