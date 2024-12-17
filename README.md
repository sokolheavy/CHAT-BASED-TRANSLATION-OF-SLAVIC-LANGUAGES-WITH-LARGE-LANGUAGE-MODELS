# Chat-Based Translation System with LLMs

This repository contains the implementation of a chat-based translation system using Large Language Models (LLMs) for Slavic languages, as described in the research paper. The system compares different translation models and implements various prompt engineering techniques.

## Project Structure

```
├── src/
│   ├── config.py            # Configuration and API keys
│   ├── models.py            # Model implementations
│   ├── translation.py       # Translation functions
│   ├── similarity.py        # Similarity metrics
│   ├── utilities.py         # Helper functions
│   └── main.py             # Main application
├── tests/                   # Test files
├── requirements.txt         # Dependencies
└── README.md               # Documentation
```

## Features

- Support for multiple LLMs (ChatGPT-4, Claude 3.5, LLaMA-3)
- Integration with Google Translate and Helsinki-NLP's Opus-MT
- Multiple evaluation metrics (COMET, TER, CHRF, Text Correlation)
- Advanced prompt engineering techniques
- Support for 7 Slavic languages

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/chat-translation.git
cd chat-translation
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your API keys
```

## Usage

Basic translation:
```python
from src.main import translate_text

result = translate_text(
    text="Hello, how are you?",
    source_lang="en",
    target_lang="uk",
    model="ChatGPT"
)
```

## Configuration

Create a `config.json` file:
```json
{
    "openai_api_key": "your-key",
    "anthropic_api_key": "your-key",
    "openrouter_api_key": "your-key",
    "default_model": "ChatGPT",
    "timeout": 30
}
```

## Key Components

- `models.py`: Implements various translation models
- `similarity.py`: Contains metrics for translation evaluation
- `translation.py`: Handles core translation logic
- `utilities.py`: Provides helper functions

## Running Tests

```bash
python -m pytest tests/
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## License

MIT License

## Citation

If you use this code in your research, please cite:
```
@article{sokol2024chat,
    title={Chat-based Translation of Slavic Languages with Large Language Models},
    author={Sokol, O. O.},
    year={2024}
}
```

## Contact

Sokol O. O. - sokoloo1996@gmail.com

## Acknowledgments

- OpenAI for GPT models
- Anthropic for Claude
- Meta for LLaMA
- Helsinki-NLP for Opus-MT

This README provides a comprehensive overview of the project structure, setup instructions, and usage guidelines. The actual implementation details would need to be adjusted based on your specific requirements and the full codebase.
