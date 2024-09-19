#!/usr/bin/env python
# -*- coding: utf-8 -*-
# src/adapters/sitemap_repo.py

"""
Concrete repository for processing sitemap files.
"""

from .abstract_repo import AbstractRepository
import xml.etree.ElementTree as ET
from typing import List

class SitemapRepository(AbstractRepository):
    """Concrete repository for handling sitemap XML files."""

    def add(self, item):
        # Implementation for adding a sitemap URL (if needed)
        pass

    def get(self, identifier):
        # Implementation for getting a URL by its identifier (index)
        pass

    def get_urls(self) -> List[str]:
        """Parse the sitemap.xml and return a list of target URLs."""
        tree = ET.parse(self.sitemap_path)
        root = tree.getroot()
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
        return [url.text for url in root.findall('ns:url/ns:loc', namespace)]
