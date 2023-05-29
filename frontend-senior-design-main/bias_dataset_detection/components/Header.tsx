import React from "react";
import Link from "next/link";
import { Bars3Icon } from "@heroicons/react/24/outline";
import { motion } from "framer-motion";

let useClickOutside = (handler: any) => {
    let navRef = React.useRef<any>();

    React.useEffect(() => {
        let maybeHandler = (e: { target: any }) => {
            if (navRef.current && !navRef.current.contains(e.target)) {
                handler();
            }
        };

        document.addEventListener("mousedown", maybeHandler);

        return () => {
            document.removeEventListener("mousedown", maybeHandler);
        };
    });
    return navRef;
};

function Header() {
    const [sidebar, setSidebar] = React.useState(false);

    function handleNavClick() {
        setSidebar(false);
    }

    const showSidebar = () => {
        setSidebar(!sidebar);
    };

    let navRef = useClickOutside(() => {
        setSidebar(false);
    });

    return (
        <nav className="border-b-2  dark:border-zinc-600 bg-white dark:bg-[#121828] top-0 z-50">
            <div className="flex flex-none">
                <div className="flex justify-between flex-1 md:justify-around max-w-7xl mt-1 lg:mx-auto">
                    <motion.div
                        initial={{
                            x: -500,
                            opacity: 0,
                            scale: 0.6,
                        }}
                        animate={{
                            x: 0,
                            opacity: 1,
                            scale: 1,
                        }}
                        transition={{
                            duration: 1.4,
                        }}
                    >
                        <div className="navBtn md:hidden flex">
                            Bias Detection
                        </div>

                        <Link href="/">
                            <a className="navBtn hidden md:inline-flex mx-4">
                                Home
                            </a>
                        </Link>

                        <Link href="/upload">
                            <a className="navBtn hidden md:inline-flex mx-4">
                                Upload
                            </a>
                        </Link>

                        <Link href="/interviews">
                            <a className="navBtn hidden md:inline-flex mx-4">
                                Human Study
                            </a>
                        </Link>

                        {/* mobile button */}
                        <div className="navBtn md:hidden flex items-center">
                            <Bars3Icon
                                className="h-7 w-7"
                                onClick={showSidebar}
                            />
                        </div>
                        {/* #121828 */}
                        {/* #6869AE */}
                    </motion.div>
                </div>
            </div>

            {/* mobile menu */}
            <div
                ref={navRef}
                className={"md:hidden " + (sidebar ? "" : "hidden")}
            >
                <Link href="/" data-test-id="Home Tag">
                    <a
                        onClick={handleNavClick}
                        className="mobileNavItem"
                        id="Home Tag"
                    >
                        Home
                    </a>
                </Link>

                <Link href="/upload">
                    <a
                        onClick={handleNavClick}
                        className="mobileNavItem"
                        id="Upload_Tag"
                    >
                        Upload
                    </a>
                </Link>

                <Link href="/interviews">
                    <a
                        onClick={handleNavClick}
                        className="mobileNavItem"
                        id="Interviews Tag"
                    >
                        human Study
                    </a>
                </Link>
            </div>
        </nav>
    );
}

export default Header;
