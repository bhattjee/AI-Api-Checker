# AI-Api-Checker

A modern AI-powered Q&A chatbot application built with FastAPI and Google's Gemini AI. This project provides a RESTful API for interacting with an AI chatbot, along with a clean, responsive web interface.

## Features

- **AI-Powered Responses**: Uses Google's Gemini AI models (currently configured for gemini-pro-latest) for intelligent question answering
- **RESTful API**: Clean FastAPI backend with CORS support
- **Modern Web Interface**: Responsive chat UI built with vanilla HTML, CSS, and JavaScript
- **Real-time Communication**: Asynchronous API endpoints for fast responses
- **Easy Setup**: Simple configuration with environment variables

## Tech Stack

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **Google GenAI**: Integration with Gemini AI models (using the new `google-genai` package)
- **Python-dotenv**: Environment variable management
- **Uvicorn**: ASGI server for running FastAPI applications
- **Pydantic**: Data validation using Python type annotations

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with responsive design
- **JavaScript (ES6+):** Client-side logic and API communication

## Project Structure

```
Chatbot-Api-Project/
├── main.py              # FastAPI application and API endpoints
├── test_api.py          # API testing script
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not in git)
├── .gitignore          # Git ignore rules
├── LICENSE             # MIT License
├── README.md           # Project documentation
└── static/
    ├── index.html      # Main web interface
    ├── script.js       # Client-side JavaScript
    └── style.css       # Styling
```

## Prerequisites

- Python 3.8 or higher
- Google AI API key (Get one from [Google AI Studio](https://makersuite.google.com/app/apikey))

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Chatbot-Api-Project
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Unix/macOS:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   - Create a `.env` file in the project root
   - Add your Google API key:
     ```
     GOOGLE_API_KEY=your_api_key_here
     ```

## Usage

### Running the API Server

Start the FastAPI server:

```bash
python main.py
```

The API will be available at `http://localhost:8000`

### API Endpoints

- **GET /**: Root endpoint
  - Returns: `{"message": "Gemini Q&A Chatbot API"}`

- **POST /ask**: Ask a question to the AI
  - Request body: `{"question": "your question here"}`
  - Returns: `{"answer": "AI response"}`

### Using the Web Interface

1. Start the API server using `python main.py`
2. Open `static/index.html` in your web browser
3. Type your question and click Send or press Enter

### Testing the API

Run the test script to verify your API key is working:

```bash
python test_api.py
```

## API Example

Using curl:

```bash
curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{"question": "What is artificial intelligence?"}'
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Troubleshooting

### API Key Issues
- Ensure your `.env` file contains a valid Google API key
- Verify the API key has the necessary permissions
- Check that the key is not expired

### Quota Exceeded (429 Error)
If you receive a `RESOURCE_EXHAUSTED` or `429` error, you have exceeded your free tier quota:
- Free tier has daily and per-minute limits on requests and tokens
- Wait for the quota to reset (typically 24 hours for daily limits, or a few minutes for per-minute limits)
- Consider upgrading to a paid plan for higher limits
- Monitor your usage at: https://ai.dev/rate-limit

### Model Availability
Google frequently updates their AI models. If you encounter model-related errors:
- The current model is configured as `gemini-pro-latest` in `main.py`
- You can switch to other available models like `gemini-flash-latest` or `gemini-2.5-flash`
- Check Google's documentation for the latest available models

### Port Already in Use
If port 8000 is already in use, modify the port in `main.py`:
```python
uvicorn.run(app, host="0.0.0.0", port=8001)  # Change to available port
```

### CORS Issues
The API is configured to allow all origins for development. For production, update the CORS middleware in `main.py` to restrict origins:
```python
allow_origins=["https://yourdomain.com"]
```
