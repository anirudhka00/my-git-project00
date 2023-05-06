from django.shortcuts import render
#from . import machine_learning_model
from . import math
def home(request):
    return render(request,"index.html")

def result(request):
    user_input = request.GET["user_input"]
    #user_input = machine_learning_model.multiplier(user_input)
    user_input = math.add(user_input)
    return render(request,"result.html",{'home_input': user_input})
