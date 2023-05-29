import React from "react";
import { useState } from "react";
import axios from "axios";
import Select, { ActionMeta } from "react-select";
import {
    useForm,
    SubmitHandler,
    Controller,
    FieldValues,
} from "react-hook-form";
import useMetricsStore from "../utilities/store";
import { useQuery } from "@tanstack/react-query";

interface inputData {
    region: string;
    gender: string;
    race: string;
    file_enrollment: File[];
    file_grad: File[];
}

interface IProps {
    setCurrentComponentIndex: Function;
}

//need both value and label because that is what the Select component requires to function
class DropdownItem {
    value: string;
    label: string;

    constructor(value: string, label: string) {
        this.value = value;
        this.label = label;
    }
}

function UploadBox({ setCurrentComponentIndex }: IProps) {
    const {
        setMetrics,
        setEnrollOverTime,
        setGradOverTime,
        setEnrollCurrent,
        setGradCurrent,
        setEthnicity,
        setGender,
    } = useMetricsStore();

    const {
        isLoading: regionLoading,
        error: regionError,
        data: regionData,
    } = useQuery(["getRegions"], () =>
        axios
            .get("http://127.0.0.1:8000/regions")
            .then((response) => response.data)
    );

    const {
        isLoading: genderLoading,
        error: genderError,
        data: genderData,
    } = useQuery(["getGenders"], () =>
        axios
            .get("http://127.0.0.1:8000/genders")
            .then((response) => response.data)
    );

    const {
        isLoading: ethnicityLoading,
        error: ethnicityError,
        data: ethnicityData,
    } = useQuery(["getEthnicities"], () =>
        axios
            .get("http://127.0.0.1:8000/ethnicities")
            .then((response) => response.data)
    );

    const { register, handleSubmit, setValue } = useForm<inputData>();

    const [selectedRegion, setSelectedRegion] = useState<DropdownItem | null>(
        null
    );

    const [selectedGender, setSelectedGender] = useState<DropdownItem | null>(
        null
    );

    const [selectedEthnicity, setSelectedEthnicity] =
        useState<DropdownItem | null>(null);

    const sendData: SubmitHandler<inputData> = async (data) => {
        setCurrentComponentIndex(1);
        const files = new FormData();
        files.append("file_enrollment", data.file_enrollment[0]);
        files.append("file_grad", data.file_grad[0]);
        axios
            .post(
                `http://127.0.0.1:8000/${data.region}/${data.gender}/${data.race}`,
                files,
                {
                    headers: {
                        "Content-Type": "multipart/form-data",
                    },
                }
            )
            .then((response) => setMetrics(response.data))
            .catch((e) => console.log(e));

        const enrollmentFile = new FormData();
        enrollmentFile.append("file_enrollment", data.file_enrollment[0]);

        const gradFile = new FormData();
        gradFile.append("file_grad", data.file_grad[0]);

        const enrollOverTimeResponse = await axios.get(
            `http://127.0.0.1:8000/enroll-over-time/${data.region}/${data.gender}/${data.race}`
        );
        const gradOverTimeResponse = await axios.get(
            `http://127.0.0.1:8000/grad-over-time/${data.region}/${data.gender}/${data.race}`
        );
        const enrollCurrentResponse = await axios.post(
            `http://127.0.0.1:8000/enroll-current/${data.region}/${data.gender}/${data.race}`,
            enrollmentFile,
            {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            }
        );
        const gradCurrentResponse = await axios.post(
            `http://127.0.0.1:8000/grad-current/${data.region}/${data.gender}/${data.race}`,
            gradFile,
            {
                headers: {
                    "Content-Type": "multipart/form-data",
                },
            }
        );

        setEnrollCurrent(enrollCurrentResponse.data);
        setEnrollOverTime(enrollOverTimeResponse.data);

        setGradCurrent(gradCurrentResponse.data);
        setGradOverTime(gradOverTimeResponse.data);

        setGender(data.gender)
        setEthnicity(data.race)

        console.log(enrollCurrentResponse.data);
        console.log(enrollOverTimeResponse.data);
    };

    if (ethnicityLoading || genderLoading || regionLoading) {
        return <p>Loading</p>;
    }

    const regions: Array<DropdownItem> = regionData.regions.map(
        (region: string) => new DropdownItem(region, region)
    );

    const genders: Array<DropdownItem> = genderData.genders.map(
        (gender: string) => new DropdownItem(gender, gender)
    );

    const ethnicities: Array<DropdownItem> = ethnicityData.ethnicities.map(
        (ethnicity: string) => new DropdownItem(ethnicity, ethnicity)
    );

    return (
        <div className="xl:pl-12 xl:pr-0 xl:pt-0 xl:pb-0 xl:absolute relative p-12">
            <form
                onSubmit={handleSubmit(sendData)}
                data-testid="form"
                id="form"
            >
                <div className="mb-8">
                    <div className="mb-8 xl:w-11/12 lg:w-1/3 md:w-1/2">
                        <label
                            className="mb-4 font-body font-medium text-gray-700"
                            htmlFor="Regions"
                        >
                            Select Region
                        </label>
                        <Select
                            options={regions}
                            onChange={(e) =>
                                setValue("region", e?.value as string)
                            }
                            theme={(theme) => ({
                                ...theme,
                                colors: {
                                    ...theme.colors,
                                    ...dropdownMenuColors,
                                },
                            })}
                            name="regions dropdown menu"
                            data-testid="regions_selected"
                            inputId="Regions"
                            className="region-select-container"
                            classNamePrefix="region-select"
                        />
                    </div>
                </div>
                <div className="mb-8 xl:w-11/12 lg:w-1/3 md:w-1/2">
                    <label
                        className="mb-4 font-body font-medium text-gray-700"
                        htmlFor="Genders"
                    >
                        Select Gender
                    </label>
                    <Select
                        options={genders}
                        onChange={(e) => setValue("gender", e?.value as string)}
                        theme={(theme) => ({
                            ...theme,
                            colors: { ...theme.colors, ...dropdownMenuColors },
                        })}
                        data-testid="genders dropdown menu"
                        inputId="Genders"
                        className="gender-select-container"
                        classNamePrefix="gender-select"
                    />
                </div>
                <div className="mb-8 xl:w-11/12 lg:w-1/3 md:w-1/2">
                    <label
                        className="mb-4 font-body font-medium text-gray-700"
                        htmlFor="Ethnicities"
                    >
                        Select Ethnicity
                    </label>
                    <Select
                        options={ethnicities}
                        onChange={(e) => setValue("race", e?.value as string)}
                        theme={(theme) => ({
                            ...theme,
                            colors: { ...theme.colors, ...dropdownMenuColors },
                        })}
                        data-testid="ethincities dropdown menu"
                        inputId="Ethnicities"
                        className="ethnicities-select-container"
                        classNamePrefix="ethnicities-select"
                    />
                </div>
                <div className="">
                    <label
                        className="mb-4 font-body font-medium text-gray-700"
                        htmlFor="file_enrollment"
                    >
                        Enrollment Dataset
                    </label>
                </div>
                <div className="mb-4">
                    <input
                        type="file"
                        {...register("file_enrollment")}
                        className="text-grey-500
                        file:mr-5 file:py-2 file:px-4
                        file:border-0
						file:font-body
                        file:font-bold
                        file:bg-[#947ABE] file:text-gray-800
                        file:hover:bg-[#897b9e]
                        rounded-lg
                        border border-gray-800"
                        data-testid="first_file"
                        id="file_enrollment"
                    />
                </div>
                <div className="">
                    <label
                        className="mb-4 font-body font-medium text-gray-700"
                        htmlFor="file_grad"
                    >
                        Graduation Dataset
                    </label>
                </div>
                <div className="mb-10">
                    <input
                        type="file"
                        {...register("file_grad")}
                        className="
                        file:mr-5 file:py-2 file:px-4
                        file:border-0
						file:font-body
                        file:font-bold
                        file:bg-[#947ABE] file:text-gray-800
                        file:hover:bg-[#897b9e]
                        rounded-lg
                        border border-gray-800"
                        data-testid="second_file"
                        id="file_grad"
                    />
                </div>
                <div className="mb-4">
                    <input
                        type="submit"
                        className="bg-[#C3B1E1]
                        hover:bg-[#897b9e] text-grey-800
						hover:cursor-pointer
                        font-body font-bold py-2 px-4 rounded border-[1px] border-black
                        focus:outline-none focus:shadow-outline"
                    />
                </div>
            </form>
        </div>
    );
}

const dropdownMenuColors = {
    primary25: "#d8c6f7",
    primary: "#C3B1E1",
};

export default UploadBox;
