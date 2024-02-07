import { PrinterOutlined } from '@ant-design/icons';
import { Button, Form, Input, Modal, Table } from 'antd';

import React, { useCallback, useContext, useEffect, useRef, useState } from "react";
import { AuthContext } from "../../context/AuthContext";
import useAxios from '../../utils/useAxios';
import '../component.css';

const point_per_amount = process.env.REACT_APP_POINT_PER_AMOUNT
export default function QrBatch(){
    const api = useRef(useAxios())
    const {messageApi} = useContext(AuthContext)
    const [batch, setBatch] = useState([])
    const [totalRecord , setTotalRecord] = useState(0)
    const [selectedRowKeys, setSelectedRowKeys] = useState([]);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [openConfirm, setOpenConfirm] = useState(false);

    var batch_details = {
        "total_qr_code":0,
        "point_per_qr":0,
        "total_amount":0,
        "point_per_amount":0,
        "total_point":0,
        "amount_per_qr":0
    }
    const [batchPreview, setBatchPreview] = useState(batch_details);

    const calculateBatch = (e) => {
        setBatchPreview({...batchPreview, [e.target.name]:parseInt(e.target.value)})
        var total_qr = e.target.name === "total_qr_code" ? parseInt(e.target.value) : batchPreview.total_qr_code
        var point_qr = e.target.name === "point_per_qr" ? parseInt(e.target.value) : batchPreview.point_per_qr
        if(total_qr > 0 && point_qr > 0 ){
            var total_point = total_qr * point_qr
            var total_amount = total_point / parseInt(point_per_amount)
            var amount_per_qr = total_amount / total_qr
            setBatchPreview({
                "total_qr_code":parseInt(total_qr),
                "point_per_qr":parseInt(point_qr),
                "total_amount":parseFloat(total_amount.toFixed(2)),
                "point_per_amount":parseInt(point_per_amount),
                "total_point":parseInt(total_point),
                "amount_per_qr":parseFloat(amount_per_qr.toFixed(2))
            })
        }
    }

    let getQrBatchData  = useCallback(async(page,pageSize) =>{
        await api.current.get(`/qr_admin/qr_batch_list/?page=${page}&page_size=${pageSize}&ordering=-id`)
        .then((res)=>{
            setTotalRecord(res.data.count)
            setBatch(res.data.results)
        })
        .catch((error)=>{
            messageApi.open({type: 'error',content: error.message})
        })

    },[messageApi])

    useEffect(()=>{
        getQrBatchData(1, 10)
    },[getQrBatchData])

    const columns = [
        {title:"Batch Number",dataIndex:"batch_number"},
        {title:"Total QR Code",dataIndex:"total_qr_code"},
        {title:"Total Amount",dataIndex:"total_amount"},
        {title:"Point Per Amount",dataIndex:"point_per_amount"},
        {title:"Total Point",dataIndex:"total_point"},
        {title:"Point Per QR",dataIndex:"point_per_qr"},
        {title:"Amount Per QR",dataIndex:"amount_per_qr"},
        {title:"Print Batch",
            dataIndex:"id",
            render:()=><Button type='primary' size='small' icon={< PrinterOutlined />} >Print</Button>
        },
    ]
    const onSelectChange =(newSelectedRowKeys)=>{
        setSelectedRowKeys(newSelectedRowKeys)
    }
    const onTableChange = (pagination, filters, sorter) =>{
        console.log("sorter", sorter);
        console.log("filters", filters);
        console.log("pagination", pagination);
    }
    const createBatch = () =>{
        setBatchPreview(batch_details)
        setIsModalOpen(true)
    }

    const handleOk= () =>{
        if ((!batchPreview.total_qr_code > 0) || (!batchPreview.point_per_qr > 0)){
            messageApi.open({type: 'error',content: "Total QR Code and Point Per QR must be grater then 0."})
            return
        }
        setOpenConfirm(true)
    }

    const handleConfirmOk = async () =>{
        setOpenConfirm(false)
        setIsModalOpen(false)
        await api.current.post(`/qr_admin/create_qr_batch/`,batchPreview)
        .then((res)=>{
            if(res.data.status === 1){
                messageApi.open({type: 'success',content: res.data.message})
                getQrBatchData(1, 10)
            }else{
                messageApi.open({type: 'error',content: res.data.message})
            }
         })
    }
    return(
        <>
        <div className='title_tab'>
            <div className='title_tab_title'>QR Batch</div>
            <div className="title_tab_div">
               <Button type="primary" onClick={createBatch}>Create Batch</Button>
            </div>
        </div>
        <div className='main_tab'>
            <Table
                columns={columns}
                dataSource={batch} rowKey="id"
                onChange={onTableChange}
                rowSelection={{selectedRowKeys,onChange: onSelectChange}}
                pagination={{total: totalRecord,
                    defaultPageSize: 10, showSizeChanger: true,
                    pageSizeOptions: ['10', '20', '50', '100'],
                    onChange: (page, pageSize) => {
                        getQrBatchData(page, pageSize);
                    }
                }}
                scroll={{y: 500}}
                size="small"/>
            <Modal title="Create Batch" open={isModalOpen} okText="Create" onOk={handleOk} onCancel={()=>setIsModalOpen(false)}>
                <Form  labelCol={{flex: '110px'}} labelAlign="left">
                    <Form.Item label="Total QR Code">
                        <Input type='number' min={0}  defaultValue={0} name="total_qr_code" value={batchPreview.total_qr_code} onChange={calculateBatch} required></Input>
                    </Form.Item>
                    <Form.Item label="Point Per QR">
                        <Input type='number' min={0} defaultValue={0} name="point_per_qr" value={batchPreview.point_per_qr} onChange={calculateBatch} required></Input>
                    </Form.Item>
                </Form>
                <div className='batch_details'>
                    <b>Batch Preview:</b>
                    <table style={{width:'100%'}}>
                    <tbody>
                    <tr>
                        <td>Total QR Code: </td>
                        <td style={{float:"right"}}>{batchPreview.total_qr_code}</td>
                    </tr>
                    <tr>
                        <td>Point Per QR: </td>
                        <td style={{float:"right"}}>{batchPreview.point_per_qr}</td>
                    </tr>
                    <tr>
                        <td>Total Amount (&#8377;): </td>
                        <td style={{float:"right"}}>{batchPreview.total_amount}</td>
                    </tr>
                    <tr>
                        <td>Point Per Amount: </td>
                        <td style={{float:"right"}}>{batchPreview.point_per_amount}</td>
                    </tr>
                    <tr>
                        <td>Total Point: </td>
                        <td style={{float:"right"}}>{batchPreview.total_point}</td>
                    </tr>
                    <tr>
                        <td>Amount Per QR (&#8377;): </td>
                        <td style={{float:"right"}}>{batchPreview.amount_per_qr}</td>
                    </tr></tbody>
                    </table>
                </div>
            </Modal>
            <Modal
                title="Confirmation"
                open={openConfirm}
                onOk={handleConfirmOk}
                onCancel={()=>setOpenConfirm(false)}
            >
                <p>Are you sure you want to create this batch ?</p>
            </Modal>
        </div>
        </>
    )
}