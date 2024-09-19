#!/usr/bin/env python
# -*- coding: utf-8 -*-
# src/adapters/file_repo.py

"""
Abstract base repository for application files (e.g., PDFs, DOCX) and concrete implementations.
"""

from .abstract_repo import AbstractRepository
import abc

class AbstractFileRepository(AbstractRepository):
    """Abstract repository for file content."""

    @abc.abstractmethod
    def extract_text(self, file_path: str) -> str:
        """Extract text content from a file."""
        raise NotImplementedError

# Concrete Implementation for PDF files
class PDFRepository(AbstractFileRepository):
    """Concrete repository for handling PDF files."""

    def add(self, item):
        # Implementation for adding a PDF file (if needed)
        pass

    def get(self, identifier):
        # Implementation for getting a PDF file by its identifier
        pass

    def extract_text(self, file_path: str) -> str:
        # Implementation for extracting text from a PDF file
        import PyPDF2
        text = ""
        with open(file_path, 'rb') as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            for page in reader.pages:
                text += page.extract_text()
        return text

# Additional implementations can be added for other file types (e.g., DOCX).
