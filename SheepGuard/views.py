from django.shortcuts import render_to_response
from django.shortcuts import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def logout_view(request):
    logout(request)


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


def index(request):
    return render_to_response("sheepguard/index.html", RequestContext(request, {}))
