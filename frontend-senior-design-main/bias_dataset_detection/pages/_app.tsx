import React from 'react';
import "../styles/globals.css";
import type { AppProps } from "next/app";
import Header from "../components/Header";

import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const queryClient = new QueryClient();

function MyApp({ Component, pageProps }: AppProps) {
    return (
        <div className="bg-[#C3B1E1]">
            <Header />
            <QueryClientProvider client={queryClient}>
                <Component {...pageProps} />
            </QueryClientProvider>
        </div>
    );
}

export default MyApp;
