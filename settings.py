import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ENV = os.environ.get('ENV')
DATA_DIR = BASE_DIR / 'data'
RESULTS_FILE = DATA_DIR / 'results.csv'
COUNTIES_FILE = DATA_DIR / 'counties.csv'
STATES_FILE = DATA_DIR / 'states.csv'

PARTIES = [
    {'code': 'democrat', 'name': 'Democrat', 'include': ('DEMOCRAT',)},
    {'code': 'republican', 'name': 'Republican', 'include': ('REPUBLICAN',)},
    {'code': 'other', 'name': 'Other', 'include': ('GREEN', 'LIBERTARIAN', 'OTHER',)},
]

INTERESTING = [
    4013,  # Maricopa County, Arizona
    39099,  # Mahoning County, Ohio
    13135,  # Gwinnett County, Georgia
    12086,  # Miami-Dade County, Florida
    48215,  # Hidalgo County, Texas
]

COUNTY_OVERRIDES = {
    29999: 'Kansas City',
    2001: 'District 1',
    2002: 'District 2',
    2003: 'District 3',
    2004: 'District 4',
    2005: 'District 5',
    2006: 'District 6',
    2007: 'District 7',
    2008: 'District 8',
    2009: 'District 9',
    2010: 'District 10',
    2011: 'District 11',
    2012: 'District 12',
    2013: 'District 13',
    2014: 'District 14',
    2015: 'District 15',
    2016: 'District 16',
    2017: 'District 17',
    2018: 'District 18',
    2019: 'District 19',
    2020: 'District 20',
    2021: 'District 21',
    2022: 'District 22',
    2023: 'District 23',
    2024: 'District 24',
    2025: 'District 25',
    2026: 'District 26',
    2027: 'District 27',
    2028: 'District 28',
    2029: 'District 29',
    2030: 'District 30',
    2031: 'District 31',
    2032: 'District 32',
    2033: 'District 33',
    2034: 'District 34',
    2035: 'District 35',
    2036: 'District 36',
    2037: 'District 37',
    2038: 'District 38',
    2039: 'District 39',
    2040: 'District 40',
}

RESULT_OVERRIDES = {
    ('MO', 'KANSAS CITY', 36000): 29999,
    ('DC', 'DISTRICT OF COLUMBIA', None): 11001,
}
