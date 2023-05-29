import React from "react";

interface IProps {
    title: string;
    body: string;
}

function Paragraph({ title, body }: IProps) {
    return (
        <>
            <div className="flex justify-center">
                <p className="text-4xl mt-20 mx-8 text-center font-body">
                    {title}
                </p>
            </div>
            <div className="flex justify-center">
                <p className="font-body mt-10 mx-8 text-center max-w-5xl">
                    {body}
                </p>
            </div>
        </>
    );
}

export default Paragraph;
