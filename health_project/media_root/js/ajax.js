console.log('loaded script.js');

$(document).ready(function(){

$("#id_search_text").keyup(function(){
$("#search_results").html("");
var input = $("#id_search_text").val()
if(input){

$.ajax({
type:"POST",
url:"/disease/search/",
data:{
'search_text':input,
'csrfmiddlewaretoken':$("input[name=csrfmiddlewaretoken]").val()
},
  success:searchSuccess,
  dataType:'html'
});
}
});
});
function searchSuccess(data, textStatus,jqXHR)
{
$("#search_results").html(data);
}
