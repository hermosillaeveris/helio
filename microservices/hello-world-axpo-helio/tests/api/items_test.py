# -*- coding: utf-8 -*-

from hello_world_axpo_helio.api.items import search


def test_search_items():
    """Search items
    """
    assert len(search()) == 2 
