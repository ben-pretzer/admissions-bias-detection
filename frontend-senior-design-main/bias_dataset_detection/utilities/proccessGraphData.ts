export function processCurrentData(data: any){
    return [
        {name:"National Universities", percentage:data.national},
        {name:"Regional Universities", percentage:data.regional},
        {name:" University", percentage:data.university}
    ]
}



