📚 Story Analyzer

An AI-powered CLI tool for analyzing children's stories - extracting subject, atmosphere, target audience, and moral lessons from any webpage.

## Project Goals
This project was developed to demonstrate:
- ✅ AI API Integration (OpenRouter)
- ✅ Prompt Engineering
- ✅ Web Scraping (BeautifulSoup)
- ✅ Professional Python Development
- ✅ CLI Tool Building
- ✅ Environment Management (UV)

## 🚀 Features
- Extract story content from any URL
- AI-powered analysis of story elements
- Identify age-appropriateness
- Extract moral lessons and themes
- Export results to text files

## 🛠️ Technology Stack
- **Language**: Python 3.11+
- **AI API**: OpenRouter (NVIDIA Nemotron)
- **Web Scraping**: BeautifulSoup4, Requests
- **Environment**: UV Virtual Environment
- **Version Control**: Git & GitHub

## 📖 How It Works
1. User provides a story URL
2. Tool scrapes the webpage for story content
3. AI analyzes the content
4. Results displayed: subject, atmosphere, age group, target audience, moral lesson

## 🎯Reedsy.com
Every week thousands of writers submit stories to Reedsy contest.
- 1M+ authors
- 3,700+ publishing professionals
- 15,000+ books published annually
- Free writing tools and educational content

##  Quick Start

```bash
# Clone
git clone https://github.com/amirhosein24/story-analyzer.git
cd story-analyzer

# Setup
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv add requests beautifulsoup4 python-dotenv openai

# Add API key to .env
echo "OPENROUTER_API_KEY=your_key_here" > .env

# Run
python main.py "url from reedsy.com"
