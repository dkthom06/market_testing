import os
import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

"""
The purpose of this program is to 
identify the stocks within the Russell 
2000 that have the greatest momentum.
It will then rank them and print out
the top 10.
"""
# downloaded stock list from: https://www.ishares.com/us/products/239710/ishares-russell-2000-etf

# How far back to collect data


momentum_span = 20
days_data = int(2.5*momentum_span)
np_momentumData = np.empty((0, 2))
print('np_momentumData shape: ' + str(np_momentumData.shape))
ticker_symbols = np.array([
    'ELF', 'ONTO', 'FIX', 'MSTR', 'SSD', 'LNW', 'PCVX', 'NXT', 'XTSLA', 'BRBR', 'APG', 'AIT', 'FN', 'WFRD', 'CYTK', 'UFPI', 'SPSC', 'ITCI', 'CHRD', 'HQY', 'RHP', 'MTDR', 'ENSG', 'SSB', 'CMC', 'SIGI', 'QLYS', 'RMBS', 'FLR', 'CHX', 'ANF', 'ATI', 'MUR', 'TENB', 'NOVT', 'MARA', 'AAON', 'OPCH', 'PR', 'GTLS', 'TMHC', 'MLI', 'BCC', 'BPMC', 'ATKR', 'ESNT', 'MTH', 'WTS', 'DUOL', 'VRNS', 'PBF', 'BECN', 'SFM', 'FTAI', 'ALKS', 'NSIT', 'TRNO', 'CWST', 'CIVI', 'MMS', 'ALTM', 'CVNA', 'ASO', 'SUM', 'EXLS', 'ALTR', 'IBP', 'NE', 'SPXC', 'STNE', 'ONB', 'FSS', 'COOP', 'BCPC', 'SIG', 'KRG', 'SM', 'HALO', 'WK', 'MTSI', 'ASGN', 'BMI', 'UBSI', 'ETRN', 'FELE', 'ZWS', 'CBT', 'MMSI', 'ABG', 'APPF', 'HOMB', 'SLAB', 'FCFS', 'GATX', 'HLNE', 'AEL', 'GKOS', 'BIPC', 'KBH', 'CADE', 'SKY', 'AMR', 'MOGA', 'PTEN', 'BBIO', 'RVMD', 'POR', 'GBCI', 'SYNA', 'HRI', 'FUL', 'CVLT', 'FFIN', 'POWI', 'MOD', 'NJR', 'TNET', 'INSM', 'PECO', 'AEO', 'COKE', 'MATX', 'ACA', 'ALIT', 'EXPO', 'KNF', 'KAI', 'HP', 'LNTH', 'FOLD', 'EPRT', 'AEIS', 'VAL', 'MGY', 'NEOG', 'HWC', 'ACLS', 'MDC', 'CRC', 'ENS', 'JXN', 'LANC', 'RDN', 'BCO', 'MAC', 'SWX', 'SHAK', 'OTTR', 'GPI', 'TEX', 'BOX', 'VLY', 'GMS', 'CBAY', 'RPD', 'HAE', 'HGV', 'UMBF', 'ORA', 'CSWI', 'WDFC', 'KTB', 'BDC', 'IRT', 'PCH', 'BKH', 'SWTX', 'AVNT', 'IRTC', 'ITRI', 'VKTX', 'APLE', 'PBH', 'LBRT', 'NPO', 'BXMT', 'GT', 'ESGR', 'MDGL', 'ALE', 'NSP', 'EVH', 'ARWR', 'WIRE', 'SANM', 'AMKR', 'ARCB', 'BHVN', 'CBZ', 'AXNX', 'MC', 'OGS', 'ACIW', 'SFBS', 'FRSH', 'ALRM', 'REZI', 'CCOI', 'TPH', 'HI', 'STNG', 'PIPR', 'DY', 'AXSM', 'ITGR', 'VC', 'JBT', 'BL', 'SHOO', 'DBRG', 'ADNT', 'AVAV', 'SMPL', 'CVCO', 'PGNY', 'MHO', 'CRS', 'FORM', 'SBRA', 'PNM', 'TDW', 'MGRC', 'ABCB', 'NARI', 'MQ', 'VRRM', 'KFY', 'RIOT', 'CNX', 'IOSP', 'ZD', 'ASB', 'PSN', 'IDCC', 'SR', 'SPT', 'CNO', 'DIOD', 'WD', 'NWE', 'BRZE', 'ACAD', 'BLKB', 'LCII', 'AX', 'WHD', 'SLG', 'NOG', 'HCC', 'BNL', 'CERE', 'TGNA', 'UCBI', 'AIN', 'SKT', 'HELE', 'DOOR', 'ARCH', 'VSH', 'FOXF', 'RUSHA', 'TMDX', 'GFF', 'TCBI', 'ICFI', 'IDYA', 'RRR', 'MTRN', 'OSCR', 'SXT', 'HUBG', 'IGT', 'SHLS', 'SEM', 'KWR', 'BTU', 'UEC', 'HASI', 'IPAR', 'AWR', 'KLIC', 'IBOC', 'SITC', 'EVTC', 'CDP', 'DOC', 'CWT', 'URBN', 'KOS', 'LIVN', 'ABM', 'BOOT', 'CLSK', 'GHC', 'BGC', 'APAM', 'FBP', 'FTDR', 'ESE', 'KTOS', 'AVA', 'WSFS', 'ROCK', 'LGIH', 'PLXS', 'UNF', 'SGRY', 'CATY', 'WERN', 'LXP', 'PAGS', 'ARVN', 'IIPR', 'CRDO', 'DOCN', 'PJT', 'MYRG', 'FL', 'YELP', 'RYTM', 'GH', 'STRL', 'OI', 'RXO', 'CNMD', 'MWA', 'CCS', 'CRNX', 'GNW', 'CSTM', 'KRYS', 'RELY', 'PATK', 'NTLA', 'QTWO', 'PRGS', 'FLYW', 'PDCO', 'PRFT', 'CEIX', 'LRN', 'RAMP', 'NMIH', 'PZZA', 'AROC', 'MTX', 'PI', 'PRMW', 'SKYW', 'BEAM', 'ENV', 'AMN', 'CALM', 'PRVA', 'SONO', 'ACLX', 'AI', 'PGTI', 'JBLU', 'FULT', 'VCEL', 'MGEE', 'AIR', 'TWST', 'RDNT', 'BLMN', 'CVBF', 'TBBK', 'NUVL', 'BOH', 'PFSI', 'CTRE', 'NHI', 'SHO', 'SFNC', 'AUB', 'PARR', 'CARG', 'PPBI', 'GVA', 'ARRY', 'MLKN', 'CPK', 'JJSF', 'OII', 'HL', 'PLUS', 'PLAY', 'CBU', 'ABR', 'STRA', 'COUR', 'TRN', 'ALG', 'FCPT', 'XRX', 'PD', 'OSIS', 'ENR', 'SDRL', 'FIBK', 'DORM', 'INDB', 'EBC', 'CRVL', 'INSW', 'VIAV', 'MODG', 'GLNG', 'IOVA', 'ARDX', 'AMPH', 'SBCF', 'FRME', 'PRIM', 'ROG', 'GOLF', 'VRNT', 'WGO', 'SCL', 'DNLI', 'BANF', 'PLAB', 'PRCT', 'AMBA', 'HNI', 'IRWD', 'UE', 'CPE', 'IMVT', 'TGH', 'SLVM', 'PSMT', 'CALX', 'FFBC', 'HURN', 'MIR', 'GSHD', 'TOWN', 'EAT', 'KMT', 'MBC', 'UCTT', 'STEP', 'DRH', 'CNS', 'UPST', 'SJW', 'EPC', 'FSLY', 'PRK', 'TGTX', 'OUT', 'SXI', 'WOR', 'BE', 'DK', 'PEB', 'CENTA', 'RCKT', 'ROAD', 'BKU', 'MYGN', 'TNC', 'BANC', 'PTCT', 'ATGE', 'PLMR', 'THS', 'SIX', 'RLJ', 'EQC', 'JOE', 'AVDX', 'SNEX', 'CNK', 'NEO', 'ACVA', 'CORT', 'ANDE', 'STR', 'ODP', 'CLDX', 'B', 'SITM', 'ENVA', 'VCYT', 'RXRX', 'NGVT', 'EPAC', 'DAN', 'UPBD', 'HEES', 'INMD', 'SDGR', 'VECO', 'AZZ', 'TALO', 'BATRK', 'IVT', 'HLMN', 'IONQ', 'WSBC', 'PRKS', 'JOBY', 'VSTO', 'TFIN', 'UPWK', 'AGM', 'TROX', 'LZB', 'CSGS', 'RNST', 'XPRO', 'ENVX', 'CAKE', 'LAUR', 'VRTS', 'SATS', 'JBGS', 'OPEN', 'BRP', 'CXW', 'VGR', 'JELD', 'IBTX', 'AMEH', 'THRM', 'WAFD', 'LKFN', 'ROIC', 'EYE', 'CWK', 'CMPR', 'TTMI', 'GNL', 'PRO', 'PTGX', 'YOU', 'DVAX', 'AKR', 'OFG', 'SQSP', 'KAR', 'TRMK', 'CBRL', 'AGYS', 'ARI', 'OMI', 'LUMN', 'DHT', 'DFIN', 'SFL', 'VERA', 'AMWD', 'RXST', 'STC', 'NBTB', 'ASAN', 'NTCT', 'JACK', 'EXTR', 'GEF', 'APPN', 'CUBI', 'WKC', 'EFSC', 'CODI', 'NVEE', 'RC', 'ATRC', 'HLIO', 'NTB', 'NMRK', 'SNDX', 'HLIT', 'STAA', 'COHU', 'KN', 'GPOR', 'MXL', 'HBI', 'MSGE', 'USPH', 'OXM', 'CNNE', 'DDS', 'BANR', 'GBX', 'JAMF', 'KYMR', 'PHR', 'CHCO', 'AGIO', 'SBH', 'GEO', 'ADUS', 'NSSC', 'XHR', 'KURA', 'PACB', 'NWBI', 'ATEC', 'DRS', 'HTH', 'ZETA', 'MGPI', 'BORR', 'MGNI', 'HLX', 'XNCR', 'HTLF', 'POWL', 'GRBK', 'CPRX', 'LESL', 'SUPN', 'TDS', 'PRG', 'FBNC', 'NAVI', 'BMBL', 'CTS', 'MCY', 'MORF', 'TNK', 'PWSC', 'FBK', 'SYBT', 'RKLB', 'DEI', 'UFPT', 'LOB', 'GOGL', 'LNN', 'UTZ', 'CXM', 'KROS', 'NWN', 'HWKN', 'ALEX', 'FCF', 'DNOW', 'HMN', 'ESRT', 'PCRX', 'KFRC', 'CASH', 'GIII', 'CHEF', 'ADEA', 'CAL', 'LTC', 'PAYO', 'GTY', 'JBI', 'OMCL', 'INBX', 'APOG', 'ALGT', 'SVC', 'OEC', 'PAR', 'LGND', 'SMTC', 'KAMN', 'ICHR', 'ELME', 'BUSE', 'XPEL', 'LZ', 'RYZB', 'ECPG', 'LADR', 'SAFT', 'HOPE', 'WLY', 'STEL', 'SCS', 'TWO', 'VRE', 'SAGE', 'SOVO', 'WRBY', 'OSW', 'UNIT', 'KW', 'HIMS', 'LMAT', 'WNC', 'CMCO', 'NNI', 'CARS', 'DO', 'BKE', 'UVV', 'LPG', 'NOVA', 'SG', 'INTA', 'BYON', 'GSAT', 'AVPT', 'PRTA', 'PMT', 'NHC', 'FIZZ', 'STBA', 'NTST', 'WABC', 'NBHC', 'BKD', 'EVBG', 'DEA', 'TCBK', 'IMKTA', 'PRDO', 'CVI', 'FLNC', 'SSTK', 'DNUT', 'MRTN', 'NWLI', 'ADMA', 'BCRX', 'ZUO', 'WINA', 'COLL', 'NX', 'INDI', 'MFA', 'AIV', 'XMTR', 'HRMY', 'PRAA', 'FDMT', 'SCHL', 'AAT', 'PFS', 'SAFE', 'CWH', 'BHE', 'VTLE', 'EIG', 'NIC', 'PEBO', 'AKRO', 'DGII', 'COMP', 'SPHR', 'PDFS', 'FBRT', 'SCSC', 'MGNX', 'RNA', 'ALKT', 'KALU', 'VICR', 'WMK', 'SASR', 'VCTR', 'TRS', 'CTKB', 'AMSF', 'UUUU', 'CHGG', 'GERN', 'DYN', 'KOP', 'FWRD', 'INFN', 'ALPN', 'MNRO', 'QCRH', 'BXC', 'CIM', 'WT', 'SGH', 'SP', 'MRC', 'GABC', 'HPP', 'ROVR', 'BFH', 'RYI', 'RLAY', 'MBUU', 'SABR', 'AUR', 'WS', 'MODN', 'BASE', 'VBTX', 'LGFB', 'UDMY', 'PLYM', 'ZIP', 'DAWN', 'UNFI', 'MMI', 'MSEX', 'AMPL', 'LC', 'CMTG', 'PRLB', 'PLRX', 'SAVA', 'TGI', 'MEG', 'MNKD', 'ACMR', 'OBK', 'AXL', 'HCSG', 'INVA', 'SHEN', 'TRUP', 'MDXG', 'NABL', 'SXC', 'ARR', 'EVRI', 'FA', 'QTRX', 'EFC', 'ATEN', 'MCRI', 'THR', 'LMND', 'ACT', 'LILAK', 'BRSP', 'HIBB', 'ECVT', 'JBSS', 'RCUS', 'ASPN', 'VSEC', 'SRCE', 'ERII', 'SPNS', 'MDRX', 'OCFC', 'PGRE', 'AVNS', 'DLX', 'TMST', 'SBSI', 'TRNS', 'SRRK', 'UMH', 'TARS', 'PAX', 'PRM', 'CDE', 'NAT', 'PDM', 'VIR', 'HAIN', 'SKWD', 'CSR', 'BHLB', 'SPNT', 'ARCT', 'BZH', 'LBAI', 'EXPI', 'ANIP', 'MATW', 'CRGY', 'BFC', 'FG', 'BRKL', 'ACCD', 'BJRI', 'EMBC', 'DCPH', 'IESC', 'FBMS', 'GRC', 'SMP', 'TTGT', 'SANA', 'QNST', 'SIBN', 'BLBD', 'CNOB', 'FDP', 'ASTE', 'AMLX', 'ATSG', 'LPRO', 'ACHR', 'FIGS', 'VRDN', 'SLCA', 'HLF', 'GDYN', 'AHH', 'ARLO', 'PUMP', 'CNXN', 'IAS', 'AUPH', 'RDFN', 'HY', 'HOV', 'ASIX', 'DOLE', 'DFH', 'CFFN', 'CABA', 'FLNG', 'NBR', 'PFC', 'MD', 'UTL', 'BELFB', 'CMP', 'SAH', 'CRAI', 'RGNX', 'HOUS', 'RAPT', 'BBSI', 'GPRE', 'TILE', 'EYPT', 'GDEN', 'ZNTL', 'RWT', 'ARQT', 'FMBH', 'MEI', 'AMRC', 'TWI', 'RGR', 'SPTN', 'NUS', 'COGT', 'APGE', 'EWTX', 'PUBM', 'VZIO', 'AORT', 'AMK', 'CHCT', 'AMBC', 'BSIG', 'GTN', 'GNK', 'KELYA', 'DDD', 'CTBI', 'MBIN', 'WWW', 'HAYN', 'BDN', 'SAVE', 'AHCO', 'AMRX', 'ETD', 'MIRM', 'HA', 'NXRT', 'GES', 'DHC', 'TMP', 'RVLV', 'DRQ', 'DIN', 'NYMT', 'INN', 'CRK', 'SILK', 'ZEUS', 'MYE', 'ETWO', 'LFST', 'DCOM', 'BGS', 'TMCI', 'NVTS', 'REX', 'EGBN', 'LAZR', 'VERV', 'RPAY', 'LQDA', 'MATV', 'DX', 'EB', 'CYRX', 'VVI', 'CLB', 'THRY', 'CCO', 'CASS', 'YEXT', 'EDIT', 'SLP', 'NVRI', 'HZO', 'IMXI', 'IMAX', 'MSFUT', 'CDRE', 'DCO', 'PCT', 'BLX', 'ASC', 'IIIN', 'HSTM', 'HCI', 'MBWM', 'VREX', 'UVSP', 'FATE', 'CFB', 'HDSN', 'IBRX', 'ZYME', 'BBUC', 'OSBC', 'RDUS', 'SWI', 'GOGO', 'CNDT', 'CRNC', 'EU', 'MTTR', 'ARKO', 'LASR', 'PTLO', 'MODV', 'PRA', 'VTOL', 'WTTR', 'CHUY', 'AMTB', 'ETNB', 'CSTL', 'OLO', 'FCEL', 'NNOX', 'KNSA', 'REVG', 'CBL', 'HBNC', 'RES', 'NVRO', 'FNA', 'KNTK', 'COCO', 'CCRN', 'BLFS', 'FCBC', 'WSR', 'CECO', 'YMAB', 'PTVE', 'SPCE', 'OCUL', 'SWBI', 'MSBI', 'GMRE', 'GLDD', 'KRUS', 'EVLV', 'PFBC', 'TVTX', 'BY', 'ACCO', 'FUBO', 'NRDS', 'HFWA', 'LGFA', 'IRON', 'LTH', 'FOR', 'PWP', 'SMMT', 'HSII', 'SNCY', 'CENX', 'BIGC', 'SBOW', 'NG', 'HCKT', 'AGX', 'HTLD', 'FMNB', 'GIC', 'ALHC', 'SCVL', 'USNA', 'CRBU', 'LWLG', 'STKL', 'EGLE', 'PLOW', 'CLW', 'BFST', 'HCAT', 'EOLS', 'CATC', 'STGW', 'VTS', 'DMRC', 'KREF', 'EQBK', 'TITN', 'WASH', 'HTBK', 'MED', 'LEU', 'IDT', 'UIS', 'UFCS', 'CLNE', 'UHT', 'VMEO', 'NRC', 'SOUN', 'TNGX', 'CEVA', 'CLBK', 'ZIMV', 'EWCZ', 'SBGI', 'WRLD', 'PKST', 'MITK', 'SMRT', 'URGN', 'HVT', 'LUNG', 'MLAB', 'ACEL', 'GOOD', 'AMRK', 'CRSR', 'GSBC', 'THFF', 'FLGT', 'CAC', 'CMRE', 'PETQ', 'AOSL', 'OABI', 'CLDT', 'MLNK', 'FWRG', 'BRY', 'CYH', 'SVV', 'TK', 'KE', 'MRNS', 'CVGW', 'EBF', 'ATRO', 'FPI', 'ADTN', 'USLM', 'AMNB', 'RICK', 'AVO', 'MCBS', 'TTI', 'IE', 'AEHR', 'TELL', 'RVNC', 'IBCP', 'DHIL', 'XPER', 'CCNE', 'OFIX', 'ATRI', 'ALX', 'MCB', 'OSUR', 'EHAB', 'SRI', 'RBCAA', 'AMAL', 'ATEX', 'MPLN', 'NR', 'CCB', 'TRST', 'PGC', 'DH', 'NRIX', 'PBI', 'ACRE', 'BATRA', 'IIIV', 'HONE', 'ATXS', 'EGY', 'CDMO', 'ALT', 'CGEM', 'MLR', 'YORW', 'VITL', 'DXPE', 'COMM', 'DENN', 'KIDS', 'MTW', 'UTI', 'NKLA', 'BFS', 'KALV', 'ALRS', 'ANAB', 'FC', 'INST', 'PNTG', 'RUSHB', 'ALLO', 'CWCO', 'MOV', 'PSFE', 'SVRA', 'AMPS', 'CVLG', 'BHB', 'STEM', 'TBPH', 'VVX', 'SGHC', 'RCEL', 'ADPT', 'HTBI', 'CSTR', 'ORIC', 'KRNY', 'NTGR', 'SMBC', 'AXGN', 'LAND', 'RGP', 'UVE', 'LXU', 'ALXO', 'FARO', 'NFBK', 'XERS', 'FFWM', 'MRSN', 'SRDX', 'MNTK', 'CPF', 'ORC', 'CDNA', 'WEAV', 'BYND', 'MVIS', 'CERS', 'TTEC', 'AMCX', 'VPG', 'FIP', 'CENT', 'HAFC', 'NEXT', 'LMB', 'DJCO', 'FFIC', 'MOFG', 'MXCT', 'OPK', 'STER', 'AVXL', 'TIPT', 'OSPN', 'CCBG', 'ALEC', 'OLMA', 'ATNI', 'SEMR', 'TWKS', 'DBI', 'METCV', 'NAPA', 'APLD', 'AROW', 'CLFD', 'SHYF', 'TPC', 'TBI', 'HLVX', 'PL', 'IVR', 'AVNW', 'RMR', 'NVAX', 'SMBK', 'NPK', 'TRTX', 'CTLP', 'RSI', 'LYTS', 'TREE', 'SHBI', 'FRPH', 'ELVN', 'NVEC', 'BHRB', 'LQDT', 'TPB', 'REPL', 'KGS', 'OIS', 'CCSI', 'ATMU', 'WULF', 'NBN', 'CTOS', 'MAX', 'SSP', 'BOC', 'CRMT', 'GNE', 'CTO', 'PX', 'GCMG', 'GCO', 'BV', 'BOOM', 'JRVR', 'AMSWA', 'BWMN', 'GDOT', 'ALNT', 'RILY', 'CARE', 'SPFI', 'ANIK', 'PLCE', 'MCFT', 'RBB', 'AAN', 'MCS', 'ESQ', 'TARO', 'BMEA', 'SMMF', 'GRND', 'SHCR', 'OLP', 'OSG', 'ABUS', 'DOMO', 'CSV', 'ADV', 'TAST', 'ACNB', 'TCMD', 'DSKE', 'ENFN', 'NKTX', 'APPS', 'LOVE', 'PRME', 'AGS', 'TERN', 'SFIX', 'EVER', 'MPB', 'IRBT', 'CNSL', 'TRUE', 'ODC', 'GCI', 'FSBC', 'LBPH', 'PLPC', 'PFIS', 'SPWR', 'BAND', 'LYEL', 'ORRF', 'HROW', 'MBI', 'LRMR', 'LIND', 'PBPB', 'TSVT', 'IRMD', 'WTBA', 'BMRC', 'ULCC', 'FBIZ', 'BALY', 'EGHT', 'TRC', 'AESI', 'LMNR', 'CZNC', 'FRBA', 'DSGR', 'RBBN', 'AVIR', 'AMWL', 'FRST', 'AVD', 'GEFB', 'FISI', 'FMAO', 'HBT', 'ARTNA', 'SD', 'TH', 'RYAM', 'GPRO', 'WTI', 'GLRE', 'BSRR', 'TRDA', 'NEWT', 'LXRX', 'BBW', 'HBCP', 'SFST', 'MCBC', 'HRTX', 'PHAT', 'SB', 'ZUMZ', 'TNYA', 'MLYS', 'FLIC', 'HIFS', 'WEST', 'OMER', 'DAKT', 'ONL', 'NRIM', 'PANL', 'GNTY', 'ONEW', 'ARIS', 'DCGO', 'EBTC', 'MVBF', 'ASTS', 'BWB', 'SPOK', 'IHRT', 'BTBT', 'NMRA', 'SLDP', 'ENTA', 'WSBF', 'SLRN', 'CIVB', 'INZY', 'PAHC', 'CHRS', 'ALTG', 'FNLC', 'HUMA', 'EAF', 'XPOF', 'EVGO', 'ONTF', 'PKE', 'VMD', 'HOFT', 'STRO', 'FNKO', 'KIND', 'TYRA', 'NWPX', 'TCBX', 'REFI', 'VNDA', 'ITOS', 'HLLY', 'WLDN', 'RRBI', 'PLL', 'OPRX', 'ARAY', 'BCML', 'ACIC', 'CRCT', 'LOCO', 'HMST', 'WALD', 'GPMT', 'SLQT', 'SNBR', 'ORGO', 'JAKK', 'CELC', 'SENEA', 'PSTX', 'SKIN', 'AGEN', 'FLWS', 'CVRX', 'SMHI', 'NUVB', 'FORR', 'PSTL', 'ASLE', 'CLMB', 'IAUX', 'INGN', 'BLFY', 'CDLX', 'ZVRA', 'IPI', 'EE', 'CBAN', 'ASUR', 'DGICA', 'CPS', 'OBT', 'ME', 'AGTI', 'LSEA', 'AURA', 'LUNA', 'FDBC', 'SIGA', 'ANGO', 'VYGR', 'JOUT', 'LILA', 'AVTE', 'ANNX', 'OOMA', 'NATR', 'OFLX', 'GCBC', 'EVC', 'EVCM', 'HYLN', 'FRGE', 'TSBK', 'SOI', 'JMSB', 'ULH', 'NN', 'CBNK', 'BOWL', 'FIHL', 'WVE', 'FSBW', 'SMLR', 'IGMS', 'UNTY', 'CVLY', 'WW', 'ZYXI', 'GEVO', 'DXLG', 'INOD', 'CVGI', 'TCX', 'OVID', 'CDXS', 'IMMR', 'LEGH', 'AMPY', 'POWW', 'PACK', 'LINC', 'KRO', 'VLGEA', 'LXFR', 'NECB', 'NXDT', 'CRDA', 'BCBP', 'BRT', 'RLGT', 'LPSN', 'REPX', 'NWFL', 'PINE', 'UTMD', 'PKBK', 'ALCO', 'QUAD', 'PKOH', 'RCKY', 'TTSH', 'PGEN', 'NKSH', 'FGEN', 'CIO', 'FVCB', 'NRDY', 'ACDC', 'ITI', 'PCB', 'SGMO', 'BLDE', 'HEAR', 'HRT', 'EHTH', 'AFCG', 'BBCP', 'KODK', 'FF', 'PLBC', 'CZFS', 'RIGL', 'CMTL', 'INSE', 'THRD', 'RMAX', 'LBC', 'MGTX', 'BWFG', 'MBCN', 'RM', 'VRA', 'ITIC', 'MYPS', 'OCN', 'MVST', 'BKSY', 'GRTS', 'CVCY', 'PFMT', 'RDVT', 'COFS', 'GRNT', 'HPK', 'WOW', 'FET', 'NRGV', 'LAW', 'GBTG', 'CFFI', 'GLUE', 'PCYO', 'SES', 'SPRY', 'SKYT', 'BLNK', 'OPI', 'WEYS', 'EPM', 'CRMD', 'ATLO', 'SSBK', 'KOD', 'PDLB', 'SSTI', 'HBIO', 'DOUG', 'TSE', 'OM', 'CHMG', 'OB', 'LVWR', 'EVBN', 'ISPR', 'ALDX', 'ATNM', 'RMNI', 'WISH', 'QSI', 'REI', 'RRGB', 'OVLY', 'CMPX', 'STHO', 'MAXN', 'ATLC', 'HNRG', 'ERAS', 'BHR', 'MG', 'KRT', 'JANX', 'SCPH', 'CLPT', 'CLAR', 'BPRN', 'ATOM', 'HSHP', 'BRCC', 'III', 'MASS', 'NATH', 'BFLY', 'PDSB', 'CIFR', 'FLL', 'SEAT', 'VABK', 'QIPT', 'XOMA', 'INFU', 'DM', 'TLYS', 'ESSA', 'TDUP', 'LCNB', 'MACK', 'PEPG', 'SAMG', 'SMTI', 'JYNT', 'SMR', 'GENC', 'PLSE', 'FSR', 'SPWH', 'LE', 'GNLX', 'PWOD', 'FENC', 'BARK', 'STOK', 'CPSI', 'MHLD', 'PRTS', 'SNPO', 'CMCL', 'RNGR', 'HFFG', 'IBEX', 'VEL', 'GWRS', 'KPTI', 'NGVC', 'BIG', 'ACTG', 'CMT', 'IMRX', 'ESCA', 'NC', 'NAUT', 'RGCO', 'TGAN', 'WLFC', 'BGFV', 'AOMR', 'RSVR', 'STRS', 'LCTX', 'GRWG', 'MEC', 'FHTX', 'INTT', 'MYFW', 'NREF', 'RXT', 'TG', 'PTSI', 'TPIC', 'AKYA', 'KLTR', 'MLP', 'CATO', 'EGAN', 'DSP', 'USCB', 'PETS', 'FCCO', 'KLXE', 'ALTI', 'AVAH', 'VTNR', 'GAMB', 'NODK', 'HIPO', 'VTYX', 'TSQ', 'VRCA', 'PBFS', 'CDZI', 'TELA', 'DHX', 'SCLX', 'XFOR', 'SWIM', 'MNSB', 'SBT', 'BH', 'TRVI', 'BLUE', 'WLLAW', 'IPSC', 'RELL', 'PPTA', 'VOXX', 'MOND', 'DC', 'CTGO', 'EVEX', 'NDLS', 'EOSE', 'MCRB', 'OMGA', 'SNFCA', 'BSVN', 'JILL', 'NOTE', 'GLT', 'OPTN', 'INNV', 'SEER', 'GBIO', 'BCAB', 'LLAP', 'CTXR', 'VUZI', 'EVI', 'KFS', 'ACRS', 'PAYS', 'EEX', 'DNMR', 'PLX', 'BIRD', 'BCOV', 'IVAC', 'EXFY', 'ACET', 'AEVA', 'EBS', 'DSGN', 'KVHI', 'SGHT', 'SKYX', 'PMTS', 'RNAC', 'PRPL', 'MPX', 'TUSK', 'AIRS', 'GRPH', 'GWH', 'ALLK', 'OBIO', 'MURA', 'STKS', 'ASRT', 'CPSS', 'BW', 'CUE', 'EP', 'VERI', 'LNZA', 'CMPO', 'CNTY', 'ATRA', 'SCWO', 'COOK', 'BTAI', 'BKKT', 'OTLK', 'CLPR', 'PROK', 'CCRD', 'NGM', 'VOR', 'CURV', 'BBAI', 'SST', 'DLTH', 'ORGN', 'CARM', 'MKTW', 'EGRX', 'HQI', 'KRMD', 'BTMD', 'PRLD', 'PMVP', 'KZR', 'GOCO', 'RLYB', 'ZURA', 'CMBM', 'AKTS', 'FEAM', 'DTC', 'METCB', 'CUTR', 'WKHS', 'BRBS', 'PNRG', 'LICY', 'FOSL', 'NVCT', 'XAIR', 'SKIL', 'EYEN', 'VIGL', 'NL', 'FOA', 'SGMT', 'TCI', 'VATE', 'PIII', 'GORV', 'TWOU', 'OPFI', 'BHIL', 'VALU', 'VHI', 'ALVR', 'IKNA', 'WLLBW', 'ZVIA', 'FTCI', 'ACRV', 'DZSI', 'CIX', 'AADI', 'CARA', 'RPHM', 'PRTH', 'UONE', 'UONEK', 'AMPX', 'RDW', 'ADRO', 'VLD', 'SWKH', 'UHG', 'ARL', 'VAXX', 'RBOT', 'ADRO', 'RENT', 'AFRI', 'VGAS', 'ELA', 'LPTV', 'BGXX', 'TSBX', 'DFLI', 'CMAX', 'EVA', '--', 'PRST', 'TIO', 'GTXI', 'CAD', 'PDLI', 'P5N994', 'CRGE', 'RTYH4'
])

