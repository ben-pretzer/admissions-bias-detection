import React from 'react';
import UploadBox from './UploadBox';
import Image from 'next/image'

interface IProps {
    setCurrentComponentIndex:Function;
}

function SubmitData({setCurrentComponentIndex} : IProps) {
    return(
        <div className='bg-[#C3B1E1] min-h-screen"'>
            <div className="ml-10 pt-5">
                <h1 className="text-3xl">
                    1. Submit Enrollment and Graduation Datasets
                </h1>
                <h3 className="text-2xl">
                    Your datasets should contain a gender and ethnicity column.
                </h3>
            </div>
            <div className="relative">
                <UploadBox setCurrentComponentIndex={setCurrentComponentIndex}/>
                <div className='xl:absolute xl:right-2 relative'>
                    <Image src="/images/MapChart_Map.png" width={725} height="515" />
                </div>
            </div>
        </div>
    )
}

export default SubmitData;