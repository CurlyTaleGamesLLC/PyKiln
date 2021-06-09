Vue.component('settingskiln', {
    props: ['pagedata', 'settingsdata', 'statusdata'],
    template: `
    <div>
    <div class="row">
        <h3 class="col-12">Kiln Configuration:</h3>
        <div class="col-12 col-md-4 mb-4">
            <label>Units:</label>
            <select :readonly="statusdata === 'firing'" class="form-control" v-model="kiln.units">
                <option value="fahrenheit">Fahrenheit</option>
                <option value="celsius">Celsius</option>
            </select>
        </div>
        <div class="col-6 col-md-4 mb-2">
            <label>Volts:</label>
            <input type="number" v-on:change="update" :readonly="statusdata === 'firing'" class="form-control text-center" v-model.number="kiln.volts" />
        </div>
        <div class="col-6 col-md-4 mb-2">
            <label>Cost per kilowatt:</label>
            <input type="number" v-on:change="update" :readonly="statusdata === 'firing'" class="form-control text-center" step="0.01" v-model.number="kiln.cost" />
        </div>
    </div>
    <div class="row">
        <div class="col-12 d-flex">
            <div class="w-20 text-center">
                <label>Zones:</label>
                <button class="btn btn-primary btn-lg btn-block px-2" :readonly="statusdata === 'firing'" @click="addZone(1)"><i class="fas fa-plus"></i></button>
                <h3 class="m-0">{{ kiln.zoneCount }}</h3>
                <button class="btn btn-primary btn-lg btn-block px-2" :readonly="statusdata === 'firing'" @click="addZone(-1)"><i class="fas fa-minus"></i></button>
            </div>

            <div class="w-60 kilnsettings">
                <img class="kilnicons-base" src="img/kiln-base.svg">
                <img class="kilnicons" :src="'./img/kiln-zones-' + kiln.zoneCount + '.svg'">
                <img class="kilnicons" :src="'./img/kiln-temp-' + kiln.sensorCount + '.svg'">
            </div>

            <div class="w-20 text-center">
                <label>Sensors:</label>
                <button class="btn btn-primary btn-lg btn-block px-2" :readonly="statusdata === 'firing'" @click="addSensor(1)"><i class="fas fa-plus"></i></button>
                <h3 class="m-0">{{ kiln.sensorCount }}</h3>
                <button class="btn btn-primary btn-lg btn-block px-2" :readonly="statusdata === 'firing'" @click="addSensor(-1)"><i class="fas fa-minus"></i></button>
            </div>
        </div>
    </div>
    <div class="row">
        <h3 class="col-12">Advanced Configuration:</h3>
        <div class="col-12 col-md-6 mb-4">
            <label>Zone Adjustment:</label>
            <div v-for="(zone, index) in kiln.zones" class="d-flex">
                <span class="zonelabel mr-4" v-show="index < kiln.zoneCount">{{ index + 1 }}</span>
                <div class="w-100" v-show="index < kiln.zoneCount">
                    <input :name="'zone'+index" v-model.number="kiln.zones[index]" type="number" v-on:change="update" :readonly="statusdata === 'firing'" class="form-control text-center" step="0.1" />
                </div>
            </div>
        </div>
        <div class="col-12 col-md-6 mb-4">
            <label>Sensor Adjustment:</label>
            <div v-for="(sensor, index) in kiln.sensors" class="d-flex">
                <span class="zonelabel mr-4" v-show="index < kiln.sensorCount">{{ index + 1 }}</span>
                <div class="w-100" v-show="index < kiln.sensorCount">
                    <input :name="'sensor'+index" v-model.number="kiln.sensors[index]" type="number" v-on:change="update" :readonly="statusdata === 'firing'" class="form-control text-center" step="0.1" />
                </div>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-12">
            <label>Sensor Type:</label>
            <!-- <input type="number" v-on:change="update" :readonly="statusdata === 'firing'" class="form-control text-center" v-model.number="kiln.units" /> -->
            <select :readonly="statusdata === 'firing'" class="form-control w-100" v-model="kiln.sensorType">
                <option value="k">K Type (Most Common)</option>
                <option value="j">J Type</option>
                <option value="n">N Type</option>
                <option value="r">R Type</option>
                <option value="s">S Type</option>
                <option value="t">T Type</option>
                <option value="e">E Type</option>
                <option value="b">B Type</option>
            </select>
        </div>
    </div>
    </div>
    `,
    data: function () {
        return {
          kiln:{
            units: this.settingsdata.units,
            volts: this.settingsdata.volts,
            cost: this.settingsdata.cost,
            zoneCount: this.settingsdata.zoneCount,
            zones: this.settingsdata.zones,
            sensorCount: this.settingsdata.sensorCount,
            sensors: this.settingsdata.sensors,
            sensorType: this.settingsdata.sensorType
          }
        }
      },
    methods: {
        update: function() {
            this.$emit('update', this.kiln);
        },
        addZone: function(value){
            let newValue = this.kiln.zoneCount + value;
            if(newValue < 1){newValue = 1;}
            if(newValue > 3){newValue = 3;}
            this.kiln.zoneCount = newValue;
            console.log(newValue);
            this.update();
        },
        addSensor: function(value){
            let newValue =  this.kiln.sensorCount + value;
            if(newValue < 1){newValue = 1;}
            if(newValue > 3){newValue = 3;}
            this.kiln.sensorCount = newValue;
            console.log(newValue);
            this.update();
        }
    }
});


