from zope.interface import implements

from kss.core import kssaction
from atreal.richfile.preview.interfaces import IPreviewable

from atreal.richfile.qualifier.common import RFView, RFTraverse
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

    @kssaction
    def loadPreview(self, iframeLoaded):
        """ User-called, to refresh the viewlet """
        if iframeLoaded == 'loaded':
            return
        ksscore = self.getCommandSet('core')
        # selector = ksscore.getCssSelector("#previewBody iframe")
        ksscore.setAttribute(ksscore.getCssSelector("#previewBody iframe"), 
            'src', 
            "%s/rfpreview" % self.context.absolute_url()
        )
        ksscore.addClass(ksscore.getCssSelector("#preview"),
            "kssattr-iframeLoaded-loaded"
        )
        ksscore.removeClass(ksscore.getCssSelector("#preview"), 
            "kssattr-iframeLoaded-unloaded"
        )


class RFPreviewTraverse(RFTraverse):
    
    plugin_interface = IPreviewable
