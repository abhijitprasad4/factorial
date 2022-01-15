from django.shortcuts import render

def index(request):
    if request.method == 'GET':
        number = int(request.GET['number'])
        fact = 1
        i = 1
        while i <= number:
            fact *= i
            i += 1
        fact = {"fact": fact,
                 "number": number,}
    else:
        fact = {}

    return render(request, "factorial/home.html", fact)