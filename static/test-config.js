

function addTestConfigInUi(element){
    $("#toAddConfig").after(
        "<tr index="+element.id+"><td name='key'>"+element.key+"</td><td name='value'>"+element.value+"</td><td><input type='button' value='删除' name='removeConfig'/><input type='button' value='编辑' name='editConfig'/></td></tr>"
    ); 
}

function bindRemoveConfigEvent(){
    $("input[name='removeConfig']").each(function(e){
        $(this).unbind();
        $(this).click(function(e){
            var tr = $(this).parent().parent()
            var index = $(tr).attr("index")
            $.ajax({
                url: '/test-config',
                data:{"id":index},
                type: 'DELETE',
                dataType:"JSON",
                success: function( response ) {
                    tr.hide()
                }   
             });
           
        });
    });

    // Edit action 
    $("input[name=editConfig]").each(function(e){
        $(this).click(function(e){
            tr = $(this).parent().parent()
            keyTd = $(tr).children("tr td[name=key]")
            index = $(tr).attr("index")
            key =$(tr).children("tr td[name=key]").text()
            value = $(tr).children("tr td[name=value]").text()
            // $(tr).children("tr td[name=key]").outerHtml()
            $(this).unbind()
            $(this).attr("name","saveConfig")
            $(this).val("保存")

            keyInput  = "<input name='inputKey' value='"+key+"' />"
            $(keyTd).text("")
            $(keyTd).html(keyInput)
            // console.log(index)
            // console.log(key)
            // console.log(value)
        });
    });
}
function initConfig() {
    $.getJSON("/test-config",
        function (data, textStatus, jqXHR) {
            data.forEach(element => {
                addTestConfigInUi(element);            
            });

          bindRemoveConfigEvent()
                    
        }
    );
}