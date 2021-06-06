Vue.component('schedulename', {
    props: ['statusdata', 'iseditingdata', 'namedata', 'firingnamedata'],
    template: `
    <div>
    <div class="row" v-if="statusdata !== 'firing'">
        <label class="col-12">Name:</label>
        <div class="form-group has-default bmd-form-group col-12">
            <div class="container">
                <div class="row">
                    <input type="text" class="form-control col schdule-name mt-2" placeholder="Schedule Name" :readonly="!iseditingdata" :value="namedata" @input="nameChange">
                </div>
            </div>
        </div>
    </div>
    <div class="row" v-if="statusdata === 'firing'">
        <label class="col-12">Name:</label>
        <div class="form-group has-default bmd-form-group col-12">
            <div class="container">
                <div class="row">
                    <input type="text" class="form-control col schdule-name mt-2" placeholder="Schedule Name" :readonly="!iseditingdata" v-model="firingnamedata">
                </div>
            </div>
        </div>
    </div>
    </div>
    `,
    methods: {
        nameChange: function(event) {
            this.message = event.target.value;
            this.$emit('updatename', this.message);
        }
    }
});




