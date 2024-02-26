from django.contrib import sitemaps
from django.urls import reverse

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.8
    

    def items(self):
        return ['home', 
            'aboutus', 
            'training',
            'contact', 
            'digital', 
            'core',
            'ai',
            'dimen','vr','dimen','python','react','angular','php','android','game','ml','dm',

            ]
    def location(self, item):
        return reverse(item)
    
    
     
