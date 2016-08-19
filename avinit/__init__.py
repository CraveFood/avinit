#!/usr/bin/env python

import re

from base64 import b64encode


DEFAULT_FONTS = [
    'HelveticaNeue-Light',
    'Helvetica Neue Light',
    'Helvetica Neue',
    'Helvetica',
    'Arial',
    'Lucida Grande',
    'sans-serif',
]

DEFAULT_SETTINGS = {
    'width': '46',
    'height': '46',
    'radius': '0',
    'font-family': ','.join(DEFAULT_FONTS),
    'font-size': '20',
    'font-weight': '400',
}

SVG_TEMPLATE = """
<svg xmlns="http://www.w3.org/2000/svg" pointer-events="none" width="{width}"
     height="{height}" style="{style}">
  <text text-anchor="middle" y="50%" x="50%" dy="0.35em"
        pointer-events="auto" fill="#ffffff" font-family="{font-family}"
        style="{text-style}">{text}</text>
</svg>
""".strip()
SVG_TEMPLATE = re.sub('(\s+|\n)', ' ', SVG_TEMPLATE)


COLORS = ["#1abc9c", "#16a085", "#f1c40f", "#f39c12", "#2ecc71", "#27ae60",
          "#e67e22", "#d35400", "#3498db", "#2980b9", "#e74c3c", "#c0392b",
          "#9b59b6", "#8e44ad", "#bdc3c7", "#34495e", "#2c3e50", "#95a5a6",
          "#7f8c8d", "#ec87bf", "#d870ad", "#f69785", "#9ba37e", "#b49255",
          "#b49255", "#a94136"]


def _from_dict_to_style(style_dict):
    return '; '.join(['{}: {}'.format(k, v) for k, v in style_dict.items()])


def _get_color(text):
    color_index = sum(map(ord, text)) % len(COLORS)
    return COLORS[color_index]


def get_svg_avatar(text, **kwargs):

    initials = '=)'
    if text:
        split_text = text.split(' ')
        if len(split_text) > 1:
            initials = split_text[0][0] + split_text[-1][0]
        else:
            initials = split_text[0][0]

    opts = DEFAULT_SETTINGS.copy()
    opts.update(kwargs)

    style = {
        'background-color': _get_color(text),
        'width': opts.get('width') + 'px',
        'height': opts.get('height') + 'px',
        'border-radius': opts.get('radius') + 'px',
        '-moz-border-radius': opts.get('radius') + 'px',
    }

    text_style = {
        'font-weight': opts.get('font-weight'),
        'font-size': opts.get('font-size') + 'px',
    }

    return SVG_TEMPLATE.format(**{
        'height': opts.get('height'),
        'width': opts.get('width'),
        'style': _from_dict_to_style(style),
        'font-family': opts.get('font-family'),
        'text-style': _from_dict_to_style(text_style),
        'text': initials.upper(),
    }).replace('\n', '')


def get_avatar_data_url(text, **kwargs):
    svg_avatar = get_svg_avatar(text, **kwargs)
    b64_avatar = b64encode(svg_avatar.encode('utf-8'))
    return b'data:image/svg+xml;base64,' + b64_avatar
