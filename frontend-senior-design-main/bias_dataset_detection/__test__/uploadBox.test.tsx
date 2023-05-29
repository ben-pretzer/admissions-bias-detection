import React from "react";
import { renderWithClient } from "./utils";
import { server } from "./setupTests";
import UploadBox from "../components/UploadBox";
import "@testing-library/jest-dom";
import selectEvent from "react-select-event";
import userEvent from "@testing-library/user-event";

describe(
    "Testing that the dropdown menus are loaded correctly," +
        "options can be selected, and files can be attached",
    () => {
        //Needed to render Upload Box
        beforeAll(() => server.listen());
        afterEach(() => server.resetHandlers());
        afterAll(() => server.close());

        test("Regions Value was selected properly", async () => {
            const result = renderWithClient(<UploadBox />);

            await selectEvent.select(
                await result.findByLabelText("Select Region"),
                ["Northwest"]
            );

            expect(result.getByText("Northwest"));
        });

        test("Gender Value was selected properly", async () => {
            const result = renderWithClient(<UploadBox />);

            await selectEvent.select(
                await result.findByLabelText("Select Gender"),
                ["Male"]
            );

            expect(result.getByText("Male"));
        });

        test("Ethnicities Value was selected properly", async () => {
            const result = renderWithClient(<UploadBox />);

            await selectEvent.select(
                await result.findByLabelText("Select Ethnicity"),
                ["Black"]
            );

            expect(result.getByText("Black"));
        });

        test("First File uploads correctly", async () => {
            const fakeFile = new File(["Hello"], "hello.txt", {
                type: "text/plain",
            });
            const result = renderWithClient(<UploadBox />);
            const inputFile = (await result.findByTestId(
                "first_file"
            )) as HTMLInputElement;

            await userEvent.upload(inputFile, fakeFile);

            expect(inputFile.files).toHaveLength(1);
        });

        test("Second File uploads correctly", async () => {
            const fakeFile = new File(["Hello"], "hello.txt", {
                type: "text/plain",
            });
            const result = renderWithClient(<UploadBox />);
            const inputFile = (await result.findByTestId(
                "second_file"
            )) as HTMLInputElement;

            await userEvent.upload(
                (await result.findByTestId("second_file")) as HTMLInputElement,
                fakeFile
            );

            expect(inputFile.files).toHaveLength(1);
        });
    }
);
