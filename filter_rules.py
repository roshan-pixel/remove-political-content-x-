"""
Political and News Content Classification Rules.
Provides fast heuristic filtering to distinguish political/news entities from tech/creator accounts.
"""

import re
from typing import Set
from config import PROTECTED_WHITELIST

POLITICAL_REGEX = re.compile(
    r'(bjp|inc|congress|minister|mantri|neta|pmo|president|sansad|mp|mla|sabha|bharat|party|dal|'
    r'sena|morcha|news|samachar|patrika|express|times|india|media|tv|today|live|pradesh|delhi|'
    r'iyc|bjym|nsui|sevadal|spokesperson|chief\s*minister|cm|governor|raj\s*bhavan|parishad|'
    r'aajtak|abp|ndtv|ani|pti|republic|zeenews|navbharat|bhaskar|amarujala|jagran|'
    r'politics|political|journalist|editor|anchor|reporter|columnist|author|cmo|cmoffice|'
    r'shashan|sarkar|yojana|vibhag|police|commissioner|secretariat|railway|adhikari)',
    re.IGNORECASE
)

class ContentFilter:
    def __init__(self, whitelist: Set[str] = PROTECTED_WHITELIST):
        self.whitelist = {w.lower() for w in whitelist}

    def is_protected(self, handle: str) -> bool:
        """
        Returns True if the handle belongs to the protected tech/creator whitelist.
        """
        clean = handle.lstrip("@").strip().lower()
        return clean in self.whitelist

    def is_political_or_news(self, handle: str, bio_or_name: str = "") -> bool:
        """
        Evaluates whether an account matches political, government, or news media heuristics.
        """
        clean = handle.lstrip("@").strip()
        if self.is_protected(clean):
            return False

        # Check handle name directly
        if POLITICAL_REGEX.search(clean):
            return True

        # Check display name and bio text
        if bio_or_name and POLITICAL_REGEX.search(bio_or_name):
            return True

        return False
