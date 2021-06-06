Vue.component('notes', {
    props: ['notedata', 'iseditingdata'],
    template: `
    <!-- Notes -->
    <div class="panel-group">
    <div class="panel panel-default">
        <div class="panel-heading">
        <h4 class="panel-title">
            <a data-toggle="collapse" href="#collapse1"><i class="fas fa-clipboard-list"></i> Notes</a>
        </h4>
        </div>
        <div id="collapse1" class="panel-collapse collapse" :class="notedata == '' ? '' : 'show'">
        <div class="panel-body">
        <textarea rows="4" cols="50" class="w-100" :value="notedata" @input="noteChange" placeholder="Any firing notes?" :readonly="!iseditingdata"></textarea>
        </div>
        </div>
    </div>
    </div>
    `,
    data() {
        return {
            message: ""
        }
    },
    methods: {
        // confirm: function(event) {
        //     event.preventDefault();
        //     console.log("modal confirm");
        //     //this.$emit('confirm');
        // }
        noteChange: function(event) {
            this.message = event.target.value;
            this.$emit('updatenote', this.message);
        }
    }
});