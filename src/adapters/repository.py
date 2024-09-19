#!/usr/bin/env python
# -*- coding: utf-8 -*-
# src/adapters/repository.py

"""
Abstract base repository defining methods that must be implemented by any repository class.
"""

import abc

class AbstractRepository(abc.ABC):
    """Abstract base class for a repository with basic operations."""

    @abc.abstractmethod
    def add(self, item):
        """Add an item to the repository."""
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, identifier):
        """Get an item from the repository by its identifier."""
        raise NotImplementedError

    # Additional abstract methods as needed for the repository lifecycle.