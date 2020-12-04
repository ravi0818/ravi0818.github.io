//----------------class-----------------//

$("#buttons>div").addClass("col-lg-2 col-md-4 col-sm-4");

$("#obj>div").addClass("col-lg-4 col-md-6 col-sm-6");

$("#obj>div>img").addClass("img-thumbnail image");



//-----------------text--------------------//
$("title").text("SuperDeals");




//-----------------function-----------------//
$(".image").click(function(){
	window.open($(this).attr("src"), "_self");
});

//$(document).ready(function(){   
//   $("#buttons").load("../snippet/buttons.html");
//});


/*$("button").click(function(){
	localStorage.setItem("text",$(this).text());
	let x=$(this).text()
	y=x+".html"
	window.open(y, "_self");
});*/

$( document ).ready(function(){
	if($("h1").text()!=="Home"){
		$("h1").text(localStorage.getItem("text"));
	}
});

//----------------------load-------------------------
$(function(){
  $("#logo").load("Snippets/logo.html"); 
});
$(function(){
  $("#list").load("Snippets/list.html"); 
});
$(function(){
  $("#FDOD").load("FetchData/Flipkart/FDOD.txt"); 
});
$(function(){
  $("#FBSOTW").load("FetchData/Flipkart/FBSOTW.txt"); 
});
$(function(){
  $("#ATDH").load("FetchData/Amazon/amzTDH.txt"); 
});
$(function(){
	$(".data1").load("FetchData/Amazon/amzBE.txt"); 
});
$(function(){
	$(".data2").load("FetchData/Amazon/amzBCA.txt"); 
});
$(function(){
	$(".data3").load("FetchData/Amazon/amzBH.txt"); 
});
$(function(){
	$(".data4").load("FetchData/Amazon/amzBB.txt"); 
});
$(function(){
	$(".data5").load(); 
});
$(function(){
	$(".data6").load(); 
});

function currentTime() {
  var date = new Date(); /* creating object of Date class */
  var hour = date.getHours();
  var min = date.getMinutes();
  var sec = date.getSeconds();
  hour = updateTime(hour);
  min = updateTime(min);
  sec = updateTime(sec);
  $("#clock").text(hour + " : " + min + " : " + sec); /* adding time to the div */
  var t = setTimeout(function(){ currentTime() }, 1000); /* setting timer */
}

function updateTime(k) {
  if (k < 10) {
    return "0" + k;
  }
  else {
    return k;
  }
}

currentTime(); /* calling currentTime() function to initiate the process */
// $(function(){
// 	$(".data").load("data.txt"); 
// });

// $(function(){
// 	$("#1").load("data1.txt"); 
// });
/*
function arrayToTable(tableData) {
        var table = $('<table></table>');
        $(tableData).each(function (i, rowData) {
            var row = $('<tr></tr>');
            $(rowData).each(function (j, cellData) {
                row.append($('<td>'+cellData+'</td>'));
            });
            table.append(row);
        });
        return table;
    }

    $.ajax({
        type: "GET",
        url: "C:\\Users\\rkpra\\Documents\\GitHub\\Web\\products.csv",
        success: function (data) {
            $('body').append(arrayToTable(Papa.parse(data).data));
        }
    });
    */