from django.shortcuts import render

# Create your views here.
def variable_view(request):
    # Example of a view that uses a variable
    context = {
        'variable_name': 'Hello, World!'
    }
    return render(request, 'learning/variables_and_constants.html', context)