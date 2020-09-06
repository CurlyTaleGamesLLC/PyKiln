var localURL = "";

var app = new Vue({
  el: '#app',
  components: {},
  data: {
    visible: false,
    message: 'Hello Vue!',
    isDev: true
  },
  delimiters: ['[[', ']]'], // required because {{ }} conflicts with Flask html templates
  methods: {
    init: function () {
      console.log("HELLO WORLD!");
    }
  },
  mounted: function () {
    console.log("Mounted!");
    this.init()
  },
  computed: {}
});