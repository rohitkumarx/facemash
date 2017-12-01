from rest_framework.serializers import (
	ModelSerializer, 
	HyperlinkedIdentityField,
	SerializerMethodField
)

from peepcompare.models import FaceMash
from peepcompare.users_api.serializers import UserDetailSerializer

class FacemashDetailSerializer(ModelSerializer):
	user = UserDetailSerializer()
	class Meta:
		model = FaceMash
		fields = [
			'user',
			'name',
			'photo',
			'ratings',
		]

class FacemashListSerializer(ModelSerializer):
	url = HyperlinkedIdentityField(
		view_name = 'facemash_api:detail'
	)
	delete_url = HyperlinkedIdentityField(
		view_name = 'facemash_api:delete'
	)
	
	user = UserDetailSerializer()#SerializerMethodField()
	image = SerializerMethodField()
	class Meta:
		model = FaceMash
		fields = [
			'url',
			'user',
			'id',
			'name',
			'image',
			'ratings',
			'delete_url'
		]

	def get_user(self, obj):
		try:
			return str(obj.user.username)
		except:
			return None
	def get_image(self,obj):
		try:
			image = obj.photo.url
		except:
			image = None
		return image

class FacemashCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = FaceMash
		fields = [
			'id',
			'name',
			'photo'
		]
"""

new_item = FacemashSerializer(data = data)

if new_item.is_valid():
	new_item.save()
else:
	print(new_item.errors)
"""