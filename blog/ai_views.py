import json
import os
import anthropic
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
@csrf_exempt
def improve_text(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'POST only'}, status=405)

    data = json.loads(request.body)
    text = data.get('text', '')
    mode = data.get('mode', 'improve')

    prompts = {
        'improve': f'Improve the following text. Make it clearer, more engaging and better structured. Keep the same meaning and tone. Return only the improved text with no explanation:\n\n{text}',
        'simplify': f'Simplify the following text. Make it easier to read and understand. Return only the simplified text with no explanation:\n\n{text}',
        'expand': f'Expand the following text with more detail and depth. Return only the expanded text with no explanation:\n\n{text}',
        'fix': f'Fix grammar, spelling and punctuation in the following text. Return only the corrected text with no explanation:\n\n{text}',
    }

    client = anthropic.Anthropic(api_key=os.environ.get('ANTHROPIC_API_KEY'))
    message = client.messages.create(
        model='claude-sonnet-4-20250514',
        max_tokens=2000,
        messages=[{'role': 'user', 'content': prompts.get(mode, prompts['improve'])}]
    )

    return JsonResponse({'result': message.content[0].text})