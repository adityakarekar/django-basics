from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the Shop Home Page!")


def about(request):
    return HttpResponse("This is the About Page of the Shop.")
