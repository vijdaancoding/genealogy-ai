import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
# Create your views here.
 
def get_person(request):
    persons = Person.nodes.all()
    nodes = [{"id": person.id, "label": person.name} for person in persons]
    edges = []
    for person in persons: 
        for child in person.father_of:
            edges.append({
                "from": person.id,
                "to": child.id, 
                "label": "FATHER_OF"
            })
        
        for child in person.mother_of:
            edges.append({
                "from": person.id,
                "to": child.id,
                "label": "MOTHER_OF"
            })
    
    context = {
        "nodes_json": json.dumps(nodes),
        "edges_json": json.dumps(edges)
    }
    return render(request, 'tree_view.html', context)