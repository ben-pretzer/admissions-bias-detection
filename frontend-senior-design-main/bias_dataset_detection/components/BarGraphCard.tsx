import React from "react";
import {
    BarChart,
    Bar,
    Cell,
    XAxis,
    YAxis,
    CartesianGrid,
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
import { InformationCircleIcon } from "@heroicons/react/24/outline";


interface GraphCardProps {
    title: string;
    graphDescription:string;
    data: Array<object>;
}

const toPercent = (number:number) => {
	return `${Math.round(number)}%`;
};

const renderTooltipContent = (o:any) => {
	const { payload, label } = o;
  
  return (
  	<div className="customized-tooltip-content">
    	<p className="total">{`${label}`}</p>
      <ul className="list">
      	{
        	payload.map((entry:any, index:number) => (
          	<li key={`item-${index}`}>
            	{`${entry.name}: ${toPercent(entry.value)}`}
            </li>
          ))
        }
      </ul>
    </div>
  );
};

function BarGraphCard({ 
    title, 
    graphDescription, 
    data 
}: GraphCardProps) {

    const [showMetricInfo, setShowMetricInfo] = React.useState(false);
    const showInfo = () => {
        setShowMetricInfo(!showMetricInfo);
    };

    return (
        <div className="bg-[#DBCDF1] m-4 p-3 rounded-xl">
            <div className="flex">
                <div className="flex flex-grow font-body font-bold mb-2">
                    {title}
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
                    <BarChart data={data} width={500} height={200}>
                        <Tooltip content={renderTooltipContent}/>
                        <CartesianGrid strokeDasharray="3 3"/>
                        <Bar dataKey="percentage" fill="#8884d8"/>
                        <XAxis dataKey='name'/> 
                        <YAxis tickFormatter={tick => `${tick}%`}/>
                    </BarChart>
                </ResponsiveContainer>
            </div>
            <ReactMarkdown
                remarkPlugins={[remarkMath]}
                rehypePlugins={[rehypeKatex]}
                className={"font-body mx-2 " + (showMetricInfo ? "" : "hidden")}
            >
                {graphDescription}
            </ReactMarkdown>
        </div>
    );
}

export default BarGraphCard;
