from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse, HttpResponseRedirect
from main.models import State, City, StateCapital
from django.template import RequestContext
from main.forms import ContactForm, CityEditForm, StateEditForm, CityNewForm, StateNewForm, StateCapitalEditForm, StateCapitalNewForm, CityRemoveForm, StateRemoveForm, StateCapitalRemoveForm
from django.core.mail import send_mail
from django.conf import settings

#list views
#detail views
#create view
#edit view
#delete view
#make the view --> make the url


def state_list(request):

    context = {}

    states = State.objects.all()

    context['states'] = states

    #template --> context dictionary --> context_instance variable
    return render_to_response('state_list.html', context, context_instance=RequestContext(request))



def state_detail(request, pk):
    context = {}

    state = State.objects.get(pk=pk)

    context['state'] = state

    city = request.GET.get('city', None)
    
    if city != None:
        cities = City.objects.filter(name__icontains=city, state=state)
    else:
        cities = City.objects.filter(state=state)

    context['cities'] = cities

    return render_to_response('state_detail.html', context, context_instance=RequestContext(request))


def state_search(request):

    context = {}

    context['request'] = request

    # context['get_vars'] = request.GET['a']

    #context['get_vars'] = request.GET.get('a', None)

    state = request.GET.get('state', None)

    #tate = request.POST.get('state', None)

    #states = State.objects.filter(name__icontains=state)


    if state != None:
        states = State.objects.filter(name__icontains=state)
    else:
        states = State.objects.all()

#    states.State.objects.all()

#    context['states'] = states

    context['states'] = states

    return render_to_response('state_search.html', context, context_instance=RequestContext(request))

def state_new(request):
    context = {}
    form = StateNewForm(request.POST or None)
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/state_capital_new/')

    return render_to_response('state_new.html', context, context_instance=RequestContext(request))


def state_edit(request, pk):
    context = {}
    state = State.objects.get(pk=pk)
    form = StateEditForm(request.POST or None, instance=state)
    context['state'] = state
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/state_list/')

    return render_to_response('state_edit.html', context, context_instance=RequestContext(request))

def state_remove(request, pk):
    context = {}
    state = State.objects.get(pk=pk)
    form = StateRemoveForm(request.POST or None, instance=state)
    context['state'] = state
    context['form'] = form
    if form.is_valid():
        form.save()
        state.delete()
        return redirect('/state_list/')

    return render_to_response('state_remove.html', context, context_instance=RequestContext(request))


def city_list(request):

    context = {}

    cities = City.objects.all()

    context['cities'] = cities

    #template --> context dictionary --> context_instance variable
    return render_to_response('city_list.html', context, context_instance=RequestContext(request))

def city_detail(request, pk):
    context = {}

    city = City.objects.get(pk=pk)

    context['city'] = city  

    return render_to_response('city_detail.html', context, context_instance=RequestContext(request))


def city_search(request):
    
    context = {}
    context['request'] = request
    city = request.GET.get('city', None)
    states = []
    if city != None:
        cities = City.objects.filter(name__icontains=city)
    else:
        cities = []
    for state in State.objects.all():
        include_state = False
        for c in cities:
            if c.state == state:
                include_state = True
            if include_state ==True:
                states.append(state)

    context['cities'] = cities                

    return render_to_response('city_search.html', context, context_instance=RequestContext(request))

def city_new(request):
    context = {}
    form = CityNewForm(request.POST or None)
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/state_list/')

    return render_to_response('city_new.html', context, context_instance=RequestContext(request))


def city_create(request):

    context = {}

    context['request'] = request.method

    context['states'] = State.objects.all()

    if request.method == "POST":
        name = request.POST.get('name', None)
        county = request.POST.get('county', None)
        latitude = request.POST.get('latitude', None)
        longitude = request.POST.get('longitude', None)
        zip_code = request.POST.get('zip_code', None)
        state_id = request.POST.get('state', None)

        if state_id != None:
            state = State.objects.get(pk=state_id)
        else:
            state = State.objects.get(name="Texas")

        the_city, created = City.objects.get_or_create(name=name)

        the_city.county = county
        the_city.lat = latitude
        the_city.lon = longitude
        the_city.state = state
        the_city.zip_code = zip_code

        the_city.save()

        context['created'] = "Operation Successful"

    elif request.method == 'GET':
        pass

    return render_to_response('city_create.html', context, context_instance=RequestContext(request))

def city_edit(request, pk):
    context = {}
    city = City.objects.get(pk=pk)
    form = CityEditForm(request.POST or None, instance=city)
    context['city'] = city
    context['form'] = form

    if form.is_valid():
        form.save()

        return redirect('/state_list/')

    return render_to_response('city_edit.html', context, context_instance=RequestContext(request))


