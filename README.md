# Multilingual AI Chatbot

A web-based chatbot that can understand and respond in multiple languages (English, German, and Farsi) using state-of-the-art language models.

## Features

- 🌐 Multilingual support (English, German, Farsi)
- 🤖 AI-powered responses
- 🔄 Automatic language detection
- 💬 Real-time chat interface
- 🎨 Modern and responsive UI

## Technologies Used

- Python 3.9+
- Flask (Web Framework)
- Hugging Face Transformers
- PyTorch
- HTML/CSS/JavaScript

## Installation

1. Clone the repository:
   ```bash
   git clone [your-repository-url]
   cd windsurf-project
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. Activate the virtual environment (if not already activated):
   ```bash
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

2. Run the Flask application:
   ```bash
   python run.py
   ```

3. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

## Project Structure

```
windsurf-project/
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── routes.py            # Web routes
│   ├── chatbot.py           # Chatbot implementation
│   ├── static/              # Static files (CSS)
│   └── templates/           # HTML templates
├── requirements.txt         # Python dependencies
└── run.py                  # Application entry point
```

## Models Used

- Translation: facebook/mbart-large-50-many-to-many-mmt
- Text Generation: facebook/opt-350m

## Contributing

Feel free to submit issues and enhancement requests!
