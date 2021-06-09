Vue.component('notify', {
    props: ['toastid', 'toasttitle', 'toastbody', 'toasttime'],
    template: `
    <!-- Toast Notification -->
    <div :id="toastid" class="toast fixed-top ml-auto mr-3 mt-3 fade hide" :data-delay="toasttime">
            <div class="toast-header">
                <strong class="mr-auto" v-html="toasttitle"></strong>
                <button type="button" class="ml-2 mb-1 close" data-dismiss="toast" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <div class="toast-body" v-if="toastbody !== ''">
                {{ toastbody }}
            </div>
        </div>
    `,
    methods: {
        confirm: function(event) {
            event.preventDefault();
            console.log("notify confirm");
            //this.$emit('confirm');
        }
    }
});