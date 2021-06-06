Vue.component('settingsbasic', {
    props: ['pagedata', 'settingsdata', 'statusdata'],
    template: `
    <div class="row">
        <div class="col-12 col-md-4 mb-4">
            <label>Units:</label>
            <select :readonly="statusdata === 'firing'" class="form-control" v-model="settingsdata.units">
                <option value="fahrenheit">Fahrenheit</option>
                <option value="celsius">Celsius</option>
            </select>
        </div>
        <div class="col-6 col-md-4 mb-2">
            <label>Volts:</label>
            <input type="number" v-on:change="test" :readonly="statusdata === 'firing'" class="form-control text-center" v-model.number="settingsdata.volts" />
        </div>
        <div class="col-6 col-md-4 mb-2">
            <label>Cost per kilowatt:</label>
            <input type="number" v-on:change="test" :readonly="statusdata === 'firing'" class="form-control text-center" step="0.01" v-model.number="settingsdata.cost" />
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


