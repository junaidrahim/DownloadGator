function post_download(){
    data = {
        "test":"test"
    }
    
    $.post("/test",data,
    (data,status)=>{
        alert(data);
    });
}