import nltk
from nltk.tokenize import sent_tokenize
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import torch

# Download necessary NLTK data
nltk.download('punkt_tab')

# Define text
text = """  
Artificial Intelligence (AI) is the simulation of human intelligence in machines that are designed to think and act like humans.
AI is widely used in various applications such as natural language processing, robotics, and machine learning. 
Natural language processing (NLP) helps computers understand and respond to human language. 
Robotics involves the design and operation of robots. 
Machine learning enables computers to learn from data without being explicitly programmed. 
There are various types of AI including narrow AI, which is specialized in one task, and general AI, which has the ability to perform any intellectual task that a human can do.  
"""  

# Split text into sentences  
sentences = sent_tokenize(text)  

# Check if PyTorch is correctly installed
try:
    # Load a pre-trained Sentence Transformer model  
    model = SentenceTransformer('bert-base-nli-mean-tokens')  
except Exception as e:
    print(f"Error loading SentenceTransformer model: {e}")
    exit()

# Compute embeddings for sentences  
try:
    sentence_embeddings = model.encode(sentences)  
except Exception as e:
    print(f"Error computing embeddings: {e}")
    exit()

def get_most_relevant_chunk(question, sentences, sentence_embeddings, model):  
    # Embed the question  
    try:
        question_embedding = model.encode([question])[0]  
    except Exception as e:
        print(f"Error encoding question: {e}")
        return None, None
      
    # Calculate cosine similarity with each chunk  
    try:
        similarities = cosine_similarity([question_embedding], sentence_embeddings)[0]  
    except Exception as e:
        print(f"Error calculating cosine similarity: {e}")
        return None, None
      
    # Get the index of the most similar chunk  
    most_similar_idx = np.argmax(similarities)  
      
    # Return the most relevant chunk  
    return sentences[most_similar_idx], similarities[most_similar_idx]  

# Example question  
question = "What is NLP?"  
  
# Get the most relevant chunk  
most_relevant_chunk, similarity = get_most_relevant_chunk(question, sentences, sentence_embeddings, model)  
  
print(f"Question: {question}")  
print(f"Most relevant chunk: {most_relevant_chunk}")  
print(f"Similarity score: {similarity}") 
