# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import TemplateView

from s31.forms import FeedBackForm
from .models import Article, Feedback, Photo, Teacher, Person


# Create your views here.

class HomeView(TemplateView):
    template_name = 'index.html'

def article_list(request):
    articles= Article.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'index.html', {'articles':articles})

class AboutView(TemplateView):
    template_name = 'about.html'

class InfoView(TemplateView):
    template_name = 'info.html'

class GalleryView(TemplateView):
    template_name = 'gallery.html'

    def dispatch(self, request, *args, **kwargs):

        context ={
            'photos':Photo.objects.all()
        }
        return  render(request, self.template_name, context)

class SheduleView(TemplateView):
    template_name = 'shedule.html'


class DopinfoView(TemplateView):
    template_name = 'dopinfo.html'

class FeedbackView(TemplateView):
    template_name = "feedback.html"

    def dispatch(self, request, *args, **kwargs):
        context = {}
        form = FeedBackForm()
        if request.method=="POST":
            form = FeedBackForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, u"Спасибо")
                return redirect(reverse("feedback"))

        context['feedback_form']=form
        return render (request, self.template_name, context)

class FeedView(TemplateView):
    template_name = 'feedbacks.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect("/")
        context ={
            'feedbacks':Feedback.objects.all()
        }
        return  render(request, self.template_name, context)

class PedsostavView(TemplateView):

    template_name = 'activities/pedsostav.html'

    def dispatch(self, request, *args, **kwargs):

        context ={
            'teachers':Teacher.objects.all()
        }
        return  render(request, self.template_name, context)

class SheduleView(TemplateView):
    template_name = 'shedule.html'


class MethodView(TemplateView):
    template_name = 'method/method_theme.html'


class PlanView(TemplateView):
    template_name = 'method/plan.html'

class StructureView(TemplateView):
    template_name = 'method/structure.html'

class NormativeView(TemplateView):
    template_name = 'method/normative.html'

class ProgressView(TemplateView):
    template_name = 'activities/progress.html'

class EventView(TemplateView):
    template_name = 'activities/events.html'

class CircleView(TemplateView):
    template_name = 'activities/circle.html'

class ParliamentView(TemplateView):
    template_name = 'activities/parliament.html'


from django.shortcuts import render
from django_tables2 import RequestConfig
from .models import Person
from .tables import PersonTable

def people(request):
    table = PersonTable(Person.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'people.html', {'table': table})