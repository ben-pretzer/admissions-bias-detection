import React from "react";

function LegendCard() {
    return (
        <div className="bg-[#DBCDF1] mt-4 mx-4 p-3 rounded-xl">
            <div className="flex">
                <div className="flex flex-grow font-body font-bold mb-2">
                    Legend
                </div>
            </div>
            <div className="flex align-middle justify-center pb-2">
                {/* <div className="inline-block w-1/4 space-y-4">
                    <div className="flex mt-3">
                        <div className="h-6 w-6 border border-white rounded-full bg-[#83a6ed]"></div>
                        <div className="font-body ml-3">University</div>
                    </div>
                    <div className="flex">
                        <div className="h-6 w-6 border border-white rounded-full bg-[#83a6ed]"></div>
                        <div className="font-body ml-3">Region</div>
                    </div>
                    <div className="flex">
                        <div className="h-6 w-6 border border-white rounded-full bg-[#8dd1e1]"></div>
                        <div className="font-body ml-3">National</div>
                    </div>
                </div> */}
                <img src="/legend.svg" width="250" height="250"></img>
            </div>
            <p className="px-6 pb-4 font-body">
                For the following metrics, numbers close to 0 mean that the data
                is more evenly distributed whereas numbers close to 1 or -1 mean
                imbalanced data.
            </p>
        </div>
    );
}

export default LegendCard;
