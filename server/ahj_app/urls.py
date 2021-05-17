from django.urls import path, include
from . import views_ahjsearch, views_ahjsearch_api, views_users, views_misc, views_edits, views_datavis


urlpatterns = [
    path('ahj/',                          views_ahjsearch_api.ahj_list,          name='ahj'),
    path('ahj-private/',                  views_ahjsearch.webpage_ahj_list,      name='ahj'),
    path('geo/address/',                  views_ahjsearch_api.ahj_geo_address,   name='ahj'),
    path('geo/location/',                 views_ahjsearch_api.ahj_geo_location,  name='ahj'),
    path('ahj-one/',                      views_ahjsearch.get_single_ahj,        name='single_ahj'),
    path('ahj/set-maintainer/',           views_users.set_ahj_maintainer,        name='ahj-maintainer'),
    path('ahj/remove-maintainer/',        views_users.remove_ahj_maintainer,     name='ahj-maintainer'),
    path('edit/',                         views_edits.edit_list,                 name='edit-list'),
    path('auth/api-token/create/',        views_users.create_api_token,          name='create-api-token'),
    path('edit/review/',                  views_edits.edit_review,               name='edit-review'),
    path('edit/update/',                  views_edits.edit_update,               name='edit-update'),
    path('edit/add/',                     views_edits.edit_addition,             name='edit-addition'),
    path('edit/delete/',                  views_edits.edit_deletion,             name='edit-deletion'),
    path('user/update/<str:username>/',   views_users.user_update,               name='user-update'),
    path('user/edits/',                   views_misc.user_edits,                 name='user-edits'),
    path('user/comments/',                views_misc.user_comments,              name='user-comments'),
    path('user-one/<str:username>/',      views_users.get_single_user,           name='single-user-info'),
    path('ahj/comment/submit/',           views_misc.comment_submit,             name="comment-submit"),
    path('leaderboard/',                  views_misc.get_leaderboard_users,      name='leaderboard'),
    path('data-vis/data-map/',            views_datavis.data_map,                name='data-map'),
    path('data-vis/data-map/polygon/',    views_datavis.data_map_get_polygon,    name='data-map'),
    path('auth/form-validator/',          views_misc.form_validator,             name='form-validator'),
    path('auth/',                         include('djoser.urls')),
    path('auth/',                         include('djoser.urls.authtoken')),
    path('edit-conts/',                   views_edits.unconfirmed_conts,         name='unconfirmed-conts'),
    path('edit-insps/',                   views_edits.unconfirmed_insps,         name='unconfirmed-insps')
]
