import nltk 
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

# Download necessary NLTK data
# nltk.download('punkt')
# nltk.download('stopwords')

# Sample text to be analyzed
text = """  
Artificial Intelligence (AI) is the simulation of human intelligence in machines that are designed to think and act like humans.
AI is widely used in various applications such as natural language processing, robotics, and machine learning. 
Natural language processing (NLP) helps computers understand and respond to human language. 
Robotics involves the design and operation of robots. 
Machine learning enables computers to learn from data without being explicitly programmed. 
There are various types of AI including narrow AI, which is specialized in one task, and general AI, which has the ability to perform any intellectual task that a human can do.  
"""  

# Function to preprocess text by removing stopwords and punctuation
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text)
    words = [word for word in words if word.lower() not in stop_words and word not in string.punctuation]
    return ' '.join(words)

# Split the text into sentences and preprocess each one
sentences = sent_tokenize(text)
preprocessed_sentences = [preprocess_text(sentence) for sentence in sentences]

# Load a pre-trained Sentence Transformer model
model = SentenceTransformer('all-mpnet-base-v2')

# Compute embeddings for the preprocessed sentences
sentence_embeddings = model.encode(preprocessed_sentences)

# Define a function to get the most relevant chunk
def get_most_relevant_chunk(question, sentences, sentence_embeddings, model):  
    question_embedding = model.encode([question])[0]  
    similarities = cosine_similarity([question_embedding], sentence_embeddings)[0]  
    most_similar_idx = np.argmax(similarities)  
    return sentences[most_similar_idx], similarities[most_similar_idx]

# Example question
question = "What is NLP?"

# Get the most relevant chunk
most_relevant_chunk, similarity = get_most_relevant_chunk(question, sentences, sentence_embeddings, model)

print(f"Question: {question}")  
print(f"Most relevant chunk: {most_relevant_chunk}")  
print(f"Similarity score: {similarity}")
