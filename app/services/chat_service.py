from fuzzywuzzy import process
from langchain.docstore.document import Document
from .data_service import get_documents

def custom_retrieval(question, threshold=80):
    documents = get_documents()
    doc_questions = [doc.page_content.split(' A: ')[0].replace('Q: ', '') 
                    for doc in documents]
    best_match, score = process.extractOne(question, doc_questions)

    if score < threshold:
        return None
    
    best_match_index = doc_questions.index(best_match)
    return documents[best_match_index]

def generate_step_by_step_answer(context, start=0, step_size=5):
    steps = [step.strip() for step in context.page_content.split('\n') if step.strip()]
    end = min(start + step_size, len(steps))
    chunk = steps[start:end]
    formatted_chunk = "<br><br>".join(chunk)
    return formatted_chunk, end < len(steps)





