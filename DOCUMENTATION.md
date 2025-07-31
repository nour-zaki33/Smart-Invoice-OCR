# Medical Invoice Processing System - Documentation

## Overview

The Medical Invoice Processing System is a comprehensive solution for processing medical invoices using OCR, AI analysis, and fraud detection. The system consists of a FastAPI backend and a Streamlit frontend.

## Features

###  Phase 1: OCR and Invoice Parsing
- **OCR Processing**: Extract text from scanned invoices (images, PDFs)
- **Invoice Parsing**: Identify patient info, services, amounts using regex and NLP
- **Data Validation**: Validate extracted data for completeness and accuracy

### Phase 2: AI Claims Analysis
- **Automated Decisions**: Approve, reject, or flag claims for clarification
- **Rule-based Logic**: Apply medical billing rules and policies
- **ML Classification**: Use machine learning for claim categorization
- **Confidence Scoring**: Provide confidence levels for decisions

### Phase 3: Fraud Detection
- **Rule-based Checks**: Detect suspicious patterns and anomalies
- **ML Anomaly Detection**: Use Isolation Forest for fraud detection
- **Risk Assessment**: Provide risk levels and recommendations
- **Pattern Analysis**: Identify duplicate services, unusual amounts

###  Phase 4: Frontend UI
- **Streamlit Dashboard**: Modern, responsive web interface
- **Upload Interface**: Drag-and-drop file upload
- **Analytics**: Charts and statistics for processed invoices
- **Real-time Processing**: Live updates during processing

## Architecture

```
Medical Invoice Processing System
├── Backend (FastAPI)
│   ├── OCR Service (pytesseract)
│   ├── Parser Service (spaCy + regex)
│   ├── AI Service (scikit-learn)
│   ├── Fraud Detection Service (Isolation Forest)
│   └── Database (SQLite/PostgreSQL)
├── Frontend (Streamlit)
│   ├── Dashboard
│   ├── Upload Interface
│   ├── Analytics
│   └── Results Viewer
└── Infrastructure
    ├── Docker Support
    ├── Health Checks
    └── Logging
```

## Installation

### Prerequisites
- Python 3.8+
- Tesseract OCR
- Docker (optional)

### Quick Start

1. **Clone and setup**:
   ```bash
   git clone <repository>
   cd medical-invoice-system
   pip install -r requirements.txt
   ```

2. **Run the system**:
   ```bash
   python start.py
   ```

3. **Access the application**:
   - API: http://localhost:8000
   - Frontend: http://localhost:8501
   - API Docs: http://localhost:8000/docs

### Docker Deployment

1. **Build and run with Docker Compose**:
   ```bash
   cd docker
   docker-compose up --build
   ```

2. **Access the application**:
   - API: http://localhost:8000
   - Frontend: http://localhost:8501

## API Endpoints

### Invoice Processing
- `POST /api/v1/invoices/upload` - Upload and process invoice
- `GET /api/v1/invoices/` - List all invoices
- `GET /api/v1/invoices/{id}` - Get invoice details

### Claims Analysis
- `POST /api/v1/claims/analyze` - Analyze claim with AI
- `POST /api/v1/claims/fraud` - Detect fraud in claim
- `POST /api/v1/invoices/{id}/process` - Complete processing pipeline

### Health & Monitoring
- `GET /api/v1/health` - Health check
- `GET /` - Root endpoint

## Usage Examples

### Upload and Process Invoice

```python
import requests

# Upload invoice
with open('invoice.pdf', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:8000/api/v1/invoices/upload', files=files)

# Get results
result = response.json()
print(f"Invoice ID: {result['invoice_id']}")
print(f"Patient: {result['extracted_data']['patient_name']}")
print(f"Total: ${result['extracted_data']['total_amount']}")
```

### Run Complete Analysis

```python
# Run AI analysis and fraud detection
invoice_id = 1
response = requests.post(f'http://localhost:8000/api/v1/invoices/{invoice_id}/process')
result = response.json()

# Check results
claim_status = result['claim_analysis']['status']
fraud_score = result['fraud_detection']['fraud_score']
print(f"Claim Status: {claim_status}")
print(f"Fraud Score: {fraud_score:.2%}")
```

## Configuration

### Environment Variables

Create a `.env` file based on `env.example`:

```env
# Application settings
APP_NAME=Medical Invoice Processing System
DEBUG=false

# Database
DATABASE_URL=sqlite:///./medical_invoices.db

# OCR settings
TESSERACT_CMD=/usr/bin/tesseract
OCR_LANGUAGE=eng

# File upload
MAX_FILE_SIZE=10485760
UPLOAD_DIR=uploads

# AI/ML settings
CONFIDENCE_THRESHOLD=0.8
FRAUD_DETECTION_ENABLED=true
```

### Supported File Formats
- **Images**: PNG, JPG, JPEG, TIFF, BMP
- **Documents**: PDF
- **Max Size**: 10MB per file

## Processing Pipeline

### 1. OCR Processing
```python
# Extract text from image/PDF
ocr_service = OCRService()
text = ocr_service.process_file('invoice.pdf')
```

### 2. Data Extraction
```python
# Parse structured data
parser_service = InvoiceParserService()
data = parser_service.parse_invoice(text)
```

### 3. AI Analysis
```python
# Analyze claim
ai_service = AIClaimsService()
decision = ai_service.analyze_claim(invoice_data, services)
```

