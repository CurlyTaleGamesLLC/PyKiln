Vue.component('modal', {
    props: ['modalid', 'modaltitle', 'modalbody', 'modalbutton', 'buttonclass'],
    template: `
    <!-- Modal -->
    <div class="modal fade" :id="modalid" tabindex="-1" role="dialog">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="modal-title-id">{{ modaltitle }}</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <i class="material-icons">clear</i>
                    </button>
                </div>
                <div v-if="modalbody !== 'conechart'" class="modal-body" v-html="modalbody"></div>
                <div v-else class="modal-body"><conechart></conechart></div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-link" data-dismiss="modal" v-if="modalbody !== 'conechart'">Back</button>
                    <button type="button" class="btn" v-bind:class="buttonclass" v-on:click="confirm" v-html="modalbutton"></button>
                </div>
            </div>
        </div>
    </div>
    `,
    methods: {
        confirm: function(event) {
            event.preventDefault();
            console.log("modal confirm");
            this.$emit('confirm');
        }
    }
});