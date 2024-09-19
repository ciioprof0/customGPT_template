#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Concrete repository for fetching YouTube video transcripts.
"""

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, VideoUnavailable
from .abstract_repo import AbstractRepository

class YouTubeRepository(AbstractRepository):
    """
    Concrete repository for fetching YouTube video transcripts.
    """

    def add(self, item):
        """Add an item to the repository (Not needed for YouTube)."""
        pass

    def get(self, video_url: str) -> str:
        """
        Get the transcript of a YouTube video by its URL.

        Args:
            video_url (str): The URL of the YouTube video.

        Returns:
            str: The transcript of the video.
        """
        video_id = self._extract_video_id(video_url)
        transcript = self.fetch_transcript(video_id)
        return transcript

    def fetch_transcript(self, video_id: str) -> str:
        """
        Fetch the transcript of a YouTube video using the video ID.

        Args:
            video_id (str): The video ID of the YouTube video.

        Returns:
            str: The transcript text.

        Raises:
            TranscriptsDisabled: If transcripts are disabled for the video.
            VideoUnavailable: If the video is unavailable.
        """
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            transcript_text = "\n".join([item['text'] for item in transcript])
            return transcript_text
        except (TranscriptsDisabled, VideoUnavailable) as e:
            raise RuntimeError(f"Unable to fetch transcript: {str(e)}")

    def _extract_video_id(self, video_url: str) -> str:
        """
        Extract the video ID from a YouTube URL.

        Args:
            video_url (str): The URL of the YouTube video.

        Returns:
            str: The video ID.
        """
        if "v=" in video_url:
            return video_url.split("v=")[1].split("&")[0]
        elif "youtu.be" in video_url:
            return video_url.split("/")[-1]
        else:
            raise ValueError("Invalid YouTube URL format")