# print input data
print()
print('Number of days of historical data: ' + str(days_data))
print('Momentum Span in days: ' + str(momentum_span))

# Set the start and end date
end_date = datetime.date.today()
start_date = end_date - datetime.timedelta(days=days_data)

print()
print(f"START")
print()
print('End Date: ' + str(end_date))
print('Start Date: ' + str(start_date))

# Get Data
def get_ticker_data(ticker):
    """
    Input ticker and the SMA timeframe you would like to calculate. The output is a dataframe with the date, Adj Close price
    """

    ticker = str(ticker)
    try:
        data = yf.download(ticker, start_date, end_date)
        print(f'Downloaded {ticker}')
    except:
        print(f"Could not download {ticker}")
        return

    try:
        data = data.drop(['High','Low','Volume', 'Close'] , axis=1)
        print(f'Dropped columns from {ticker}')
    
    except:
        print(f'Could not drop columns from {ticker}')
        return
       
    return data

def get_momentum(data,xDaysMomentum=20):
    lastPrice = data['Adj Close'].iloc[-1]
    print('Last Price: ' + str(lastPrice))
    dataShift = data['Adj Close'].iloc[-xDaysMomentum]
    print('DataShift: ' + str(dataShift))
    momentum = (lastPrice - dataShift) / dataShift
    if -0.002 < momentum < 0.002:
        momentum = 0.0
    print('Calculated momentum: ' + str(momentum))

    return momentum

