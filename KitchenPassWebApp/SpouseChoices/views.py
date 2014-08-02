from SpouseChoices.models import SpouseRequest, SpouseResponse
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from django.views.generic.list import ListView
from gcm.models import Device, get_device_model
# Create your views here.
# def index(request):
#     spouseReq = SpouseRequest.objects.order_by('question')[:5]
    
# def index(request):
#     top_spouse_requests = SpouseRequest.objects.order_by('question')[:5]
#     context = RequestContext(request, {'top_spouse_requests' : top_spouse_requests,})
#     return render(request, 'index.html', context)


class IndexView(ListView):
    context_object_name = 'SpouseRequests'
    template_name = 'index.html'
    queryset = SpouseRequest.objects.order_by('-votes')
    
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['SpouseResponses'] = SpouseResponse.objects.order_by('-votes')
        context['Devices'] = Device.objects.order_by('dev_id')
        return context

def detail(request, SpouseRequest_id):
    return HttpResponse("DETAIL PAGE: %s" % SpouseRequest_id)


def sendPost(request, SpouseRequest_id):
    sReq = SpouseRequest.objects.get(id=SpouseRequest_id)
    phone = get_device_model().objects.get(name='device1')
    phone.send_message(sReq.question, collapse_key='somethingfromview')  
    return HttpResponse('Spouse %s has send following message: %s' % (SpouseRequest_id, sReq))
        
        