#  Story Analyzer

Analyze stories and discover their subject, atmosphere, target audience, and moral lessons.

##  Quick Start

```bash
# Clone
git clone https://github.com/yourusername/story-analyzer.git
cd story-analyzer

# Setup
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv add requests beautifulsoup4 python-dotenv openai

# Add API key to .env
echo "OPENROUTER_API_KEY=your_key_here" > .env

# Run
python main.py "url from reedsy.com"
