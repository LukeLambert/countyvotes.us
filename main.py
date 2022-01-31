from collections import namedtuple

import flask
import humanize

import settings
from data import get_results, get_states

app = flask.Flask(__name__)
app.results = get_results()
app.states = get_states()
app.years = list(app.results[48453].years.keys())


@app.route('/')
def home_view():
    interesting = []
    for fips_code in settings.INTERESTING:
        county = app.results[fips_code]
        interesting.append({
            'fips_code': fips_code,
            'name': county.name,
            'state': app.states[county.state]
        })
    return flask.render_template('home.html', interesting=interesting)


@app.route('/<int:fips_code>/')
def county_view(fips_code):
    try:
        county = app.results[fips_code]
    except KeyError:
        flask.abort(404)
    state = app.states[county.state]
    results_by_year = []
    results_by_party = {}
    for party in settings.PARTIES:
        results_by_party[party['code']] = {
            'code': party['code'],
            'name': party['name'],
            'shares': [],
        }
    for year, counts in sorted(county.years.items()):
        shares = []
        total = sum(counts)
        for idx, party in enumerate(settings.PARTIES):
            code = party['code']
            votes = counts[idx]
            shares.append({
                'code': code,
                'votes': votes,
                'percentage': '{:.1f}'.format(votes / total * 100),
            })
            results_by_party[code]['shares'].append({
                'year': year,
                'votes': votes,
                'total': total,
            })
        results_by_year.append({
            'year': year,
            'shares': shares,
            'total': total,
        })
    results_by_party = list(results_by_party.values())
    return flask.render_template(
        'county.html',
        county=county,
        state=state,
        parties=settings.PARTIES,
        results_by_year=results_by_year,
        results_by_party=results_by_party,
    )


@app.route('/counties/')
def counties_view():
    State = namedtuple('State', ['name', 'counties'])
    County = namedtuple('County', ['fips_code', 'name'])
    states = {}
    for code, name in app.states.items():
        states[code] = State(name=name, counties=[])
    for fips_code, county in app.results.items():
        code = county.state
        states[code].counties.append(County(fips_code=fips_code, name=county.name))
    return flask.render_template('counties.html', states=states)


@app.route('/counties.json')
def counties_json():
    state_codes = list(app.states.keys())
    counties = []
    for fips_code, county in app.results.items():
        state_index = state_codes.index(county.state)
        counties.append([fips_code, county.name, state_index])
    data = {
        'states': list(app.states.values()),
        'counties': counties,
    }
    return flask.jsonify(data)


@app.route('/sources/')
def sources_view():
    return flask.render_template('sources.html')


@app.route('/robots.txt')
def robots_txt():
    content = 'User-agent: *\nDisallow:'
    return flask.Response(content, mimetype='text/plain')


@app.route('/404.html')
@app.errorhandler(404)
def error_404_view(e):
    return flask.render_template('404.html'), 404


@app.context_processor
def context_processor():
    return {
        'intcomma': humanize.intcomma,
        'min_year': min(app.years),
        'max_year': max(app.years),
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
