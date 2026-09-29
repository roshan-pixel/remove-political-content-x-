"""
Configuration and Seed List definitions for X Political Content Remover.
"""

# Daemon connection settings
DAEMON_URL = "http://127.0.0.1:10086/command"
STATUS_URL = "http://127.0.0.1:10086/status"
SESSION_NAME = "clean-x-feed"
DEFAULT_TIMEOUT = 30

# Whitelist: NEVER block these tech / AI / developer accounts
PROTECTED_WHITELIST = {
    "karpathy", "gdb", "fchollet", "sama", "ylecun", "elonmusk", "huggingface",
    "OpenAI", "Google", "GoogleAI", "AnthropicAI", "github", "Bugcrowd",
    "hackthebox_eu", "thedawgyg", "stokfredrik", "InsiderPhD", "intigriti",
    "TCMSecurity", "Hacker0x01", "Uber_Comms", "cyberswag_voxel", "ChuanmingLiu",
    "hingeloss", "DrJimFan", "Tesla_AI", "adcock_brett", "akshay_pachaar",
    "axbom", "Techmeme", "KaulAyushman", "TheOndrakGuy", "deepseek_ai"
}

# Seed handles: Explicitly targeted entities, parties, state units, leaders, and news media
SEED_HANDLES = [
    # Explicitly requested news targets
    "IEhindi",
    "thewirehindi",
    "MaktoobMedia",
    "TheQuint",
    "thewire_in",
    
    # BJP & Core Leadership & Subordinate Wings
    "BJP4India",
    "narendramodi",
    "AmitShah",
    "JPNadda",
    "myogiadityanath",
    "BJYM",
    "BJP4Delhi",
    "BJP4UP",
    "BJP4Maharashtra",
    "BJP4Gujarat",
    "BJP4Karnataka",
    "BJP4Bengal",
    "BJP4Rajasthan",
    "BJP4MP",
    "amitmalviya",
    "sambitswaraj",
    "smritiirani",
    "PiyushGoyal",
    "RajnathSingh",
    "DrSJaishankar",
    "ianuragthakur",
    "nitin_gadkari",
    "Dev_Fadnavis",
    "himantabiswa",
    "blsanthosh",
    "sunilbansalbjp",
    
    # Congress & Core Leadership & Subordinate Wings
    "INCIndia",
    "RahulGandhi",
    "priyankagandhi",
    "kharge",
    "IYC",
    "NSUI",
    "INCDelhi",
    "INCUttarPradesh",
    "INCKarnataka",
    "INCMaharashtra",
    "INCGujarat",
    "INCRajasthan",
    "INCMP",
    "INCBengal",
    "SupriyaShrinate",
    "Pawankhera",
    "Jairam_Ramesh",
    "shashitharoor",
    "kcvenugopalmp",
    "siddaramaiah",
    "DKShivakumar",
    "SachinPilot",
    "rssurjewala",
    "digvijaya_28",
    "Chidambaram_IN",
    
    # Official / Governmental & Regional Political Entities
    "PMOIndia",
    "rashtrapatibhvn",
    "AamAadmiParty",
    "ArvindKejriwal",
    "msisodia",
    "raghav_chadha",
    "SamajwadiParty",
    "yadavakhilesh",
    "AITCofficial",
    "MamataOfficial",
    "ShivSenaUBT_",
    "OfficeofUT",
    "NCPspeaks",
    "PawarSpeaks",
    "RJDforIndia",
    "yadavtejashwi",
    
    # Mainstream Indian News Outlets & Portals
    "IndianExpress",
    "aajtak",
    "ABPNews",
    "ZeeNews",
    "IndiaToday",
    "ndtv",
    "ndtvindia",
    "News18India",
    "TimesNow",
    "Republic_Bharat",
    "republic",
    "DDNewslive",
    "ANI",
    "PTI_News",
    "BBCHindi",
    "NavbharatTimes",
    "DainikBhaskar",
    "AmarUjalaNews",
    "JagranNews",
    "the_hindu",
    "htTweets",
    "News24tvchannel",
    "TV9Bharatvarsh",
    "ZeeNewsHindi"
]
