"""Simple Story Analyzer - Single File Version"""

import os
import re
import sys
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
from dotenv import load_dotenv

# Load API key
load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

def extract_story(url):
    """Extract story from webpage."""
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove unwanted elements
        for tag in soup(['script', 'style', 'nav', 'footer', 'header', 'aside']):
            tag.decompose()
        
        # Get title
        title = soup.title.string if soup.title else "Unknown Story"
        title = re.sub(r'\s+', ' ', title).strip()
        
        # Get text from paragraphs
        paragraphs = soup.find_all('p')
        text = ' '.join([p.get_text() for p in paragraphs])
        text = re.sub(r'\s+', ' ', text).strip()
        
        return {
            'title': title,
            'text': text[:3000],
            'url': url
        }
        
    except Exception as e:
        return {'error': str(e)}

def analyze_story(title, text):
    """Analyze story with AI."""
    if not api_key:
        return "❌ Error: OPENROUTER_API_KEY not found in .env file"
    
    if len(text) < 100:
        return "❌ Error: Story text too short or empty"
    
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )
    
    prompt = f"""
    Analyze this children's story and tell me:
    
    1. 📖 SUBJECT: What is the story about? (1 sentence)
    2. 🎨 ATMOSPHERE: What's the mood/tone?
    3. 👶 AGE GROUP: What age group would enjoy this?
    4. 👧 WHO WOULD LOVE IT: What kind of kids would like this?
    5. 🌟 MAIN LESSON: What's the moral or key takeaway?
    
    Story Title: {title}
    Story: {text[:3000]}
    """
    
    try:
        response = client.chat.completions.create(
            model="nvidia/nemotron-3-super-120b-a12b:free",
            messages=[
                {"role": "system", "content": "You analyze children's stories. Extract subject, atmosphere, and target audience. Be clear and concise."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.5,
            max_tokens=600
        )
        
        return response.choices[0].message.content
        
    except Exception as e:
        return f"❌ Error analyzing story: {str(e)}"

def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("\n❌ Please provide a story URL")
        print("\nUsage:")
        print(f"  python story_analyzer.py \"https://example.com/story\"")
        print(f"  python story_analyzer.py \"https://example.com/story\" --save")
        sys.exit(1)
    
    url = sys.argv[1]
    save = "--save" in sys.argv
    
    print("\n" + "="*60)
    print("📖 STORY ANALYZER")
    print("="*60)
    print(f"\n🔗 URL: {url}")
    print("⏳ Fetching story...\n")
    
    # Extract story
    story = extract_story(url)
    
    if 'error' in story:
        print(f"❌ Error: {story['error']}")
        sys.exit(1)
    
    print(f"📌 Title: {story['title']}")
    print(f"📝 Length: {len(story['text'])} characters")
    print("\n🤖 Analyzing with AI...\n")
    
    # Analyze
    result = analyze_story(story['title'], story['text'])
    
    # Display
    print("="*60)
    print(result)
    print("="*60)
    
    # Save if requested
    if save:
        filename = f"analysis_{re.sub(r'[^a-zA-Z0-9]', '_', story['title'][:20])}.txt"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Story: {story['title']}\n")
            f.write(f"URL: {url}\n\n")
            f.write(result)
        print(f"\n💾 Saved to: {filename}")
    
    print(f"\n🔗 Source: {url}")
    print("\n✅ Done!")

if __name__ == "__main__":
    main()