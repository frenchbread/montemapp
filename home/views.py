from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.core.urlresolvers import reverse
from models import Testers
from forms import TestersForm



def home(request):

    args = {}
    args.update(csrf(request))

    form = TestersForm()


    #packing bags and fly--------------------------------------------------
    template = 'home.html'
    context = RequestContext(request)
    args.update({'form': form})

    return render_to_response(template, args, context_instance=context)


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def keepme(request):

    response = HttpResponse(mimetype="text/html")
    response['content-type'] = "text/html; charset=UTF-8"

    if request.method == 'POST':
        form = TestersForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.ip = get_client_ip(request)
            f.agent = request.META.get('HTTP_USER_AGENT', '')
            f.save()

            response.write("<div class='alert alert-success crazy' role='alert'><strong>You have been added to the list. We'll email you.</strong></div>")
        else:
            response.write("<div class='alert alert-danger crazy' role='alert'><strong>Form is not valid, sorry. Please try again</strong></div>")
    else:
        raise Http404

    return response
