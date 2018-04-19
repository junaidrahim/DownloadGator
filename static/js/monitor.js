function parse_and_fill(data){
    document.getElementById("monitor_container").innerHTML = "";
    for(i=0;i<data.length;i++){
        var text = `
        <div class="card" style="width: 18rem;margin-left: 15px;float:left;margin-bottom:10px;margin-top:10px">
            <div class="card-body">
            <h5 class="card-title">`+ data[i].folder+`</h5>
            <h6 class="card-subtitle mb-2 text-muted">`+ data[i].time+`</h6>
            <p class="card-text">`+ data[i].link +`</p>
            <button class="btn btn-info card-link" data-toggle="modal" data-target="#detailsModal`+i.toString()+`">View</button>

            <div class="modal fade" id="detailsModal`+i.toString()+`" tabindex="-1" role="dialog" aria-labelledby="detailsModalTitle" aria-hidden="true">
                <div class="modal-dialog modal-lg" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="detailsModalTitle">`+ data[i].folder +`</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            <pre>`+ data[i].wget_log+`</pre>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                        </div>
                    </div>
                </div>
            </div>

            </div>
        </div>
        `
        document.getElementById("monitor_container").innerHTML += text;
    }
}


function getMonitoringData(){
    $.ajax({
        type:"GET",
        url:"/api/monitor", //call the api every 5 sec to fetch the data and 
        success:function(data){
            parse_and_fill(data); //update the html
            setTimeout(function(){getMonitoringData();},60000);
        }
    });
}

getMonitoringData();
