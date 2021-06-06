import {app, getParameterByName} from './pykiln.js';

//list of default IP addresses for common routers
//used for scanning for PyKiln on local network
import router from './router.js';

//Scan common router IP addresses to find local network
var scanIndex = 0;
var goodIPs = [];

export function FindNetworkIP(){

    //use this as a starting point
    // var urlData = getParameterByName("devices");
    // var decodedData = decodeURIComponent(urlData);
    // var jsonObject = JSON.parse(decodedData);
    // console.log(jsonObject );

    //Used to scan for PyKilns on local network
    //Parses device IP and subnet mask in CIDR format 
    //from the computer running the python setup utility 
    let devices = getParameterByName('devices');
    if(devices != undefined){
        //devices = "";
        console.log(devices);
        let devicesParsed = devices.toString().split(",");
        for(let i = 0; i < devicesParsed.length; i++){
            // let device = {};
            // device.ip = devicesParsed.toString().split("/")[0];
            // device.subnet = devicesParsed.toString().split("/")[1];
            // this.scan.devices.push(device);
            let deviceIP = devicesParsed.toString().split("/")[0];
            // if(deviceIP != ""){
            app.scan.devices.push(deviceIP);
            // }
            
        }
    }
    

    scanIndex = 0;
    goodIPs = [];
    if(app.scan.devices.length > 0){
        CheckRouterIP(app.scan.devices);
    }
    else{
        CheckRouterIP(router.router);
    }
}

function CheckRouterIP(routers){

    app.scan.title = "Finding Router IP:";
    
    console.log("SCANNING! " + scanIndex);
    console.log(routers.length);
    if(scanIndex >=  routers.length || app.page != "scanning"){
        console.log("SCAN COMPLETE!");
        console.log(goodIPs);
        scanPyKilnIndex = 0;
        pyKilnIP = [];
        CheckPyKilnIP();
        return;
    }

    app.scan.ip = routers[scanIndex];
    app.scan.progress = scanIndex / parseFloat(routers.length);


    //Short timeout to speed things up
    axios.get('http://' + routers[scanIndex], {timeout:150})
    .then((response) => {
        console.log(response.data);
        console.log('good2 ' + routers[scanIndex]);
        goodIPs.push(routers[scanIndex]);
        scanIndex++;
        CheckRouterIP(routers);
    })
    .catch((error) => {
        if (error.code === 'ECONNABORTED'){
            console.log('timeout ' + routers[scanIndex]);
        } else {
            console.log(error);
            console.log('good ' + routers[scanIndex]);
            goodIPs.push(routers[scanIndex]);
        }
        scanIndex++;
        CheckRouterIP(routers);
    }); 

}


var scanPyKilnIndex = 0;
var pyKilnIP = [];

function CheckPyKilnIP(){

    app.scan.title = "Finding PyKiln IP:";

    let baseIP = goodIPs[1].substring(0, goodIPs[1].lastIndexOf('.')) + ".";
    
    console.log("SCANNING! " + baseIP + scanPyKilnIndex);
    if(scanPyKilnIndex >=  255 || app.page != "scanning"){
        console.log("SCAN COMPLETE!");
        console.log(pyKilnIP);
        app.page = "results";
        return;
    }

    app.scan.ip = baseIP + scanPyKilnIndex;
    app.scan.progress = scanPyKilnIndex / 255.0;
    
    //Short timeout to speed things up
    axios.get('http://' + baseIP + scanPyKilnIndex + "/index.html", {
        timeout:200, 
        crossDomain: true,
        withCredentials: true
    })
    .then((response) => {
        console.log(response.data);
        console.log('good2 ' + baseIP + scanPyKilnIndex);
        pyKilnIP.push(baseIP + scanPyKilnIndex);
        app.scan.results = pyKilnIP;
        scanPyKilnIndex++
        CheckPyKilnIP();
    })
    .catch((error) => {
        scanPyKilnIndex++
        CheckPyKilnIP();
    });  

}