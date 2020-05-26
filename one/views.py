from django.shortcuts import render, HttpResponsePermanentRedirect, reverse


def index_redirect(request):
    return HttpResponsePermanentRedirect(reverse("app1_index"))


def index(request):
    return render(request, "one/index.html")
