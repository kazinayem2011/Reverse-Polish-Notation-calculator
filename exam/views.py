from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, redirect
# from .forms import *
import math
import operator


# Create your views here.
operation_types = {'+':operator.add,
       '-':operator.sub,
       '*':operator.mul,
       '/':operator.truediv,
       '^':operator.pow,
       'sin':math.sin,
       'tan':math.tan,
       'cos':math.cos,
       'pi':math.pi}


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass


def calculator(request):
    arg = {}
    if request.method == 'POST':
        equation = request.POST.get('equation').split(' ')
        answer = calculate(request, equation)
        arg['answer'] = answer

    return render(request, 'exam/exam.html', arg)


def calculate(request, equation):
    stack = []
    result = 0
    for i in equation:
        if is_number(i):
            stack.insert(0,i)
        else:
            if len(stack) < 2:
                print('Error: wrong expression')
                messages.success(request, 'Error: wrong expression')
                break
            else:
                if len(i) == 1:
                    n1 = float(stack.pop(1))
                    n2 = float(stack.pop(0))
                    result = operation_types[i](n1,n2)
                    stack.insert(0,str(result))
                else:
                    n1 = float(stack.pop(0))
                    try:
                        result = operation_types[i](math.radians(n1))
                    except KeyError:
                        print('KeyError: wrong expression')
                        messages.success(request, 'Error: wrong expression')
                    stack.insert(0,str(result))
    return result
