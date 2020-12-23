from django.shortcuts import render, redirect

from reg_user.forms import RegsitrationForm

def home(request):
    if request.method == 'POST':
        form = RegsitrationForm(request.POST)
        if form.is_valid():
            #form.save()
            messages.success(request, 'New success!')
            return redirect('reg_user/home')
        else:
            messages.error(request, 'Invalid Please try again.')
    else:
        form = RegsitrationForm()
    return render(request, 'reg_user/home.html', {'form': form})

def form2(request):
    if request.method == 'POST':
        form = RegsitrationForm(request.POST)
        if form.is_valid():
            #form.save()
            messages.success(request, 'New success!')
            return redirect('reg_user/form2')
        else:
            messages.error(request, 'Invalid Please try again.')
    else:
        form = RegsitrationForm()
    return render(request, 'reg_user/form2.html', {'form': form})
