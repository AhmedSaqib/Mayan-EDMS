from __future__ import unicode_literals

from django.conf.urls import url

from .views import (
    ImpersonateEndView, ImpersonateStartView, MayanLoginView, MayanLogoutView,
    MayanPasswordChangeDoneView, MayanPasswordChangeView,
    MayanPasswordResetCompleteView, MayanPasswordResetConfirmView,
    MayanPasswordResetDoneView, MayanPasswordResetView, UserSetPasswordView
)

urlpatterns_authenticattion = [
    url(regex=r'^login/$', view=MayanLoginView.as_view(), name='login_view'),
    url(
        regex=r'^logout/$', view=MayanLogoutView.as_view(), name='logout_view'
    ),
]

urlpatterns_password = [
    url(
        regex=r'^password/change/done/$',
        view=MayanPasswordChangeDoneView.as_view(), name='password_change_done'
    ),
    url(
        regex=r'^password/change/$', view=MayanPasswordChangeView.as_view(),
        name='password_change_view'
    ),
    url(
        regex=r'^password/reset/complete/$',
        view=MayanPasswordResetCompleteView.as_view(),
        name='password_reset_complete_view'
    ),
    url(
        regex=r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        view=MayanPasswordResetConfirmView.as_view(),
        name='password_reset_confirm_view'
    ),
    url(
        regex=r'^password/reset/done/$',
        view=MayanPasswordResetDoneView.as_view(),
        name='password_reset_done_view'
    ),
    url(
        regex=r'^password/reset/$', view=MayanPasswordResetView.as_view(),
        name='password_reset_view'
    ),
    url(
        regex=r'^users/(?P<pk>\d+)/set_password/$',
        view=UserSetPasswordView.as_view(), name='user_set_password'
    ),
    url(
        regex=r'^users/multiple/set_password/$',
        view=UserSetPasswordView.as_view(), name='user_multiple_set_password'
    ),
]

urlpatterns_user_impersonation = [
    url(
        regex=r'^impersonate/end/$', view=ImpersonateEndView.as_view(),
        name='impersonate_end'
    ),
    url(
        regex=r'^impersonate/start/$', view=ImpersonateStartView.as_view(),
        name='impersonate_start'
    )
]

urlpatterns = []
urlpatterns.extend(urlpatterns_authenticattion)
urlpatterns.extend(urlpatterns_password)
urlpatterns.extend(urlpatterns_user_impersonation)
