Vue.component('settingsnotifications', {
    props: ['pagedata', 'settingsdata', 'statusdata'],
    template: `
    <div>
    <div class="row">
        <h3 class="col-12">Notifications:</h3>
        <div class="col-12 mb-4" :class="notifications.emailValid ? '' : 'has-danger'">
            <label>Email:</label>
            <input type="email" v-on:change="emailFormat" :readonly="statusdata === 'firing'" class="form-control" v-model="notifications.email" />
        </div>
        <div class="col-12 mb-4">
            <div class="togglebutton">
                <label class="d-flex">
                    <input type="checkbox" v-model="notifications.news" v-on:change="update">
                    <span class="toggle mr-4"></span>
                    <span class="w-100">Be the first to hear updates on changes to PyKiln</span>
                    
                </label>
                </div>
        </div>
        <div class="col-12 mb-4">
            <div class="togglebutton">
                <label class="d-flex">
                    <input type="checkbox" v-model="notifications.analytics" v-on:change="update">
                    <span class="toggle mr-4"></span>
                    <span class="w-100">I agree to providing anonymous data for making improvements to PyKiln</span>
                </label>
                </div>
        </div>
        <h4 class="col-12">Audio Alerts:</h4>
        <div class="col-12 mb-4">
            <div class="togglebutton">
                <label class="d-flex">
                    <input type="checkbox" v-model="notifications.audio" v-on:change="update">
                    <span class="toggle mr-4"></span>
                    <span class="w-100">Enable or Disable the audio feedback from PyKiln</span>
                </label>
                </div>
        </div>
        
    </div>
    </div>
    `,
    data: function () {
        return {
          notifications:{
            email: this.settingsdata.email,
            emailValid:false,
            news: this.settingsdata.news,
            analytics: this.settingsdata.analytics,
            audio: this.settingsdata.audio
          }
        }
      },
    methods: {
        update: function() {
            this.$emit('update', this.notifications);
        },
        emailFormat: function(event) {
            // console.log(event.target.value);

            let emailToCheck = '';
            if(event.target == undefined){
                emailToCheck = event;
            }
            else{
                emailToCheck = event.target.value;
            }

            if(emailToCheck != ''){
                this.notifications.emailValid = (/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(emailToCheck));
            }
            else{
                this.notifications.emailValid = true;
            }
            
            this.update();
            // if (/^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/.test(event.target.value)){return (true)}
            // return (false)
        }
    },
    mounted() {
        this.emailFormat(this.settingsdata.email);
    }
});


