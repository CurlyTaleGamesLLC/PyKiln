Vue.component('modal', {
    props: ['modalid','modaltitle','modalbody','modalbutton', 'buttonclass'],
    template: `
    <!-- Modal -->
    <div class="modal fade" :id="modalid" tabindex="-1" role="dialog">
        <div class="modal-dialog modal-dialog-centered" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="modal-title-id">{{ modaltitle }}</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>

                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Back</button>
                    <button type="button" class="btn" v-bind:class="buttonclass" data-dismiss="modal" v-on:click="confirm" v-html="modalbutton"></button>
                </div>
            </div>
        </div>
    </div>
    `,
    methods: {
      confirm: function(event){
        event.preventDefault();
        console.log("modal confirm");
        this.$emit('confirm');
      }
    }
  });



/*

{% with modalid="start-confirm-modal", modaltitle="Start Firing Schedule?", modalbody="", buttonid="btn-start-schedule", modalbutton="<i class='fas fa-burn'></i> Start Schedule", modalfunction="startFire(schedule.path)" %}
{% include 'modal-primary.html' %}
{% endwith %}

{% with modalid="stop-confirm-modal", modaltitle="Stop Firing Schedule?", modalbody="", buttonid="btn-stop-schedule", modalbutton="<i class='fas fa-ban'></i> Stop Schedule", modalfunction="stopFire"  %}
{% include 'modal-danger.html' %}
{% endwith %}

*/