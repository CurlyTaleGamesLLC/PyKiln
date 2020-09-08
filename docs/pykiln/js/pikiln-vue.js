Array.prototype.move = function(from, to) {
    this.splice(to, 0, this.splice(from, 1)[0]);
    return this;
};

var app = new Vue({
    el: '#app',
    data: {
    
        firing:{
            status:'firing',
            name:'test firing',
            segment:0,
            error:"",
            timeRemaining:""
        },
        cost:0,
        timeEstimate:"2:00",
        schedule:{
            name:'',
            path:'',
            segments:[
            {
                rate:100,
                temp:200,
                hold:10
            },
            {
                rate:100,
                temp:200,
                hold:10
            }
            ],
            units:''
        },
        scheduleList:[],
        cTemp:[],
        settings:[],
        totals:{
            fires:4,
            cost:4,
            time:1
        },
        log:[]
    },
    delimiters: ['[[', ']]'],
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
  
      //saves the settings, and checks to make sure the email address is valid
      saveSettings: function () {
          var self = this;
  
          //validate email address format
          var reg = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/
          self.settings.email = reg.test(self.settings.email) ? self.settings.email : "";
  
          axios.post('/api/save-settings', self.settings)
              .then(response => {
                  console.log(response.data);
                  $('#alert-container').html('<div class="alert alert-warning alert-dismissible mt-3" role="alert" id="alert-save-settings"><strong>Settings Saved!</strong><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>');
  
                  setTimeout(function () {
                    $('#alert-container').html('')
                  }, 4000);
              });
      },

      incrementZones() { 
        this.settings.zoneCount++;
        if(this.settings.zoneCount > 3){
          this.settings.zoneCount = 3;
        }
      },
      decrementZones() { 
        this.settings.zoneCount--;
        if(this.settings.zoneCount < 1){
          this.settings.zoneCount = 1;
        }
      },
      incrementTemp() { 
        this.settings.tempCount++;
        if(this.settings.tempCount > 3){
          this.settings.tempCount = 3;
        }
      },
      decrementTemp() { 
        this.settings.tempCount--;
        if(this.settings.tempCount < 1){
          this.settings.tempCount = 1;
        }
      },
  
      //updates the current temperature in the navigation bar and on the home screen during a fire
      getCurrentTemp: function(){
        var self = this;
        axios.get("/api/temperature").then(response => {
          self.cTemp = response.data;

          //truncate temperature readings to 2 decimal places
          //if(self.cTemp.temp.length > 0){
            for(var i = 0; i < self.cTemp.temp.length; i++){
              self.cTemp.temp[i] = Math.floor(self.cTemp.temp[i] * 100) / 100;
            }
          //}
          

        });
      },

      //updates the highlighted segment when a schedule is being fired
      getCurrentSegment: function(){
        var self = this;
        axios.get("/api/get-current-segment").then(response => {
          self.firing = response.data;
          self.firing.timeRemaining = self.formatTime(self.firing.totalTime - self.firing.currentTime)
        });
      },

      //gets list of all firing schedules
      getScheduleList: function(){
        var self = this;
        axios.get("/api/list-schedules").then(response => {
          self.scheduleList = response.data;
        });
      },

      //load schedule selected from dropdown
      onScheduleSelect: function(event){
        var self = this;
        self.onScheduleSelectPath(event.target.value);
      },

      onScheduleSelectPath: function(path){
        if (path != "select-schedule") {
            var self = this;
            axios.get("/api/get-schedule?schedulePath=" + path).then(response => {
                self.schedule = [];
                self.schedule = response.data;
                self.schedule.path = path;

                self.updateTimeEstimate(path);
                //forces a refresh of the current status
                self.getCurrentSegment();
            });
        }
      },

      //updates the estimated time for the current schedule
      updateTimeEstimate: function(path){
        var self = this;
        axios.get("/api/get-time-estimate?schedulePath=" + path).then(response => {
            console.log(response.data);
            self.timeEstimate = self.formatTime(response.data['time'] * 3600);
        });
      },

      //starts the firing schedule
      startFire: function(path){
        var self = this;
        axios.get("/api/start-fire?schedulePath=" + path).then(response => {
            console.log(response.data);
            self.getCurrentSegment();
        });
      },

      //stops the firing schedule
      stopFire: function(){
        var self = this;
        axios.get("/api/stop-fire").then(response => {
            console.log(response.data);
            self.getCurrentSegment();
            //sometimes it takes a second for the status to change to stopped
            setTimeout(function () {self.getCurrentSegment()}, 500);
        });
      },

      //gets list of all firing schedules
      getTotals: function(){
        var self = this;
        axios.get("/api/load-totals").then(response => {
          self.totals = response.data;
        });
      },

      formatTime: function(value){
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
      },

      formatCost: function(value){
        return "$" + value.toFixed(2).toString();
      },

       //gets list of all firing schedules
      getChart: function(){
        var self = this;
        axios.get("/api/get-chart").then(response => {
          self.log = response.data;
          LoadLineGraph(self.log['startTime'], self.log['tempLog'], self.log['scheduleLog']);
        });
      },

      //move firing schedule segments up or down
    move(from, to) {
        this.schedule.segments.move(from, to);
    },
    //delete firing schedule segment
    remove (index) {
        this.$delete(this.schedule.segments, index)
      },
      //add a firing schedule segment
    addRow() {
        var self = this;

        var lastRow;
        if(self.schedule.segments.length == 0){
            lastRow = JSON.parse('{"rate":200, "temp":800, "hold":0}');
        }
        else{
            lastRow = JSON.stringify(self.schedule.segments[self.schedule.segments.length - 1]);
            lastRow = JSON.parse(lastRow);
        }
        self.schedule.segments.push(lastRow);
    },
    //edit the title of a firing schedule
    onEditTitle: function(event){
        var src = event.target.innerHTML;
        this.schedule.name = src;
    },
    //edit the value of the ramp rate, target temp, or hold time of a firing schedule
    onEdit: function(event, key, index){
        console.log("EDIT:");
        console.log(event);
        console.log(key + " " + index);
        var src = event.target.innerHTML;
        this.schedule.segments[index][key] = parseInt(src);

        //hack to break weird bug that rows of the same value are linked together
        var jsonString = JSON.stringify(this.schedule.segments[index]);
        this.schedule.segments[index] = JSON.parse(jsonString);
    },
    //deselect the editable field for a firing schedule
    endEdit(){
        this.$el.querySelector('.editme').blur()
    },
    onScheduleSave: function(){
        var self = this;

        axios.post('/api/save-schedule', self.schedule)
        .then(response => {
            console.log(response.data);

            //update name of saved schedule in list
            for(var i = 0; i < self.scheduleList.length; i++){
                if(self.scheduleList[i].path == self.schedule.path){
                    self.scheduleList[i].name = self.schedule.name;
                }
            }

            //show schedule saved message for 4 seconds
            $('#alert-container').html('<div class="alert alert-warning alert-dismissible mt-1" role="alert" id="alert-save-settings"><strong>Schedule Saved!</strong><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>');
    
            setTimeout(function () {
              $('#alert-container').html('')
            }, 4000);
        });
    },
    onScheduleCreateNew: function(){
        var self = this;

        axios.post('/api/create-schedule', self.schedule)
        .then(response => {
            console.log(response.data);

            var newSchedule = {};
            newSchedule['name'] = "Untitled Schedule";
            newSchedule['path'] = response.data['filename'];

            self.scheduleList.push(newSchedule);
            //give vue a moment to update itself before selecting new schedule
            setTimeout(function () {
                $("#fireScheduleList").val(response.data['filename']).change();
                self.onScheduleSelectPath(response.data['filename']);
            }, 500);

            
        });
    },

    onDeleteSchedule: function(){
        var self = this;

        if(self.schedule.path == null){return;}
        
        axios.delete('/api/delete-schedule?schedulePath=' + self.schedule.path)
        .then(response => {
            console.log(response.data);

            for(var i = 0; i < self.scheduleList.length; i++){
                if(self.scheduleList[i].path == self.schedule.path){
                    self.$delete(self.scheduleList, i);
                }
            }
            self.schedule = JSON.parse('{"name":"", "path":""}');
            
            $("#fireScheduleList").val("select-schedule").change();
        });
    },

    //downloads schedule
    onScheduleDownload: function(){
        var self = this;
        
        if(self.schedule.path == null){return;}

        axios.get('api/get-schedule?schedulePath=' + self.schedule.path).then(response => {
            var json = JSON.stringify(response.data);
            var blob = new Blob([json], {type: "application/json"});
            var url  = URL.createObjectURL(blob);
      
            var link = document.createElement('a');
            link.setAttribute('href', url);
            link.setAttribute('download', response.data['name'] + '.json');
            
            var aj = $(link);
            aj.appendTo('body');
            aj[0].click();
            aj.remove();
            
            URL.revokeObjectURL(url);
        });
      },
      onScheduleDuplicate: function(){
        var self = this;

        if(self.schedule.path == null){return;}

        axios.post('/api/duplicate-schedule?schedulePath=' + self.schedule.path)
        .then(response => {
            console.log(response.data);

            var newSchedule = {};
            newSchedule['name'] = response.data['name'];
            newSchedule['path'] = response.data['filename'];

            self.scheduleList.push(newSchedule);
            //give vue a moment to update itself before selecting new schedule
            setTimeout(function () {
                $("#fireScheduleList").val(response.data['filename']).change();
                self.onScheduleSelectPath(response.data['filename']);
            }, 500);

            
        });
    }
   
  },
    mounted: function () {
      if (window.location.pathname == "/" || window.location.pathname == "/index") {
        //home page
        this.getScheduleList();
      }
      if (window.location.pathname == "/firing-schedules") {
        //edit firing schedules page
        this.getScheduleList();
        CelsiusConeChart();
      }
      if (window.location.pathname == "/logging") {
        //logging page
        this.getTotals();
        this.getChart();
      }
      if (window.location.pathname == "/settings") {
        //settings page
        this.loadSettings();
      }
  
      //continually gets the current temperature
      this.getCurrentTemp();
      setInterval(() => {this.getCurrentTemp()}, 3000);

      //continually gets the current status
      this.getCurrentSegment();
      setInterval(() => {this.getCurrentSegment()}, 5000);
      
    }
  });