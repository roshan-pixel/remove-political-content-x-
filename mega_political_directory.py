"""
Mega Political & News Account Directory for India.
Comprehensive curated registry of Indian political parties, state wings, politicians,
ministers, news channels, digital portals, and political commentators.
"""

# Categorized seed handles to power large-scale purges (1000+ target capacity)
MEGA_POLITICAL_SEEDS = [
    # --- BJP Core & Central Leadership ---
    "BJP4India", "narendramodi", "AmitShah", "JPNadda", "RajnathSingh", "nitin_gadkari",
    "myogiadityanath", "myogioffice", "Dev_Fadnavis", "himantabiswa", "DrSJaishankar",
    "PiyushGoyal", "smritiirani", "ianuragthakur", "KirenRijiju", "blsanthosh",
    "amitmalviya", "sambitswaraj", "SudhanshuTrived", "Shehzad_Ind", "Tejasvi_Surya",
    "BJYM", "sunilbansalbjp", "dpradhanbjp", "AshwiniVaishnaw", "mansukhmandviya",
    "girirajsinghbjp", "byadavbjp", "gssjodhpur", "HardeepSPuri", "gkishanreddy",
    "sarbanandsonwal", "nstomar", "PrahladJoshi", "ShripadYNaik", "fskulaste",
    "ramdasathawale", "AnupriyaSPatel", "Gen_VKSingh", "DrJitendraSingh", "SomParkashBJP",
    "Rao_InderjitS", "SPSinghBaghelpr", "KapilPatil_", "DrSubhasSarkar", "BhagwatKarad",
    "DrRanjanRajkhe1", "PratimaBhoumik", "DrShashiTharoor", "me_meenakshi", "Annapurna4BJP",
    "A_Narayanaswamy", "AjaybhattBJP4UK", "BLVermaRBS", "AjayMishraINI", "NisithPramanik",

    # --- BJP State Chapters (All 28 States & 8 UTs) ---
    "BJP4Delhi", "BJP4UP", "BJP4Maharashtra", "BJP4Gujarat", "BJP4Karnataka",
    "BJP4Bengal", "BJP4Rajasthan", "BJP4MP", "BJP4Bihar", "BJP4Punjab",
    "BJP4Haryana", "BJP4Telangana", "BJP4Andhra", "BJP4Assam", "BJP4Odisha",
    "BJP4Jharkhand", "BJP4CG", "BJP4TamilNadu", "BJP4Kerala", "BJP4Goa",
    "BJP4Tripura", "BJP4Himachal", "BJP4Uttarakhand", "BJP4JnK", "BJP4Manipur",
    "BJP4Meghalaya", "BJP4Nagaland", "BJP4Sikkim", "BJP4Mizoram", "BJP4Arunachal",
    "BJP4Puducherry", "BJP4Chandigarh", "BJP4Ladakh", "BJP4Lakshadweep", "BJP4AnN",
    "BJP4DadraNagar", "BJP4DamanDiu", "BJP4Mumbai", "BJP4Kolkata", "BJP4Bangalore",
    "BJP4Hyderabad", "BJP4Chennai", "BJP4Pune", "BJP4Lucknow", "BJP4Varanasi",
    "BJP4Ayodhya", "BJP4Gorakhpur", "BJP4Noida", "BJP4Ghaziabad", "BJP4Meerut",

    # --- BJP State Ministers, Deputy CMs & State Office Bearers ---
    "brajeshpathakup", "kpmaurya1", "Satishmahanaup", "aksharmaBharat", "swatantrabjp",
    "Bhupendraupbjp", "dharam_pal_bjp", "sureshkkhanna", "babyranimourya", "laxmikantbjp",
    "drdineshbjp", "Chaudharybjp", "KapilDevBjp", "dayashankarup", "ravindrajaisbjp",
    "Anupvalmikibjp", "jpsrathorebjp", "NitinAgarwal_UP", "AsimArunUP", "sandipsinghbjp",
    "sanjaynishad_up", "om_rajbhar", "dr_maheshsharma", "drsanjeevbalyan", "manojtiwariMP",
    "RaviKishanOffl", "DineshLalYadav", "harsimratbadal_", "PemaKhanduBJP", "biren_singhbjp",
    "DrPramodPSawant", "DrMohanYadav51", "vishnudsofficial", "Bhupendrapbjp", "NayabSainiBJP",
    "PushkarDhami", "manoharparrikar", "ChouhanShivraj", "VasundharaBJP", "RamanSinghbjp",

    # --- Congress (INC) Core Leadership ---
    "INCIndia", "RahulGandhi", "priyankagandhi", "kharge", "kcvenugopalmp",
    "Jairam_Ramesh", "Pawankhera", "SupriyaShrinate", "shashitharoor", "siddaramaiah",
    "DKShivakumar", "SachinPilot", "rssurjewala", "digvijaya_28", "Chidambaram_IN",
    "BhupeshBaghel", "ashokgehlot51", "IYC", "NSUI", "srinivasiyc", "VarunChoudhry22",
    "AICCMedia", "INCSandesh", "bharatjodo", "KhabriINC", "INCSCDept", "INCMinority",
    "sevadal", "MahilaCongress", "AICC_OBC", "Kisan_Congress", "ProfCong",

    # --- Congress State Chapters & Leaders ---
    "INCDelhi", "INCUttarPradesh", "INCKarnataka", "INCMaharashtra", "INCGujarat",
    "INCRajasthan", "INCMP", "INCBihar", "INCPunjab", "INCHaryana", "INCTelangana",
    "INCAndhraPradesh", "INCAssam", "INCOdisha", "INCJharkhand", "INCCG", "INCKerala",
    "INCGoa", "INCTripura", "INCHimachal", "INCUttarakhand", "INCJammuKashmir",
    "INCManipur", "INCMeghalaya", "INCNagaland", "INCSikkim", "INCMizoram",
    "INCArunachal", "INCPuducherry", "INCChandigarh", "shaktisinhgohil", "GovindDotasra",
    "JituPatwari", "AjayRallanbjp", "AjayRai_INC", "DKS_Official", "MBPatil",
    "GParameshwara", "PawanKhera", "drajoykumar", "AlkaLamba", "RaghuSharmaINC",
    "manickamtagore", "Deepak_Babaria", "avinashpandeinc", "MohanMarkamINC", "bhupinder_hooda",

    # --- Aam Aadmi Party (AAP) ---
    "AamAadmiParty", "ArvindKejriwal", "msisodia", "raghav_chadha", "SanjayAzadSln",
    "AtishiAAP", "Saurabh_MLAgk", "BhagwantMann", "AAPDelhi", "AAPPunjab",
    "AAPGujarat", "AAPGoa", "AAPHaryana", "AAPHimachal", "AAMumbai", "AamAadmiUP",
    "SomnathBharti", "AmanatullahAAP", "dilipkpandey", "drashokktanwar", "HarjotBains_AAP",
    "Meet_Hayer", "CheemaAap", "AmanArora_AAP", "BalbirSinghAAP", "LaljitBhullarAAP",

    # --- Samajwadi Party (SP) & Allies ---
    "SamajwadiParty", "yadavakhilesh", "dimpleyadav", "shivpalsinghyad", "MediaCellSP",
    "samajwadipartyup", "yuvajan_sabha", "samajwadichhatrasabha", "samajwadilohia",
    "ramgopalyadav", "STHasanSP", "IqbalMahmoodSP", "AbuAsimAzmi", "ManojPandeySP",
    "AzadSamajParty", "BhimArmyChief", "Ch_ZiaurRahman", "AwadheshPrasadSP",

    # --- Trinamool Congress (TMC) ---
    "AITCofficial", "MamataOfficial", "abhishekaitc", "derekobrienmp", "MahuaMoitra",
    "AITCBengal", "AITCGod", "AITCTripura", "AITCAssam", "DrKakoliGBst", "SougataRoyMP",
    "KalyanBanerjee", "dolasen7", "sayani06", "mimichakraborty", "nusratchirps",
    "JawharSircar", "shantanu_sen", "DrSantanuSen", "BabulSupriyo", "FirhadHakim",

    # --- Other Regional Parties (DMK, AIADMK, Shiv Sena, NCP, RJD, JDU, BSP, Left) ---
    "arivalayam", "mkstalin", "Udhaystalin", "KanimozhiDMK", "TRBRajaa", "Dayanidhi_Maran",
    "AIADMKOfficial", "EPSTamilNadu", "OfficeOfOPS", "drkdhanapal", "cvshanmugam",
    "ShivSenaUBT_", "OfficeofUT", "AUThackeray", "rautsanjay61", "Priyanka_Chatur",
    "mieknathshinde", "Shivsenaofc", "Dev_Fadnavis", "ChhaganCBhujbal",
    "NCPspeaks", "PawarSpeaks", "Supriya_Sule", "AjitPawarSpeaks", "Praful_Patel",
    "RJDforIndia", "yadavtejashwi", "laluprasadrjd", "MisaBharti", "ManojKJhaRJD",
    "Jduonline", "NitishKumar", "LalanSingh_1", "SanjayJhaINC",
    "BspUp2022", "Mayawati", "AkashAnandBSP", "SatishChandraMisra",
    "cpimspeak", "SitaramYechury", "ComradeDRaja", "bengar_cpi", "pinarayivijayan",
    "asadowaisi", "aimim_national", "AkbarOwaisi_IN", "Imtiaz_Jaleel",
    "JMMparty", "HemantSorenJMM", "KalpanaSorenJMM", "BJD_Odisha", "Naveen_Odisha",
    "BRSparty", "KTRBRS", "trsharish", "KavithaKalvakuntla", "ysjagan", "YSRCParty",

    # --- Aaj Tak & India Today Media Network ---
    "aajtak", "AajTakHD", "lallantop", "mumbaitak", "UPTakOfficial", "Bihartakchannel",
    "MPTakOfficial", "DilliTak", "GujaratTak", "SportsTak_tr", "KisanTak", "CrimeTak_",
    "LifeTak", "IndiaToday", "IndiaTodayFLASH", "rahulkanwal", "anjanaomkashyap",
    "chitraaum", "SwetaSinghAT", "vikasbha", "shailendrasmohi", "GauravCSawant",
    "ShivAroor", "PreetiChoudhry", "PoojaShali", "Akshita_N", "SnehaMordani",

    # --- ABP News Network ---
    "ABPNews", "ABPNewsLive", "AbpGanga", "ABPAnanda", "abpmajhatv", "abpasmitatv",
    "abpsanjha", "abpdesam", "abpnadu", "ABP_Asam", "RubikaLiyaquat", "awasthis",
    "romanaisarkhan", "ShekhawatGajend", "pratimamishra1", "AdarshJhaNews",

    # --- Zee Media Network ---
    "ZeeNews", "ZeeNewsHindi", "ZEEUPUK", "ZeeMPCG", "ZeeRajasthan_", "ZeeBiharNews",
    "ZeeDNHNews", "ZeeDelhiNCR", "Zeephh", "Zee24Ghanta", "Zee24TaasNews", "ZeeNewsEnglish",
    "WIONews", "sudhirchaudhary", "dna", "AnanyaAwasthi_", "rameshsharmazee", "ZeeSalaam",

    # --- Network18 / News18 Network ---
    "News18India", "CNNnews18", "News18UP", "News18Bihar", "News18MP", "News18Rajasthan",
    "News18Punjab", "News18Lokmat", "News18Bengali", "News18Kannada", "News18Telugu",
    "News18Tamil", "News18Kerala", "News18Assam", "news18dotcom", "Firstpost",
    "AMISHDEVGAN", "Zakka_Jacob", "maryashakil", "PrateekTNews", "Anand_Narsimhan",

    # --- Times Network ---
    "TimesNow", "TimesNowNavbharat", "MirrorNow", "ETNOWlive", "NavbharatTimes",
    "MaharashtraTime", "Ei_Samay", "Vijaykarnataka", "SushantBSinha", "PadmajaJoshi",
    "Ranjan_TimesNow", "NikunjGarg_", "navikakumar", "VineetJainTimes",

    # --- Republic Media Network ---
    "republic", "Republic_Bharat", "RepublicBangla", "RepublicKannada", "arnab522",
    "rhythmv", "ShawanSen", "AishwaryaKapoor", "PiyushRepublic", "NiranjanRepublic",

    # --- TV9 Media Network ---
    "TV9Bharatvarsh", "tv9gujarati", "tv9kannada", "TV9Telugu", "TV9Marathi",
    "TV9Bangla", "DChaurasia2312", "NishantChaturved", "ShamsTahirKhan", "SayeedAnsari_",

    # --- NDTV Network ---
    "ndtv", "ndtvindia", "ndtvmpcg", "NDTVRajasthan", "ndtvmarathi", "ravishndtv",
    "saurabhshukla_s", "umashankarsingh", "Nidhi", "maryashakil_ndtv", "GargiRawat",

    # --- Print, Digital & Independent News Portals ---
    "IndianExpress", "IEhindi", "the_hindu", "htTweets", "DainikBhaskar",
    "AmarUjalaNews", "JagranNews", "thewire_in", "thewirehindi", "TheQuint",
    "newslaundry", "nlhindi", "AltNews", "theprintindia", "Scroll_in",
    "MaktoobMedia", "Frontline_India", "CaravanMagazine", "Outlookindia", "TelegraphIn",
    "DeccanHerald", "DeccanChronicle", "freepressjournal", "Oneindia", "oneindiahindi",
    "SakalMediaGroup", "Lokmat", "DailyThanthi", "DinakaranNews", "Eenadu_News",
    "SakshiPost", "Mathrubhumi", "ManoramaOnline", "SudarshanNewsTV", "SureshChavhanke",
    "News24tvchannel", "manakgupta", "sakshijoshii", "abhisar_sharma", "AjitAnjum",
    "PunyaPrasun", "ppbajpai", "PrashantKishor", "kunalkamra88", "BarkhaDutt",
    "BDUTT", "rajdeepsardesai", "sagarikaghose", "svaradarajan", "mkvenu1",
    "khanumarfa", "rohini_sgh", "bainjal", "seemay", "free_thinker", "zoo_bear",
    "pbhushan1", "SafooraZargar", "AfreenFatima136", "SharjeelUsmani", "AamirAzizJmi",
    "khan_zafarul", "MariyaS87", "KanojiaPJ", "alishan_jafri", "IsmatAraa",
    "sharatpradhan21", "avadheshjpr", "hrishirajanand_", "khannaushad74", "ashvita_singh",
    "MaqboolMajid", "sugataraju", "s_banchariya", "mofussil_scribe", "Gautampratimgo1",
    "sranjan19", "hussainhaidry", "Jayati1609", "madhutrehan", "Openthemag",

    # --- Government PR, Ministries & Official Channels ---
    "PMOIndia", "rashtrapatibhvn", "HMOIndia", "MIB_India", "FinMinIndia", "RailMinIndia",
    "MoHFW_INDIA", "EduMinOfIndia", "mygovindia", "DRDO_India", "PIB_India", "PIBHindi",
    "PIBFactCheck", "DDNewslive", "DDNewsHindi", "Sansad_TV", "airnewsalerts", "AIRNewsHindi",
    "CMOfficeUP", "RajCMO", "CMOMaharashtra", "CMOGujarat", "CMOKarnataka", "CMOBengal",
    "CMO_Odisha", "CMOTamilNadu", "CMOKerala", "CMO_Assam", "CMOPunjab", "CMODelhi"
]
