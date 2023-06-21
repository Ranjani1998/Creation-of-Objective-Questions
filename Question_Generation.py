#!/usr/bin/env python
# coding: utf-8

# Develop a solution that can automatically generate
# objective questions with multiple correct answers based on a given chapter from a subject.
# The generated questions should test the reader's understanding of the chapter and have
# more than one possible correct answer to increase the complexity and challenge of the
# questions.The generated questions should not only test the reader's comprehension of the
# chapter but also encourage them to think beyond the surface level and explore different
# perspectives and possibilities. Ultimately, the objective of this project is to develop a robust
# and accurate solution that can aid educators in creating engaging and challenging
# assessments for their students.

# In[1]:


import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer

def get_mca_questions(context):
    # Tokenize the context into sentences
    sentences = sent_tokenize(context)
    
    # Initialize a list to store the generated questions
    mca_questions = []
    
    for sentence in sentences:
        # Tokenize the sentence into words
        words = word_tokenize(sentence)
        
        # Remove stopwords
        words = [word.lower() for word in words if word.lower() not in stopwords.words('english')]
        
        # Perform part-of-speech tagging
        pos_tags = pos_tag(words)
        
        # Extract nouns and verbs from the sentence
        nouns = [word for word, pos in pos_tags if pos.startswith('NN')]
        verbs = [word for word, pos in pos_tags if pos.startswith('VB')]
        
        if nouns and verbs:
            # Generate a question based on the nouns and verbs
            question = "Which of the following are " + ' or '.join(verbs) + " " + ' or '.join(nouns) + "?"
            
            # Extract two correct options from the nouns
            correct_options = nouns[:2]
            
            # Generate options by lemmatizing the verbs
            lemmatizer = WordNetLemmatizer()
            options = [lemmatizer.lemmatize(verb, 'v') for verb in verbs]
            
            # Append the question, options, and correct options to the list
            mca_questions.append({
                'question': question,
                'options': options,
                'correct_options': correct_options
            })
    
    # Return the list of generated questions
    return mca_questions


#     The get_mca_questions function takes a context parameter, which is the text from a given chapter.
#     It tokenizes the context into sentences using the sent_tokenize function from NLTK.
#     It iterates over each sentence and performs the following steps:
#         Tokenizes the sentence into words using the word_tokenize function.
#         Removes stopwords from the words using a list of stopwords from the NLTK library.
#         Performs part-of-speech tagging on the words using the pos_tag function.
#         Extracts nouns and verbs from the sentence based on their part-of-speech tags.
#         Generates a question using the extracted nouns and verbs.
#         Extracts two correct options from the nouns.
#         Generates options by lemmatizing the verbs using the WordNet lemmatizer.
#         Appends the question, options, and correct options to the mca_questions list.
#     Finally, it returns the list of generated questions.

# In[2]:


import PyPDF2
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('omw-1.4')

def extract_text_from_pdf(pdf_path):
    text = ""
    
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        
        for page in reader.pages:
            text += page.extract_text()
    
    return text

# Provide the path to the PDF file
pdf_path = r"C:\Users\Subaranjani\Desktop\Subaranjani_nlp_assignment\Dataset\chapter-2.pdf"

# Extract text from the PDF file
pdf_text = extract_text_from_pdf(pdf_path)

# Generate MCA questions using the extracted text
mca_questions = get_mca_questions(pdf_text)

# Print the generated questions
for question in mca_questions:
    print("Q: " + question['question'])
    print("Options: " + ', '.join(question['options']))
    print("Correct Options: " + ', '.join(question['correct_options']))
    print()


# In[3]:


# Provide the path to the PDF file
pdf_path = r"C:\Users\Subaranjani\Desktop\Subaranjani_nlp_assignment\Dataset\chapter-3.pdf"

# Extract text from the PDF file
pdf_text = extract_text_from_pdf(pdf_path)

# Generate MCA questions using the extracted text
mca_questions = get_mca_questions(pdf_text)

# Print the generated questions
for question in mca_questions:
    print("Q: " + question['question'])
    print("Options: " + ', '.join(question['options']))
    print("Correct Options: " + ', '.join(question['correct_options']))
    print()


# In[4]:


# Provide the path to the PDF file
pdf_path = r"C:\Users\Subaranjani\Desktop\Subaranjani_nlp_assignment\Dataset\chapter-4.pdf"

# Extract text from the PDF file
pdf_text = extract_text_from_pdf(pdf_path)

# Generate MCA questions using the extracted text
mca_questions = get_mca_questions(pdf_text)

# Print the generated questions
for question in mca_questions:
    print("Q: " + question['question'])
    print("Options: " + ', '.join(question['options']))
    print("Correct Options: " + ', '.join(question['correct_options']))
    print()

