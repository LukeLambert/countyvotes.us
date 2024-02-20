(() => {
    const results = JSON.parse(document.getElementById('results-by-party').textContent)
    const style = getComputedStyle(document.body)
    const colors = {
        text: style.getPropertyValue('--color-chart-text'),
        gridlines: style.getPropertyValue('--color-chart-gridlines'),
        democrat: style.getPropertyValue('--color-chart-democrat'),
        democratBg: style.getPropertyValue('--color-chart-democrat-bg'),
        republican: style.getPropertyValue('--color-chart-republican'),
        republicanBg: style.getPropertyValue('--color-chart-republican-bg'),
        other: style.getPropertyValue('--color-chart-other'),
        otherBg: style.getPropertyValue('--color-chart-other-bg'),
    }
    const labels = results[0].shares.map(share => share.year)
    const scaleOptions = {
        ticks: {
            color: colors.text,
        },
        grid: {
            color: colors.gridlines
        }
    }
    const baseOptions = {
        scales: {
            x: scaleOptions,
            y: scaleOptions
        },
        plugins: {
            legend: {
                display: true,
                labels: {
                    color: colors.text
                }
            }
        }
    }
    const percentagesOptions = JSON.parse(JSON.stringify(baseOptions))
    percentagesOptions.scales.x.stacked = true
    percentagesOptions.scales.y.stacked = true
    percentagesOptions.scales.y.bounds = 'data'

    new Chart(document.getElementById('votes-chart'), {
        type: 'bar',
        data: {
            labels: labels,
            datasets: results.map(result => {
                return {
                    label: result.name,
                    data: result.shares.map(share => share.votes),
                    borderWidth: 1,
                    backgroundColor: colors[result.code + 'Bg'],
                    borderColor: colors[result.code],
                }
            })
        },
        options: baseOptions
    })

    new Chart(document.getElementById('percentages-chart'), {
        type: 'bar',
        data: {
            labels: labels,
            datasets: results.map(result => {
                return {
                    label: result.name,
                    data: result.shares.map(share => share.votes / share.total * 100),
                    borderWidth: 1,
                    backgroundColor: colors[result.code + 'Bg'],
                    borderColor: colors[result.code],
                }
            })
        },
        options: percentagesOptions
    })
})()
