Vue.component('scanprogress', {
    props: ['scantitledata', 'scanipdata', 'scanprogressdata'],
    template: `
    <div class="container">
        <div class="row">
            <h3 class="col-12 mt-0">{{ scantitledata }}</h3>
            <p class="col-12">Checking: {{ scanipdata }}</p>
            <div class="col-12">
                <div class="progress">
                    <div class="progress-bar progress-bar-striped progress-bar-animated" :style="{ width: (scanprogressdata * 100) + '%' }"></div>
                </div>
            </div>
            <div class="col-12">
                <div class="d-flex">
                    <button class="btn btn-rose btn-lg w-100" @click="stop"><i class="fas fa-ban"></i> Stop Scanning</button>
                </div>
            </div>
        </div>
    </div>
    `,
    methods: {
        stop: function(event) {
            console.log("stop confirm");
            this.$emit('stop');
        }
    }
});




