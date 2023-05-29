import useMetricsStore from "../utilities/store";

interface ICardContent {
	[key: string]: { description: string };
}



export const graphsCardContent: ICardContent = {
	currentEnroll: {
		description: `The current enrollment ratio of the given gender and ethnicity,
        in other universites of the region, all universities in the US, and the university that was uploaded`,
	},
	currentGrad: {
		description: `The current graduation ratio of the given gender and ethnicity,
        in other universites of the region, all universities in the US, and the university that was uploaded`,
	},
	overTimeEnroll: {
		description: `The enrollment ratio of the given gendeer and ethnicity, in other universities of the region and
        all universities of the region, from 2012 to 2020`,
	},
	overTimeGrad: {
		description: `The graduation ratio of the given gendeer and ethnicity, in other universities of the region and
        all universities of the region, from 2012 to 2020`,
    },
};