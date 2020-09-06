const $TABLE = $('#table');
const $BTN = $('#export-btn');
const $EXPORT = $('#export');

var editSchedule;
var loadedSchedule;

const newTr = `
<tr class="segment-row hide">
    <td></td>
    <td class="numbersOnly" contenteditable="true">50</td>
    <td class="numbersOnly" contenteditable="true">1000</td>
    <td class="numbersOnly" contenteditable="true">50</td>
    <td class="pt-3-half">
    <span class="table-up mr-2"><a class="badge badge-secondary" href="#!"><i class="fas fa-long-arrow-alt-up" aria-hidden="true"></i></a></span>
    <span class="table-down"><a class="badge badge-secondary" href="#!"><i class="fas fa-long-arrow-alt-down" aria-hidden="true"></i></a></span>
    </td>
    <td>
    <span class="table-remove"><button type="button" class="btn btn-danger btn-rounded btn-sm my-0"><i class="fas fa-trash"></i></button></span>
    </td>
</tr>`;

//Start Firing Schedule
$('#btn-start-schedule').click(function () {
  $.getJSON("api/start-fire?schedulePath=" + loadedSchedule['path'], function (result) {
    console.log(result);
    $('#btn-start-schedule-modal').addClass('d-none');
    $('#btn-stop-schedule-modal').removeClass('d-none');
    $('#home-time-group').removeClass('d-none');
    $('#home-schedule-list').addClass('d-none');
    $('#home-estimates').addClass('d-none');
  });
});

//Stop Firing Schedule
$('#btn-stop-schedule').click(function () {
  $.getJSON("api/stop-fire", function (result) {
    console.log(result);
    $('#btn-stop-schedule-modal').addClass('d-none');
    $('#btn-start-schedule-modal').removeClass('d-none');
    $('#home-time-group').addClass('d-none');
    $('#home-schedule-list').removeClass('d-none');
    $('#home-estimates').removeClass('d-none');
  });
});

//updates time left and progress bar on home page
function UpdateTimer(currentTime, totalTime){
  var percent = currentTime/totalTime;
  $('#home-time-bar').css("width", (percent * 100).toFixed(2) + '%');
  $('#home-time-remaining').text(FormatTime(totalTime - currentTime));
}


$('#btn-add-segment').click(function () {
  const $clone = $TABLE.find('tbody tr').last().clone(true).removeClass('hide table-line');
  if ($TABLE.find('tbody tr').length === 0) {
    $('tbody').append(newTr);
  }
  $TABLE.find('table').append($clone);
});

function ScheduleToJSON(){
  var newSchedule = new Object();
  newSchedule.name = $('#schedule-title').text();
  newSchedule.units = loadedUnits;
  newSchedule.path = editSchedule;
  newSchedule.segments = [];

  var index = 0;

  var saveRate;
  var saveTemp;
  var saveHold;

  $(".segment-row td").each(function () {
    //console.log($(this).html());
    //console.log(index % 6);

    if (index % 6 == 1) {
      saveRate = parseInt($(this).text());
    }
    if (index % 6 == 2) {
      saveTemp = parseInt($(this).text());
    }
    if (index % 6 == 3) {
      saveHold = parseInt($(this).text());
      newSchedule.segments.push({ rate: saveRate, temp: saveTemp, hold: saveHold });
    }
    index++;
  });

  //console.log(newSchedule);
  return newSchedule;
}

$('#btn-save-schedule').click(function () {
  console.log("Schedule Saved");

  $.ajax({
    type: "POST",
    contentType: "application/json; charset=utf-8",
    url: "api/save-schedule",
    data: JSON.stringify(ScheduleToJSON()),
    success: function (data) {
      console.log(data);
      LoadSchedules();

      $('#alert-container').html('<div class="alert alert-warning alert-dismissible mt-1" role="alert" id="alert-save-settings"><strong>Schedule Saved!</strong><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>');

      setTimeout(function () {
        $('#alert-container').html('')
      }, 4000);
    }
  });



});

$('#btn-delete-schedule').click(function () {
  console.log("Schedule Deleted");
  if (editSchedule == null) {return;}

  $.ajax({
    url: 'api/delete-schedule?schedulePath=' + editSchedule,
    type: 'DELETE',
    success: function (result) {
      console.log(result);
      $("#fireScheduleList").val("select-schedule").change();
      $("#fireScheduleList option[value='" + editSchedule + "']").remove();
      $('#schedule-title').text('');
      $('#schedule-body').html('');
      $("#schedule-group").addClass('d-none');
      editSchedule = null;
    }
  });

});

