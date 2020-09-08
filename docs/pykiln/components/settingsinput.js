Vue.component('settingsinput', {
    props: ['name', 'icon', 'label', 'type', 'step', 'value'],
    template: `
    <div class="form-group col-12 col-md-6">
        <h5>{{name}}</h5>
        <div class="input-group my-2">
            <div class="input-group-prepend">
                <span class="input-group-text"><i class="fas" :class="icon"></i></span>
            </div>
            <input v-on:change="updateValue($event.target.value)" v-if="type == 'number'" type="number" :step="step" class="form-control" v-model.number="displayValue">
            <input v-on:change="updateValue($event.target.value)" v-if="type == 'text'" type="text" class="form-control" v-model.number="displayValue">
            <input v-on:change="updateValue($event.target.value)" v-if="type == 'checkbox'" type="checkbox" class="form-control" v-model.number="displayValue">
        </div>
        <small v-if="label != undefined" class="form-text text-muted">{{label}}</small>
    </div>
    `,
    data: function () {
        return {
            displayValue:""
        };
    },
    mounted: function () {
        this.displayValue = this.$props.value;
    },
    methods: {
        updateValue: function (newValue) {
        //   this.$emit('input', value);
            var returnValue = newValue;
            if(this.$props.type == "number"){
                var decimalPlaces = 0;
                var stepValue = this.$props.step;
                if (Math.floor(stepValue) != stepValue){
                    decimalPlaces = this.$props.step.toString().split(".")[1].length;
                }
                returnValue = parseFloat(parseFloat(returnValue).toFixed(decimalPlaces));
            }
            this.displayValue = returnValue;
            this.$emit('update:value', returnValue);
        }
      }
  });

