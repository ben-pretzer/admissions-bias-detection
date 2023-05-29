import React from "react";
import { InformationCircleIcon } from "@heroicons/react/24/outline";
import {
    RadialBar,
    RadialBarChart,
    ResponsiveContainer,
    Tooltip,
} from "recharts";
import { TooltipProps } from "recharts";
import {
    ValueType,
    NameType,
} from "recharts/src/component/DefaultTooltipContent";
import ReactMarkdown from "react-markdown";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import "katex/dist/katex.min.css"; // `rehype-katex` does not import the CSS for you

interface IBias {
    regional_bias: boolean;
    national_bias: boolean;
}

interface MetricsCardProps {
    metricName: string;
    metricDescription: string;
    metrics: Array<object>;
    biases: IBias;
}

function MetricsCard({
    metricName,
    metricDescription,
    metrics,
    biases,
}: MetricsCardProps) {
    const [showMetricInfo, setShowMetricInfo] = React.useState(false);
    const showInfo = () => {
        setShowMetricInfo(!showMetricInfo);
    };

    const CustomTooltip = ({
        active,
        payload,
        label,
    }: TooltipProps<ValueType, NameType>) => {
        if (active && payload && payload.length) {
            return (
                <div className="p-3 bg-white/50 drop-shadow-lg border-none rounded-lg">
                    <p className="font-body">{`${payload[0].payload.name} : ${payload[0].value}`}</p>
                </div>
            );
        }
        return null;
    };

    return (
        <div className="bg-[#DBCDF1] m-4 p-3 rounded-xl">
            <div className="flex">
                <div className="flex flex-grow font-body font-bold mb-2">
                    {metricName}
                </div>
                <div>
                    <InformationCircleIcon
                        className="h-6 w-6 hover:cursor-pointer"
                        onClick={showInfo}
                    />
                </div>
            </div>
            <div className="flex justify-center my-3">
                <ResponsiveContainer width="70%" height={300}>
                    <RadialBarChart
                        innerRadius="20%"
                        outerRadius="90%"
                        data={metrics}
                        startAngle={270}
                        endAngle={630}
                        cx="50%"
                        cy="50%"
                    >
                        <RadialBar
                            label={{ fill: "#323131", position: "insideStart" }}
                            background
                            dataKey="metric"
                        />
                        <Tooltip content={<CustomTooltip />} />
                    </RadialBarChart>
                </ResponsiveContainer>
            </div>
            <div className="text-center font-body m-4 space-y-1">
                <div>
                    <span className="font-bold">Regional Bias: </span>
                    {biases.regional_bias?.toString()}
                </div>
                <div>
                    <span className="font-bold">National Bias: </span>
                    {biases.national_bias?.toString()}
                </div>
            </div>
            <ReactMarkdown
                remarkPlugins={[remarkMath]}
                rehypePlugins={[rehypeKatex]}
                className={"font-body mx-5 " + (showMetricInfo ? "" : "hidden")}
            >
                {metricDescription}
            </ReactMarkdown>
        </div>
    );
}

export default MetricsCard;
