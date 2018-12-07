var active_type='';
new Vue({
    el:'#app',
    data:{
        show: false,
        loading: false,
        finished: false,
        model_show:false,
        model_text:'',
        active_type:'激情小说',
        now_page:0,
        navbar:{title:'看小说'},
        notice:{text:''},
        list: [],
        actions: [
            {id:'yse',name:'激情小说',count:999},
            {id:'tse',name:'家庭乱伦',count:999},
            {id:'ose',name:'校园春色',count:999},
            {id:'qse',name:'武侠玄幻',count:999},
            {id:'mse',name:'淫妻交换',count:999},
            {id:'sse',name:'强奸系列',count:999},
            {id:'mse',name:'长篇连载',count:999},
            {id:'kse',name:'另类小说',count:999},

        ]
    },
    methods:{
        onClickRight() {
            // 类别选择菜单状态切换
            this.show=!this.show;;
        },
        onSelect(item) {
            // 点击选项时默认不会关闭菜单，可以手动关闭
            this.show = false;
            this.now_page=0;
            this.active_type=item.name;
            this.list=[];
            this.$toast(item.name);
            this.onLoad()
        },
        onLoad() {
            var _this=this;
            this.navbar['title']='看小说  '+_this.active_type;
            this.now_page++;
            this.$toast.loading({
                mask: true,
                message: '加载中...'
              });
            $.ajax({
                type: "post",
                url: "/get_content",
                data: {"item_type": this.active_type, "page_num": this.now_page, "limt": 20},
                success: function (data) {
                    _this.notice['text']='网站通知：'+data.msg;
                    for (var i = 0;  i < data.data.length; i++) {
                        _this.list.push(data.data[i]);
                    };

                }
            });
            
            this.loading = false;
            if (this.list.length >= 400) {
                this.finished = true;
                this.$toast('没有更多了');
            }
        },
        open_model(item_id,item_name){
            var _this=this;
            this.$toast('正在加载内容');
            this.$notify(item_name);
            $.ajax({
                url:'get_item_content',
                type: "post",
                data: {"item_id": item_id},
                success:function(data){
                    _this.model_text='<p style="text-align: center">'+item_name+'</p>'+data.data;
                    _this.model_show=true;
                }

            });
        },
        close_model(){
            var _this=this;
            this.model_show=false;
            this.$toast('阅读窗口已关闭');
            _this.model_text='';
        }
    }
})