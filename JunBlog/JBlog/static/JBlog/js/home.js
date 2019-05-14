var index=new Vue({
    el:'#index',
    data:{

        "topmeau": [{ 'name': "博客" }, { 'name': "关于" }, { 'name': "随笔" }, { 'name': "友链"}],
        "date": '111',

    },
    methods:{
        SetTime:function(){
          setInterval(function(){
            index.$data.date = Date()
          },1000)
        },

    },
    mounted(){
      this.SetTime();
    }
})
