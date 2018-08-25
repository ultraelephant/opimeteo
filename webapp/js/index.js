function posttogetvalues(value)
{
 var request = new XMLHttpRequest();
 request.open('POST', 'getvalues.php', true);
 request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8');
 request.onreadystatechange = function()
 {
  if (request.readyState == 4 && request.status == 200)
  {
   document.getElementById('values').innerHTML = request.responseText;
  }
 }
 request.send('getvalue_dbname=' + value);
}

function getselectedvalue (selectid)
{
 var e = document.getElementById(selectid).value;
 return e;
}

var timerId = setInterval(function () {posttogetvalues(getselectedvalue('getvalue_dbname'))}, 10000);
