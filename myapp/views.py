from django.shortcuts import render
from celeryproject.celery import add
from celery.result import AsyncResult
# Create your views here.
def index(request):
    result = add.delay(10,20)
    print("results: ", result)
    return render(request,"myapp/home.html", {'result':result})
def check_result(request, task_id):
    # Retrieve the task result using the task_id
    result = AsyncResult(task_id)
    # print("Ready: ", result.ready())
    # print("Successful: ", result.successful())
    # print("Failed: ", result.failed())
    # print("Get: ", result.get())
    return render(request, 'myapp/result.html', {'result':result})
def about(request):
    print("results: ")
    return render(request,"myapp/about.html")
def contact(request):
    print("results: ")
    return render(request,"myapp/contact.html") 