def city_update(request):
    context = {}
    context['cities'] = City.objects.all()

    return render_to_response('city_update.html', context, context_instance=RequestContext(request))

def city_update_spec(request):
    city_id = request.POST.get('city_id', None)
    print city_id
    context = {}
    context['selected_city'] = City.objects.get(pk=city_id)
    context['request'] = request.method
    print context['request']
    context['cities'] = City.objects.all()

    context['states'] = State.objects.all()

    if request.method == "POST":
        name = request.POST.get('name', None)
        zip_code = request.POST.get('zip_code', None)
        lat = request.POST.get('lat', None)
        lon = request.POST.get('lon', None)
        county = request.POST.get('county', None)
        print county
        state_id = request.POST.get('state', None)
        state = ''
        if state_id != None:
            state = State.objects.get(pk=state_id)
            the_city = City.objects.get(pk=city_id)
            the_city.zip_code = zip_code
            the_city.lat = lat
            the_city.lon = lon
            the_city.state = state
            the_city.county = county
            the_city.save()
        else:
            pass
        

        context['created'] = "Operation Successful"

    elif request.method == 'GET':
        pass

    return render_to_response('city_update_spec.html', context, context_instance=RequestContext(request))

def city_delete(request):
    city_id = request.POST.get('city_id', None)
    print city_id
    context = {}
    context['cities'] = City.objects.all()
    context['request'] = request.method
    print City.objects.filter(pk=city_id)
    City.objects.filter(pk=city_id).delete()
    if city_id != None:
        return HttpResponseRedirect('/city_list/')
    else:
        pass
    
    return render_to_response('city_delete.html', context, context_instance=RequestContext(request))

def city_remove(request, pk):
    context = {}
    city = City.objects.get(pk=pk)
    form = CityRemoveForm(request.POST or None, instance=city)
    context['city'] = city
    context['form'] = form
    if form.is_valid():
        form.save()
        city.delete()
        return redirect('/state_list/')

    return render_to_response('city_remove.html', context, context_instance=RequestContext(request))

def state_capital_detail(request, pk):

    context = {}

    state_capital = StateCapital.objects.get(pk=pk)

    context['state_capital'] = state_capital 

    return render_to_response('state_capital_detail.html', context, context_instance=RequestContext(request))

def state_capital_search(request):
    
    context = {}

    context['request'] = request

    state_capital = request.GET.get('state_capital', None)

    if state_capital != None:
        state_capitals = StateCapital.objects.filter(name__icontains=state_capital)
    else:
        state_capitals = StateCapital.objects.all() 

    context['state_capitals'] = state_capitals

    return render_to_response('state_capital_search.html', context, context_instance=RequestContext(request))
def state_capital_list(request):

    context = {}

    state_capitals = StateCapital.objects.all()

    context['state_capitals'] = state_capitals

    #template --> context dictionary --> context_instance variable
    return render_to_response('state_capital_list.html', context, context_instance=RequestContext(request))

def state_capital_edit(request, pk):
    context = {}
    state_capital = StateCapital.objects.get(pk=pk)
    form = StateCapitalEditForm(request.POST or None, instance=state_capital)
    context['state_capital'] = state_capital
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/state_list/')

    return render_to_response('state_capital_edit.html', context, context_instance=RequestContext(request))

def state_capital_new(request):
    context = {}
    form = StateCapitalNewForm(request.POST or None)
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('/state_list/')

    return render_to_response('state_capital_new.html', context, context_instance=RequestContext(request))

def state_capital_remove(request, pk):
    context = {}
    state_capital = StateCapital.objects.get(pk=pk)
    form = StateCapitalRemoveForm(request.POST or None, instance=state_capital)
    context['state_capital'] = state_capital
    context['form'] = form
    if form.is_valid():
        form.save()
        state_capital.delete()
        return redirect('/state_list/')

    return render_to_response('state_capital_remove.html', context, context_instance=RequestContext(request))


def contact_view(request):
    context = {}

    if request.method =='POST':
        form = ContactForm(request.POST)
        context['form'] = form
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']

            send_mail('STATES SITE MESSAGE FROM %s' % name, 
                message, email,
                [settings.EMAIL_HOST_USER], 
                fail_silently=False)
            context['message'] = "email sent"
        else:
            context['message'] = form.errors
    elif request.method == 'GET':
        form = ContactForm()
        context['form'] = form
    return render_to_response('contact_view.html', context, context_instance=RequestContext(request))

def state_home(request):
    context = {}
    return render_to_response('state_home.html', context, context_instance=RequestContext(request))

