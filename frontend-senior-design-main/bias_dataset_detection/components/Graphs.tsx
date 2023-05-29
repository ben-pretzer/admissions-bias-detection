import React from "react";
import useMetricsStore from "../utilities/store";
import BarGraphCard from "./BarGraphCard";
import LineGraphCard from "./LineGraphCard"
import { processCurrentData } from "../utilities/proccessGraphData";
import { graphsCardContent } from "../constants/graphCardContent";





function Graphs() {
    const {
        enrollOverTimeData,
        enrollCurrentData,
        gradOverTimeData,
        gradCurrentData,
        gender, 
        ethnicity,
    } = useMetricsStore();

    const enrollCurrentArray = processCurrentData(enrollCurrentData)
    const gradCurrentArray = processCurrentData(gradCurrentData)

    return (
        <div className="grid grid-cols-1 lg:grid-cols-2 mx-auto p-4">
            <LineGraphCard 
                title={`Enrollment Rate Over Time of ${ethnicity} ${gender}`} 
                data={enrollOverTimeData} 
                graphDescription={graphsCardContent.overTimeEnroll.description}
            />
            <LineGraphCard 
                title={`Graduation Rate Over Time of ${ethnicity} ${gender}`} 
                data={gradOverTimeData}
                graphDescription={graphsCardContent.overTimeGrad.description}
             />
            <BarGraphCard 
            title={`Current Enrollment Rate of ${ethnicity} ${gender}`} 
                data={enrollCurrentArray} 
                graphDescription={graphsCardContent.currentEnroll.description}
            />
            <BarGraphCard 
                title={`Current Graduation Rate of ${ethnicity} ${gender}`} 
                data={gradCurrentArray} 
                graphDescription={graphsCardContent.currentGrad.description}
            />
        </div>
    );
}

export default Graphs;
