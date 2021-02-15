var app = new Vue({
    el: '#app',
    components: {
        draggable: window['vuedraggable']
    },
    data: {
        list: [
            { name: "John 1", id: 0 },
            { name: "Joao 2", id: 1 },
            { name: "Jean 3", id: 2 }
          ],
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
        add: function() {
          this.list.push({ name: "Juan " + id, id: id++ });
        },
        replace: function() {
          this.list = [{ name: "Edgard", id: id++ }];
        },
        add2: function() {
          this.list2.push({ name: "Juan " + id, id: id++ });
        },
        replace2: function() {
          this.list2 = [{ name: "Edgard", id: id++ }];
        }
      },
    mounted: function () {
        //console.log(getParameterByName("ip"));
        //this.system.ip = getParameterByName("ip");


    }
  });