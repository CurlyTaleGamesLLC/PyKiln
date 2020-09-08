Vue.component('heading', {
    props: ['title'],
    template: `
    <div class="row">
        <h2 class="col-12 mb-3">{{title}}</h2>
    </div>
    `
  });