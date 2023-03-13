from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def whatsapp(request):
    user = request.POST.get('From')
    message = request.POST.get('Body')
    print(f'{user} says {message}')

    return HttpResponse('Hello!')
