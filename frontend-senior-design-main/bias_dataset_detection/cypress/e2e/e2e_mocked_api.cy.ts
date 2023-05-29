export {};

describe("User Journey with mocked API", () => {
    beforeEach(() => {
        cy.viewport(1920, 1080);
        cy.visit("http://localhost:3000");
    });

    it(
        "Starts on landing page," +
            "navigates to Upload page, selects options," +
            "and submits request to backend",
        () => {
            /**
             * Mock API calls so that Upload Page can load successfully
             */

            cy.intercept(
                {
                    method: "GET",
                    url: "/regions",
                },
                { regions: ["Northwest"] }
            ).as("Get Regions");

            cy.intercept(
                {
                    method: "GET",
                    url: "/genders",
                },
                { genders: ["Male"] }
            ).as("Get Genders");

            cy.intercept(
                {
                    method: "GET",
                    url: "/ethnicities",
                },
                { ethnicities: ["Black"] }
            ).as("Get Ethnicities");

            /**
             * Selects options on the Upload Box and sends request
             * to the server with files included
             */

            cy.get("#Upload_Tag").click({ force: true }); //Since button is hidden, need to force it

            cy.get(".region-select__control") //Finds the region dropdown menu
                .click()
                .get(".region-select__menu") //find opened dropdown menu
                .find(".region-select__option") //find all options
                .first()
                .click(); //click first option

            cy.get(".gender-select__control")
                .click()
                .get(".gender-select__menu")
                .find(".gender-select__option")
                .first()
                .click();

            cy.get(".ethnicities-select__control")
                .click()
                .get(".ethnicities-select__menu")
                .find(".ethnicities-select__option")
                .first()
                .click();

            const enrollment_file = "mock_enroll.csv";
            const graduation_file = "mock_grad.csv";

            cy.get("#file_enrollment").attachFile(enrollment_file);
            cy.get("#file_grad").attachFile(graduation_file);

            cy.get('input[type="submit"]').click();

            /**
             * Intercepts the expected request that is made to the backend
             */

            cy.intercept(
                {
                    method: "POST",
                    url: "/Northwest/Male/Black",
                },
                []
            ).as("Return files");

            /**
             * Asserts that the request includes the files that were mocked
             */

            cy.wait("@Return files")
                .its("request.body")
                .should("include", "mock_enroll.csv");
            cy.get("@Return files")
                .its("request.body")
                .should("include", "mock_grad.csv");
        }
    );
});