$('#btn-create-schedule').click(function () {
  console.log("Schedule Created");
  $.post("api/create-schedule", function (data) {
    console.log(data);
    console.log(data['filename']);
    var newScheduleOption = '<option value="' + data['filename'] + '">' + 'Untitled Schedule' + '</option>'
    $('#fireScheduleList').html($('#fireScheduleList').html() + newScheduleOption);
    $("#fireScheduleList").val(data['filename']).change();
    //$("#schedule-group").removeClass('d-none');
  });
});

$('#btn-duplicate-schedule').click(function () {
  console.log("Schedule Duplicated");
  if (editSchedule == null) {return;}

  $.post("api/duplicate-schedule", {schedulePath: editSchedule}, function (data) {
    console.log(data);
    console.log(data['filename']);

    var newScheduleOption = '<option value="' + data['filename'] + '">' + data['name'] + '</option>'
    $('#fireScheduleList').html($('#fireScheduleList').html() + newScheduleOption);
    $("#fireScheduleList").val(data['filename']).change();
    //$("#schedule-group").removeClass('d-none');
  });
});

$('#btn-download-schedule').click(function () {
  console.log("Download Schedule");
  var selectedSchedule =  $('select[name="fireScheduleList"]').val();
  if (selectedSchedule != "select-schedule") {
    $.getJSON('api/get-schedule?schedulePath=' + selectedSchedule, function (result) {
      var json = JSON.stringify(result);
      var blob = new Blob([json], {type: "application/json"});
      var url  = URL.createObjectURL(blob);

      var link = document.createElement('a');
      link.setAttribute('href', url);
      link.setAttribute('download', result['name'] + '.json');
      
      var aj = $(link);
      aj.appendTo('body');
      aj[0].click();
      aj.remove();
      
      URL.revokeObjectURL(url);
    });
  }
});

$('#btn-import-schedule').click(function () {
  console.log("Import Schedule");
  $('#import-schedule').click();
});

//auto submits the schedule import upload
$('#import-schedule').on('change', function () {
  $('#importForm').submit();
});


$TABLE.on('click', '.table-remove', function () {
  $(this).parents('tr').detach();
});

$TABLE.on('click', '.table-up', function () {
  const $row = $(this).parents('tr');
  if ($row.index() === 0){return;}
  $row.prev().before($row.get(0));
});

$TABLE.on('click', '.table-down', function () {
  const $row = $(this).parents('tr');
  $row.next().after($row.get(0));
});

// A few jQuery helpers for exporting only
jQuery.fn.pop = [].pop;
jQuery.fn.shift = [].shift;

$BTN.on('click', () => {

  const $rows = $TABLE.find('tr:not(:hidden)');
  const headers = [];
  const data = [];

  // Get the headers (add special header logic here)
  $($rows.shift()).find('th:not(:empty)').each(function () {

    headers.push($(this).text().toLowerCase());
  });

  // Turn all existing rows into a loopable array
  $rows.each(function () {
    const $td = $(this).find('td');
    const h = {};

    // Use the headers from earlier to name our hash keys
    headers.forEach((header, i) => {

      h[header] = $td.eq(i).text();
    });

    data.push(h);
  });

  // Output the result
  $EXPORT.text(JSON.stringify(data));
});

function LoadSettings() {
  $.getJSON("api/load-settings", function (result) {
    console.log(result);
    $('#cost').val(result['cost']);
    $('#max-temp').val(result['max-temp']);
    $('#offset-temp').val(result['offset-temp']);
    $('#volts').val(result['volts']);
    $("#timezone").val(result['notifications']['timezone']);

    var units = (result['units'] == "celsius")
    console.log("units = " + units);

    $('#units-setting').bootstrapToggle(units ? "off" : "on");
    // if (units) {
    //   $("#units-setting").removeAttr('checked');
    // }
    // else {
    //   $("#units-setting").prop("checked", true);
    // }

    var enableEmail = result['notifications']['enable-email'];
    $('#toggle-email').bootstrapToggle(enableEmail ? "on" : "off");
    

    $('#sender').prop('value', result['notifications']['sender']);
    $('#sender-password').prop('value', result['notifications']['sender-password']);
    $('#receiver').prop('value', result['notifications']['receiver']);
  });
}



function LoadSchedules() {
  $.getJSON("api/list-schedules", function (result) {
    console.log(result);
    var dropdownHTML = '<option value="select-schedule" selected>Select Schedule</option>';

    for (var i = 0; i < result['schedules'].length; i++) {
      var optionValue = result['schedules'][i]['path'];
      var optionName = result['schedules'][i]['name'];
      var optionData = '<option value="' + optionValue + '">' + optionName + '</option>'
      console.log(optionName + " " + optionValue);
      dropdownHTML += optionData;
    }

    $('#fireScheduleList').html(dropdownHTML);
  });
}

