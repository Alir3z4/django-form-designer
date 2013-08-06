from form_designer.contrib.cms_plugins.form_designer_form.models import CMSFormDefinition
from form_designer.views import process_form
from form_designer import settings

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import ugettext as _


class FormDesignerPlugin(CMSPluginBase):
    model = CMSFormDefinition
    module = _('Form Designer')
    name = _('Form')
    admin_preview = False
    render_template = 'html/formdefinition/detail.html'

    def render(self, context, instance, placeholder):
        if instance.form_definition.form_template_name:
            form_template = instance.form_definition.form_template_name
        else:
            form_template = settings.DEFAULT_FORM_TEMPLATE
        context['form_template'] = form_template

        # Redirection does not work with CMS plugin, hence disable:
        return process_form(context['request'], instance.form_definition, context, disable_redirection=True)


plugin_pool.register_plugin(FormDesignerPlugin)
