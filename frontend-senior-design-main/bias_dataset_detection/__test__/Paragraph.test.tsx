import React from "react";
import {render, fireEvent} from "@testing-library/react";
import {test} from "@jest/globals";
import Paragraph from "../components/Paragraph";



test("<Paragraph /> has the title" ,() => {
    
    const {getByText} = render(<Paragraph title="mock" body="test" />);

    expect(getByText("mock")) 
})