$('#btn-save-settings').click(function () {
  $.post('./api/update-settings', $('form#form-settings').serialize(), function (data) {
    console.log("POSTED");
    console.log(data);
    //$('.alert').alert()
    $('#alert-container').html('<div class="alert alert-warning alert-dismissible mt-3" role="alert" id="alert-save-settings"><strong>Settings Saved!</strong><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>');

    setTimeout(function () {
      $('#alert-container').html('')
    }, 4000);
    
  },
    'json' // I expect a JSON response
  );
});

var loadedUnits;
$('select[name="fireScheduleList"]').change(function () {
  if ($(this).val() != "select-schedule") {
    console.log("Load " + $(this).val());
    editSchedule = $(this).val();

    //$("#fireScheduleList option[value='select-schedule']").remove();
    $.getJSON("api/get-schedule?schedulePath=" + $(this).val(), function (result) {
      console.log(result);
      console.log("schedule units = " + result['units']);
      loadedSchedule = result;
      loadedUnits = result['units'];
      $('#schedule-title').text(result['name']);
      if(result['units'] == "fahrenheit"){
        $('.degrees').each(function () {$(this).html($(this).html().replace("°C", "°F"))});
      }
      else{
        $('.degrees').each(function () {$(this).html($(this).html().replace("°F", "°C"))});
      }
      
      $('#schedule-body').html('');
      for (i = 0; i < result['segments'].length; i++) {
        var newRate = result['segments'][i]['rate'];
        var newTemp = result['segments'][i]['temp'];
        var newHold = result['segments'][i]['hold'];
        var isEdit = window.location.pathname == "/firing-schedules";
        var newSegment = LoadSegment(newRate, newTemp, newHold, isEdit);
        $('#schedule-body').html($('#schedule-body').html() + newSegment);
      }
      $("#schedule-group").removeClass('d-none');

      //Estimate Time
      UpdateEstimateTime();
      

    });

    

  }
});

function UpdateEstimateTime(){
  console.log("update time estimate");
  if(loadedSchedule == null){
    return;
  }
  console.log("update time estimate2");
  if(window.location.pathname == "/firing-schedules"){
    loadedSchedule = ScheduleToJSON();
  }
  console.log(loadedSchedule);
  var totalLength = 0;

  //assume room temperature
  //editSchedule
  var startTemp = loadedUnits == "fahrenheit" ? 72 : 22.222;
  startTemp = 0;

  for(var i = 0; i < loadedSchedule['segments'].length; i++){
    var tempDifference = Math.abs(loadedSchedule['segments'][i]['temp'] - startTemp)
    var rampTime = (tempDifference/loadedSchedule['segments'][i]['rate']) * 60;
    //console.log("seg + " + rampTime);
		totalLength += rampTime * 60;
		//console.log("hold + " + loadedSchedule['segments'][i]['hold']);
    totalLength += loadedSchedule['segments'][i]['hold'];
    startTemp = loadedSchedule['segments'][i]['temp'];
  }
  //console.log("totalLength = " + totalLength);

  $('#home-time').text(FormatTime(totalLength));
  $('#home-time-summary').text(FormatTime(totalLength));
  return totalLength
}

function LoadSegment(rate, temp, hold, isEdit) {
  var html = '<tr class="segment-row"><td></td><td class="numbersOnly" contenteditable="' + isEdit + '">';
  html += rate;
  html += '</td><td class="numbersOnly" contenteditable="' + isEdit + '">';
  html += temp;
  html += '</td><td class="numbersOnly" contenteditable="' + isEdit + '">'
  html += hold;
  html += '</td>'
  if (isEdit) {
    html += '<td class="pt-3-half"><span class="table-up mr-2"><a class="badge badge-secondary" href="#!"><i class="fas fa-long-arrow-alt-up" aria-hidden="true"></i></a></span><span class="table-down"><a class="badge badge-secondary" href="#!"><i class="fas fa-long-arrow-alt-down" aria-hidden="true"></i></a></span></td><td><span class="table-remove"><button type="button" class="btn btn-danger btn-rounded btn-sm my-0"><i class="fas fa-trash"></i></button></span></td></tr>';
  }

  return html;
}


var currentUnits;
function GetSettings() {
  $.getJSON("api/load-settings", function (result) {
    console.log(result);
    //$('#cost').val(result['cost']);
    //$('#max-temp').val(result['max-temp']);
    var units = (result['units'] == "celsius")
    console.log("units = " + units);
    currentUnits = result['units'];
  });
}

