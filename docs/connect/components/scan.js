Vue.component('scan', {
    props: ['pagedata'],
    template: `
    <div class="container">
        <div class="row mb-4">
        
            <h3 class="col-12 mt-0" v-if="pagedata === 'home'">Dude, where's my kiln?</h3>
            <h3 class="col-12 mt-0" v-else>Still not seeing your PyKiln?</h3>
            <div class="col-12">
                <p>If you forgot to write down or bookmark the IP address of your PyKiln you can scan your network to find it. Make sure your are connected to the same network as your PyKiln. Scanning is currently only supported on IPv4 networks with a subnet mask of 255.255.255.0 (this is most consumer networks).</p>    
                <p>If you still aren't finding it, you can plug your PyKiln into your computer and run the wifi-reset.py script to reconnect it to your WiFi network.</p>
                <p>After that if it's not showing up, please <a target="_blank" href="https://github.com/CurlyTaleGamesLLC/PyKiln/issues/new?title=Add%20Router%20to%20Default%20List&body=Router%20Brand%3A%0AModel%20Number%3A%0ANetwork%20IP%20Address%3A">create a new issue on our GitHub and include the brand, model number, and IP address of your router</a> so we can add it to our router IP address list.</p>
            </div>
            <div class="col-12">
                <div class="d-flex">
                    <button class="btn btn-primary btn-lg w-100" @click="scan"><i class="fas fa-search"></i> Scan Network for PyKiln</button>
                </div>
            </div>
        </div>
    </div>
    `,
    methods: {
        scan: function(event) {
            event.preventDefault();
            console.log("scan confirm");
            this.$emit('scan');
        }
    }
});

// Good resource for prefilling GitHub Issues with URL encoded data
// https://eric.blog/2016/01/08/prefilling-github-issues/
// https://github.com/CurlyTaleGamesLLC/PyKiln/issues/new?title=Add%20Router%20to%20Default%20List&body=Router%20Brand%3A%0AModel%20Number%3A%0ANetwork%20IP%20Address%3A


