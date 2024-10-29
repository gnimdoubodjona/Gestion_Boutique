const barCanvas=document.getElementById("barCanvas");

const barChart=new CharacterData(barCanvas,{
    type:"bar",
    data:{
        labels:["beee","tokuo"],
        datasets:[
            {
                data:[134,14555,456]
            }
        ]
    }
})