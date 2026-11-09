from django.shortcuts import render

from .models import Workshop

def workshop_list(request):
    workshop = Workshop.objects.all()
    context = {
        "workshops". workshops
    }

    return render(request, "workshops/workshop_list.html", context)