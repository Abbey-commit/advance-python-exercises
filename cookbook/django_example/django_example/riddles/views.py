from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to the Riddles app! View reflective prompts here.")

def detail(request, riddle_id):
    return HttpResponse(f"Viewing reflective prompt {riddle_id}")

def answer(request, riddle_id):
    return HttpResponse(f"Submitting response for prompt {riddle_id}")