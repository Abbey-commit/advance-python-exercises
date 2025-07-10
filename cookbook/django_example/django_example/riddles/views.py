from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Riddle, Option

def index(request):
    latest_riddles = Riddle.objects.order_by('-created_at')[:5]
    context = {
        'latest_riddles': latest_riddles,
        'message': 'Explore these prompts to reflect and grow.'
    }
    return render(request, 'riddles/index.html', context)

def detail(request, riddle_id):
    riddle = get_object_or_404(Riddle, id=riddle_id)
    return render(request, 'riddles/detail.html', {'riddle': riddle})

def answer(request, riddle_id):
    riddle = get_object_or_404(Riddle, id=riddle_id)
    if request.method == 'POST':
        try:
            selected_option = riddle.option_set.get(id=request.POST['option'])
            if selected_option.is_correct:
                return HttpResponseRedirect(reverse('riddles:index'))
            else:
                error_message = "That’s not quite it. Try another response!"
                return render(request, 'riddles/answer.html', {
                    'riddle': riddle,
                    'error_message': error_message
                })
        except (KeyError, Option.DoesNotExist):
            return render(request, 'riddles/answer.html', {
                'riddle': riddle,
                'error_message': 'Please select a response.'
            })
    return render(request, 'riddles/answer.html', {'riddle': riddle})