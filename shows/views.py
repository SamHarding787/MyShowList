from django.shortcuts import render
from .forms import ShowForm
from .models import Show

def add_show(request):
	if request.method == 'POST':
		form = ShowForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('add_show')
	else:
		form = ShowForm()
	return render(request, 'shows/add_show.html', {'form': form})

def show_list(request):
	shows = Show.objects.all()
	return render(request, 'shows/show_list.html', {'shows': shows})
