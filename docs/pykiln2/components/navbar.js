Vue.component('navbar', {
    props: ['pagedata', 'ipdata', 'statedata', 'degreesdata'],
    template: `
    <nav class="navbar navbar-inverse navbar-expand-lg bg-dark">
        <div class="container">
            <div class="navbar-translate">
                <a class="navbar-brand" @click="browse($event, 'home')" href="#0"><img src="/img/pykiln-white-logo.svg" height="25px"> <!-- <i class="fas fa-burn"></i> PyKiln --></a>
                <!-- <div class="d-lg-none">100°F | 100°F | 100°F</div> -->
                <div class="col mb-1 text-center d-lg-none">
                    <i class="fas fa-thermometer-half temp-icon"></i>
                    <span class="badge badge-pill badge-secondary bg-dark mx-1 temp-padding" v-for="(element, index) in statedata.temp" :key="index">{{element}}{{ degreesdata }}</span>
                </div>
                <button class="navbar-toggler" :class="ipdata != '' ? '' : 'd-none'" type="button" data-toggle="collapse" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="navbar-toggler-icon"></span>
                    <span class="navbar-toggler-icon"></span>
                    <span class="navbar-toggler-icon"></span>
                </button>
            </div>
            <div class="collapse navbar-collapse">
                <div class="col mb-1 text-center">
                    <i class="fas fa-thermometer-half temp-icon"></i>
                    <span class="badge badge-pill badge-secondary bg-dark mx-1 temp-padding" v-for="(element, index) in statedata.temp" :key="index">{{element}}{{ degreesdata }}</span>
                </div>
                <ul class="navbar-nav ml-auto" :class="ipdata != '' ? '' : 'd-none'">
                    <li class="nav-item" :class="pagedata == 'logs' ? 'active' : ''">
                        <a @click="browse($event, 'logs')" href="javascript:;" class="nav-link">
                            <span class="material-icons">assignment</span> Logs
                        </a>
                    </li>
                    <li class="nav-item" :class="pagedata == 'settings' ? 'active' : ''">
                        <a @click="browse($event, 'settings')" href="javascript:;" class="nav-link">
                            <i class="material-icons">settings</i> Settings
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>
    `,
    methods: {
        browse: function(event, newPage) {
            event.preventDefault();
            console.log("navbar confirm " + newPage);
            this.$emit('browse', newPage);
        }
    }
});




