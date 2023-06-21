# Creation-of-Objective-Questions

## Aim
The goal of the assignment is to develop a solution that can automatically
generate objective questions with multiple correct answers based on a given
chapter from a subject. The questions should test the reader's understanding of
the chapter and have more than one possible correct answer to increase
complexity. The questions should also encourage critical thinking and exploring
different perspectives. The objective is to create a robust and accurate solution
that can assist educators in creating engaging assessments for students.
## Solution Approach:
1. Preprocess the context: Before generating questions, it's important to preprocess the context to clean the text, remove unnecessary information, and tokenize it into sentences or paragraphs for further processing.
2. Extract relevant information: Analyze the preprocessed context to identify important facts, concepts, or statements that can serve as the basis for generating questions. This could involve techniques such as named entity recognition, part-of-speech tagging, or dependency parsing.
3. Generate questions: Based on the extracted information, formulate questions that test the reader's understanding. These questions should have multiple correct answer options. You can use templates or patterns to create various types of questions, such as "Which of the following are examples of...?" or "Which of the following are sources of...?".
4. Return the generated questions: Organize the generated questions into a list and return it from the get_mca_questions function.
