export const columnData = [
    {label:'ID', prop:'user_id',width:'80',align:'center'},
    {label:'用户名', prop:'username',align:'center'},
    {label:'用户昵称', prop:'nick_name',align:'center'},
    {label:'性别', prop:'sex',width:'80',align:'center'},
    {label:'状态', prop:'status', width:'120',align:'center'},
    {label:'邮箱', prop:'email',width:'190', align:'center'},
    {label:'电话', prop:'phone',align:'center'},
    {label:'备注', prop:'remark',align:'center'},
    {label:'管理', prop:'action', width:'150',align:'center'},
]

export const searchData = [
    {label:'账 号', prop:'username',type:'input', placeholder:'请输入账号搜索'},
    {label:'电 话', prop:'phone',type:'input', placeholder:'请输入电话搜索'},
    {label:'状 态', prop:'status',type:'selection', placeholder:'请选择状态',
        teleported:false,
        option:[
            {
                label: '启用',
                value: '0'
            },
            {
                label: '禁用',
                value: '1'
            },
        ]}
]
