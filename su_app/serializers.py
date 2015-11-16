from rest_framework import serializers

class StatusUpdateSerializer(serializers.Serializer):
	id              = serializers.UUIDField(allow_null=True, required = False, read_only=True)
	#author          = serializers.CharField(required = True, min_length=6, error_messages={'min_length':'The author username cannot be less than 6 characters'})
	author          = serializers.CharField(required = True)

	#user_id         = serializers.UUIDField(required=False)

	created_at      = serializers.DateTimeField(allow_null=True,required=False, read_only=True)
	updated_at      = serializers.DateTimeField(allow_null=True,required=False, read_only=True)
	view_count      = serializers.IntegerField(allow_null=True, required=False, read_only=True)
	like_count      = serializers.IntegerField(allow_null=True, required=False, read_only=True)
	comment_count   = serializers.IntegerField(allow_null=True, required=False, read_only=True)
	share_count   	= serializers.IntegerField(allow_null=True, required=False, read_only=True)
	body            = serializers.CharField(max_length=400, error_messages={'max_length':'The content cannot be longuer than 400 characters'})
	location		= serializers.CharField(allow_null=True, required=False)
	at_mention 		= serializers.ListField(child=serializers.CharField(),required=False)
	tags 			= serializers.ListField(child=serializers.CharField(),required=False)

	link 			= serializers.URLField(required=False, allow_null=True) # check that it is a valid http link

	actor 			= serializers.DictField(required=False, allow_null=True,read_only=True)

	privacy_level	= serializers.CharField(allow_null=True, default='public')

	image_url	    = serializers.ImageField(allow_null=True, required=False, use_url=False)
	video_url 		= serializers.FileField(allow_null=True, required=False, use_url=False)

	photo 			= serializers.DictField(read_only=True)
	actions 		= serializers.DictField(read_only=True)

	video 			= serializers.CharField(required=False, allow_null=True, read_only=True)
