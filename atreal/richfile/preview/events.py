from zope.interface.interfaces import IInterface
from zope.component import queryUtility

from atreal.richfile.preview.interfaces import IPreview, IPreviewable


def is_richfilepreview_installed():
    """
    """
    return queryUtility(IInterface, name=u'atreal.richfile.preview.IRichFilePreviewSite', default=False)


def buildAndStorePreview(obj, event):
    """
    """
    if not is_richfilepreview_installed():
        return
    print "atreal.richfile.preview: build and store preview for %s" % ('/'.join(obj.getPhysicalPath()),)
    IPreviewable(obj).process()


def cleanPreviewData(obj, event):
    """
    """
    if not is_richfilepreview_installed():
        return
    print "atreal.richfile.preview: clean data for %s" % ('/'.join(obj.getPhysicalPath()),)
    IPreviewable(obj).cleanUp()
