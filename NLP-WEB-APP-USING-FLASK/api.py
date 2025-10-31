import paralleldots
from config import Config
import os
import time
import random

# Print debugging information
print(f"API Key from Config: {Config.PARALLELDOTS_API_KEY}")
print(f"API Key from ENV: {os.environ.get('PARALLELDOTS_API_KEY', 'Not found')}")

# Set API key from configuration
try:
    paralleldots.set_api_key(Config.PARALLELDOTS_API_KEY)
except Exception as e:
    print(f"Error setting API key: {str(e)}")

# Flag to use mock API instead of real API
USE_MOCK_API = True

def mock_ner(text):
    """Mock implementation of NER for testing when API is unavailable"""
    # Simulate processing time
    time.sleep(1)

    # Extract potential entities from the text
    words = text.split()
    entities = []

    # Look for capitalized words as potential entities
    for word in words:
        word = word.strip('.,!?":;()[]{}')
        if word and word[0].isupper() and len(word) > 2:
            # Determine entity type based on some simple rules
            if word in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']:
                category = 'date'
            elif word in ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']:
                category = 'date'
            elif word in ['UN', 'USA', 'UK', 'EU', 'NATO', 'WHO']:
                category = 'organization'
            elif word in ['France', 'China', 'India', 'Germany', 'Japan', 'Russia', 'Brazil', 'Canada']:
                category = 'place'
            else:
                # Randomly assign a category for other capitalized words
                categories = ['person', 'organization', 'place', 'date', 'title']
                category = random.choice(categories)

            entities.append({
                'name': word,
                'category': category
            })

    return {
        'entities': entities,
        'usage': 'mock',
        'model': 'mock-ner-model'
    }

def ner(text):
    try:
        print(f"NER Analysis - Input text: {text}")

        if USE_MOCK_API:
            print("Using mock NER API")
            ner_result = mock_ner(text)
        else:
            print(f"Using ParallelDots API with key: {paralleldots.get_api_key()}")
            ner_result = paralleldots.ner(text)

        print(f"NER Response: {ner_result}")
        return ner_result
    except Exception as e:
        print(f"Error in NER analysis: {str(e)}")
        return {"error": f"Failed to perform NER analysis: {str(e)}"}

def mock_sentiment(text):
    """Mock implementation of sentiment analysis for testing when API is unavailable"""
    # Simulate processing time
    time.sleep(1)

    # Simple sentiment analysis based on keywords
    positive_words = ['good', 'great', 'excellent', 'happy', 'positive', 'wonderful', 'love', 'best', 'beautiful', 'success']
    negative_words = ['bad', 'terrible', 'awful', 'sad', 'negative', 'hate', 'worst', 'ugly', 'failure', 'poor']

    text_lower = text.lower()

    # Count occurrences of positive and negative words
    positive_count = sum(1 for word in positive_words if word in text_lower)
    negative_count = sum(1 for word in negative_words if word in text_lower)

    # Calculate sentiment scores
    total = positive_count + negative_count
    if total == 0:
        # No sentiment words found, assume neutral
        positive = 0.33
        negative = 0.33
        neutral = 0.34
    else:
        positive = min(0.95, max(0.05, positive_count / (total * 2)))
        negative = min(0.95, max(0.05, negative_count / (total * 2)))
        neutral = max(0.05, 1 - positive - negative)

    return {
        'positive': positive,
        'negative': negative,
        'neutral': neutral,
        'usage': 'mock',
        'model': 'mock-sentiment-model'
    }

def mock_abuse(text):
    """Mock implementation of abuse detection for testing when API is unavailable"""
    # Simulate processing time
    time.sleep(1)

    # Simple abuse detection based on keywords
    abusive_words = ['hate', 'stupid', 'idiot', 'fool', 'dumb', 'moron', 'jerk', 'ass', 'damn', 'hell']

    text_lower = text.lower()

    # Count occurrences of abusive words
    abusive_count = sum(1 for word in abusive_words if word in text_lower)

    # Calculate abuse score
    if abusive_count > 0:
        abusive = min(0.95, max(0.5, abusive_count * 0.2))
    else:
        abusive = 0.05

    non_abusive = 1 - abusive

    return {
        'abusive': abusive,
        'non_abusive': non_abusive,
        'usage': 'mock',
        'model': 'mock-abuse-model'
    }

def sentiment_analysis(text):
    try:
        if USE_MOCK_API:
            print("Using mock sentiment analysis API")
            sentiment = mock_sentiment(text)
        else:
            sentiment = paralleldots.sentiment(text)
        return sentiment
    except Exception as e:
        print(f"Error in sentiment analysis: {str(e)}")
        return {"error": f"Failed to perform sentiment analysis: {str(e)}"}

def abuse_detection(text):
    try:
        if USE_MOCK_API:
            print("Using mock abuse detection API")
            abuse = mock_abuse(text)
        else:
            abuse = paralleldots.abuse(text)
        return abuse
    except Exception as e:
        print(f"Error in abuse detection: {str(e)}")
        return {"error": f"Failed to perform abuse detection: {str(e)}"}
