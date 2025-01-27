from flask import Blueprint, jsonify, request, session, render_template
from langchain.docstore.document import Document  # Add this import
from app.services.chat_service import custom_retrieval, generate_step_by_step_answer

chat_bp = Blueprint('chat', __name__)

@chat_bp.route('/')
def home():
    return render_template('index.html')

@chat_bp.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    question = data.get('message')
    
    context = custom_retrieval(question)
    
    if context:
        answer, has_more = generate_step_by_step_answer(context)
        session['full_answer'] = context.page_content
        session['last_step'] = 5
        return jsonify({
            'message': answer,
            'has_more': has_more
        })
    
    return jsonify({
        'message': "I'm sorry, I couldn't find an answer for that question.",
        'has_more': False
    })

@chat_bp.route('/api/read_more', methods=['POST'])
def read_more():
    last_step = session.get('last_step', 0)
    context_content = session.get('full_answer', '')
    
    if context_content:
        context = Document(page_content=context_content)
        next_chunk, has_more = generate_step_by_step_answer(context, start=last_step)
        
        if next_chunk:
            session['last_step'] = last_step + 5
            return jsonify({
                'message': next_chunk,
                'has_more': has_more
            })
    
    return jsonify({
        'message': "No more steps.",
        'has_more': False
    })