# def ticker_list():
#     pd_ticker_list = pd.read_csv('C:\\Projects\\cb_api\\russell_2000_data\\russell2000StockList.csv', header=None, index_col=0)
#     np_ticker_list = pd_ticker_list.to_numpy()
#     np_ticker_list = np.reshape(np_ticker_list, (-1,1))
#     return np_ticker_list

# Cycle through each ticker and append the np_momentumData array with the ticker name and momentum
print('ticker_symbols length: ' + str(len(ticker_symbols)))
np_short_ticker_symbols = ticker_symbols
# print(np_short_ticker_symbols)

# try:
#     test1 = get_ticker_data(np_short_ticker_symbols[0], momentum_span)
#     print(test1)
# except:
#     print('Could not get momentum for ' + np_short_ticker_symbols[0])
pd_ticker_momentum = pd.DataFrame(columns=['Ticker', 'Momentum'])
for ticker in np_short_ticker_symbols:
    print(ticker)
    try:
        # get the last momentum value for the ticker
        temp1 = get_ticker_data(ticker)
        print('Retreived momentum data for ' + ticker)
        momentum = get_momentum(temp1, momentum_span)

        

    except:
        print('Could not get data or momentum for ' + ticker)

    # Append the ticker and momentum into a panda dataframe
    pd_ticker_momentum = pd_ticker_momentum._append({'Ticker': ticker, 'Momentum': momentum}, ignore_index=True)

print('')

print('')

print('****************************************')

# Sort the pd_ticker_momentum array by momentum in decreasing order
pd_ticker_momentum = pd_ticker_momentum.sort_values(by=['Momentum'], ascending=False)
print('Num of Tickers Analyzed: ' + str(len(pd_ticker_momentum)))
print('')
print(f'Sorted' + str(pd_ticker_momentum.head(20)))
pd_ticker_momentum.to_csv(str(end_date) + '_russell_2000_with_momentum_days_' + str(momentum_span) + '.csv')

# Sort the np_momentumData array by momentum in decreasing order
# np_momentumData = np_momentumData[np.argsort(np_momentumData[:, 1])][::-1]


print()
print('****************END****************')
print()
