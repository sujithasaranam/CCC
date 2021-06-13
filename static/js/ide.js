let editor;

window.onload = function() {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/c_cpp");
       var textarea = $('#code');
       editor.getSession().on('change', function () {
       textarea.val(editor.getSession().getValue());
   });
}


function changeLanguage() {

    let language = $("#languages").val();

    if(language == 'c' || language == 'cpp')editor.session.setMode("ace/mode/c_cpp");
    else if(language == 'php')editor.session.setMode("ace/mode/php");
    else if(language == 'py')editor.session.setMode("ace/mode/python")
    else if(language == 'java')editor.session.setMode("ace/mode/java");
    else if(language == 'node')editor.session.setMode("ace/mode/javascript");
}

/*
$("select").on('change',function(){
    if($(this).find('option:selected').text()=="No")
        $("#btnSubmit").attr('disabled',true)
    else
        $("#btnSubmit").attr('disabled',false)
 });*/