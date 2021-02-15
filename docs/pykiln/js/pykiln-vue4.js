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
        list: [
            { name: "John 1", text:"", id: 0 },
            { name: "Joao 2", text:"", id: 1 },
            { name: "Jean 3", text:"", id: 2 }
          ],
          sort:'',
          isDragging:'',
          id:2,
        myArray:[
            {
                id:0,
                name:"ben0"
            },
            {
                id:1,
                name:"ben1"
            },
            {
                id:2,
                name:"ben2"
            },
            {
                id:3,
                name:"ben3"
            }
        ],
        drag:'',
        firing:{
            status:'idle',
            name:'test firing',
            segment:0,
            error:"",
            timeRemaining:""
        },
        pages:{
            current:"index",
            nav:"",
            id:-1
        },
        ctemp:20
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

        removeAt(idx) {
          this.list.splice(idx, 1);
        },
        add: function() {
          this.id++;
          //let id = this.id;
          this.list.push({ name: "Juan " + this.id, text:"", id: this.id});
          // this.list.push({ name: "Juan " + this.id, id, text: "" });
        }
      },
    mounted(){
        //console.log(getParameterByName("ip"));
        //this.system.ip = getParameterByName("ip");
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
    }
  });