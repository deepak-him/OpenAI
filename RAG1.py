import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk import FreqDist

# Download necessary NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Function 1: Retrieve information based on the topic
def retrieve_information(library, topic):
    if topic in library:
        return library[topic]
    else:
        return "Topic not found in the library."

# Function 2: Process text using NLP (Keyword Extraction and Sentence Ranking)
def process_text_nlp(text):
    sentences = sent_tokenize(text)
    words = text.lower().split()
    
    # Remove stopwords and non-important words
    stop_words = set(stopwords.words('english'))
    important_words = [word for word in words if word.isalpha() and word not in stop_words]
    
    # Calculate word frequency
    freq_dist = FreqDist(important_words)
    
    # Rank sentences based on the frequency of important words they contain
    ranked_sentences = sorted(sentences, key=lambda sent: sum(freq_dist[word.lower()] for word in sent.split() if word.lower() in freq_dist), reverse=True)
    
    # Use top-ranked sentences to create a processed text
    top_sentences = ranked_sentences[:2]  # You can adjust the number of sentences to include
    processed_text = ' '.join(top_sentences)
    
    return processed_text

# Function 3: Generate a story using the retrieved and processed information
def generate_story(retrieved_info):
    processed_info = process_text_nlp(retrieved_info)
    story = (
        "🌟 Welcome to our journey through the Solar System! 🚀\n\n"
        f"{processed_info}\n\n"
        "Isn't it amazing how these planets, so different yet so connected, orbit the Sun in perfect harmony? "
        "The wonders of space are truly fascinating! 🪐✨"
    )
    return story

# Library with detailed information
library = {
    "planets": "There are eight planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.",
    "planet_sizes": "Jupiter is the largest planet, while Mercury is the smallest.",
    "planet_distances": "Mercury is closest to the Sun, and Neptune is the farthest.",
    "sun": "The Sun is a star that is the center of our Solar System.",
    "moons": "Jupiter has the most moons, with over 70, while Earth has just one."
}

# Step 2: Use the functions to retrieve information and generate a story
topic = "planets"
retrieved_info = retrieve_information(library, topic)
story = generate_story(retrieved_info)

# Output the story
print(story)

# Now, let's do a more detailed retrieval and story generation
retrieved_info_planets = retrieve_information(library, "planets")
retrieved_info_sizes = retrieve_information(library, "planet_sizes")
retrieved_info_distances = retrieve_information(library, "planet_distances")

# Combine the retrieved information
combined_info = f"{retrieved_info_planets} {retrieved_info_sizes} {retrieved_info_distances}"

# Generate a more detailed story with NLP processing
detailed_story = generate_story(combined_info)

# Output the more detailed story
print(detailed_story)
