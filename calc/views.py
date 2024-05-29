# calc/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def calculate(request):
    if request.method == 'GET':
        num1 = float(request.GET.get('num1', 0))
        num2 = float(request.GET.get('num2', 0))
        operation = request.GET.get('operation')

        if operation == 'add':
            result = num1 + num2
        elif operation == 'sub':
            result = num1 - num2
        elif operation == 'mul':
            result = num1 * num2
        elif operation == 'div':
            result = num1 / num2 if num2 != 0 else 'Error'
        else:
            result = 'Invalid operation'

        return render(request, 'home.html', {'result': result})
