.. contents::

Overview
========

Preview Support Plugin for RichFileQualifier 


Description
===========

This Plone Component is a plugin for atreal.richfile.qualifier_ system.

.. _atreal.richfile.qualifier: http://pypi.python.org/pypi/atreal.richfile.qualifier

``atreal.richfile.preview`` provides the ability to view the HTML preview of
a file in a viewlet. Mimetypes supported are: ::

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

This package requires Products.AROfficeTranforms_ and his dependencies.

.. _Products.AROfficeTranforms: http://pypi.python.org/pypi/Products.AROfficeTransforms


Authors
=======

|atreal|_

* `atReal Team`_

  - Jean-Nicolas Bes [drjnut]
  - Matthias Broquet [tiazma]
  - Florent Michon [f10w]

.. |atreal| image:: http://www.atreal.fr/medias/atreal-logo-48.png
.. _atreal: http://www.atreal.fr/
.. _atReal Team: mailto:contact@atreal.fr


Contributors
============

* 


Credits
=======

* Thanks to ARFilePreview

