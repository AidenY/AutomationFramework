


function addTestObjectInUi(element){
    $("#toAddObject").after(
        "<tr index="+element.id+"><td name='page'>"+element.page+"</td><td name='name'>"+element.name+"</td><td name='value'>"+element.value+"</td><td><input type='button' value='删除' name='removeObject'/><input type='button' value='编辑' name='editObject'/></td></tr>"
    ); 
}

function bindRemoveObjectEvent(){
    $("input[name='removeObject']").each(function(e){
        $(this).unbind();
        $(this).click(function(e){
            var tr = $(this).parent().parent()
            var index = $(tr).attr("index")
            $.ajax({
                url: '/test-object',
                data:{"id":index},
                type: 'DELETE',
                dataType:"JSON",
                success: function( response ) {
                    tr.hide()
                }   
             });
           
        });
    });
}
function initObject() {
    $.getJSON("/test-object",
        function (data, textStatus, jqXHR) {
            data.forEach(element => {
                addTestObjectInUi(element);
            });

          bindRemoveConfigEvent()
                    
        }
    );
}