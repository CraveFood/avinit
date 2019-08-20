
======
avinit
======

Generate avatars using name initials

Avinit gets the first letter of the first and last word of a given text and generates a SVG avatar from it. Avinit it's also capable to generate a data link so the avatar can be sent directly in the URL.

Inspired on: http://judelicio.us/initial.js/


Installation
============

.. code-block::

  pip install avinit


If you need PNG support you will also need to install `CairoSVG`.
This can be accomplished by:

.. code-block::

  pip install avinit[png]


Usage
=====

.. code-block:: python

  In [1]: import avinit

  In [2]: avinit.get_svg_avatar('seocam')
  Out[2]: '<svg xmlns="http://www.w3.org/2000/svg" pointer-events="none" width="46" height="46" style="background-color: #3498db; -moz-border-radius: 0px; width: 46px; height: 46px; border-radius: 0px"> <text text-anchor="middle" y="50%" x="50%" dy="0.35em" pointer-events="auto" fill="#ffffff" font-family="HelveticaNeue-Light,Helvetica Neue Light,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif" style="font-weight: 400; font-size: 20px">S</text> </svg>'

  In [3]: avinit.get_svg_avatar('Sergio Oliveira')
  Out[3]: '<svg xmlns="http://www.w3.org/2000/svg" pointer-events="none" width="46" height="46" style="background-color: #d870ad; -moz-border-radius: 0px; width: 46px; height: 46px; border-radius: 0px"> <text text-anchor="middle" y="50%" x="50%" dy="0.35em" pointer-events="auto" fill="#ffffff" font-family="HelveticaNeue-Light,Helvetica Neue Light,Helvetica Neue,Helvetica,Arial,Lucida Grande,sans-serif" style="font-weight: 400; font-size: 20px">SO</text> </svg>'

  In [4]: avinit.get_avatar_data_url('seocam')
  Out[4]: b'data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHBvaW50ZXItZXZlbnRzPSJub25lIiB3aWR0aD0iNDYiIGhlaWdodD0iNDYiIHN0eWxlPSJiYWNrZ3JvdW5kLWNvbG9yOiAjMzQ5OGRiOyAtbW96LWJvcmRlci1yYWRpdXM6IDBweDsgd2lkdGg6IDQ2cHg7IGhlaWdodDogNDZweDsgYm9yZGVyLXJhZGl1czogMHB4Ij4gPHRleHQgdGV4dC1hbmNob3I9Im1pZGRsZSIgeT0iNTAlIiB4PSI1MCUiIGR5PSIwLjM1ZW0iIHBvaW50ZXItZXZlbnRzPSJhdXRvIiBmaWxsPSIjZmZmZmZmIiBmb250LWZhbWlseT0iSGVsdmV0aWNhTmV1ZS1MaWdodCxIZWx2ZXRpY2EgTmV1ZSBMaWdodCxIZWx2ZXRpY2EgTmV1ZSxIZWx2ZXRpY2EsQXJpYWwsTHVjaWRhIEdyYW5kZSxzYW5zLXNlcmlmIiBzdHlsZT0iZm9udC13ZWlnaHQ6IDQwMDsgZm9udC1zaXplOiAyMHB4Ij5TPC90ZXh0PiA8L3N2Zz4='


To choose the avatar colors you can send a list with the hex color codes:

.. code-block:: python

  colors = ['#000', '#111', '#222']
  avinit.get_svg_avatar('Hello Word', colors=colors)


There is also support to generate PNG avatars (if installed with support):

.. code-block:: python

  avinit.get_png_avatar('Hello Word', output_file='/tmp/test.png')


If you need to add radius to your avatars you can use the radius parameter:

.. code-block:: python

  avinit.get_svg_avatar('Hello Word', radius=15)
