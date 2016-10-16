from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import TemplateView
from django.template import RequestContext

class TimelineView(TemplateView, View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated and not request.GET.get('example'):
            return render(request, template_name='index.html')
        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        # TODO: Implement posting new tweets
        messages.warning(request, "Posting new tweets not implemented")

        return redirect(request.POST.get('next', 'home'))


class ProfileView(TemplateView, View):
    template_name = "profile.html"

    def get(self, request, *args, **kwargs):
        # TODO: Implement profile pages
        # messages.warning(request, "Profiles not implemented")
        # return redirect('home')
        return self.render_to_response({})

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return self.render_to_response({})