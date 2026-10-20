from django.shortcuts import render, redirect
from .forms import ShowForm
from .models import Show

def add_show(request):
	if request.method == 'POST':
		form = ShowForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('show_list')
	else:
		form = ShowForm()
	return render(request, 'shows/add_show.html', {'form': form})

def show_list(request):
	query = request.GET.get('q')

	if query:
		shows = Show.objects.filter(title__icontains=query)
	else:
		shows = Show.objects.all()

	return render(request, 'shows/show_list.html', {
		'shows': shows,
		'query': query
	})

def delete_show(request, show_id):
	if request.method == 'POST':
		show = Show.objects.get(id=show_id)
		show.delete()
	return redirect('show_list')
