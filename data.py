#!/usr/bin/env python3

import csv
from collections import namedtuple

from natsort import natsorted

import settings


def get_counties():
    counties = settings.COUNTY_OVERRIDES.copy()
    with settings.COUNTIES_FILE.open('r') as f:
        reader = csv.reader(f)
        for _, state_fips, county_fips, county_name, _ in reader:
            fips_code = int(state_fips + county_fips)
            counties[fips_code] = county_name
    return counties


def get_states():
    with settings.STATES_FILE.open('r') as f:
        reader = csv.DictReader(f)
        states = [(row['code'], row['name']) for row in reader]
    states = dict(sorted(states, key=lambda state: state[1]))
    return states


def get_results():
    counties = get_counties()
    County = namedtuple('County', ['name', 'state', 'years'])
    party_indexes = {}
    for idx, party in enumerate(settings.PARTIES):
        for included in party['include']:
            party_indexes[included] = idx
    results = {}
    with settings.RESULTS_FILE.open('r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                votes = int(row['candidatevotes'])
            except ValueError:
                continue
            try:
                fips_code = int(row['county_fips'])
            except ValueError:
                fips_code = None
            override_lookup = (row['state_po'], row['county_name'], fips_code)
            fips_code = settings.RESULT_OVERRIDES.get(override_lookup, fips_code)
            if fips_code in [None, 2099]:
                continue
            year = int(row['year'])
            if fips_code not in results:
                results[fips_code] = County(
                    name=counties[fips_code],
                    state=row['state_po'],
                    years={}
                )
            county = results[fips_code]
            if year not in county.years:
                county.years[year] = [0] * len(settings.PARTIES)
            result = county.years[year]
            party_index = party_indexes[row['party']]
            result[party_index] += votes
    results = dict(natsorted(results.items(), key=lambda r: r[1].name))
    return results
