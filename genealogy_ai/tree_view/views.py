import json
from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
# Create your views here.
 
def get_person(request):
    try:
        """persons = Person.nodes.all()
        nodes = [{"id": person.uid, "label": person.name} for person in persons]
        edges = []
        for person in persons: 
            for child in person.father_of.all():
                edges.append({
                    "from": str(person.uid),
                    "to": str(child.uid), 
                    "label": "FATHER_OF"
                })
            
            for child in person.mother_of.all():
                edges.append({
                    "from": str(person.uid),
                    "to": str(child.uid),
                    "label": "MOTHER_OF"
                })
        
        context = {
            "nodes_json": json.dumps(nodes),
            "edges_json": json.dumps(edges)
        }
        return render(request, 'tree_view/tree_view.html', context)"""

        nodes = Person.nodes.all()
        print(f"size: {len(Person.nodes)}")
        edges = []
        for node in nodes:
            for child in node.father_of.all():
                edges.append({
                    "source": node.name,
                    "target": child.name
                })
        graph_nodes = [{'name': node.name} for node in nodes]
        graph_edges = edges

        graph = {"Nodes": [{"name": node.name} for node in nodes], "Edges": edges}
        print(f"Graph Data: {graph}")

        context = {
            'nodes': json.dumps(graph_nodes),
            'links': json.dumps(graph_edges)
        }
        return render(request, 'tree_view/tree_view.html', context)
    except Exception as e:
        print(f"An error occured: {str(e)}")
        return HttpResponse(f"An error occured: {str(e)}", status=500)
