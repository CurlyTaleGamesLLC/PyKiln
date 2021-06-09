//ChartJS library to display line graphs segments for firing schedules
import { SetData, Init } from './charts.js';
import {FindNetworkIP} from './pykiln-scan.js';



const message = [
    "vue.draggable",
    "draggable",
    "component",
    "for",
    "vue.js 2.0",
    "based",
    "on",
    "Sortablejs"
];

export var app = new Vue({
    el: '#app',
    components: {
        draggable: window['vuedraggable']
    },
    data: {

        // list: [],

        //segment sorting
        sort: '',
        isDragging: '',
        // id: 2,
        drag: '',

        //selected schedule
        schedule:{
            name:"",
            id:"",
            segments:[],
            notes: "",
        },

        lastSchedule:{
            name:"",
            id:"",
            segments:[],
            notes: "",
        },

        //current state of PyKiln
        state:{
            status: "idle",
            schedule:{
                name:"test firing",
                id:"1234",
                progress: 0.5
            },
            temp: [1,2,3],
            units:"fahrenheit"
        },

        //list of all schedules on PyKiln
        schedules:[
            {name:"abc", id:"123"},
            {name:"def", id:"456"},
            {name:"hij", id:"789"}
        ],

        page:"settings",
        ip:"",
        isEditing: false,

        //Used to scan and recover IP of PyKiln
        scan:{
            title:"",
            ip:"",
            progress: 0.0,
            results:[],
            devices:[]
        },

        //settings for PyKiln
        settings:{
            kiln:{
                units: "fahrenheit",
                volts: 120,
                cost: 0.14,
                zoneCount:2,
                zones:[1,2,3],
                sensorCount: 3,
                sensors:[4,5,6],
                sensorType:"k",
            },
            notifications:{
                email:"test@test.com",
                emailValid: false,
                news: true,
                analytics: true,
                audio: true
            },
            alarms:{
                max: 2500,
                maxEnable: false,
                above: 50,
                aboveEnable: false,
                below: 30,
                belowEnable: true
            }
           
        }

    },
    methods: {
        removeAt(index) {
            this.schedule.segments.splice(index, 1);
            //this.updateGraph();
        },
        add: function() {
            let newSegment = { rate: 100, target: 200, hold: 30, uuid: uuidv4()};
            //copy the values of the last segment
            if(this.schedule.segments.length > 0){
                let index = this.schedule.segments.length - 1
                newSegment.rate = this.schedule.segments[index].rate;
                newSegment.target = this.schedule.segments[index].target;
                newSegment.hold = this.schedule.segments[index].hold;
            }
            this.schedule.segments.push(newSegment);
            //this.updateGraph();
        },
        updateGraph: function() {
            console.log("UPDATE!");
            SetData(this.schedule.segments);
        },
        test: function() {
            console.log("THIS IS A TEST!");
        },
        startFiring: function(){
            console.log("Start Firing");
            $('#start-confirm-modal').modal("hide");
            this.state.status = "firing";

            // axios.post('http://' + this.ip + "/start", {id: this.schedule.id})
            // .then(function (response) {
            //     console.log(response);
            //     $('#start-confirm-modal').modal("hide");
            // });
        },
        stopFiring: function(){
            console.log("Stop Firing");
            $('#stop-confirm-modal').modal("hide");
            this.state.status = "idle";

            // axios.post('http://' + this.ip + "/stop")
            // .then(function (response) {
            //     console.log(response);
            //     $('#stop-confirm-modal').modal("hide");
            // });

        },
        conesModal: function(){
            console.log("Close Modal");
            $('#cone-chart-modal').modal("hide");
        },
        browsePage: function(newPage){
            if(this.unsavedChanges){
                console.log("ARE YOU SURE?");
                //add parameter to modal that behaves like a return URL
                
            }
            else{
                this.page = newPage;
            }
        },
        backToListModal: function(){
            this.backToList(true);
        },
        backToList: function(isModal){
            if(this.unsavedChanges && !isModal){
                $("#unsaved-confirm-modal").modal("show");
            }
            else{
                $("#unsaved-confirm-modal").modal("hide");
                this.isEditing = false; 
                this.schedule.id = '';
            }
        },
        connect: function(newIP){
            this.ip = newIP;
            this.page = "home";
        },
        startScan: function() {
                this.page = "scanning";
                this.scan.results = [];
                FindNetworkIP(this);
        },
        loadSchedule: function(scheduleID){
            this.isEditing = false;
            this.schedule.id = scheduleID;
            this.lastSchedule = JSON.parse(JSON.stringify(this.schedule));
            console.log("schedule loaded! " + scheduleID);
        },
        saveSchedule: function(){
            setTimeout(() => { 
                this.isEditing = false;
                console.log("schedule saved!"); 
            }, 100);
            this.lastSchedule = JSON.parse(JSON.stringify(this.schedule));
        },
        newSchedule: function(){
            let newSegment = { rate: 100, target: 200, hold: 30, uuid: uuidv4()};
            let blankSchedule = {
                name: "New Schedule",
                id:"",
                segments:[newSegment],
                notes:""
            };
            this.importSchedule(blankSchedule);
        },
        exportSchedule: function(){
            console.log("Export Schedule");
            DownloadSchedule(this.schedule);
        },
        importSchedule: function(importedSchedule){
            console.log("Import Schedule");
            this.schedule = importedSchedule;
            this.schedule.id = uuidv4();
            this.lastSchedule = JSON.parse(JSON.stringify(this.schedule));
            this.isEditing = true;
        },
        deleteSchedule: function(){
            console.log("Delete Schedule");
            $('#delete-confirm-modal').modal("hide");
            
            //remove schedule from list of schedules
            var removeIndex = this.schedules.map(function(item) { return item.id; }).indexOf(this.schedule.id);
            this.schedules.splice(removeIndex, 1);

            this.schedule.id = "";
            // this.page = "home";

            // axios.delete('http://' + this.ip + "/schedule/" + this.schedule.id)
            // .then(function (response) {
            //     console.log(response);
            //     $('#delete-confirm-modal').modal("hide");
            // });
        },
        updatekiln: function(newSettings){
            this.settings.kiln = newSettings;
        },
        updatenotifications: function(newSettings){
            this.settings.notifications = newSettings;
        },
        updatealarms: function(newSettings){
            this.settings.alarms = newSettings;
        }
    },
    mounted() {
        
        //get IP of PyKiln from URL Parameter
        let ip = getParameterByName('ip');
        if(ip == undefined){ip = "";}
        console.log(ip);
        this.ip = ip;

        //Only track annoymous data if they have opted in
        if(this.settings.notifications.analytics){
            LoadGTM();
        }
    },
    computed: {
        dragOptions() {
            return {
                animation: 0,
                group: "description",
                disabled: false,
                ghostClass: "ghost"
            };
        },
        draggingInfo() {
            return this.dragging ? "under drag" : "";
        },
        degrees: function () {
            let degreeText = "°";
            let unitText = this.settings.kiln.units == "fahrenheit" ? "F" : "C";
            if(this.state.status == "firing"){
                unitText = this.state.units == "fahrenheit" ? "F" : "C";
            }
            return degreeText + unitText;
        },
        unsavedChanges(){
            return JSON.stringify(this.lastSchedule) != JSON.stringify(this.schedule);
        }
    },
    watch: {
        'schedule.id': function (val) {
            if(val != ""){
                this.$nextTick(() => {
                    Init(this.page == 'logs');
                });
            }
        },
        page: function(val){
            PageView();
        },
        'state.status': function(val){
            if(val != "firing"){
                SetFavicon("./img/favicon/");
                // this.$nextTick(() => {
                //     Init(this.page == 'logs');
                // });
            }
            else{
                SetFavicon("./img/favicon-active/");
            }
        },
        'schedule.segments': function(){
            console.log("Schedule Changed, Update Graph");
            SetData(this.schedule.segments);
        }
      }
});

function SetFavicon(path){
    let favicons = document.getElementsByClassName("favicon");
    for(let i = 0; i < favicons.length; i++){
        let hrefURL = favicons[i].href.split("/");
        favicons[i].href= path + hrefURL[hrefURL.length - 1];
    }
}

export function getParameterByName(name, url = window.location.href) {
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

function LoadGTM(){
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-193021525-1');
}

function PageView(){
    // console.log(app.page);
    if (window.ga){
        window.ga.getAll()[0].set('page', "/" + app.page);
        window.ga.getAll()[0].send('pageview')
    }
}

function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

function DownloadSchedule(fileData) {
    const content = JSON.stringify(fileData);
    const a = document.createElement("a");
    const file = new Blob([content], { type: "text/plain"});
    a.href = URL.createObjectURL(file);
    let fileName = fileData.name;
    if(fileName == ""){
        fileName = "Untitled Firing Schedule";
    }
    a.download = fileName + ".json";
    a.click();
}
