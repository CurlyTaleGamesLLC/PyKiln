Vue.component('settingsalarms', {
    props: ['pagedata', 'settingsdata', 'statusdata'],
    template: `
    <div class="row">
        <h3 class="col-12">Alarms:</h3>
        <p class="col-12 mb-4">Enabling these alarms will stop the firing schedule and send you a notification. They indicate there is a problem with the kiln or the kiln can not heat or cool at the rate specified in the firing schedule.</p>
        <div class="col-12 mb-4 d-flex">
            <div class="togglebutton">
                <label class="d-flex">
                    <input type="checkbox" :checked="settingsdata.maxEnable">
                    <span class="toggle mr-4"></span>
                </label>
            </div>
            <label>Max Temperature:</label>
            <div class="w-100">
                <input v-model.number="settingsdata.max" type="number" v-on:change="test" :readonly="statusdata === 'firing'" class="form-control text-center" step="0.1" />
            </div>
        </div>
        <div class="col-12 col-md-6 mb-4 d-flex">
            <div class="togglebutton">
                <label class="d-flex">
                    <input type="checkbox" :checked="settingsdata.aboveEnable">
                    <span class="toggle mr-4"></span>
                </label>
            </div>
            <label>Above Schedule:</label>
            <div class="w-100">
                <input v-model.number="settingsdata.above" type="number" v-on:change="test" :readonly="statusdata === 'firing'" class="form-control text-center" step="0.1" />
            </div>
        </div>
        <div class="col-12 col-md-6 mb-4 d-flex">
            <div class="togglebutton">
                <label class="d-flex">
                    <input type="checkbox" :checked="settingsdata.belowEnable">
                    <span class="toggle mr-4"></span>
                </label>
            </div>
            <label>Below Schedule:</label>
            <div class="w-100">
                <input v-model.number="settingsdata.below" type="number" v-on:change="test" :readonly="statusdata === 'firing'" class="form-control text-center" step="0.1" />
            </div>
        </div>
       
    </div>
    `,
    methods: {
        update: function(event) {
            // event.preventDefault();
            console.log("select confirm");
            console.log(event.target.value);
            this.$emit('select', event.target.value);
        },

        test: function(){
            console.log("TEST!!!");
        }
    }
});


