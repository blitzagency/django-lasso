from tastypie.authorization import Authorization
from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from links.models import Link,Tag


class LinkResource(ModelResource):
	class Meta:
		queryset = Link.objects.all()
		authorization = Authorization()
		resource_name = 'link'

					
class TagResource(ModelResource):
	link = fields.ForeignKey(LinkResource, 'link')
	class Meta:
		queryset = Tag.objects.all()
		authorization = Authorization()
		resource_name = 'tag'
		filtering = {
						'value': ALL
					}
		