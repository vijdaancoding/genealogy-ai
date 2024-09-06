from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
 
def helloWorld(request):
    html = f"""
            <h1>Home</h1>
            """
    return render(request, 'tree_view/tree_view.html')