export {};

describe(
    "User Journey calling backend API," + "requires backend to be online",
    () => {
        beforeEach(() => {
            cy.viewport(1920, 1080);
            cy.visit("http://localhost:3000");
        });

        it(
            "Starts on landing page," +
                "navigates to Upload page, selects options," +
                "submits request to backend",
            () => {
                /**
                 * Selects options on the Upload Box and sends request
                 * to the server with files included
                 */
                //West
                cy.get("#Upload_Tag").click({ force: true }); //Since button is hidden, need to force it

                cy.get(".region-select__control") //Finds the region dropdown menu
                    .click()
                    .get(".region-select__menu") //find opened dropdown menu
                    .find(".region-select__option") //find all options
                    .first()
                    .click(); //click first option

                //Female
                cy.get(".gender-select__control")
                    .click()
                    .get(".gender-select__menu")
                    .find(".gender-select__option")
                    .last()
                    .click();

                //White
                cy.get(".ethnicities-select__control")
                    .click()
                    .get(".ethnicities-select__menu")
                    .find(".ethnicities-select__option")
                    .last()
                    .click();

                const enrollment_file = "biased_enrollment.csv";
                const graduation_file = "biased_graduation.csv";

                cy.get("#file_enrollment").attachFile(enrollment_file);
                cy.get("#file_grad").attachFile(graduation_file);

                //Adds an alias to the API call so that the response can be checked
                cy.intercept("POST", "/West/Female/White").as(
                    "file_submission"
                );

                cy.get('input[type="submit"]').click();

                cy.get("@file_submission")
                    .its("response.body")
                    .then((response) => {
                        expect(response.bias_cb_national).eql(true);
                        expect(response.bias_kl_national).eql(true);
                        expect(response.bias_dpl_national).eql(true);
                        expect(response.bias_ks_national).eql(true);
                        expect(response.bias_tvd_national).eql(true);
                    });
            }
        );
    }
);
