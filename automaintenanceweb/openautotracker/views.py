__author__ = 'rerobins'


from django.views.generic import TemplateView
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


class LandingPage(TemplateView):

    template_name = "landing.html"

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated():
            return HttpResponseRedirect(reverse('auto_maintenance_car_list'))

        return super(LandingPage, self).get(request, *args, **kwargs)


class PrivacyPage(TemplateView):
    template_name = "privacy.html"


class ChangeLogPage(TemplateView):
    template_name = "changelog.html"


class TermsOfServicePage(TemplateView):
    template_name = "termsofservice.html"
