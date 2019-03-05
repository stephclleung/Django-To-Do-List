from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect #for redirect
from .models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.
# Browser calls a page = browser is REQUESTING a page //GET
# Posting a form : POST request

def home(request):
	total = List.objects.filter(done__lte=False).count()
	print(f"Total number of things to do : {total}")
	if request.method == 'POST':
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			items = List.objects.all
			messages.success(request, ('Quick Add: Item has been successfully added to To-Do List.'))
			return render(request, 'home.html', {'itemsInPage': items, 'total' : total})

	else: #GET request
		items = List.objects.all
		return render(request, 'home.html', {'itemsInPage': items, 'total' : total})
		#return render(items, 'home.html', {'items' : items})
		# render(source, destinate, dictionary key/value)

def edit(request, itemID):
	this_item = List.objects.get(pk=itemID)
	if this_item:
		if request.method == 'POST':
			form = ListForm(request.POST or None, instance=this_item)
			print(form)
			if form.is_valid():
				form.save()
				messages.success(request, ('Edit: Item has been edited.'))
				return redirect('home_page')
		else:
			return render(request, 'edit.html', {'itemForEdit' : this_item})

def add(request):
	if request.method == 'POST':
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			items = List.objects.all
			messages.success(request, ('Add in Detail: Item has been successfully added to To-Do List.'))
			total = List.objects.count()
			return render(request, 'home.html', {'itemsInPage': items, 'total' : total})

	return render(request, 'add.html', {})

def delete(request, itemID):
	item = List.objects.get(pk=itemID)
	if item:
		item.delete()
		messages.success(request, ('Delete: Item has been deleted from To-Do List.'))
	return redirect('archive_page') #django.shortcuts, django.http's HttpResponseRedirect



def mark_done(request, itemID):
	item = List.objects.get(pk=itemID)
	if item:
		item.done = True
		print(f"{item.item} 's done is mark to : {item.done}")
		print(f"Checking archive: {item.archived}")
		if item.archived:
			item.archved = False
		item.save()
	return redirect('home_page')

def undo_done(request, itemID):
	item = List.objects.get(pk=itemID)
	print(f"{item.item} 's done is mark to : {item.done}")
	if item:
		item.done = False
		#archive = False
		print(f"{item.item} 's done is mark to : {item.done}")
		item.save()
	return redirect('home_page')

def archive(request):
	archived_total = List.objects.filter(archived__lte=True).count()
	 #GET request
	items = List.objects.filter(archived__lte=True)
	return render(request, 'archive.html', {'itemsInPage': items, 'archived_total' : archived_total})
	#return render(items, 'home.html', {'items' : items})
	# render(source, destinate, dictionary key/value)

def undo_archive(request, itemID):
	item = List.objects.get(pk=itemID)
	if item:
		item.archived = False
		print(f"{item.item} 's archived is mark to : {item.archived}")
		item.save()
	return redirect('archive_page')

def mark_archive(request, itemID):
	item = List.objects.get(pk=itemID)
	if item:
		item.archived = True
		print(f"{item.item} 's archived is mark to : {item.archived}")
		item.save()
	return redirect('home_page')
