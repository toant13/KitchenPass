from SpouseChoices.models import SpouseRequest, SpouseResponse
from django.http.response import HttpResponse
from django.shortcuts import render
from django.template.context import RequestContext


# Create your views here.
# def index(request):
#     spouseReq = SpouseRequest.objects.order_by('question')[:5]
    
def index(request):
    top_spouse_requests = SpouseRequest.objects.order_by('question')[:5]
    context = RequestContext(request, {'top_spouse_requests' : top_spouse_requests,})
    return render(request, 'index.html', context)

def detail(request, SpouseRequest_id):
    return HttpResponse("DETAIL PAGE: %s" % SpouseRequest_id)