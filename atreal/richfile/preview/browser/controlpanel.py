from zope.interface import Interface
from zope.component import adapts
from zope.interface import implements
from zope.schema import TextLine, Choice, List, Bool
from zope.formlib import form

from Products.CMFDefault.formlib.schema import ProxyFieldProperty
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.Five.browser.pagetemplatefile import ZopeTwoPageTemplateFile

from atreal.richfile.preview import RichFilePreviewMessageFactory as _
from atreal.richfile.preview.interfaces import IPreviewable
from plone.app.controlpanel.form import ControlPanelForm
from atreal.richfile.qualifier.common import RFControlPanel


class IRichFilePreviewSchema(Interface):
    """ """
    
    rf_preview_collapsed = Bool(
        title=_(u"label_rf_preview_collapsed",
                default=u"Display collapsed ?"),
        description=_(u"help_rf_preview_collapsed",
                      default=u"Do you want the plugin's display to be collapsed ?"
                     ),
        default=False)

    
class RichFilePreviewControlPanelAdapter(SchemaAdapterBase):
    adapts(IPloneSiteRoot)
    implements(IRichFilePreviewSchema)

    rf_preview_collapsed = ProxyFieldProperty(IRichFilePreviewSchema['rf_preview_collapsed'])


    
class RichFilePreviewControlPanel(RFControlPanel):
    template = ZopeTwoPageTemplateFile('controlpanel.pt')
    form_fields = form.FormFields(IRichFilePreviewSchema)
    label = _("RichFilePreview settings")
    description = _("RichFilePreview settings for this site.")
    form_name = _("RichFilePreview settings")
    plugin_iface = IPreviewable
    supported_ifaces = ('atreal.richfile.preview.interfaces.IPreview',)
    
