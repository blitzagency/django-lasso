from links.models import Link
from links.models import Tag
from django.contrib import admin



class TagInline(admin.StackedInline):
	model = Tag
	extra = 3

class LinkAdmin(admin.ModelAdmin):
	list_display = ('url', 'pub_date')
	inlines = [TagInline]

admin.site.register(Link, LinkAdmin)
