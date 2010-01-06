from zope.interface import implements

from atreal.richfile.preview.interfaces import IPreviewable
from atreal.richfile.qualifier.common import RFPlugin

import re
from Products.CMFCore.utils import getToolByName

class ToPreviewableObject(RFPlugin):
    """
    """
    implements(IPreviewable)


    _re_imgsrc = re.compile('<[iI][mM][gG]([^>]*) [sS][rR][cC]="([^">]*)"([^>]*)>')
    
    class _replacer(object):
        
        def __init__(self, sublist, instance):
            self.sublist = sublist
            self.instance = instance
        
        def __call__(self, match):
            prefix = match.group(1)
            inside = match.group(2)
            postfix = match.group(3)
            # patch inside
            if inside.startswith('./'):
                # some .swt are converted with this prefix
                inside = inside[2:]
            if inside in self.sublist:
                # convert elems that are known images 
                inside = '%s/rfpreview/%s' % (self.instance.getId(), inside)
            result = '<img%s src="%s"%s>' % (prefix, inside, postfix)
            return result

    def process(self):
        """ 
        """
        transforms = getToolByName(self.context, 'portal_transforms')
        file = self.context.getPrimaryField().getAccessor(self.context)()
        if isinstance(file.data, str):
            data = file.data
        else:
            data = file.data.open().read()
        data = transforms.convertTo('text/html', data, filename=file.filename)
        
        if data is None:
            self.setSubObject ('preview.html', "")
            return
        
        #get the html code
        html_converted = data.getData()
        #update internal links
        #remove bad character '\xef\x81\xac' from HTMLPreview
        html_converted = re.sub('\xef\x81\xac', "", html_converted)
        
        # patch image sources since html base is that of our parent
        subobjs = data.getSubObjects()
        if len(subobjs)>0:
            for id, data in subobjs.items():
                self.setSubObject(id, data)
            html_converted = self._re_imgsrc.sub(self._replacer(subobjs.keys(), self.context), html_converted)
        
        #store the html in the HTMLPreview field for preview
        self.setSubObject ('preview.html', html_converted)
