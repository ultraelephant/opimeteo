$(document).on('change','#getvalue_dbname', function()
{
 var selected = $('#getvalue_dbname option:selected').val();
 $("#values").text(selected);
});
