Vue.component('navbar', {
  props: ['name','current'],
  template: `
    <nav class="navbar navbar-expand-lg bg-dark navbar-dark mb-4">
      
    <!-- Main Home Button -->
    <a class="navbar-brand" href="index">{{name}} <i class="fas fa-burn"></i></a>

    <!-- Mobile Temp and Firing Schedule -->
    <span class="text-light d-lg-none d-xl-none">

        <!-- Average Temperature -->
        <b class="d-inline-block">
            <span>72</span>
            <span>°F</span>
        </b>

        <span class="current-schedule">Current Schedule Name</span>
    </span>

    <!-- Mobile Drop Down Button -->
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup"
        aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

    <!-- Pages -->
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav">
            <a class="nav-item nav-link" :class="{active: current == 'index'}" href="index" v-on:click="setPage">Home <span class="sr-only">(current)</span></a>
            <a class="nav-item nav-link" :class="{active: current == 'firing-schedules'}" href="firing-schedules" v-on:click="setPage">Edit Firing Schedules</a>
            <a class="nav-item nav-link" :class="{active: current == 'logging'}" href="logging" v-on:click="setPage">Logging</a>
            <a class="nav-item nav-link" :class="{active: current == 'settings'}" href="settings" v-on:click="setPage">Settings</a>
        </div>
    </div>

    <!-- Desktop Temp and Firing Schedule -->
    <span class="text-light d-none d-lg-block d-xl-block">

        <!-- Average Temperature -->
        <b class="d-inline-block">
            <span>73</span>
            <span>°F</span>
        </b>

    </span>
  </nav>
  `,
  methods: {
    setPage: function(event){
      event.preventDefault();
      this.$emit('custom', event.target.pathname.slice(1));
    }
  }
});