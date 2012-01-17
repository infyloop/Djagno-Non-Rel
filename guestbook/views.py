# Create your views here.
from django.shortcuts import render_to_response
from guestbook.models import Entry
from guestbook.forms import EntryForm

def guestbook(request):
	form=EntryForm(request.POST)
	if form.is_valid():
		form.save()
	entries=Entry.objects.all().order_by("-date")
	templates={'form': form, 'entries': entries}
	return render_to_response("gbook.html", templates)
