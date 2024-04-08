from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def handler403(request, exception):
    """
    Display custom 403 page
    """
    return render(request, "403.html", status=403)


def handler404(request, exception):
    """
    Display custom 404 page
    """
    return render(request, "404.html", status=404)


def handler405(request, exception):
    """
    Display custom 405 page
    """
    return render(request, "405.html", status=405)


def handler500(request):
    """
    Display custom 500 page
    """
    return render(request, "500.html", status=500)
