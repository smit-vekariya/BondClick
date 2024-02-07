import { Card, Col, Progress, Row } from 'antd';
import React, { useCallback, useEffect, useRef, useState } from "react";
import useAxios from '../../utils/useAxios';


export default function CompanyDashBoard(){
    const api = useRef(useAxios())
    const [dashboard, setDashBoard] = useState({})


    const getDashBoardData = useCallback(async() =>{
        await api.current.get('/qr_admin/company_dashboard/')
        .then((res)=>{
            setDashBoard(res.data.data)
            console.log("res.data.data", res.data.data);
        })
    },[])


    useEffect(()=>{
        getDashBoardData()
    },[getDashBoardData])

    return(
        <>
        <div className='title_tab'>
            <div className='title_tab_title'>Dashboard</div>
        </div>
        <div className='main_tab'>
            <Row>
                <Col span={8}>
                    <Card title="Total User" bordered={true}>{dashboard.total_bond_user}</Card>
                </Col>
                <Col span={8}>
                    <Card title="Total Batch" bordered={true}>{dashboard.total_qr_batch}</Card>
                </Col>
                <Col span={8}>
                    <Card title="Total QR Code" bordered={true}>{dashboard.total_qr_code}</Card>
                </Col>
            </Row>
            <Row >
                <Card title="Used QR Code" bordered={true}>
                    <div style={{display:'Flex'}}>
                        <div><Progress type="circle" percent={dashboard.used_in_percentage} strokeColor={{'0%': '#108ee9','100%': '#87d068'}} /></div>
                        <div style={{padding: '12px 7px 0px 58px'}}>
                            <table><tbody>
                                    <tr><td><b>{dashboard.total_used_qr}</b></td><td>Used code</td></tr>
                                    <tr><td><b>{dashboard.total_remain_qr}</b></td><td>Remain code</td></tr>
                                    <tr><td colSpan="2"><hr></hr></td></tr>
                                    <tr><td><b>{dashboard.total_qr_code}</b></td><td>Total code</td></tr>
                            </tbody></table>
                        </div>
                    </div>
                </Card>
            </Row>
        </div>
        </>
    )
}