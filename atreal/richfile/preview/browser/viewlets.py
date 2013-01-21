from plone.app.layout.viewlets import ViewletBase
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from atreal.richfile.qualifier.browser.viewlets import RichfileViewlet
from atreal.richfile.preview.interfaces import IPreview
from atreal.richfile.preview.interfaces import IPreviewable
from atreal.richfile.preview.browser.controlpanel import IRichFilePreviewSchema
from atreal.richfile.preview import RichFilePreviewMessageFactory as _

class PreviewViewlet(RichfileViewlet):
    
    marker_interface = IPreview
    plugin_interface = IPreviewable
    plugin_id = 'preview'
    plugin_title = 'Preview'
    controlpanel_interface = IRichFilePreviewSchema
    
        
    index = ViewPageTemplateFile("viewlet.pt")

    def getPreview(self):
        """
        """
        data, mime = IPreviewable(self.context).getSubObject('preview.html')
        return data.decode('utf-8')

    def previewLoadable(self):
        """ Shall we load the preview whe loading the page ? """
        config = self._getConfig()
        if not config:
            return True 
        collapsed = self.collapsed()
        # if we set collapsed to False in the conf, we always load the preview
        if not collapsed:
            return True
        if collapsed and config.rf_load_preview_collapsed:
            return True         

        