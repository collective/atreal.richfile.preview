from zope.interface import implements

from atreal.richfile.preview.interfaces import IPreviewable

from atreal.richfile.qualifier.common import RFView
from atreal.richfile.qualifier.interfaces import IRFView
from atreal.richfile.preview import RichFilePreviewMessageFactory as _

class RFPreviewView(RFView):
    
    plugin_interface = IPreviewable
    kss_id = 'preview'
    viewlet_name = 'atreal.richfile.preview.viewlet'
    update_message = _('The preview has been updated.')
    active_message = _('Preview activated.')
    unactive_message = _('Preview un-activated.') 
    

    def getPreview(self):
        """
        """
        data, mime = IPreviewable(self.context).getSubObject('preview.html')
        return data.decode('utf-8')