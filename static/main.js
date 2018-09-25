
$(document).ready(function () {
    $("#logTextArea").html("")
     setInterval('retrieveLog()',1000);

    $("#runAuto").click(function(e){
        $("#logTextArea").html("Start testing")
        $.get("/run",
            function (data, textStatus, jqXHR) {
                // $("#logTextArea").text("Start testing")
                console.log(data)
            }
        );
    });

    


    // Actions:
    $.get("/get-defined-actions",
        function (data, textStatus, jqXHR) {
            data.result.forEach(value => {
                $("#toAddCase td select[name='action']").append("<option value='"+value+"'>"+value+"</option>")             
            });
           
        }
    );
    $.get("/get-object-names",
    function (data, textStatus, jqXHR) {
        data.result.forEach(value => {
            $("#toAddCase td select[name='name']").append("<option value='"+value+"'>"+value+"</option>")             
        });
       
    }
);
    


    // Init test case 
    initTestCase();
    $("#toAddCase td input[name='test_case_name']").val('默认');
    $("#addCase").click(function(e) {
        var caseNameElement = $($($(this).parent().parent().children()[0]).children()[0]);
        var nameElement = $($($(this).parent().parent().children()[1]).children()[0]);
        var actionElement = $($($(this).parent().parent().children()[2]).children()[0]);
        var argsElement = $($($(this).parent().parent().children()[3]).children()[0]);
        var caseName = caseNameElement.val()
        var name = nameElement.val()
        var action = actionElement.val()
        var args = argsElement.val()
        if(caseName=="" || name == "" || action == "" || args == ""){
            console.log("Please input test case name, name , action and args")
            return;
        }
        // valueElement.val("")
        // nameElement.val("");
        var data = {"test_case_name":caseName,"name":name,"action":action,"args":args}
        $.post("/test-case", data,
        function (data, textStatus, jqXHR) {
            addTestCaseInUi(data);
            bindRemoveCaseEvent();
            },
            "json"
        );
    });

    // Init Config
    initConfig();

    $("#addConfig").click(function(e) { 
        var nameElement = $($($(this).parent().parent().children()[0]).children()[0]);
        var valueElement = $($($(this).parent().parent().children()[1]).children()[0]);
        var value = valueElement.val()
        var name = nameElement.val()
        if(name=="" || value == ""){
            console.log("Please input key and value")
            return;
        }
        // valueElement.val("")
        // nameElement.val("");
        var data = {"key":name,"value":value}
        $.post("/test-config", data,
        function (data, textStatus, jqXHR) {
            addTestConfigInUi(data);
            bindRemoveConfigEvent();
            },
            "json"
        );
    });

    // Init Objects
    initObject();
    $("#toAddObject td input[name='page']").val('ALL');
    $("#addObject").click(function(e) {
        var pageElement = $($($(this).parent().parent().children()[0]).children()[0]);
        var nameElement = $($($(this).parent().parent().children()[1]).children()[0]);
        var valueElement = $($($(this).parent().parent().children()[2]).children()[0]);
        var page = pageElement.val()
        var value = valueElement.val()
        var name = nameElement.val()
        if(name=="" || value == "" || page == ""){
            console.log("Please input page, name and value")
            return;
        }
        // valueElement.val("")
        // nameElement.val("");
        var data = {"page":page,"name":name,"value":value}
        $.post("/test-object", data,
        function (data, textStatus, jqXHR) {
            addTestObjectInUi(data);
            bindRemoveObjectEvent();
            },
            "json"
        );
    });
});

function retrieveLog(){
    $.get("/log", 
        function (data, textStatus, jqXHR) {
            // $("#logTextArea").html("")
            if(data.log!=""){
                console.log("log return {"+data.log+"}")
                $("#logTextArea").text(data.log)
            }else{
                console.log("No log return")
            }
           
        }
    );
}

function genInput(element){
    value = $(element).text()
    name =  $(element).attr("name")
    return "<input name='"+name+"'>"+value+"</input>"
}