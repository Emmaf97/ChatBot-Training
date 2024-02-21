                                                                                  # This Project idea was ihonspired by https://www.youtube.com/watch?v=CkkjXTER2KE

import json 
from difflib import get_close_matches                                             #Import necessary libraries to use for chatbot

def load_knowledge_base(file_path: str) -> dict:                                  #Specify file path of type string and return dictionary.
                                                                                  #This will then load knowledge_base.json into the programme
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def save_knowledge_base(file_path: str, data: dict):                               #This function saves the users answers into the knowledge_base.json file building up a memory.
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)
        
            
def find_best_match(user_question: str, questions: list [str])  -> str | None:     #Find the best match in the dictionary returns str or None if no match exists
    matches: list = get_close_matches(user_question, questions, n=1, cutoff=0.8)
    return matches[0] if matches else None

def get_answer_for_question(question: str, knowledge_base: dict) -> str | None:
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]
        
        
def chatbot():                                                                    #Creating the knowledge base based on user input.
                                                                                  #Updating and saving this to the json file.
                                                                                  #Checking whether input is present in the file and if not adding it.
                                                                                  #Type skip to exit programme
    knowledge_base: dict = load_knowledge_base("knowledge_base.json")
    while True:
        user_input: str = input("You: ")
        if user_input.lower() == quit:
            break
        
        best_match: str | None = find_best_match(user_input, [q["question"] for q in knowledge_base["questions"]])
        
        if best_match:
            answer: str = get_answer_for_question(best_match, knowledge_base)
            print(f'Bot: {answer}')
        else:
            print('I don\'t know the answer. Can you teach me? ')
            new_answer: str = input('Type the answer or "skip" to skip: ')
        
            if new_answer.lower() != "skip":
                knowledge_base["questions"].append({"question": user_input, "answer": new_answer})
                save_knowledge_base("knowledge_base.json", knowledge_base)
                print('Bot: Thank you! I have updated my knowledge base')
                               
if __name__ == '__main__':
    chatbot()