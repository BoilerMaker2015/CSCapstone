from django.shortcuts import render,redirect
from .forms import EngineerForm
from .models import Engineer
# Create your views here.

# get all the engineers for the home page
def index(request):
    engineer_list = Engineer.objects.all()
    context = {"engineers": engineer_list} 
    return render(request, "engineerIndex.html", context)

def addEngineer(request):

    form_class = EngineerForm
    if (request.method == "POST"):
        form = form_class(request.POST)
        if (form.is_valid()):
            form.save()

            #engineer_list = Engineer.objects.all()
            #context = {"engineers": engineer_list}
            #return render(request, "engineerIndex.html", context)
            return redirect("engineer:index")
    else:

        context = {"form": form_class}
        return render(request, "engineerForm.html",context )

