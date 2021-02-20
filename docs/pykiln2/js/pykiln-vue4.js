import { SetData, Init } from './charts.js';

const message = [
    "vue.draggable",
    "draggable",
    "component",
    "for",
    "vue.js 2.0",
    "based",
    "on",
    "Sortablejs"
];

var app = new Vue({
    el: '#app',
    components: {
        draggable: window['vuedraggable']
    },
    data: {
        list: [],
        sort: '',
        isDragging: '',
        id: 2,
        drag: '',
        firing: {
            status: 'idle',
            name: 'test firing',
            segment: 0,
            error: "",
            timeRemaining: ""
        },
        pages: {
            current: "index",
            nav: "",
            id: -1
        },
        ctemp: 20
    },
    methods: {
        // add: function() {
        //   this.list.push({ name: "Juan " + id, id: id++ });
        // },
        // replace: function() {
        //   this.list = [{ name: "Edgard", id: id++ }];
        // },
        // add2: function() {
        //   this.list2.push({ name: "Juan " + id, id: id++ });
        // },
        // replace2: function() {
        //   this.list2 = [{ name: "Edgard", id: id++ }];
        // },

        removeAt(index) {
            this.list.splice(index, 1);
            this.updateGraph();
        },
        add: function() {
            this.id++;
            //let id = this.id;
            this.list.push({ rate: 1, target: 2, hold: 3, uuid: this.id });
            // this.list.push({ name: "Juan " + this.id, id, text: "" });
            this.updateGraph();
        },
        updateGraph: function() {
            console.log("UPDATE!");
            SetData(this.list);
        }
    },
    mounted() {
        //console.log(getParameterByName("ip"));
        //this.system.ip = getParameterByName("ip");
        //SetData();
        Init();
    },
    computed: {
        dragOptions() {
            return {
                animation: 0,
                group: "description",
                disabled: false,
                ghostClass: "ghost"
            };
        },
        draggingInfo() {
            return this.dragging ? "under drag" : "";
        }
        // },
        // watch: {
        //     list: function(value) {

        //         console.log(value);
        //         SetData(value);
        //     }
    }
});