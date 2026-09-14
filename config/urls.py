from django.contrib import admin
from django.urls import include, path
from apps.core.views import home, health

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home, name="home"),
    path("health/", health, name="health"),
    path("services/", include("apps.services.urls")),
    path("solutions/", include("apps.solutions.urls")),
    path("industries/", include("apps.industries.urls")),
    path("sap/", include("apps.sap_expertise.urls")),
    path("case-studies/", include("apps.case_studies.urls")),
    path("insights/", include("apps.insights.urls")),
    path("team/", include("apps.team.urls")),
    path("contact/", include("apps.contact.urls")),
    path("assessment/", include("apps.assessments.urls")),
    path("seo/", include("apps.seo.urls")),
]
handler404="apps.core.views.error_404"
handler403="apps.core.views.error_403"
handler500="apps.core.views.error_500"
