import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords

# # Function 1: Retrieve information based on the topic
# def retrieve_information(library, topic):
#     if topic in library:
#         return library[topic]
#     else:
#         return "Topic not found in the library."

# # Function 2: Generate a story using the retrieved information
# def generate_story(retrieved_info):
#     story = f"Let me tell you about the Solar System. {retrieved_info} The planets orbit around the Sun. Isn't that cool?"
#     return story

# # Library with detailed information
# library = {
#     "planets": "There are eight planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune.",
#     "planet_sizes": "Jupiter is the largest planet, while Mercury is the smallest.",
#     "planet_distances": "Mercury is closest to the Sun, and Neptune is the farthest.",
#     "sun": "The Sun is a star that is the center of our Solar System.",
#     "moons": "Jupiter has the most moons, with over 70, while Earth has just one."
# }

# # Step 2: Use the functions to retrieve information and generate a story
# topic = "planets"
# retrieved_info = retrieve_information(library, topic)
# story = generate_story(retrieved_info)

# # Output the story
# # print(story)

# # Now, let's do a more detailed retrieval and story generation
# retrieved_info_planets = retrieve_information(library, "planets")
# retrieved_info_sizes = retrieve_information(library, "planet_sizes")
# retrieved_info_distances = retrieve_information(library, "planet_distances")

# # Combine the retrieved information
# combined_info = f"{retrieved_info_planets} {retrieved_info_sizes} {retrieved_info_distances}"

# # Generate a more detailed story
# detailed_story = generate_story(combined_info)

# # Output the more detailed story
# print(detailed_story)




# Download necessary NLTK data
nltk.download('punkt_tab')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')

# Function 1: Retrieve information based on the topic
def retrieve_information(library, topic):
    if topic in library:
        return library[topic]
    else:
        return "Topic not found in the library."

# Function 2: Process text using NLP (e.g., summarization)
def process_text_nlp(text):
    sentences = sent_tokenize(text)
    # Simple processing: removing stopwords and keeping important sentences
    stop_words = set(stopwords.words('english'))
    filtered_sentences = [sentence for sentence in sentences if not any(word in stop_words for word in sentence.lower().split())]
    # Joining the filtered sentences to create a processed text
    processed_text = ' '.join(filtered_sentences)
    return processed_text

# Function 3: Generate a story using the retrieved and processed information
def generate_story(retrieved_info):
    processed_info = process_text_nlp(retrieved_info)
    story = f"Let me tell you about the Solar System. {processed_info} The planets orbit around the Sun. Isn't that fascinating?"
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
# print(story)

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
