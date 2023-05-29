import create from "zustand";

interface IStore {
    metrics: object;
    setMetrics: (metrics: object) => void;

    enrollOverTimeData: Array<object>;
    setEnrollOverTime: (enrollOverTimeData: Array<object>) => void;

    gradOverTimeData: Array<object>;
    setGradOverTime: (gradOverTimeData: Array<object>) => void;

    enrollCurrentData: object;
    setEnrollCurrent: (enrollCurrentData: object) => void;

    gradCurrentData: object;
    setGradCurrent: (gradCurrentData: object) => void;

    gender: string;
    setGender: (gender: string) => void;

    ethnicity: string;
    setEthnicity: (ethnicity:string) => void;
}

const useMetricsStore = create<IStore>((set) => ({
    metrics: {},
    setMetrics: (metrics: object) =>
        set((state) => ({
            ...state,
            metrics,
        })),
    enrollOverTimeData: [],
    setEnrollOverTime: (enrollOverTimeData: Array<object>) =>
        set((state) => ({
            ...state,
            enrollOverTimeData,
        })),
    gradOverTimeData: [],
    setGradOverTime: (gradOverTimeData: Array<object>) =>
        set((state) => ({
            ...state,
            gradOverTimeData,
        })),
    enrollCurrentData: {},
    setEnrollCurrent: (enrollCurrentData: object) =>
        set((state) => ({
            ...state,
            enrollCurrentData,
        })),
    gradCurrentData: {},
    setGradCurrent: (gradCurrentData: object) =>
        set((state) => ({
            ...state,
            gradCurrentData,
        })),

        gender: "",
        setGender: (gender:string) => set({gender}),

        ethnicity: "",
        setEthnicity: (ethnicity:string) => set({ethnicity})
}));

export default useMetricsStore;
