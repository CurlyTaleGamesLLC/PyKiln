//highlight current page
function HighlightNav(){
  $('.nav-item').each(function () {
    //console.log($(this).attr('href'));
    if ("/" + $(this).attr('href') == window.location.pathname) {
      $(this).addClass("active");
    }
    if ($(this).attr('href') == "index" && window.location.pathname == "/") {
      $(this).addClass("active");
    }
  });
}

//only allow numbers to be entered into field with numbersOnly class
function NumbersOnly(){
  $('.numbersOnly').each(function () {

    var numberText = $(this).text();
    var regex = new RegExp(/[^0-9\.]/g); // expression here
    var isNumber = false;

    $(this).filter(function () {
      isNumber = regex.test(numberText);
      return isNumber;
    });

    if (isNumber) {
      console.log("DIFF " + numberText + " " + isNumber);
      $(this).text(numberText.replace(/[^0-9\.]/g, ''));
    }

    if (parseInt(numberText) > 9999) {
      $(this).text(9999)
    }
  });
}

//deselect input fields when enter is pressed
$(document).on('keypress',function(e) {
  if(e.which == 13) {
      $(':focus').blur()
  }
});

$(document).ready(function () {
  HighlightNav();

  //Filter Numbers Only
  setInterval(function () {NumbersOnly()}, 333);
});


//converts fahrenheit to celsius
function f2c(value){
  return (value - 32) * 5 / 9;
}

function CelsiusConeChart(){
  console.log("rows?");
  var index = 0;

  $('.cone-row').each(function() {
    if(index > 0){
      var newHtml = $(this).html();

      var newTemp = $(this).find("td").eq(3).text().replace("°F", "");
      newTemp = f2c(parseInt(newTemp));

      newHtml += AddTD(newTemp.toFixed(0) + "°C");
      console.log(newHtml);
      
      $(this).html(newHtml);
    }
    index++;
  });
}


function ScrapeTable(){
  var newHtml = "";
  var index = 0;
  $('#cone-table tr').each(function() {
    
    if(index < 36){
      newHtml += '<tr>'; 
      newHtml += AddTD($(this).find("td").eq(0).text());
      newHtml += AddTD($(this).find("td").eq(1).text());
      newHtml += AddTD($(this).find("td").eq(2).text());
      newHtml += AddTD($(this).find("td").eq(3).text());
      index++;
      newHtml += '</tr>';
    }
     
  });
  return newHtml;
}

function AddTD(cellData){
  return '<td>' + cellData + '</td>';
}