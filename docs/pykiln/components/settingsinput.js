Vue.component('settingsinput', {
    props: ['field', 'status', 'value'],
    template: `
    <div class="form-group col-12 col-md-6">
        <h5>{{field.name}}</h5>
        <div class="input-group my-2">
            <div class="input-group-prepend">
                <span class="input-group-text"><i class="fas" :class="field.icon"></i></span>
            </div>
            <input :disabled="inputDisabled" v-on:change="updateValue($event.target.value)" v-if="field.type == 'number'" type="number" :step="field.step" class="form-control" v-model.number="displayValue">
            <input :disabled="inputDisabled" v-on:change="updateValue($event.target.value)" v-if="field.type == 'text'" type="text" class="form-control" v-model="displayValue">
            
            <select :disabled="inputDisabled" v-on:change="updateValue($event.target.value)" v-if="field.type == 'select'" class="custom-select" v-model="displayValue">
                <option v-for="option in field.options" :key="option.value" :value="option.value">{{option.label}}</option>
            </select>

        </div>
        <small v-if="field.note != undefined" class="form-text text-muted">{{field.note}}</small>
    </div>
    `,
    data: function () {
        return {
            displayValue:"",
            inputDisabled:true
        };
    },
    mounted: function () {
        this.displayValue = this.$props.value;
        // Should people be able to change certain settings even when they are running a firing schedule?
        //if(this.$props.status == undefined || this.$props.status != "firing"){
        if(this.$props.status != "firing"){
            this.inputDisabled = false;
        }
    },
    methods: {
        updateValue: function (newValue) {
        //   this.$emit('input', value);
            var returnValue = newValue;
            if(this.$props.field.type == "number"){
                var decimalPlaces = 0;
                var stepValue = this.$props.field.step;
                if (Math.floor(stepValue) != stepValue){
                    decimalPlaces = this.$props.field.step.toString().split(".")[1].length;
                }
                returnValue = parseFloat(parseFloat(returnValue).toFixed(decimalPlaces));
            }
            if(this.$props.field.type == "select"){
                if(returnValue == "true"){
                    returnValue = true;
                }
                if(returnValue == "false"){
                    returnValue = false;
                }
            }
            this.displayValue = returnValue;
            this.$emit('update:value', returnValue);
        }
      }
  });

