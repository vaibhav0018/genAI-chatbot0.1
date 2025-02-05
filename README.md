![Screenshot from 2025-02-05 14-35-52](https://github.com/user-attachments/assets/2234fdc0-2ae7-46ad-8c2a-145d14ef8586)
## 🚀 Key Features

- **Real-time Google Sheets Sync**: Automatic data fetching from Google Sheets
- **Vector Embeddings**: Uses `sentence-transformers/all-MiniLM-L6-v2` for efficient text embeddings
- **Chroma Vector Store**: Fast similarity search capabilities
- **Pandas Integration**: Efficient data processing and transformation
- **Background Scheduling**: Automated data refresh mechanism
- **Scalable Architecture**: Blueprint-based modular design
- **Production-Ready**: Includes error handling, and security measures
- **Secure Configuration**: Environment-based security management

## 📋 Prerequisites

- Python 3.8 or higher
- Access to Google Sheets API
- Required Python packages:
  - langchain
  - pandas
  - requests
  - chromadb
  - sentence-transformers
  - huggingface-hub

## 🛠️ Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
```

2. Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure environment variables
```bash
cp .env.example .env
# Edit .env with your configuration
HUGGINGFACEHUB_API_TOKEN = "your-huggingface-hub-api-token"
GOOGLE_SHEET_ID = "your-google-sheet-id"
GOOGLE_SHEET_GID = "your-google-sheet-gid"
```

## 🏗️ Project Structure
```
packages/
├── app/                      # Application core
│   ├── __init__.py          # App initialization
│   ├── routes/              # API endpoints
│   │   ├── chat_routes.py   # Chat functionality routes
│   ├── services/            # Business logic
│   │   ├── chat_service.py  # Chat processing service
│   │   ├── data_service.py  # Data management service
│   ├── templates/           # HTML templates
├── config.py                # Configuration management
├── constants.py             # Global constants
├── requirements.txt         # Project dependencies
└── run.py                  # Application entry point
```

## ⚙️ Configuration

### Environment Variables
```env
FLASK_ENV=development
FLASK_SECRET_KEY=your-secret-key
GOOGLE_SHEETS_API_KEY=your-api-key
DATA_REFRESH_INTERVAL=3  # minutes
```

## 🚀 Usage

### Initialize Data Fetch
```python
from app.services.data_service import fetch_google_sheet_data

# Fetch and process data
fetch_google_sheet_data()
```

### Access Vector Store
```python
from app.services.data_service import get_vectorstore

# Get vector store instance
vectorstore = get_vectorstore()

# Perform similarity search
results = vectorstore.similarity_search("your query here")
```

## 🔄 Background Task Configuration

The application uses APScheduler to maintain data freshness:

```python
scheduler.add_job(fetch_google_sheet_data, 'interval', minutes=3)
```

## 🛡️ Error Handling

The service includes robust error handling for:
- Google Sheets API connectivity issues
- Data format validation
- Vector store operations
- Embedding model loading

## 📈 Performance Considerations

- Embedding operations are computationally intensive
- Vector store is maintained in memory
- Regular data refresh may impact performance
- Consider batch processing for large datasets

## 🔍 Monitoring

Monitor these metrics for optimal performance:
- Google Sheets API response times
- Vector store query latency
- Memory usage during embedding updates
- Background task execution times


## 🚀 Running the Application

### Development
```bash
flask run --debug
```

### Production
```bash
gunicorn -w 4 -b 0.0.0.0:8000 run:app
```

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=app tests/
```

## 📈 Performance Monitoring

The application includes built-in monitoring for:
- Background task execution
- API response times
- Google Sheets API usage
- Error rates and types

## 🔒 Security Features

- Environment-based secret management
- CSRF protection
- Rate limiting
- Secure headers configuration


## 📝 API Documentation

[Link to detailed API documentation - if available]

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

## 📞 Support

- Email: patilvaibhav0018@gmail.com

---
⭐️ If this project helps you, don't forget to give it a star!
