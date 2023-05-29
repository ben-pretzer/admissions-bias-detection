import React from "react";
import { VscCircleLargeFilled } from "react-icons/vsc";
import { useStore } from "zustand";
import useMetricsStore from "../utilities/store";

interface IProps {
    currentComponentIndex: number;
    setCurrentComponentIndex: Function;
}

function NavBar({ currentComponentIndex, setCurrentComponentIndex }: IProps) {
    const changeComponent = (index: number) => {
        setCurrentComponentIndex(index);
    };

    /**
     * Either have a parameter in both stores, or check if one of the elements is on its default state
     */

    const { metrics, enrollOverTimeData } = useMetricsStore();

    let hasMetricInfo: boolean = Object.keys(metrics).length === 0;
    let hasRawDataInfo: boolean = enrollOverTimeData.length === 0;

    return (
        <div className="bg-[#947ABE] font-body">
            <div>
                <h1 className="ml-10 mb-2 pt-5 text-white text-xl">
                    Bias Detection
                </h1>
            </div>
            <div className="grid grid-cols-3 w-56 pl-6 text-sm pb-10 text-white">
                <div className="m-auto text-center">
                    <button
                        onClick={() => {
                            changeComponent(0);
                        }}
                    >
                        <VscCircleLargeFilled
                            size="20"
                            className={
                                currentComponentIndex !== 0
                                    ? "text-white/50"
                                    : "text-white"
                            }
                        />
                    </button>
                    <div className="m-auto">Data</div>
                </div>
                <div className="m-auto text-center">
                    <button
                        onClick={() => {
                            changeComponent(1);
                        }}
                        disabled={hasRawDataInfo}
                    >
                        <VscCircleLargeFilled
                            size="20"
                            className={
                                currentComponentIndex !== 1
                                    ? "text-white/50"
                                    : "text-white"
                            }
                        />
                    </button>
                    <div className="m-auto">Metrics</div>
                </div>
                <div className="m-auto text-center">
                    <button
                        onClick={() => {
                            changeComponent(2);
                        }}
                        disabled={hasMetricInfo}
                    >
                        <VscCircleLargeFilled
                            size="20"
                            className={
                                currentComponentIndex !== 2
                                    ? "text-white/50"
                                    : "text-white"
                            }
                        />
                    </button>
                    <div className="m-auto">Graphs</div>
                </div>
            </div>
        </div>
    );
}

export default NavBar;
