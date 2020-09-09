var app = new Vue({
    el: '#app',
    data: {
        system:{
            name:"PyKiln",
            version:"0.2",
            wifiNetwork:"My cool Wifi",
            ip:"127.0.0.1",
            timezone:"eastern",
            uptime:"2:00",
            connection:"online",
            filespace:"2.0MB"
        },
        settings:{
            name:"PyKiln",
            volts:120,
            units:"fahrenheit",
            maxTemp:2500,
            sensors:2,
            sensorAdjustment:[0,0,0,0],
            zones:3,
            zoneAdjustment:[100,100,100,100,100,100],
            cost:0.14,
            email:"example@example.com",
            audio:false,
            timezone:"eastern"
            
        },
        settingsFields:{
            name:{
                name:"Kiln Name",
                icon:"fa-user",
                note:"This name will be used in the navbar on the page as well as in email notifications.",
                type:"text",
                id:6
            },
            volts:{
                name:"Kiln Voltage",
                icon:"fa-bolt",
                note:"Measure your mains voltage, usually 120 or 220 volts for USA/Canada.",
                type:"number",
                step:1,
                id:0
            },
            cost:{
                name:"Cost Per Kilowatt",
                icon:"fa-dollar-sign",
                type:"number",
                step:0.01,
                id:1
            },
            email:{
                name:"Email",
                icon:"fa-at",
                note:"Get email updates when your firing has completed, or if your kiln has any thermal errors.",
                type:"text",
                id:2
            },
            audio:{
                name:"Audio Alerts",
                icon:"fa-volume-up",
                type:"select",
                options:[
                    {label:"Enabled", value:true},
                    {label:"Disabled", value:false}
                ],
                id:3
            },
            units:{
                name:"Default Units",
                icon:"fa-thermometer-half",
                type:"select",
                options:[
                    {label:"Fahrenheit", value:"fahrenheit"},
                    {label:"Celsius", value:"celsius"}
                ],
                id:4
            },
            maxTemp:{
                name:"Max Temperature",
                icon:"fa-fire-extinguisher",
                note:"Shuts off kiln if temperature is exceeded.",
                type:"number",
                step:1,
                id:5
            },
            timezone:{
                name:"Timezone",
                icon:"fa-clock",
                note:"Select the closest date/time.",
                type:"select",
                options:[],
                id:7
            }
        },
        status:{
            status:""
        },
        firing:{
            status:'idle',
            name:'test firing',
            segment:0,
            error:"",
            timeRemaining:""
        },
        pages:{
            current:"index",
            nav:"",
            id:-1
        },
        ctemp:20
    },
    methods: {
        //loads the settings
        loadSettings: function () {
            var self = this;
            axios.get("/api/load-settings").then(response => {
                self.settings = response.data;
                console.log("settings:");
                console.log(self.settings);
            });
        },
        loadNav: function () {
            var self = this;
            axios.get("/templates/nav2.html").then(response => {
                self.pages.nav = response.data;
                self.$forceUpdate();
            });
        },
        pageSelect: function(newPage) {
            console.log("ran");
            console.log(newPage)
            this.pages.current = newPage;

            //updates timezone values
            var updatedTimeZones = [];
            var utcTime = moment.utc();
            console.log(utcTime);
            for(var i = -12; i < 13; i++){
                var newOption = {"label": toTimeZone(utcTime, i), "value":i}
                updatedTimeZones.push(newOption);
            }
            this.settingsFields.timezone.options = updatedTimeZones;

            //updates all settings fields
            Object.keys(this.settingsFields).forEach(myfield => {
                this.settingsFields[myfield].id = uuidv4();
            })

            

            // this.settings.updated = false;
            // this.$nextTick(() => {this.settings.updated = true});
        },
        test: function() {
            console.log("test");
        },
        incrementSensors: function(){
            this.settings.sensors = Math.min(this.settings.sensors + 1, 4);
        },
        decrementSensors: function(){
            this.settings.sensors = Math.max(this.settings.sensors - 1, 1);
        },
        incrementZones: function(){
            this.settings.zones = Math.min(this.settings.zones + 1, 6);
        },
        decrementZones: function(){
            this.settings.zones = Math.max(this.settings.zones - 1, 1);
        },
        saveSettings: function(){
            console.log("Settings Saved!");
        }
  },
    mounted: function () {
        console.log(getParameterByName("ip"));
        this.system.ip = getParameterByName("ip");

        

        //this.loadNav();
        // this.$refs.component1.open = true
        //<child ref="component1"></child>
    }
  });

function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
        var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
        return v.toString(16);
    });
}

function toTimeZone(newTime, zone) {
    //var format = 'YYYY/MM/DD HH:mm:ss ZZ';
    var format = 'HH:mm YYYY/MM/DD';
    return moment(newTime).utcOffset(zone).format(format);
}