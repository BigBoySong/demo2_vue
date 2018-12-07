#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-10-11 14:29:58
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os,json
from peewee import *
from playhouse.db_url import connect

#创建链接
db = connect('mysql://root:songnan1994@localhost:3306/sex_text')

#定义数据表模型
class ITEM_Info(Model):
	item_title = CharField(null=True,index = True)
	item_type= CharField(null=True,index = True)
	item_update=CharField(null=True,index = True)
	item_url=CharField(null=True,index = True)
	item_filepath=CharField(null=True,index = True)
	item_briefly=TextField(null=True)
	class Meta:
		database = db

def db_get_item_content(item_id):
	item = ITEM_Info.get(ITEM_Info.id == item_id)
	return item.item_filepath

def db_get_item_count(item_type):
	with db.atomic():
		count=ITEM_Info.select().where(ITEM_Info.item_type == item_type).count()
	return {'count':count}

def db_get_item(page_num,limt,item_type):
	data=[]
	with db.atomic():
		for item in ITEM_Info.select().where(ITEM_Info.item_type == item_type).order_by(-ITEM_Info.item_update).paginate(page_num, limt):
			briefly=item.item_briefly
			data.append({'id': item.id,'time':item.item_update,'text':item.item_title})
	return data
	