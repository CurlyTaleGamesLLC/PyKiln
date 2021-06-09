Vue.component('scanresults', {
    props: ['scanresultsdata'],
    template: `
    <div class="container">
        <div class="row mb-4">
            <h3 class="col-12 mt-0">Scan Results:</h3>
            <div class="col-12" v-for="item in scanresultsdata">
                <div class="d-flex">
                    <button @click="connect(item)" class="btn btn-primary w-66"><i class="fas fa-wifi"></i> {{ item }}</button>
                    <button @click="beep(item)" class="btn btn-secondary w-34"><i class="fas fa-bell"></i> Beep Me</button>
                </div>
            </div>
        </div>
    </div>
    `,
    methods: {
        connect: function(ip) {
            //event.preventDefault();
            console.log("Connect to " + ip);
            
            var newurl = window.location.protocol + "//" + window.location.host + window.location.pathname + '?ip=' + ip;
            window.history.pushState({ path: newurl }, '', newurl);
            this.$emit('connect', ip);
        },
        beep: function(ip){
            console.log("BEEP! " + ip);
            axios.get('http://' + ip + "/beep", {
                crossDomain: true,
                withCredentials: true
            });
        }
    }
});


