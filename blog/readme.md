# Setting Up Template Dir
    @settings.py
    Locate your template section
        'DIRS': [os.path.join(BASE_DIR, 'templates')],

# Setting Up Static 
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# Post
## Admin will upload images, We need a place to stop it during development 
    @settings.py
        ### add the following 
                MEDIA_ROOT = os.path.join(BASE_DIR,"media")
                MEDIA_URL  = '/media/'
    @urls.py  project url
