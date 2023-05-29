interface ICardContent {
    [key: string]: { title: string; description: string };
}

export const metricsCardContent: ICardContent = {
    cb: {
        title: "Class Imbalance",
        description: `Class imbalance (CI) is used to see how well balanced the dataset is as a whole. We
		take the ratios of the specific races from enrollment data and then take the ratios
		from the graduation data, and then run it through the following function:  
		&nbsp;  
		$$CI = (n_a - n_d)/(n_a + n_d)$$    
		$n_a$ = enrollment ratio  
		$n_d$ = graduation ratio  
		&nbsp;  
		Returns a number from [-1, 1]; The further away the number is from 0 (either on the positive or 
		negative side), the more biased/imbalanced the data is.`,
    },
    ks: {
        title: "Kolmogorov-Smirnov metric",
        description: `The Kolmogorov-Smirnov (KS) metric is very similar to KL since it deals with divergence in the dataset.
		It looks for the max divergence within the enrollment data and graduation data
		in terms of a certain race and gender. The ratios of that certain race and gender from enrollment
		data and graduation data are put in this function:  
		&nbsp;  
		$$KS = max(|Pa - Pd|)$$  
		$P_a$ = enrollment data ratio  
		$P_d$ = graduation data ratio  
		&nbsp;  
		The range of LP values are [0, 1], where:  
		- Values near zero indicate the labels were evenly distributed between facets in all outcome categories.  
		- Values near one indicate the labels for one outcome is very divergent.
		`,
    },
    dpl: {
        title: "Label Imbalance",
        description: `Label Imbalance (DPL) is used to analyze the selected race and gender by getting the ratio
		of number of students admitted from the enrollment data and the corresponding race and gender
		ratio from graduation data to see number of students that graduated. We run the ratios 
		through this function:  
		&nbsp;  
		$$DPL = (q_a - q_d)$$   
		$q_a$ = ratio of students from enrollment data  
		$q_d$ = ratio of students from graduation data  
		&nbsp;  
		- Positive DPL values indicate that facet $a$ is has a higher proportion of positive outcomes when compared with facet $d$.  
		- Values of DPL near zero indicate a more equal proportion of positive outcomes between facets and a value of zero indicates perfect demographic parity.  
		- Negative DPL values indicate that facet $d$ has a higher proportion of positive outcomes when compared with facet $a$.`,
    },
    kl: {
        title: "Kullback-Leibler divergence",
        description: `The Kullback-Leibler divergence (KL) measures how much the enrollment ratio of the selected race and gender
		diverges from the graduation ratio of the race and gender. It helps us see if the ratios will stay pretty consistent
		or change significantly if we collect more enrollment and graduation data. We get the enrollment ratio of race and gender and 
		graduation rate of race and gender and run it through this function:  
		&nbsp;  
		$$KL(Pa || Pd) = ∑yP_a(y)*log[P_a(y)/P_d(y)]$$  
		$P_a$ = enrollment ratio  
		$P_d$ = graduation ratio  
		&nbsp;  
		- Range of values for the KL metric is [0, +∞).  
		- Values near zero mean the outcomes are similarly distributed for the different facets.  
		- Positive values mean the label distributions diverge, the more positive the larger the divergence.`,
    },
    tvd: {
        title: "Total Variation Distance",
        description: `Total Variation Distance (TVD) indicates the largest possible difference between the data
		distribution of enrollment versus graduation in regards to the selected race and gender. It is similar to using L1
		norm to decide the minimum number of substitutions required to change one string into another when
		comparing to binary strings. In the bias detection context, TVD quantifies how many outcomes in facet $a$ would have to be changed to match the outcomes in facet $d$.  
		&nbsp;  
		$$TVD =  ½*|na - nd|$$  
		$n_a$ = enrollment data ratio  
		$n_d$ = graduation data ratio  
		&nbsp;  
		- The range of TVD values is [0, 1)  
		- Values near zero mean the labels are similarly distributed.  
		- Positive values mean the label distributions diverge, the more positive the larger the divergence.
		`,
    },
};