function GetStatus() {
  $.getJSON("api/get-current-status", function (result) {
    console.log(result);

    //display the name of the firing schedule in the nav bar
    if(result['status'] == "firing"){
      $.getJSON("api/get-current-schedule", function (result2) {
        $('.current-schedule').each(function () {$(this).text(" | " + result2['name'])});
      });
    }
    else{
      $('.current-schedule').each(function () {$(this).text("")});
    }

    if(result['status'] == "complete"){
      console.log("COMPLETE");
      //$('#home-time-summary').text();
      $('#home-cost-summary').text("$3.55");      
      $('#home-complete').removeClass("d-none");
      $('#time-cost-estimates').addClass("d-none");
    }
    else if(result['status'] == "error"){
      console.log("ERROR");
      $('#home-error-title').text(" Faulty Relay #1");
      $('#home-error-message').text("The 1st relay is not properly turning off or on. Please turn off power and replace the faulty relay with a new one");
      $('#home-error').removeClass("d-none");
      $('#time-cost-estimates').addClass("d-none");
    }
     
    //$('#status-state').text(result['status']);
    //$('#status-start-time').text(result['start-time']);

    //update currently selected segment on the home page
    if (window.location.pathname == "/" || window.location.pathname == "/index") {
      $.getJSON("api/get-current-segment", function (result2) {
        console.log(result2)
        $('.segment-row').each(function () {
          var isFiring = result['status'] == "firing"
          var isSegmentIndex = $(this).index() == result2['segment']
          if (isFiring && isSegmentIndex) {
            $(this).addClass("current-segment");
            $(this).addClass("text-light");
          }
          else {
            $(this).removeClass("current-segment");
            $(this).removeClass("text-light");
          }
        });
      });
    }

  });

   //update the current temperature inside the kiln in the nav bar
   $.getJSON("api/temperature", function (result) {
     //need to pass units as well with temp
     console.log(result);
    var tempUnits = result['units'] == "celsius" ? "°C" : "°F";
    var tempUnitsText = result['temp'] + tempUnits;
    $('.current-temperature').each(function () {$(this).text(tempUnitsText)});
  });

  //update time remaining
  $.getJSON("api/get-total-time", function (result) {
    console.log("time");
    console.log(result);
    UpdateTimer(result['currentTime'], result['totalTime']);
    //UpdateTimer(result['totalTime']/2, result['totalTime']);
  });
}

function HighlightNav(){
  //highlight current page
  $('.nav-item').each(function () {
    console.log($(this).attr('href'));
    if ("/" + $(this).attr('href') == window.location.pathname) {
      $(this).addClass("active");
    }
    if ($(this).attr('href') == "index" && window.location.pathname == "/") {
      $(this).addClass("active");
    }
  });
}

function NumbersOnly(){
  $('.numbersOnly').each(function () {

    var numberText = $(this).text();

    var regex = new RegExp(/[^0-9\.]/g); // expression here
    var isNumber = false;

    $(this).filter(function () {
      isNumber = regex.test(numberText);
      //console.log("TEST " + $(this).text() + " " + text);
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

//deselect input fields
$(document).on('keypress',function(e) {
  if(e.which == 13) {
      $(':focus').blur()
  }
});

$(document).ready(function () {
  HighlightNav();

  //Filter Numbers Only
  setInterval(function () {NumbersOnly()}, 333);

  GetStatus();
  setInterval(function () { GetStatus() }, 5000);
  
  if(window.location.pathname == "/firing-schedules"){
    setInterval(function () {UpdateEstimateTime()}, 333);
  }
  
});

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

function f2c(value){
  return (value - 32) * 5 / 9;
}

//format time to be hours:mins (2:45)
function FormatTime(value){
  valueMins = value / 60;
  if(valueMins < 0){
    valueMins = 0;
  }
  var hours = Math.floor(valueMins / 60).toString();
  var mins = Math.floor(valueMins % 60).toString();
  if(mins.length < 2){
    mins = "0" + mins;
  }
  return hours + ":" + mins;
}



function GetTotals(){
  $.getJSON("api/load-totals", function (result) {
    console.log(result);

    $('#log-fires').text(result['fires']);
    $('#log-time').text(FormatTime(result['time']));

    var formatCost = "$";
    if(result['cost'] < 1){
      formatCost += "0.";
    }
    if(result['cost'] < .10){
      formatCost += "0";
    }
    formatCost += result['cost'].toString();

    $('#log-cost').text(formatCost);

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