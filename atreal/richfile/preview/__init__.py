from zope.i18nmessageid import MessageFactory
RichFilePreviewMessageFactory = MessageFactory('atreal.richfile.preview')

from atreal.richfile.preview.interfaces import IPreview

def initialize(context):
    """Initializer called when used as a Zope 2 product."""
    try:
        from atreal.richfile.qualifier.registry import registerRFPlugin
    except:
        return
    
    supported_mimetypes = [
        "application/pdf",
        "application/msword",
        "application/msexcel",
        "application/vnd.ms-excel",
        "application/vnd.ms-powerpoint",
        "application/vnd.oasis.opendocument.text",
        "application/vnd.oasis.opendocument.text-master",
        "application/vnd.oasis.opendocument.text-template",
        "application/vnd.oasis.opendocument.text-web",
        "application/vnd.oasis.opendocument.spreadsheet",
        "application/vnd.oasis.opendocument.spreadsheet-template",
        "application/vnd.oasis.opendocument.presentation",
        "application/vnd.oasis.opendocument.presentation-template",
        "application/vnd.oasis.opendocument.chart",
        "application/vnd.oasis.opendocument.database",
        "application/vnd.sun.xml.writer",
        "application/vnd.sun.xml.impress",
        "application/vnd.sun.xml.calc",
        ]
    
    registerRFPlugin(IPreview, supported_mimetypes)