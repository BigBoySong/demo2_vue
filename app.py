#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-11-22 21:11:17
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
from db import *
from flask import Flask ,render_template,jsonify,request


app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/get_content',methods=['POST'])
def get_content():
	if request.method=='POST':
		page_num,limt,item_type=(int(request.form['page_num']),int(request.form['limt']),str(request.form['item_type']))
		data=db_get_item(page_num,limt,item_type)
		return jsonify({'data':data,'msg':'本网站数据来源互联网爬虫嗅探所获,如有侵权请于网站管理员联系!<<Mail:910976007@qq.com>>'})

@app.route('/get_item_count',methods=['POST'])
def get_item_count():
	if request.method=='POST':
		item_type=str(request.form['item_type'])
		data=db_get_item_count(item_type)
		return jsonify(data)

@app.route('/get_item_content',methods=['POST'])
def get_item_content():
	if request.method=='POST':
		item_id=request.form['item_id']
		item_save_filepath=db_get_item_content(item_id)
		with open(item_save_filepath,'r') as f:
			data=f.read()
		return jsonify({'data':data})
















if __name__=='__main__':
	app.run(host='192.168.2.100',port='8060',debug=True)
