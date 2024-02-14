import { QrcodeOutlined } from "@ant-design/icons";
import { Button, Input, Modal, QRCode, Table } from "antd";
import React, { useCallback, useContext, useEffect, useRef, useState } from "react";
import { AuthContext } from "../../context/AuthContext";
import useAxios from "../../utils/useAxios";

export default function QrCode(){
    const api = useRef(useAxios())
    const { Search } = Input;
    const [QRCodeData , setQRCodeData] = useState([])
    const [totalRecord , setTotalRecord] = useState(0)
    const [selectedRowKeys, setSelectedRowKeys] = useState([]);
    const {messageApi} = useContext(AuthContext)
    const [dataList, setDataList] =useState({page:1,pageSize:10,orderBy:"-id",search:""})



    let getQRCodeData = useCallback(async()=>{
        await api.current.get(`/qr_admin/qr_code_list/?page=${dataList.page}&page_size=${dataList.pageSize}&ordering=${dataList.orderBy}&search=${dataList.search}`)
        .then((res)=>{
            setTotalRecord(res.data.count)
            setQRCodeData(res.data.results)
        })
        .catch((error)=>{
                messageApi.open({type: 'error',content: error.message})
        })
    },[dataList, messageApi])

    useEffect(()=>{
        getQRCodeData()
    },[getQRCodeData])


    const onSelectChange =(newSelectedRowKeys)=>{
        setSelectedRowKeys(newSelectedRowKeys)
    }

    const onTableChange = (pagination, filters, sorter) =>{
        var orderBy = sorter.order ? (sorter.order === "ascend"? "":"-") + sorter.field : "-id"
        setDataList({...dataList,page:pagination.current,pageSize:pagination.pageSize,orderBy:orderBy})
    }
    const openQRCode = (qr_code) =>{
         Modal.info({
            title: `QR Code`,
            content: (<><div style={{padding: '4% 23%'}}><QRCode size={150} type="svg" value={qr_code}/></div><div>{qr_code}</div></>),
            onOk() {},
        })

    }

    const columns = [
        {title:"QR Number",dataIndex:"qr_number",sorter: true},
        {title:"QR Code",dataIndex:"qr_code", width: '30%',sorter: true},
        {title:"Batch Number",dataIndex:"batch__batch_number",sorter: true},
        {title:"Point",dataIndex:"point",sorter: true},
        {title:"Used On",dataIndex:"used_on",sorter: true},
        {title:"Used By",dataIndex:"used_by__mobile",sorter: true},
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
            <div className="title_tab_div">
              <Search placeholder="Search by Qr Number, Batch number" allowClear={true} onChange={(e)=> {if(e.target.value===""){setDataList({...dataList, search:""})}}} onSearch={(value) => setDataList({...dataList, search:value})} style={{ width: 200 }} />
            </div>
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
                }}
                scroll={{y: 500}}
                size="small"/>
        </div>
        </>
    )
}