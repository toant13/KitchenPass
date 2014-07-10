from SpouseChoices.models import SpouseRequest, SpouseResponse
from django.http.response import HttpResponse
from django.views.generic.list import ListView


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
        return context

def detail(request, SpouseRequest_id):
    return HttpResponse("DETAIL PAGE: %s" % SpouseRequest_id)