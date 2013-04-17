from django.db import models



class Page(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=200)
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True)
    content = models.TextField()
    promo_image = models.ImageField(upload_to='images/learn', blank=True, null=True)
    template = models.CharField(max_length=200, blank=True, null=True)
    
    def __unicode__(self):
        return self.title
    
    def get_root(self):
        
        def _iterator(obj):
            if obj.parent:
                return _iterator(obj.parent)
            else:
                return obj
        
        return _iterator(self)
        
    
    def get_nav_tree(self):
        if self.parent is None: 
            nav_items = Page.objects.filter(parent=self)
        else:
            if self.parent.parent is None:
                nav_items = Page.objects.filter(parent=self.parent)
            else:
                if self.parent.parent.parent is None:
                    nav_items = Page.objects.filter(parent=self.parent.parent)
                else:
                    if self.parent.parent.parent.parent is None:
                        nav_items = Page.objects.filter(parent=self.parent.parent.parent)
        return nav_items
    
    def get_children(self):
        items = Page.objects.filter(parent=self)
        return items
    
    def get_absolute_url(self):
        url = "/%s/" % self.slug  
        return url
