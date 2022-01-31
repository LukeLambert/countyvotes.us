(() => {
    const search = document.getElementById('search');

    new autoComplete({
        selector: '#search',
        wrapper: false,
        data: {
            src: async () => {
                try {
                    search.setAttribute('placeholder', 'Loading counties…');
                    const source = await fetch(COUNTIES_JSON_URL);
                    const data = await source.json();
                    search.setAttribute('placeholder', 'Search counties');
                    return data.counties.map(county => {
                        return {
                            id: county[0],
                            name: `${county[1]}, ${data.states[county[2]]}`,
                        };
                    });
                } catch (error) {
                    return error;
                }
            },
            keys: ['name'],
            cache: true
        },
        searchEngine: (query, record) => {
            const needle = query.toLowerCase().split(/[ ,]+/).join(' ');
            const haystack = record.toLowerCase().split(/[ ,]+/).join(' ');
            if (haystack.startsWith(needle)) {
                return record;
            }
        },
        events: {
            input: {
                selection(event) {
                    const id = event.detail.selection.value.id;
                    window.location = `/${id}/`;
                }
            }
        }
    });
})()

