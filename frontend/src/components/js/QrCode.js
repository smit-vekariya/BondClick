import { Table } from "antd";
import React, { useCallback, useEffect, useRef, useState } from "react";
import useAxios from "../../utils/useAxios";

export default function QrCode(){
    const api = useRef(useAxios())
    const [QRCode , setQRCode] = useState([])
    const [totalRecord , setTotalRecord] = useState(0)
    const [selectedRowKeys, setSelectedRowKeys] = useState([]);


    let getQRCodeData = useCallback(async(page, pageSize)=>{
        await api.current.get(`/qr_admin/qr_code_list/?page=${page}&page_size=${pageSize}&ordering=-id`)
        .then((res)=>{
            setTotalRecord(res.data.count)
            setQRCode(res.data.results)

        })
    },[])

    useEffect(()=>{
        getQRCodeData(1, 10)
    },[getQRCodeData])


    const onSelectChange =(newSelectedRowKeys)=>{
        setSelectedRowKeys(newSelectedRowKeys)
    }

    const onTableChange = (pagination, filters, sorter) =>{
        console.log("sorter", sorter);
        console.log("filters", filters);
        console.log("pagination", pagination);
    }
    const columns = [
        {title:"QR Number",dataIndex:"qr_number"},
        {
            title:"QR Code",
            dataIndex:"qr_code",
            width: '30%',
        },
        {title:"Batch Number",dataIndex:"batch"},
        {title:"Point",dataIndex:"point"},
        {title:"Used On",dataIndex:"used_on"},
        {title:"Used By",dataIndex:"used_by"},

    ]

    return(
        <>
        <div className='title_tab'>
            <div className='title_tab_title'>QR Code</div>
        </div>
        <div className='main_tab'>
            <Table
                columns={columns}
                dataSource={QRCode} rowKey="id"
                onChange={onTableChange}
                rowSelection={{selectedRowKeys,onChange: onSelectChange}}
                pagination={{total: totalRecord,
                    defaultPageSize: 10, showSizeChanger: true,
                    pageSizeOptions: ['10', '20', '50', '100'],
                    onChange: (page, pageSize) => {
                        getQRCodeData(page, pageSize);
                    }
                }}
                scroll={{y: 500}}
                size="small"/>
        </div>
        </>
    )
}