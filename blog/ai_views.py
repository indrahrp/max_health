import json
import os
import anthropic
from datetime import date
from django.http import JsonResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required

_client = None

def _get_client():
    global _client
    if _client is None:
        _client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
    return _client


@staff_member_required
@csrf_exempt
def improve_text(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)

    data = json.loads(request.body)
    text = data.get('text', '')
    mode = data.get('mode', 'improve')

    user_prompts = {
        'improve': f'Improve the following text. Make it clearer, more engaging and better structured. Keep the same meaning and tone. Return only the improved text:\n\n{text}',
        'simplify': f'Simplify the following text. Make it easier to read and understand. Return only the simplified text:\n\n{text}',
        'expand': f'Expand the following text with more detail and depth. Return only the expanded text:\n\n{text}',
        'fix': f'Fix grammar, spelling and punctuation in the following text. Return only the corrected text:\n\n{text}',
        'tldr': f'Write a 2-3 sentence TL;DR summary of the following content. Return only the summary:\n\n{text}',
    }

    system = [
        {
            'type': 'text',
            'text': 'You are a health and wellness writing assistant. Follow instructions exactly. Return only the requested output with no additional explanation or commentary.',
            'cache_control': {'type': 'ephemeral'},
        }
    ]

    client = _get_client()
    message = client.messages.create(
        model='claude-sonnet-4-6',
        max_tokens=2000,
        system=system,
        messages=[{'role': 'user', 'content': user_prompts.get(mode, user_prompts['improve'])}],
    )

    return JsonResponse({'result': message.content[0].text})


_CHAT_SYSTEM = None

def _chat_system_block():
    global _CHAT_SYSTEM
    if _CHAT_SYSTEM is None:
        _CHAT_SYSTEM = [
            {
                'type': 'text',
                'text': (
                    'You are a knowledgeable assistant for a blog called "Essential Topics" covering '
                    'artificial intelligence (LLMs, machine learning, AI safety, prompt engineering), '
                    'human health and medicine, molecular biology, and genetics/genomics. '
                    'Answer questions clearly and helpfully based on current evidence and research. '
                    'For health questions, note that individual decisions should be discussed with a qualified healthcare provider. '
                    'Keep answers concise (under 300 words) and insightful. '
                    'If a question is clearly outside these four domains, politely redirect.'
                ),
                'cache_control': {'type': 'ephemeral'},
            }
        ]
    return _CHAT_SYSTEM


_RATE_LIMIT_PER_DAY = 15


@csrf_exempt
def health_chat(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)

    # Session-based rate limiting
    today = str(date.today())
    session_key = f'chat_count_{today}'
    count = request.session.get(session_key, 0)
    if count >= _RATE_LIMIT_PER_DAY:
        return JsonResponse({'error': 'Daily question limit reached. Come back tomorrow!'}, status=429)

    data = json.loads(request.body)
    question = data.get('question', '').strip()
    if not question:
        return JsonResponse({'error': 'No question provided'}, status=400)
    if len(question) > 1000:
        return JsonResponse({'error': 'Question too long'}, status=400)

    request.session[session_key] = count + 1

    client = _get_client()
    message = client.messages.create(
        model='claude-sonnet-4-6',
        max_tokens=600,
        system=_chat_system_block(),
        messages=[{'role': 'user', 'content': question}],
    )

    return JsonResponse({'answer': message.content[0].text})
