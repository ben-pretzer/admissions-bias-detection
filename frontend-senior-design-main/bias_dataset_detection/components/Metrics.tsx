import React from "react";
import { metricsCardContent } from "../constants/metricsCardContent";
import useMetricsStore from "../utilities/store";
import MetricsCard from "./MetricsCard";
import { processData } from "../utilities/processData";
import LegendCard from "./LegendCard";

function Metrics() {
    const { metrics } = useMetricsStore();
    {
        console.log(metrics);
    }
    const {
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
    } = processData(metrics);

    {
        console.log(dplMetrics);
    }
    return (
        <div className="grid grid-cols-1 lg:grid-cols-3 mx-auto p-4">
            <LegendCard />
            <MetricsCard
                metricName={metricsCardContent.cb.title}
                metricDescription={metricsCardContent.cb.description}
                metrics={cbMetrics}
                biases={cbBiases}
            />
            <MetricsCard
                metricName={metricsCardContent.ks.title}
                metricDescription={metricsCardContent.ks.description}
                metrics={ksMetrics}
                biases={ksBiases}
            />
            <MetricsCard
                metricName={metricsCardContent.dpl.title}
                metricDescription={metricsCardContent.dpl.description}
                metrics={dplMetrics}
                biases={dplBiases}
            />
            <MetricsCard
                metricName={metricsCardContent.kl.title}
                metricDescription={metricsCardContent.kl.description}
                metrics={klMetrics}
                biases={klBiases}
            />
            <MetricsCard
                metricName={metricsCardContent.tvd.title}
                metricDescription={metricsCardContent.tvd.description}
                metrics={tvdMetrics}
                biases={tvdBiases}
            />
        </div>
    );
}

export default Metrics;
