from django.contrib.sitemaps import Sitemap
from videos.models import Video

class VideoSitemap(Sitemap):
    def videos(self):
        return Video.objects.all()
