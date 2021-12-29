from django.shortcuts import render
import requests
import json
# Create your views here.
def HomePage(request):
    return render(request,'index.html')

def LoginPage(request):

    return render(request,'loginpage.html')


def AddBook(request):
    return render(request, 'addbook.html')


def UpdateBook(request,book_id):
    res = requests.get('http://127.0.0.1:8000/book_detail/'+str(book_id)+'/')
    data = json.loads(res.text)
    d = {"data":data}
    return render(request, 'updatebook.html',d)


