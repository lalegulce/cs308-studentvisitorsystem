from django.shortcuts import render
from .forms import GuideLoginForm
from .models import GuideCredentials
from cs308_proje.decorators import logintracker , login_check_required
# Create your views here.

def guide_login(request):

    if request.method == 'POST':
        form = GuideLoginForm(request.POST)

        if form.is_valid():
            guide_username = form.cleaned_data['guide_username']
            guide_password = form.cleaned_data['guide_password']

            guide = GuideCredentials.objects.get(guide_username = guide_username)
            
            if guide_password == guide.guide_password:
                loginchecker = logintracker()
                loginchecker.activate(guide_username)
                
                messages.info(request,"SUCCESSFULLY LOGGED IN!")

                return redirect('http://127.0.0.1:8000/guide-profile/')
        else:
            return redirect('http://127.0.0.1:8000/')
    else:
        return redirect('http://127.0.0.1:8000/')

def guide_login_page(request):
    form = GuideLoginForm()

    return render(request, 'guide_app/guide_login.html', {'guide_login': form})

def guide_logout(request):
    logout = logintracker()
    logout.deactivate()
    messages.info(request,"SUCCESSFULLY LOGGED OUT!")
    return redirect('http://127.0.0.1:8000')

def guide_profile_page(request):
    return render(request, 'guide_app/guide_profile_page.html', {})
