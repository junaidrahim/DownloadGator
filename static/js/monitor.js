function parse_and_fill(data){
   
}


function getMonitoringData(){
    $.ajax({
        type:"GET",
        url:"/api/monitor", //call the api every 5 sec to fetch the data and 
        success:function(data){
            parse_and_fill(data); //update the html
            setTimeout(function(){getMonitoringData();},5000);
        }
    });
}

getMonitoringData();
