from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from . import views
from django.conf.urls.static import static

from s31.views import AboutView, InfoView, GalleryView, SheduleView, DopinfoView, FeedbackView, FeedView, PedsostavView, \
    MethodView, PlanView, StructureView, ParliamentView, CircleView, EventView, ProgressView

from s31.views import AboutView, InfoView, GalleryView, SheduleView, DopinfoView, FeedbackView, FeedView, PedsostavView
from .views import HomeView
from django.conf import settings
from .views import article_list


urlpatterns = [
    url(r'^$', views.article_list, name='article_list'),
    url(r'^$', HomeView.as_view()),
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', AboutView.as_view(),name='about' ),
    url(r'^info/$', InfoView.as_view(),name='info' ),
    url(r'^gallery/$', GalleryView.as_view(),name='gallery'),
    url(r'^shedule/$', SheduleView.as_view(),name='shedule'),
    url(r'^dopinfo/$', DopinfoView.as_view(),name='dopinfo'),
    url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),
    url(r'^feedbacks/$', FeedView.as_view(), name="feedbacks"),
    url(r'^activities/pedsostav/$', PedsostavView.as_view(), name="pedsostav"),
    url(r'^activities/parliament/$', ParliamentView.as_view(), name="parliament"),
    url(r'^activities/circle/$', CircleView.as_view(), name="circle"),
    url(r'^activities/events/$', EventView.as_view(), name="events"),
    url(r'^activities/progress/$', ProgressView.as_view(), name="progress"),
    url(r'^method/method_theme/$', MethodView.as_view(), name="method_theme"),
    url(r'^method/plan/$', PlanView.as_view(), name="plan"),
    url(r'^method/structure/$', StructureView.as_view(), name="structure"),
    url(r'^method/normative/$', PedsostavView.as_view(), name="normative"),
    url(r'^pedsostav/$', PedsostavView.as_view(), name="pedsostav"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) \
            + static(settings.STATIC_URL, document_root = settings.STATICFILES_DIRS)
