from django.http import HttpResponse

# Create your views here.
def index(request):
	name = "bipul"
    return HttpResponse("hello world")
