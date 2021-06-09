Vue.component('selectschedule', {
    props: ['schedulesdata'],
    template: `
    <div class="container">
    <div class="row">
        <div class="col-12">
            <div class="form-group">
                <label for="sel1">Select Firing Schedule:</label>
                <select class="form-control" id="sel1" @change="select($event)">
                    <option v-for="item in schedulesdata" :key="item.id" :value="item.id">{{ item.name }}</option>
                
                    <!-- <option>Biscuit Fire Cone 06</option>
                    <option>Biscuit Fire Cone 05</option>
                    <option>Biscuit Fire Cone 04</option>
                    <option>Biscuit Fire Cone 03</option> -->
                </select>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col-6 col-md-auto pr-sm-0">
            <button @click="newschedule" class="btn btn-primary btn-block"><i class="fas fa-file-alt"></i> New Schedule<div class="ripple-container"></div></button>
        </div>
   
        <div class="col-6 col-md-auto pr-sm-0">
            <label for="import-schedule" class="btn btn-primary btn-link btn-block">
                <i class="fas fa-file-upload"></i> Import<div class="ripple-container"></div>
            </label>
            <input class="d-none" id="import-schedule" type="file" ref="myFile" @change="upload" accept="application/json"/>
        </div>
    </div>
   </div>
    `,
    methods: {
        select: function(event) {
            // event.preventDefault();
            console.log("select confirm");
            console.log(event.target.value);
            this.$emit('select', event.target.value);
        },
        newschedule: function(){
            console.log("newschedule confirm");
            this.$emit('newschedule');
        },
        upload: function(){

            console.log('selected a file');
            console.log(this);
            console.log(this.$refs.myFile.files[0]);

            let file = this.$refs.myFile.files[0];
            if(!file || file.type !== 'application/json') return;

            let reader = new FileReader();
            reader.readAsText(file, "UTF-8");
            reader.onload =  evt => {
                let uploadedSchedule = JSON.parse(evt.target.result);
                console.log(uploadedSchedule);
                this.$emit('upload', uploadedSchedule);
            }
            reader.onerror = evt => {
                console.error(evt);
            }
        }
    }
});


