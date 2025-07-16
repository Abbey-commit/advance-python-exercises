from django.shortcuts import render
from .models import Riddle

def index(request):
    latest_riddles = Riddle.objects.order_by('-created_at')[:5]
    context = {
        'latest_riddles': latest_riddles,
        'message': 'Explore these prompts to reflect and grow.'
    }
    return render(request, 'riddles/index.html', context)

