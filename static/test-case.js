

function addTestCaseInUi(element){
    if(element.args == "[]"){
        element.args = ""
    }
    $("#toAddCase").after(
        "<tr index="+element.id+"><td name='test_case_name'>"+element.test_case_name+"</td><td name='name'>"+element.name+"</td><td name='action'>"+element.action+"</td><td name='args'>"+element.args+"</td><td><input type='button' value='删除' name='removeCase'/><input type='button' value='编辑' name='editCase'/></td><td></td><td></td></tr>"
    ); 
}

function bindRemoveCaseEvent(){
    $("input[name='removeCase']").each(function(e){
        $(this).unbind();
        $(this).click(function(e){
            var tr = $(this).parent().parent()
            var index = $(tr).attr("index")
            $.ajax({
                url: '/test-case',
                type: 'DELETE',
                data:{
                    id:index
                },
                dataType:"JSON",
                success: function( response ) {
                    tr.hide()
                }   
             });
           
        });
    });
}
function initTestCase() {
    $.getJSON("/test-case",
        function (data, textStatus, jqXHR) {
            data.forEach(element => {
                addTestCaseInUi(element);            
            });

          bindRemoveConfigEvent()
                    
        }
    );
}