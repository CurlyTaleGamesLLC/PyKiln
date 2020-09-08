var app = new Vue({
    el: '#app',
    data: {
        system:{
            name:"my pykiln1",
            version:"0.2",
            wifiNetwork:"My cool Wifi",
            ip:"127.0.0.1",
            timezone:"eastern",
            uptime:"2:00",
            connection:"online",
            filespace:"2.0MB"
        },
        settings:{
            volts:120,
            units:"fahrenheit",
            maxTemp:2500,
            sensors:2,
            sensorAdjustment:[0,0,0,0],
            zones:3,
            zoneAdjustment:[100,100,100,100],
            cost:0.14,
            email:"example@example.com",
            updated:false
        },
        status:{
            status:""
        },
        firing:{
            status:'firing',
            name:'test firing',
            segment:0,
            error:"",
            timeRemaining:""
        },
        pages:{
            current:"home",
            nav:""
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

         

            this.settings.updated = false;
            this.$nextTick(() => {this.settings.updated = true});

        
        },
        test: function() {
            console.log("test");
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