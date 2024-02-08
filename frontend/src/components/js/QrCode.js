import { QrcodeOutlined } from "@ant-design/icons";
import { Button, Modal, QRCode, Table } from "antd";
import React, { useCallback, useContext, useEffect, useRef, useState } from "react";
import { AuthContext } from "../../context/AuthContext";
import useAxios from "../../utils/useAxios";


export default function QrCode(){
    const api = useRef(useAxios())
    const [QRCodeData , setQRCodeData] = useState([])
    const [totalRecord , setTotalRecord] = useState(0)
    const [selectedRowKeys, setSelectedRowKeys] = useState([]);
    const {messageApi} = useContext(AuthContext)



    let getQRCodeData = useCallback(async(page, pageSize)=>{
        await api.current.get(`/qr_admin/qr_code_list/?page=${page}&page_size=${pageSize}&ordering=-id`)
        .then((res)=>{
            setTotalRecord(res.data.count)
            setQRCodeData(res.data.results)
        })
        .catch((error)=>{
                messageApi.open({type: 'error',content: error.message})
        })
    },[messageApi])

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
    const openQRCode = (qr_code) =>{
         Modal.info({
            title: `QR Code`,
            content: (<><div style={{padding: '4% 23%'}}><QRCode size={150} type="svg" value={qr_code}/></div><div>{qr_code}</div></>),
            onOk() {},
        })

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
        {title:"View QR",
            dataIndex:"qr_code",
            render:(qr_code)=>(<Button type='primary'
            onClick={()=>openQRCode(qr_code)} size='small' icon={<QrcodeOutlined />}>View QR</Button>)
        }
    ]

    return(
        <>
        <div className='title_tab'>
            <div className='title_tab_title'>QR Code</div>
        </div>
        <div className='main_tab'>
            <Table
                columns={columns}
                dataSource={QRCodeData} rowKey="id"
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