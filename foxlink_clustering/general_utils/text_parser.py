# -*- coding: utf-8 -*-

from bs4 import Comment

# Verify if an element is not under an invisible tag or a comment
def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