### 4. Fraud Detection
```python
# Detect fraud
fraud_service = FraudDetectionService()
fraud_result = fraud_service.detect_fraud(invoice_data, services)
```

## Data Models

### Invoice
```python
{
    "id": 1,
    "filename": "invoice.pdf",
    "patient_name": "John Smith",
    "hospital_name": "City General Hospital",
    "invoice_number": "INV-2024-001",
    "invoice_date": "2024-01-15",
    "total_amount": 666.75,
    "currency": "USD",
    "services": [...],
    "ocr_processed": true,
    "ai_analyzed": true,
    "fraud_checked": true
}
```

### Service
```python
{
    "id": 1,
    "invoice_id": 1,
    "service_name": "Emergency Room Consultation",
    "service_code": "ER001",
    "quantity": 1,
    "unit_price": 250.00,
    "total_price": 250.00,
    "description": "Emergency consultation"
}
```

### Claim Analysis
```python
{
    "status": "approved",  # approved, rejected, needs_clarification
    "confidence_score": 0.85,
    "decision_reason": "Standard medical procedure",
    "flags": ["Missing diagnosis code"],
    "suggested_actions": ["Request additional documentation"]
}
```

### Fraud Detection
```python
{
    "is_fraudulent": false,
    "fraud_score": 0.15,
    "risk_level": "low",  # low, medium, high, critical
    "flags": [],
    "suspicious_patterns": [],
    "recommendations": ["Standard processing"]
}
```

## Testing

### Run Tests
```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_ocr.py

# Run with coverage
pytest --cov=app tests/
```

### Test Sample Invoice
```bash
# Use the sample invoice for testing
python -c "
from app.services.ocr_service import OCRService
from app.services.parser_service import InvoiceParserService

ocr = OCRService()
parser = InvoiceParserService()

with open('sample_invoice.txt', 'r') as f:
    text = f.read()

data = parser.parse_invoice(text)
print(f'Patient: {data.patient_name}')
print(f'Hospital: {data.hospital_name}')
print(f'Total: ${data.total_amount}')
"
```

## Performance

### Benchmarks
- **OCR Processing**: ~2-5 seconds per page
- **AI Analysis**: ~1-2 seconds per invoice
- **Fraud Detection**: ~0.5-1 second per invoice
- **Complete Pipeline**: ~5-10 seconds per invoice

### Optimization Tips
1. **Image Quality**: Higher resolution images improve OCR accuracy
2. **File Size**: Compress large PDFs before upload
3. **Batch Processing**: Process multiple invoices in parallel
4. **Caching**: Enable model caching for faster subsequent runs

## Troubleshooting

### Common Issues

1. **Tesseract not found**:
   ```bash
   # Ubuntu/Debian
   sudo apt-get install tesseract-ocr
   
   # macOS
   brew install tesseract
   
   # Windows
   # Download from https://github.com/UB-Mannheim/tesseract/wiki
   ```

2. **spaCy model missing**:
   ```bash
   python -m spacy download en_core_web_sm
   ```

3. **Port already in use**:
   ```bash
   # Change ports in start.py or use different ports
   uvicorn app.main:app --port 8001
   streamlit run frontend/streamlit_app.py --server.port 8502
   ```

4. **Database errors**:
   ```bash
   # Delete and recreate database
   rm medical_invoices.db
   python start.py
   ```

### Logs
- **API Logs**: Check console output or logs/app.log
- **Frontend Logs**: Check Streamlit console output
- **Docker Logs**: `docker-compose logs`

## Security Considerations

### Data Protection
- All uploaded files are stored locally
- No data is sent to external services
- Database is local (SQLite) or secured (PostgreSQL)

### Access Control
- No authentication implemented (Phase 5)
- API endpoints are public
- Consider implementing JWT authentication for production

### File Validation
- File type validation
- File size limits
- Malicious file scanning (recommended)

## Deployment

### Production Checklist
- [ ] Set `DEBUG=false`
- [ ] Use strong `SECRET_KEY`
- [ ] Configure PostgreSQL database
- [ ] Set up SSL/TLS certificates
- [ ] Implement authentication
- [ ] Configure logging
- [ ] Set up monitoring
- [ ] Backup strategy

### Cloud Deployment
```bash
# AWS/GCP/Azure
docker build -t medical-invoice-system .
docker run -p 8000:8000 medical-invoice-system
```

## Contributing

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make changes
4. Add tests
5. Submit pull request

### Code Style
- Follow PEP 8
- Use type hints
- Add docstrings
- Write unit tests

## License

MIT License - see LICENSE file for details.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the API documentation
3. Create an issue on GitHub
4. Contact the development team

## Roadmap

### Phase 5: Authentication & Security
- [ ] JWT authentication
- [ ] Role-based access control
- [ ] API rate limiting
- [ ] Audit logging

### Phase 6: Integrations
- [ ] Email notifications
- [ ] WhatsApp integration
- [ ] Webhook support
- [ ] Payment processing

### Phase 7: Testing & QA
- [ ] Comprehensive test suite
- [ ] Performance testing
- [ ] Security testing
- [ ] User acceptance testing

### Phase 8: Deployment
- [ ] CI/CD pipeline
- [ ] Monitoring setup
- [ ] Backup automation
- [ ] Scaling configuration 