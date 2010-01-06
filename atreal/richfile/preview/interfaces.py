from zope.interface import Interface

class IRichFilePreviewLayer(Interface):
    """ Marker interface that defines a Zope 3 browser layer.
    """

class IRichFilePreviewSite(Interface):
    """ Marker interface for sites with this product installed.
    """ 

class IPreview(Interface):
    """
    """
    
class IPreviewable(Interface):
    """
    """
