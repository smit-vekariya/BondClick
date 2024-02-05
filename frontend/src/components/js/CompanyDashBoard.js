import { Card, Col, Progress, Row } from 'antd';
import React, { useEffect, useState } from "react";
import useAxios from '../../utils/useAxios';


export default function CompanyDashBoard(){
    const api = useAxios()
    const [dashboard, setDashBoard] = useState({})

    useEffect(()=>{
        getDashBoardData()
    },[])

    const getDashBoardData = async() =>{
        await api.get('/qr_admin/company_dashboard/')
        .then((res)=>{
            setDashBoard(res.data.data)
        })
    }

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
                        <div><Progress type="circle" percent={90} strokeColor={{'0%': '#108ee9','100%': '#87d068'}} /></div>
                        <div style={{padding: '12px 7px 0px 58px'}}>
                            <table><tbody>
                                    <tr><td><b></b></td><td>Used token</td></tr>
                                    <tr><td><b></b></td><td>Remain token</td></tr>
                                    <tr><td><b></b></td><td>Total token</td></tr>
                            </tbody></table>
                        </div>
                    </div>
                </Card>
            </Row>
        </div>
        </>
    )
}