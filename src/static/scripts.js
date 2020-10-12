function Post(self, url){
    var row = self.parentElement.parentElement;
    console.log(row.childElementCount);
    row.childNodes[1].childNodes[0].innerText = "IT WORKED!";
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            console.log(this.status);
            if(row.childElementCount == 3){row.childNodes[1].childNodes[0].innerText = this.responseText;}
        }
    }
    xhttp.open("POST", url, true);
    xhttp.send();
}

function GetStatus(url){
    var xhttp = new XMLHttpRequest();
    
    // xhttp.open("GET", url, false);
    // xhttp.send();
    // var data = JSON.parse(xhttp.responseText);
    
    // return xhttp.responseText;
    var data = {
        "state":"Idle",
        "system":{
            "name":"My Cool PyKiln",
            "version":"0.1",
            "wifiNetwork":"My awesome WiFi",
            "ip":"127.0.0.1",
            "timezone":"Eastern",
            "uptime":"1:00",
            "connection":"Offline",
            "filespace":"3.0 Mb",
        },
        "electrical":{
            "volts":"120",
            "current":"2.0 amps"
        },
        "temperature":{
            "units":"Fahrenheit",
            "sensor1":"72*F",
            "sensor2":"72*F",
            "sensor3":"72*F",
            "sensor4":"72*F",
        },
        "relays":{
            "contactor":"OK",
            "relay1":"OK",
            "relay2":"OK",
            "relay3":"OK",
            "relay4":"OK",
            "relay5":"OK",
            "relay6":"OK"
        }
    };

    var good = ["OK", "Online"];
    var warning = ["Delayed"];
    var bad = ["Not Connected", "Offline"];

    Object.keys(data).forEach(sectionName => {
        // Update the State table
        if(sectionName == "state"){
            document.getElementById("state").innerText = data["state"];
            if(data["state"] == "Idle"){
                // Enable test buttons if the kiln isn't running
                var testButtons = document.getElementsByClassName("t-btn");
                for(var b = 0; b < testButtons.length; b++){
                    console.log(testButtons[b]);
                    testButtons[b].disabled = false;
                }
            }
            return;
        }

        // Get Section and Add Table Header
        var section = document.getElementById(sectionName);
        var threeColumn = sectionName == "relays" ? "<td></td>" : "";
        var html = "<tr><td>" + sectionName[0].toUpperCase() + sectionName.slice(1) + "</td><td></td>" + threeColumn + "</tr>";

        for(var i = 0; i < Object.keys(data[sectionName]).length; i++){
            // insert row label into table
            var key = Object.keys(data[sectionName])[i];
            // Format the label
            var keyLabel = ""; 
            for(var p = 0; p < key.length; p++){
                if(key[p] == key[p].toUpperCase()){keyLabel += " ";}
                if(p == 0){keyLabel += key[p].toUpperCase();}
                else{keyLabel += key[p];}
                if(p == key.length - 1){keyLabel += ":";}
            }
            // insert value into table
            var value = data[sectionName][Object.keys(data[sectionName])[i]];
            // Format certain keywords
            if(good.indexOf(value) != -1){value = '<span class="state">' + value + '</span>';}
            if(warning.indexOf(value) != -1){value = '<span class="state bad">' + value + '</span>';}
            if(bad.indexOf(value) != -1){value = '<span class="state bad">' + value + '</span>';}

            var relayHtml = "";
            if(sectionName == "relays"){relayHtml = "<td><button onclick=\"Post(this, '/api/relay" + i + "')\" class=\"btn\">Test</button></td>";}
            //relayHtml = '<td><button onclick="' + "Post(this, '/api/relay" + i + "')" + '" class="btn">Test</button></td>';}
            
            html += "<tr><td>" + keyLabel + "</td><td>" + value + "</td>" + relayHtml + "</tr>";
        }

        if(sectionName == "system"){html += "<tr><td></td><td><button onclick=\"Post(this, '/api/reboot')\" class=\"btn\">Reboot</button></td></tr>";}
        else if(sectionName == "electrical"){html += "<tr><td></td><td><button onclick=\"Post(this, '/api/temperature')\" class=\"btn\">Update</button></td></tr>";}
        else if(sectionName == "temperature"){html += "<tr><td></td><td><button onclick=\"Post(this, '/api/temperature')\" class=\"btn\">Update All</button></td></tr>";}

        section.innerHTML = html;
    });
}

var wifi;
var password;
var host;
var configBtn;

function ConfigurePage(){
    configBtn = document.getElementById("configBtn");
    wifi = document.getElementById("wifi");
    password = document.getElementById("password");
    host = document.getElementById("host");
    setInterval(CheckConfiguration, 0.5 * 1000);
}

function CheckConfiguration(){
    configBtn.disabled = wifi.value.length == 0;
}

function ConfigureWifi(){
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '/api/configure', true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.onload = function () {
        if (xhr.status >= 200 && xhr.status < 300) {
            document.getElementById("wifi-form").className = "d-none";
            document.getElementById("wifi-connect").className = "content";
            setTimeout(function(){ ipChecker = setInterval(CheckIP, 5000)}, 10000);
        }
    };
    xhr.send('wifi=' + wifi.value + '&password=' + password.value + '&host=' + host.value);
}

var ipChecker;
function CheckIP(){
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            var ipData = JSON.parse(this.responseText);
            console.log(ipData);
            if(ipData.ip != ""){
                document.getElementById("wifi-connect").className = "d-none";
                document.getElementById("wifi-complete").className = "content tcenter";
                document.getElementById("new-ip").innerText = ipData.ip;
                document.getElementById("new-ip").href = "http://" + ipData.ip;
                clearInterval(ipChecker);
            }
        }
    };
    xmlhttp.open("GET", "/api/ip", true);
    xmlhttp.send();
}