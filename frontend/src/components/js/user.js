import { Table } from 'antd';
import React, { useEffect, useState } from "react";
import useAxios from "../../utils/useAxios";
import '../component.css';

export default function User(){
    const api = useAxios()
    const [users, setUsers] = useState([])
    const [totalRecord , setTotalRecord] = useState(0)
    const [selectedRowKeys, setSelectedRowKeys] = useState([]);

    useEffect(()=>{
        getUserData(1, 10)
    }, [])

    let getUserData = async (page, pageSize) =>{
        await api.get(`/qr_admin/user_list/?page=${page}&page_size=${pageSize}&ordering=-id`)
            .then((res)=>{
                setTotalRecord(res.data.count)
                setUsers(res.data.results)
        })
    }

    const columns = [
        {title:"Name",dataIndex:"full_name"},
        {title:"Mobile No.",dataIndex:"mobile"},
        {title:"Address",dataIndex:"address"},
        {title:"Pin Code",dataIndex:"pin_code"},
        {title:"City",dataIndex:"city"},
        {title:"State",dataIndex:"state"},
        {title:"Distributor",dataIndex:"distributor"},
    ]

    const onSelectChange =(newSelectedRowKeys)=>{
        setSelectedRowKeys(newSelectedRowKeys)
    }

    const onTableChange = (pagination, filters, sorter) =>{
        console.log("sorter", sorter);
        console.log("filters", filters);
        console.log("pagination", pagination);

    }

    return(
    <>
       <div className='title_tab'>
            <div className='title_tab_title'>Bond Users</div>
        </div>
        <div className='main_tab'>
        <Table
            columns={columns}
            dataSource={users} rowKey="id"
            onChange={onTableChange}
            rowSelection={{selectedRowKeys,onChange: onSelectChange}}
            pagination={{total: totalRecord,
                defaultPageSize: 10, showSizeChanger: true,
                pageSizeOptions: ['10', '20', '50', '100'],
                onChange: (page, pageSize) => {
                    getUserData(page, pageSize);
                }
            }}
            scroll={{y: 500}}
            size="small"/>
        </div>
    </>
    )
}
