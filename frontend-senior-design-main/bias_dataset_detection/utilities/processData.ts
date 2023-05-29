export function processData(metrics: any) {
    const nationalFill = "#8dd1e1";
    const regionalFill = "#83a6ed";
    const uniFill = "#ffc658";
    const natlAvg = "National Average";
    const regionalAvg = "Regional Average";
    const uni = "University";

    const cbMetrics = [
        {
            name: uni,
            metric: Math.round(metrics.cb_uni_ratio * 100) / 100,
            fill: uniFill,
        },
        {
            name: regionalAvg,
            metric: Math.round(metrics.cb_regional_ratio * 100) / 100,
            fill: regionalFill,
        },
        {
            name: natlAvg,
            metric: Math.round(metrics.cb_national_ratio * 100) / 100,
            fill: nationalFill,
        },
    ];

    const dplMetrics = [
        {
            name: uni,
            metric: Math.round(metrics.dpl_uni_ratio * 100) / 100,
            fill: uniFill,
        },
        {
            name: regionalAvg,
            metric: Math.round(metrics.dpl_regional_ratio * 100) / 100,
            fill: regionalFill,
        },
        {
            name: natlAvg,
            metric: Math.round(metrics.dpl_national_ratio * 100) / 100,
            fill: nationalFill,
        },
    ];

    const klMetrics = [
        {
            name: uni,
            metric: Math.round(metrics.kl_uni_ratio * 100) / 100,
            fill: uniFill,
        },
        {
            name: regionalAvg,
            metric: Math.round(metrics.kl_regional_ratio * 100) / 100,
            fill: regionalFill,
        },
        {
            name: natlAvg,
            metric: Math.round(metrics.kl_national_ratio * 100) / 100,
            fill: nationalFill,
        },
    ];

    const ksMetrics = [
        {
            name: uni,
            metric: Math.round(metrics.ks_uni_ratio * 100) / 100,
            fill: uniFill,
        },
        {
            name: regionalAvg,
            metric: Math.round(metrics.ks_regional_ratio * 100) / 100,
            fill: regionalFill,
        },
        {
            name: natlAvg,
            metric: Math.round(metrics.ks_national_ratio * 100) / 100,
            fill: nationalFill,
        },
    ];

    const tvdMetrics = [
        {
            name: uni,
            metric: Math.round(metrics.tvd_uni_ratio * 100) / 100,
            fill: uniFill,
        },
        {
            name: regionalAvg,
            metric: Math.round(metrics.tvd_regional_ratio * 100) / 100,
            fill: regionalFill,
        },
        {
            name: natlAvg,
            metric: Math.round(metrics.tvd_national_ratio * 100) / 100,
            fill: nationalFill,
        },
    ];

    const cbBiases = {
        regional_bias: metrics.bias_cb_regional,
        national_bias: metrics.bias_cb_national,
    };

    const dplBiases = {
        regional_bias: metrics.bias_dpl_regional,
        national_bias: metrics.bias_dpl_national,
    };

    const klBiases = {
        regional_bias: metrics.bias_dpl_regional,
        national_bias: metrics.bias_dpl_national,
    };

    const ksBiases = {
        regional_bias: metrics.bias_ks_regional,
        national_bias: metrics.bias_ks_national,
    };

    const tvdBiases = {
        regional_bias: metrics.bias_tvd_regional,
        national_bias: metrics.bias_tvd_national,
    };

    return {
        cbMetrics,
        dplMetrics,
        klMetrics,
        ksMetrics,
        tvdMetrics,
        cbBiases,
        dplBiases,
        klBiases,
        ksBiases,
        tvdBiases,
    };
}
