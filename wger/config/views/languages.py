# -*- coding: utf-8 -*-

# This file is part of wger Workout Manager.
#
# wger Workout Manager is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# wger Workout Manager is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License

import logging

from django.core.urlresolvers import reverse
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext as _
from django.utils.translation import ugettext_lazy

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from wger.core.models import Language

from wger.utils.generic_views import WgerDeleteMixin
from wger.utils.generic_views import WgerFormMixin
from wger.utils.generic_views import WgerPermissionMixin


logger = logging.getLogger('wger.custom')


class LanguageListView(WgerPermissionMixin, ListView):
    '''
    Show an overview of all languages
    '''
    model = Language
    template_name = 'language/overview.html'
    context_object_name = 'language_list'
    permission_required = 'core.change_language'


class LanguageDetailView(WgerPermissionMixin, DetailView):
    model = Language
    template_name = 'language/view.html'
    context_object_name = 'view_language'
    permission_required = 'core.change_language'


class LanguageCreateView(WgerFormMixin, CreateView):
    '''
    Generic view to add a new language
    '''

    model = Language
    title = ugettext_lazy('Add')
    form_action = reverse_lazy('config:language:add')
    permission_required = 'core.add_language'


class LanguageDeleteView(WgerDeleteMixin, DeleteView):
    '''
    Generic view to delete an existing language
    '''

    model = Language
    success_url = reverse_lazy('config:language:overview')
    messages = ugettext_lazy('Successfully deleted')
    permission_required = 'core.delete_language'

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(LanguageDeleteView, self).get_context_data(**kwargs)

        context['title'] = _(u'Delete {0}?').format(self.object.full_name)
        context['form_action'] = reverse('config:language:delete', kwargs={'pk': self.object.id})

        return context


class LanguageEditView(WgerFormMixin, UpdateView):
    '''
    Generic view to update an existing language
    '''

    model = Language
    form_action_urlname = 'config:language:edit'
    permission_required = 'core.change_language'

    def get_context_data(self, **kwargs):
        '''
        Send some additional data to the template
        '''
        context = super(LanguageEditView, self).get_context_data(**kwargs)
        context['title'] = _(u'Edit {0}').format(self.object.full_name)
        return context
