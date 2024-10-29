from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView
from .models import Gym, Member
from django.shortcuts import render

# Create your views here.
class GymListView(ListView):
    model = Gym
    template_name = 'gym_list.html'
    context_object_name = 'all_gyms_list'

class GymDetailView(DetailView):
    model = Gym
    template_name = 'gym_detail.html'

class GymCreateView(CreateView):
    model = Gym
    template_name = 'gym_create.html'
    fields = ['name', 'location','year_established']

class GymUpdateView(UpdateView):
    model = Gym
    template_name = 'gym_edit.html'
    fields = ['location']

class GymEquipListView(ListView):
    model = Gym
    template_name = 'gym_equip_list.html'
    context_object_name = 'all_gyms_list'

def query1(request):
    # Initialize an empty context to pass to the template
    context = {
        'member_name': None,
        'error_message': None,
    }

    try:
        oldest_member = Member.objects.earliest('dob')
        context['member_name'] = oldest_member.name

    except Member.DoesNotExist:
        context['error_message'] = "No clubs found."
    except Exception as e:
        context['error_message'] = f"An unexpected error occurred: {e}"

    # Render the template with the context
    return render(request, 'db_query1.html', context)

def query2(request):
    # Initialize an empty context to pass to the template
    context = {
        'member_num': None,
        'error_message': None,
    }

    try:
        context['member_num'] = Member.objects.all().count()

    except Member.DoesNotExist:
        context['error_message'] = "No members found."
    except Exception as e:
        context['error_message'] = f"An unexpected error occurred: {e}"

    # Render the template with the context
    return render(request, 'db_query2.html', context)

def query3(request):
    try:
        num = Member.objects.all().count()
    except Member.DoesNotExist:
        raise Http404("Member does not exist")
    return render(request, 'query2.html', {'number': num})

class QueryLinksView(TemplateView):
    template_name='queries_list.html'