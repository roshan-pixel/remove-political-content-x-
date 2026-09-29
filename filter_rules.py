"""
Political and News Content Classification Rules.
Provides fast heuristic filtering to distinguish political/news entities from tech/creator accounts.
"""

import re
from typing import Set
from config import PROTECTED_WHITELIST

POLITICAL_REGEX = re.compile(
    r'(bjp|inc|congress|minister|mantri|neta|pmo|president|sansad|mp|mla|sabha|party|dal|'
    r'sena|morcha|news|samachar|patrika|express|times|media|tv|today|live|pradesh|'
    r'iyc|bjym|nsui|sevadal|spokesperson|chief\s*minister|cm|governor|raj\s*bhavan|parishad|'
    r'aajtak|abp|ndtv|ani|pti|republic|zeenews|navbharat|bhaskar|amarujala|jagran|'
    r'politics|political|journalist|editor|anchor|reporter|columnist|cmo|cmoffice|'
    r'shashan|sarkar|yojana|vibhag|police|commissioner|secretariat|railway|adhikari)',
    re.IGNORECASE
)

# Financial markets, indices, and banking exemptions (NEVER flag as political)
FINANCIAL_MARKET_REGEX = re.compile(
    r'(bse|nse|sensex|nifty|stock|equity|exchange|indices|trading|invest|mutual\s*fund|rbi|sebi)',
    re.IGNORECASE
)

class ContentFilter:
    def __init__(self, whitelist: Set[str] = PROTECTED_WHITELIST):
        self.whitelist = {w.lower() for w in whitelist}

    def is_protected(self, handle: str) -> bool:
        """
        Returns True if the handle belongs to the protected tech, creator, or financial market whitelist.
        """
        clean = handle.lstrip("@").strip().lower()
        return clean in self.whitelist

    def is_political_or_news(self, handle: str, bio_or_name: str = "") -> bool:
        """
        Evaluates whether an account matches political or news media heuristics,
        strictly excluding financial markets, indices, and banking institutions.
        """
        clean = handle.lstrip("@").strip()
        if self.is_protected(clean):
            return False

        # If it's a financial market, stock exchange, or banking account -> Protect it
        if FINANCIAL_MARKET_REGEX.search(clean) or FINANCIAL_MARKET_REGEX.search(bio_or_name):
            return False

        # Check handle name directly for political / news keywords
        if POLITICAL_REGEX.search(clean):
            return True

        # Check display name and bio text
        if bio_or_name and POLITICAL_REGEX.search(bio_or_name):
            return True

        return False
