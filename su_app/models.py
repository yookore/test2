from django.db import models
from django.conf import settings
# Create your models here.

from cassandra.cqlengine import columns, connection
from cassandra.cqlengine.models import Model

from uuid import uuid1, uuid4
from datetime import datetime
import os, json

print ">>>In models.py"

from su_app.yookosusers import YookosUser
user = YookosUser()
#connection.setup(consistency=3)

class StatusUpdate(Model):
	__table_name__  = 'statusupdate'

	author          = columns.Text(primary_key=True)
	id              = columns.TimeUUID(primary_key = True, clustering_order='DESC') # can't cluster by the first primary key

	user_id 		= columns.UUID(index=True)

	body            = columns.Text(required = True)
	location        = columns.Text(required=False)

	created_at      = columns.DateTime(default=datetime.now())
	updated_at      = columns.DateTime(default=datetime.now())

	view_count      = columns.Integer(default=0)
	like_count      = columns.Integer(default=0)
	comment_count   = columns.Integer(default=0)
	share_count   	= columns.Integer(default=0)

	tags            = columns.List(value_type=columns.Text(), default=[])
	at_mention      = columns.List(value_type=columns.Text(), default=[]) # @mention: [username1, username2,....]

	uri_image       = columns.List(value_type=columns.UUID(), default=[]) #['url1','url2',...'urln']
	img             = columns.Bytes()
	image_url       = columns.Text()
	video_url 		= columns.Text()

	link       		= columns.Text()

	privacy_level	= columns.Text(required=False, default='public')

	# For the photo
	url        		= columns.Text(required=False)
	url_thumbnail   = columns.Text(required=False)

	# For the video
	url_video 		= columns.Text(required=False)

	deleted 		= columns.Boolean(default=False)

	def actor(self):
		return user.get_upm(self.author)

	def actions (self):
		return {
			'like':		'/api/v1/likes/%s/'%(self.id),
			'comment':	'/api/v1/comments/%s/list/'%(self.id),
		}

	def photo (self):
		return {
			'url_original': self.url,
			'url_thumbnail': self.url_thumbnail
		}
	def video (self):
		return self.url_video

	def __unicode__(self):
		return self.body

	def __str__(self):
		return  self.body

	def serialise(self):
		d =  {}
		'''
		for k in post.keys():
			if isinstance(post[k], datetime):
				d[k] = str(post[k])
			else:
				d[k] = post[k]
		'''
		d['body'] 	= self.body
		d['author'] = self.author

		return json.dumps(d)
