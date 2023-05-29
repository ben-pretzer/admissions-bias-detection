import React from "react";
import ReactMarkdown from "react-markdown";
import remarkMath from "remark-math";
import rehypeKatex from "rehype-katex";
import "katex/dist/katex.min.css";
import { interviewContent } from "../constants/interviewsContent";

function interviews() {
    return (
        <div className="bg-white min-h-screen">
            <div>
                <h1 className="flex flex-col items-center pt-8">
                    <span className="mt-2 text-3xl font-body font-extrabold tracking tight text-gray-900 sm:text-4xl">
                        {" "}
                        Human Study
                    </span>
                    <hr className="mt-2 border-t-2 w-20 mx-auto border-[#C3B1E1]" />
                </h1>
            </div>
            <div className="mx-auto font-body prose lg:max-w-none lg:w-1/2 md:prose-lg mt-2">
                <ReactMarkdown className="w-full">
                    {interviewContent}
                </ReactMarkdown>
            </div>
        </div>
    );
}

export default interviews;
