from __future__ import unicode_literals
import youtube_dl

#++++++++++++++++++++++++++++++++++++++++

def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading, now converting ...')

ydl_opts = {}

ydl_opts = {
    'format': 'best',      
    'outtmpl': 'C:/Users/Juan/%(title)s.%(ext)s',        
    'noplaylist' : True,        
    'progress_hooks': [my_hook],  
}

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=K9FfOpBaK0I'])

#***************************************

#ydl_opts = {}

#with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#    meta = ydl.extract_info(
#        'https://www.youtube.com/watch?v=9bZkp7q19f0', download=False) 

#print 'upload date : %s' %(meta['upload_date'])
#print 'uploader    : %s' %(meta['uploader'])
#print 'views       : %d' %(meta['view_count'])
#print 'likes       : %d' %(meta['like_count'])
#print 'dislikes    : %d' %(meta['dislike_count'])
#print 'id          : %s' %(meta['id'])
#print 'format      : %s' %(meta['format'])